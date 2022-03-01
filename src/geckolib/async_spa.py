""" GeckoAsyncSpa class """

import logging
import asyncio
import importlib
import socket
import time
from enum import Enum

from .const import GeckoConstants
from .driver import (
    GeckoAsyncUdpProtocol,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoRFErrProtocolHandler,
    GeckoUnhandledProtocolHandler,
    GeckoWatercareProtocolHandler,
    # Rest
    GeckoAsyncStructure,
    Observable,
)

_LOGGER = logging.getLogger(__name__)


class GeckoSpaConnectionState(Enum):
    DISCONNECTED = 1
    PING_STARTED = 2
    GOT_FIRMWARE_VERSION = 3
    GOT_CHANNEL = 4
    GOT_CONFIG_FILES = 5

    CONNECTED = 10

    # Error states
    CANNOT_FIND_SPA_PACK = 99
    CANNOT_FIND_CONFIG_VERSION = 98
    CANNOT_FIND_LOG_VERSION = 97
    NO_PING_RESPONSE = 96
    PROTOCOL_RETRY_EXCEEDED = 95


class GeckoAsyncSpa(Observable):
    """GeckoAsyncSpa class manages an instance of a spa, and is the main point of contact for
    control and monitoring. Uses the declarations found in pack/* to build
    an object that exposes the properties and capabilities of your spa. This class
    should only be used via a Facade which hides the implementation details"""

    def __init__(self, client_id, spa_descriptor, taskman):
        super().__init__()

        self.client_id = client_id
        self.descriptor = spa_descriptor
        self._taskman = taskman

        self._con_lost = None
        self._transport = None
        self._protocol = None
        self._connection_state = GeckoSpaConnectionState.DISCONNECTED

        self.intouch_version_en = ""
        self.intouch_version_co = ""

        self.channel = 0
        self.signal = 0

        self.config_version = 0
        self.log_version = 0

        self.pack_class = None
        self.pack_type = ""
        self.config_class = None
        self.log_class = None

        self.pack = None
        self.version = ""
        self.config_number = 0

        self.struct = GeckoAsyncStructure(self._on_set_value, self._on_async_set_value)

    @property
    def sendparms(self):
        return (
            self.descriptor.destination[0],
            self.descriptor.destination[1],
            self.descriptor.identifier,
            self.client_id,
        )

    @property
    def connection_state(self):
        return self._connection_state

    def _set_connection_state(self, state: GeckoSpaConnectionState):
        old_state = self._connection_state
        self._connection_state = state
        self._on_change(self, old_state, self._connection_state)

    async def connect(self):
        loop = asyncio.get_running_loop()
        self._con_lost = loop.create_future()

        self._transport, self._protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(
                self._con_lost,
                (self.descriptor.destination[0], self.descriptor.destination[1]),
            ),
            family=socket.AF_INET,
        )
        self._on_change(self)

        self._taskman.add_task(
            GeckoUnhandledProtocolHandler().consume(self._protocol),
            "Unhandled packet",
        )
        self._taskman.add_task(
            GeckoPacketProtocolHandler(on_handled=self._on_packet).consume(
                self._protocol
            ),
            "Packet handler",
        )
        self._taskman.add_task(
            GeckoAsyncPartialStatusBlockProtocolHandler(
                on_handled=self._on_partial_status_update
            ).consume(self._protocol),
            "Partial status block handler",
        )
        self._taskman.add_task(
            GeckoRFErrProtocolHandler().consume(self._protocol),
            "RFErr handler",
        )
        self._taskman.add_task(self.ping_loop(), "Ping loop")
        self._taskman.add_task(self.refresh_loop(), "Refresh loop")
        self._set_connection_state(GeckoSpaConnectionState.PING_STARTED)

        version_handler = await self._protocol.get(
            lambda: GeckoVersionProtocolHandler.request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=self.sendparms,
            )
        )
        if version_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return

        self.intouch_version_en = "{0} v{1}.{2}".format(
            version_handler.en_build, version_handler.en_major, version_handler.en_minor
        )
        self.intouch_version_co = "{0} v{1}.{2}".format(
            version_handler.co_build, version_handler.co_major, version_handler.co_minor
        )
        self._set_connection_state(GeckoSpaConnectionState.GOT_FIRMWARE_VERSION)
        _LOGGER.debug(
            "Got in.touch2 firmware version EN(Home) %s/CO(Spa) %s, now get channel",
            self.intouch_version_en,
            self.intouch_version_co,
        )

        get_channel_handler = await self._protocol.get(
            lambda: GeckoGetChannelProtocolHandler.request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=self.sendparms,
            )
        )

        if get_channel_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return

        self.channel = get_channel_handler.channel
        self.signal = get_channel_handler.signal_strength
        self._set_connection_state(GeckoSpaConnectionState.GOT_CHANNEL)
        _LOGGER.debug("Got channel %s/%s, now get config", self.channel, self.signal)

        config_file_handler = await self._protocol.get(
            lambda: GeckoConfigFileProtocolHandler.request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=self.sendparms,
            )
        )

        if config_file_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return

        # Stash the config and log structure declarations
        self.config_version = config_file_handler.config_version
        self.log_version = config_file_handler.log_version
        plateform_key = config_file_handler.plateform_key.lower()

        _LOGGER.debug(
            "Got %s config version %s and log version %s, check if we can support this",
            plateform_key,
            self.config_version,
            self.log_version,
        )
        self._set_connection_state(GeckoSpaConnectionState.GOT_CONFIG_FILES)

        pack_module_name = f"geckolib.driver.packs.{plateform_key}"
        try:
            GeckoPack = importlib.import_module(pack_module_name).GeckoPack
            self.pack_class = GeckoPack(self.struct)
            self.pack_type = self.pack_class.type
        except ModuleNotFoundError:
            self._set_connection_state(GeckoSpaConnectionState.CANNOT_FIND_SPA_PACK)
            _LOGGER.warning(
                "Cannot find spa pack for %s", config_file_handler.plateform_key
            )
            return

        config_module_name = (
            f"geckolib.driver.packs.{plateform_key}-cfg-{self.config_version}"
        )
        try:
            GeckoConfigStruct = importlib.import_module(
                config_module_name
            ).GeckoConfigStruct
            self.config_class = GeckoConfigStruct(self.struct)
        except ModuleNotFoundError:
            self._set_connection_state(
                GeckoSpaConnectionState.CANNOT_FIND_CONFIG_VERSION
            )
            _LOGGER.warning(
                "Cannot find GeckoConfigStruct module for %s v%s",
                config_file_handler.plateform_key,
                self.config_version,
            )
            return

        log_module_name = (
            f"geckolib.driver.packs.{plateform_key}-log-{self.log_version}"
        )
        try:
            GeckoLogStruct = importlib.import_module(log_module_name).GeckoLogStruct
            self.log_class = GeckoLogStruct(self.struct)
        except ModuleNotFoundError:
            self._set_connection_state(GeckoSpaConnectionState.CANNOT_FIND_LOG_VERSION)
            _LOGGER.warning(
                "Cannot find GeckoLogStruct module for %s v%s",
                config_file_handler.plateform_key,
                self.log_version,
            )
            return

        _LOGGER.debug(
            "Got spa configuration Type %s - CFG %s/LOG %s, now ask for initial "
            "status block",
            self.pack_type,
            self.config_version,
            self.log_version,
        )

        if not await self.struct.get(
            self._protocol,
            lambda: GeckoStatusBlockProtocolHandler.full_request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=self.sendparms,
            ),
        ):
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return

        _LOGGER.debug("Status block was completed, so spa can be connected")

        self.struct.build_accessors(self.config_class, self.log_class)

        self.pack = self.accessors[GeckoConstants.KEY_PACK_TYPE].value
        self.version = "{0} v{1}.{2}".format(
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_ID].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REV].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REL].value,
        )
        self.config_number = self.accessors[GeckoConstants.KEY_CONFIG_NUMBER].value

        self._set_connection_state(GeckoSpaConnectionState.CONNECTED)
        _LOGGER.debug("Spa connected")

    def disconnect(self):
        self._protocol.disconnect()
        self._protocol = None
        self._transport = None

    @property
    def isopen(self):
        if self._protocol is None:
            return False
        return self._protocol.isopen

    def _on_packet(self, handler, socket, sender):
        if handler.parms == self.sendparms:
            self._protocol.datagram_received(handler.packet_content, handler.parms)
        else:
            _LOGGER.warning(
                "Dropping packet from %s because it didn't match %s",
                handler.parms,
                self.sendparms,
            )

    async def ping_loop(self):
        _LOGGER.info("Ping loop started")

        self._last_ping = time.monotonic()

        while self.isopen:

            ping_handler = await self._protocol.get(
                lambda: GeckoPingProtocolHandler.request(
                    parms=self.sendparms,
                    timeout=GeckoConstants.PING_FREQUENCY_IN_SECONDS,
                ),
                None,
                1,
            )

            if ping_handler is not None:
                self._last_ping = time.monotonic()
            elif (
                time.monotonic() - self._last_ping
                > GeckoConstants.PING_DEVICE_NOT_RESPONDING_TIMEOUT
            ):
                _LOGGER.warning("Spa is not responding to pings")
                self._set_connection_state(GeckoSpaConnectionState.NO_PING_RESPONSE)

            await asyncio.sleep(GeckoConstants.PING_FREQUENCY_IN_SECONDS)

        _LOGGER.info("Ping loop finished")

    async def refresh_loop(self):
        """The refresh loop is simply to ensure that our understanding
        of the live parts of the spastruct are always up-to-date. We
        shouldn't need to do this, but this is belt and braces stuff"""
        _LOGGER.info("Refresh loop started")
        while self.isopen:
            if self.connection_state == GeckoSpaConnectionState.CONNECTED:
                """Refresh the live spa data block"""
                await asyncio.sleep(
                    GeckoConstants.SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS
                )
                if not await self.struct.get(
                    self._protocol,
                    lambda: GeckoStatusBlockProtocolHandler.request(
                        self._protocol.get_and_increment_sequence_counter(),
                        self.log_class.begin,
                        self.log_class.end,
                        parms=self.sendparms,
                    ),
                ):
                    self._set_connection_state(
                        GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED
                    )
            await asyncio.sleep(0)

    def _on_partial_status_update(self, handler, socket, sender):
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])

    async def _on_async_set_value(self, pos, length, newvalue):
        pack_command_handler = await self._protocol.get(
            lambda: GeckoPackCommandProtocolHandler.set_value(
                self._protocol.get_and_increment_sequence_counter(),
                self.pack_type,
                self.config_version,
                self.log_version,
                pos,
                length,
                newvalue,
                parms=self.sendparms,
            )
        )

        if pack_command_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)

    def _on_set_value(self, pos, length, newvalue):
        self._taskman.add_task(
            self._on_async_set_value(pos, length, newvalue), "Set value task"
        )

    @property
    def accessors(self):
        return self.struct.accessors

    async def async_press(self, keypad):
        """Simulate a button press async"""
        pack_command_handler = await self._protocol.get(
            lambda: GeckoPackCommandProtocolHandler.keypress(
                self._protocol.get_and_increment_sequence_counter(),
                self.pack_type,
                keypad,
                parms=self.sendparms,
            )
        )

        if pack_command_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)

    def press(self, keypad):
        """Simulate a button press"""
        self._taskman.add_task(self.async_press(keypad), "Button press task")

    async def async_get_watercare(self):
        get_watercare_handler = await self._protocol.get(
            lambda: GeckoWatercareProtocolHandler.request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=self.sendparms,
            )
        )

        if get_watercare_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return None

        return get_watercare_handler.mode

    async def async_set_watercare(self, new_mode) -> None:
        set_watercare_handler = await self._protocol.get(
            lambda: GeckoWatercareProtocolHandler.set(
                self._protocol.get_and_increment_sequence_counter(),
                new_mode,
                parms=self.sendparms,
            )
        )

        if set_watercare_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)

    @property
    def status_line(self) -> str:
        if self.connection_state == GeckoSpaConnectionState.DISCONNECTED:
            return "Disconnected"
        elif self.connection_state == GeckoSpaConnectionState.PING_STARTED:
            return "Ping started"
        elif self.connection_state == GeckoSpaConnectionState.GOT_FIRMWARE_VERSION:
            return "Got in.touch2 firmware version"
        elif self.connection_state == GeckoSpaConnectionState.GOT_CHANNEL:
            return "Got RF channel"
        elif self.connection_state == GeckoSpaConnectionState.GOT_CONFIG_FILES:
            return "Got config files"
        elif self.connection_state == GeckoSpaConnectionState.CONNECTED:
            return f"Connected, last ping {int(time.monotonic() - self._last_ping)} seconds ago"
        elif self.connection_state == GeckoSpaConnectionState.NO_PING_RESPONSE:
            return "Spa not responding to pings"
        elif self.connection_state == GeckoSpaConnectionState.CANNOT_FIND_SPA_PACK:
            return "Cannot find spa pack"
        elif (
            self.connection_state == GeckoSpaConnectionState.CANNOT_FIND_CONFIG_VERSION
        ):
            return "Cannot find config version"
        elif self.connection_state == GeckoSpaConnectionState.CANNOT_FIND_LOG_VERSION:
            return "Cannot find log version"
        elif self.connection_state == GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED:
            return "Protocol retry failure"
        else:
            return "Uknown spa connection state"
