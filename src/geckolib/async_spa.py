""" GeckoAsyncSpa class """

from datetime import datetime
import logging
import asyncio
import importlib
import socket
import time
from typing import Optional

from .spa_connection_state import GeckoSpaConnectionState
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_tasks import AsyncTasks

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


class GeckoAsyncSpa(Observable):
    """GeckoAsyncSpa class manages an instance of a spa, and is the main point of
    contact for control and monitoring. Uses the declarations found in pack/* to build
    an object that exposes the properties and capabilities of your spa. This class
    should only be used via a Facade which hides the implementation details"""

    def __init__(
        self,
        client_id: bytes,
        spa_descriptor: GeckoAsyncSpaDescriptor,
        taskman: AsyncTasks,
    ) -> None:
        super().__init__()

        self.client_id = client_id
        self.descriptor = spa_descriptor
        self._taskman = taskman

        self._con_lost: Optional[asyncio.Future] = None
        self._transport: Optional[asyncio.BaseTransport] = None
        self._protocol: Optional[GeckoAsyncUdpProtocol] = None
        self._connection_state: GeckoSpaConnectionState = (
            GeckoSpaConnectionState.DISCONNECTED
        )

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
    def sendparms(self) -> tuple:
        return (
            self.descriptor.destination[0],
            self.descriptor.destination[1],
            self.descriptor.identifier,
            self.client_id,
        )

    @property
    def connection_state(self) -> GeckoSpaConnectionState:
        return self._connection_state

    @property
    def revision(self) -> str:
        """Get the revision of the spa pack structure used to generate
        the pack modules"""
        # TODO: Need to add base classes and type hinting to auto-generated
        # pack code and remove type-hint suppression below
        return self.pack_class.revision  # type: ignore

    def _set_connection_state(self, state: GeckoSpaConnectionState) -> None:
        old_state = self._connection_state
        self._connection_state = state
        self._on_change(self, old_state, self._connection_state)

    def _get_version_handler_func(self) -> GeckoVersionProtocolHandler:
        assert self._protocol is not None
        return GeckoVersionProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(), parms=self.sendparms
        )

    def _get_channel_handler_func(self) -> GeckoGetChannelProtocolHandler:
        assert self._protocol is not None
        return GeckoGetChannelProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    def _get_config_file_handler_func(self) -> GeckoConfigFileProtocolHandler:
        assert self._protocol is not None
        return GeckoConfigFileProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    async def connect(self) -> None:
        loop = asyncio.get_running_loop()
        self._con_lost = loop.create_future()

        self._transport, _protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(
                self._con_lost,
                (self.descriptor.destination[0], self.descriptor.destination[1]),
            ),
            family=socket.AF_INET,
        )
        assert isinstance(_protocol, GeckoAsyncUdpProtocol)
        self._protocol = _protocol
        self._on_change(self)

        self._taskman.add_task(
            GeckoUnhandledProtocolHandler().consume(self._protocol),
            "Unhandled packet",
        )
        self._taskman.add_task(
            GeckoPacketProtocolHandler(async_on_handled=self._async_on_packet).consume(
                self._protocol
            ),
            "Packet handler",
        )
        self._taskman.add_task(
            GeckoAsyncPartialStatusBlockProtocolHandler(
                async_on_handled=self._async_on_partial_status_update
            ).consume(self._protocol),
            "Partial status block handler",
        )
        self._taskman.add_task(
            GeckoRFErrProtocolHandler().consume(self._protocol),
            "RFErr handler",
        )
        self._taskman.add_task(self._ping_loop(), "Ping loop")
        self._taskman.add_task(self._refresh_loop(), "Refresh loop")
        self._set_connection_state(GeckoSpaConnectionState.PING_STARTED)

        version_handler = await self._protocol.get(self._get_version_handler_func)
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

        get_channel_handler = await self._protocol.get(self._get_channel_handler_func)
        if get_channel_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return

        self.channel = get_channel_handler.channel
        self.signal = get_channel_handler.signal_strength
        self._set_connection_state(GeckoSpaConnectionState.GOT_CHANNEL)
        _LOGGER.debug("Got channel %s/%s, now get config", self.channel, self.signal)

        config_file_handler = await self._protocol.get(
            self._get_config_file_handler_func
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
            # TODO: Need to add base classes and type hinting to auto-generated
            # pack code and remove type-hint suppression below
            self.pack_type = self.pack_class.type  # type: ignore
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

    def disconnect(self) -> None:
        """Disconnect the spa from the async protocol"""
        if self._protocol is not None:
            self._protocol.disconnect()
            self._protocol = None
        self._transport = None

    @property
    def isopen(self) -> bool:
        """Return True if the spa has a UDP socket with the in.touch EN module"""
        if self._protocol is None:
            return False
        return self._protocol.isopen

    async def _async_on_packet(
        self, handler: GeckoPacketProtocolHandler, sender: tuple
    ) -> None:
        if handler.parms == self.sendparms:
            assert self._protocol is not None
            self._protocol.datagram_received(handler.packet_content, handler.parms)
        else:
            _LOGGER.warning(
                "Dropping packet from %s because it didn't match %s",
                handler.parms,
                self.sendparms,
            )

    @property
    def last_ping_at(self) -> datetime:
        """The datetime of the last successful ping respons"""
        return self._last_ping_at

    async def _ping_loop(self) -> None:
        _LOGGER.info("Ping loop started")

        self._last_ping = time.monotonic()
        self._last_ping_at = datetime.now()

        while self.isopen:

            assert self._protocol is not None
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
                self._last_ping_at = datetime.now()
                self._on_change()
            elif (
                time.monotonic() - self._last_ping
                > GeckoConstants.PING_DEVICE_NOT_RESPONDING_TIMEOUT
            ):
                _LOGGER.warning("Spa is not responding to pings")
                self._set_connection_state(GeckoSpaConnectionState.NO_PING_RESPONSE)

            await asyncio.sleep(GeckoConstants.PING_FREQUENCY_IN_SECONDS)

        _LOGGER.info("Ping loop finished")

    def _get_status_block_handler_func(self) -> GeckoStatusBlockProtocolHandler:
        assert self._protocol is not None
        assert self.log_class is not None
        return GeckoStatusBlockProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            self.log_class.begin,
            self.log_class.end,
            parms=self.sendparms,
        )

    async def _refresh_loop(self) -> None:
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
                    self._protocol, self._get_status_block_handler_func
                ):
                    self._set_connection_state(
                        GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED
                    )
            await asyncio.sleep(0)

    async def _async_on_partial_status_update(
        self,
        handler: GeckoAsyncPartialStatusBlockProtocolHandler,
        sender: tuple,
    ) -> None:
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])

    async def _on_async_set_value(self, pos, length, newvalue) -> None:
        assert self._protocol is not None
        pack_command_handler = await self._protocol.get(
            lambda: GeckoPackCommandProtocolHandler.set_value(
                self._protocol.get_and_increment_sequence_counter(),  # type: ignore
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

    def _on_set_value(self, pos, length, newvalue) -> None:
        self._taskman.add_task(
            self._on_async_set_value(pos, length, newvalue), "Set value task"
        )

    @property
    def accessors(self) -> dict:
        return self.struct.accessors

    async def async_press(self, keypad) -> None:
        """Simulate a button press async"""
        assert self._protocol is not None
        pack_command_handler = await self._protocol.get(
            lambda: GeckoPackCommandProtocolHandler.keypress(
                self._protocol.get_and_increment_sequence_counter(),  # type: ignore
                self.pack_type,
                keypad,
                parms=self.sendparms,
            )
        )

        if pack_command_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)

    def press(self, keypad) -> None:
        """Simulate a button press"""
        self._taskman.add_task(self.async_press(keypad), "Button press task")

    def _get_watercare_handler_func(self) -> GeckoWatercareProtocolHandler:
        assert self._protocol is not None
        return GeckoWatercareProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    async def async_get_watercare(self) -> Optional[int]:
        assert self._protocol is not None
        get_watercare_handler = await self._protocol.get(
            self._get_watercare_handler_func
        )

        if get_watercare_handler is None:
            self._set_connection_state(GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED)
            return None

        return get_watercare_handler.mode

    async def async_set_watercare(self, new_mode) -> None:
        assert self._protocol is not None
        set_watercare_handler = await self._protocol.get(
            lambda: GeckoWatercareProtocolHandler.set(
                self._protocol.get_and_increment_sequence_counter(),  # type: ignore
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
            return "Connected"
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
