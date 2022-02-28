""" GeckoAsyncSpa class """

import logging
import asyncio
import importlib
import socket
import time
from enum import Enum


from .const import GeckoConstants
from .driver import (
    GeckoUdpSocket,
    GeckoAsyncUdpProtocol,
    GeckoHelloProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoPartialStatusBlockProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoRFErrProtocolHandler,
    GeckoUnhandledProtocolHandler,
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

        self.struct = GeckoAsyncStructure(self._on_set_value)

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
            lambda: GeckoAsyncUdpProtocol(self._con_lost), family=socket.AF_INET
        )
        self._on_change(self)

        self._taskman.add_task(
            GeckoUnhandledProtocolHandler().consume(None, self._protocol.queue),
            "Unhandled packet",
        )
        self._taskman.add_task(
            GeckoPacketProtocolHandler().consume(self._protocol, self._protocol.queue),
            "Packet handler",
        )
        self._taskman.add_task(
            GeckoPartialStatusBlockProtocolHandler(
                on_handled=self._on_partial_status_update
            ).consume(self._protocol, self._protocol.queue),
            "Partial status block handler",
        )
        self._taskman.add_task(
            GeckoRFErrProtocolHandler().consume(self._protocol, self._protocol.queue),
            "RFErr handler",
        )
        self._taskman.add_task(self.ping_loop(), "Ping loop")
        self._set_connection_state(GeckoSpaConnectionState.PING_STARTED)

        version_handler = GeckoVersionProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
            on_handled=self._on_version_received,
        )
        self._taskman.add_task(
            version_handler.consume(self._protocol, self._protocol.queue),
            "Version handler",
        )
        self._protocol.queue_send(version_handler, self.sendparms)

        _LOGGER.debug("Wait for complete connection now")
        while self.connection_state != GeckoSpaConnectionState.CONNECTED:
            await asyncio.sleep(0)

    def disconnect(self):
        self._protocol.disconnect()
        self._protocol = None
        self._transport = None

    @property
    def isopen(self):
        if self._protocol is None:
            return False
        return self._protocol.isopen

    def _on_ping_response(self, _handler, _socket, _sender):
        self._last_ping = time.monotonic()

    async def ping_loop(self):
        _LOGGER.info("Ping loop started")

        self._last_ping = time.monotonic()
        ping_handler = GeckoPingProtocolHandler.request(
            parms=self.sendparms, on_handled=self._on_ping_response
        )

        self._taskman.add_task(
            ping_handler.consume(None, self._protocol.queue), "Ping response handler"
        )

        while self.isopen:
            self._protocol.queue_send(ping_handler, self.sendparms)
            await asyncio.wait(
                [self._con_lost], timeout=GeckoConstants.PING_FREQUENCY_IN_SECONDS
            )

            if (
                time.monotonic() - self._last_ping
                > GeckoConstants.PING_DEVICE_NOT_RESPONDING_TIMEOUT
            ):
                self._handle_no_ping_response()

        _LOGGER.info("Ping loop finished")

    def _handle_no_ping_response(self):
        _LOGGER.warning(
            # TODO
            "TODO: Spa is not responding to pings, need to consider what to do"
        )

    def _on_partial_status_update(self, handler, socket, sender):
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])
        else:
            handler.changes.clear()

    def _on_set_value(self, pos, length, newvalue):
        # We issue a pack command to acheive this ...
        self._taskman.add_task(
            GeckoPackCommandProtocolHandler().consume(
                self._protocol, self._protocol.queue
            )
        )
        self._protocol.queue_send(
            GeckoPackCommandProtocolHandler.set_value(
                self._protocol.get_and_increment_sequence_counter(),
                self.pack_type,
                self.config_version,
                self.log_version,
                pos,
                length,
                newvalue,
                parms=self.sendparms,
            ),
            self.sendparms,
        )

    def _on_version_received(self, handler, socket, sender):
        self.intouch_version_en = "{0} v{1}.{2}".format(
            handler.en_build, handler.en_major, handler.en_minor
        )
        self.intouch_version_co = "{0} v{1}.{2}".format(
            handler.co_build, handler.co_major, handler.co_minor
        )
        self._set_connection_state(GeckoSpaConnectionState.GOT_FIRMWARE_VERSION)
        _LOGGER.debug(
            "Got in.touch2 firmware version EN(Home) %s/CO(Spa) %s, now get channel",
            self.intouch_version_en,
            self.intouch_version_co,
        )

        get_channel_handler = GeckoGetChannelProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=sender,
            on_handled=self._on_channel_received,
        )
        self._taskman.add_task(
            get_channel_handler.consume(self._protocol, self._protocol.queue),
            "Get channel handler",
        )
        self._protocol.queue_send(
            get_channel_handler,
            sender,
        )

    def _on_channel_received(self, handler, socket, sender):
        self.channel = handler.channel
        self.signal = handler.signal_strength
        self._set_connection_state(GeckoSpaConnectionState.GOT_CHANNEL)
        _LOGGER.debug("Got channel %s/%s, now get config", self.channel, self.signal)

        config_file_handler = GeckoConfigFileProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=sender,
            on_handled=self._on_config_received,
        )

        self._taskman.add_task(
            config_file_handler.consume(self._protocol, self._protocol.queue),
            "Config file handler",
        )
        self._protocol.queue_send(config_file_handler, sender)

    def _on_config_received(self, handler, socket, sender):
        # Stash the config and log structure declarations
        self.config_version = handler.config_version
        self.log_version = handler.log_version
        plateform_key = handler.plateform_key.lower()

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
            _LOGGER.warning("Cannot find spa pack for %s", handler.plateform_key)
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
                handler.plateform_key,
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
                handler.plateform_key,
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

        self.struct.retry_request(
            self._protocol,
            self._taskman,
            GeckoStatusBlockProtocolHandler.full_request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=sender,
                on_complete=self._on_status_block_complete,
            ),
            sender,
        )

    def _on_status_block_complete(self, _handler, _protocol, _queue):
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

    @property
    def accessors(self):
        return self.struct.accessors

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
        else:
            return "Uknown spa connection state"
