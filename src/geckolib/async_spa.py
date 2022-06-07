""" GeckoAsyncSpa class """

from datetime import datetime, timezone
import logging
import asyncio
import importlib
import socket
import time
from typing import Optional, Tuple, List

from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_tasks import AsyncTasks
from .spa_events import GeckoSpaEvent

from .const import GeckoConstants
from .config import GeckoConfig, config_sleep
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
    GeckoWatercareErrorHandler,
    GeckoRemindersProtocolHandler,
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
        event_handler: GeckoSpaEvent.CallBack,
    ) -> None:
        super().__init__()

        self.client_id = client_id
        self.descriptor = spa_descriptor
        self._taskman = taskman
        self._event_handler: GeckoSpaEvent.CallBack = event_handler

        self._con_lost: Optional[asyncio.Future] = None
        self._transport: Optional[asyncio.BaseTransport] = None
        self._protocol: Optional[GeckoAsyncUdpProtocol] = None
        self._is_connected = False

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
        self._last_ping_at: Optional[datetime] = None

    @property
    def sendparms(self) -> tuple:
        return (
            self.descriptor.destination[0],
            self.descriptor.destination[1],
            self.descriptor.identifier,
            self.client_id,
        )

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    @property
    def revision(self) -> str:
        """Get the revision of the spa pack structure used to generate
        the pack modules"""
        # TODO: Need to add base classes and type hinting to auto-generated
        # pack code and remove type-hint suppression below
        return self.pack_class.revision  # type: ignore

    def _get_version_handler_func(self) -> GeckoVersionProtocolHandler:
        assert self._protocol is not None
        return GeckoVersionProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(False),
            parms=self.sendparms,
        )

    def _get_channel_handler_func(self) -> GeckoGetChannelProtocolHandler:
        assert self._protocol is not None
        return GeckoGetChannelProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(False),
            parms=self.sendparms,
        )

    def _get_config_file_handler_func(self) -> GeckoConfigFileProtocolHandler:
        assert self._protocol is not None
        return GeckoConfigFileProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(False),
            parms=self.sendparms,
        )

    async def _async_on_rferr(
        self, handler: GeckoRFErrProtocolHandler, sender: tuple
    ) -> None:
        await self._event_handler(GeckoSpaEvent.ERROR_RF_ERROR)
        # If we've had too many RFErr messages, then we bail waiting for user action
        if handler.total_error_count > GeckoConstants.MAX_RF_ERRORS_BEFORE_HALT:
            _LOGGER.error(
                (
                    "Spa %s has too many RF errors, so disconnecting "
                    "awaiting user intervention"
                ),
                self.descriptor.name,
            )
            await self._event_handler(GeckoSpaEvent.ERROR_TOO_MANY_RF_ERRORS)

    async def _connect(self) -> None:
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
        await asyncio.sleep(GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS)

        self._taskman.add_task(
            GeckoUnhandledProtocolHandler().consume(self._protocol),
            "Unhandled packet",
            "SPA",
        )
        self._taskman.add_task(
            GeckoPacketProtocolHandler(async_on_handled=self._async_on_packet).consume(
                self._protocol
            ),
            "Packet handler",
            "SPA",
        )
        self._taskman.add_task(
            GeckoAsyncPartialStatusBlockProtocolHandler(
                self._protocol, async_on_handled=self._async_on_partial_status_update
            ).consume(self._protocol),
            "Partial status block handler",
            "SPA",
        )
        self._taskman.add_task(
            GeckoRFErrProtocolHandler(async_on_handled=self._async_on_rferr).consume(
                self._protocol
            ),
            "RFErr handler",
            "SPA",
        )
        self._taskman.add_task(
            GeckoWatercareErrorHandler(async_on_handled=self._async_on_wcerr).consume(
                self._protocol
            ),
            "WCErr handler",
            "SPA",
        )
        self._taskman.add_task(self._ping_loop(), "Ping loop", "SPA")
        self._taskman.add_task(self._refresh_loop(), "Refresh loop", "SPA")
        await asyncio.sleep(GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS)

        version_handler = await self._protocol.get(self._get_version_handler_func)
        if version_handler is None:
            _LOGGER.error("Cannot get version, protocol retry count exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED
            )
            return

        self.intouch_version_en = "{0} v{1}.{2}".format(
            version_handler.en_build, version_handler.en_major, version_handler.en_minor
        )
        self.intouch_version_co = "{0} v{1}.{2}".format(
            version_handler.co_build, version_handler.co_major, version_handler.co_minor
        )
        _LOGGER.debug(
            "Got in.touch2 firmware version EN(Home) %s/CO(Spa) %s, now get channel",
            self.intouch_version_en,
            self.intouch_version_co,
        )
        await self._event_handler(
            GeckoSpaEvent.CONNECTION_GOT_FIRMWARE_VERSION,
            intouch_version_en=self.intouch_version_en,
            intouch_version_co=self.intouch_version_co,
        )
        await asyncio.sleep(GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS)

        get_channel_handler = await self._protocol.get(self._get_channel_handler_func)
        if get_channel_handler is None:
            _LOGGER.error("Cannot get channel, protocol retry count exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED
            )
            return

        self.channel = get_channel_handler.channel
        self.signal = get_channel_handler.signal_strength
        _LOGGER.debug("Got channel %s/%s, now get config", self.channel, self.signal)
        await self._event_handler(
            GeckoSpaEvent.CONNECTION_GOT_CHANNEL,
            channel=self.channel,
            signal=self.signal,
        )
        await asyncio.sleep(GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS)

        config_file_handler = await self._protocol.get(
            self._get_config_file_handler_func
        )
        if config_file_handler is None:
            _LOGGER.error("Cannot get file, protocol retry count exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED
            )
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
        await self._event_handler(
            GeckoSpaEvent.CONNECTION_GOT_CONFIG_FILES,
            plateform_key=plateform_key,
            config_version=self.config_version,
            log_version=self.log_version,
        )
        await asyncio.sleep(GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS)

        pack_module_name = f"geckolib.driver.packs.{plateform_key}"
        try:
            GeckoPack = importlib.import_module(pack_module_name).GeckoPack
            self.pack_class = GeckoPack(self.struct)
            # TODO: Need to add base classes and type hinting to auto-generated
            # pack code and remove type-hint suppression below
            self.pack_type = self.pack_class.type  # type: ignore
        except ModuleNotFoundError:
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_CANNOT_FIND_SPA_PACK,
                pack_module_name=pack_module_name,
            )
            _LOGGER.error(
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
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_CANNOT_FIND_CONFIG_VERSION,
                config_version=self.config_version,
            )
            _LOGGER.error(
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
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_CANNOT_FIND_LOG_VERSION,
                log_version=self.log_version,
            )
            _LOGGER.error(
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

        await self._event_handler(GeckoSpaEvent.CONNECTION_INITIAL_DATA_BLOCK_REQUEST)
        await asyncio.sleep(GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS)

        if not await self.struct.get(
            self._protocol,
            lambda: GeckoStatusBlockProtocolHandler.full_request(
                self._protocol.get_and_increment_sequence_counter(False),
                parms=self.sendparms,
            ),
        ):
            _LOGGER.error("Cannot get full struct, protocol retry count exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED
            )

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

        self._is_connected = True
        await self._event_handler(GeckoSpaEvent.CONNECTION_SPA_COMPLETE)
        _LOGGER.debug("Spa connected")

    async def connect(self) -> None:
        """Connection wrapper with exception safety"""
        try:
            await self._connect()
        except:  # noqa
            _LOGGER.exception("Exception during spa connection")
            raise

    async def disconnect(self) -> None:
        """Disconnect the spa from the async protocol"""
        self._is_connected = False
        await self._event_handler(GeckoSpaEvent.RUNNING_SPA_DISCONNECTED)
        self.struct.reset()
        self._taskman.cancel_key_tasks("SPA")
        if self._protocol is not None:
            self._protocol.disconnect()
            self._protocol = None
        self._transport = None
        self.unwatch_all()

    @property
    def isopen(self) -> bool:
        """Return True if the spa has a UDP socket with the in.touch EN module"""
        if self._protocol is None:
            return False
        return self._protocol.isopen

    @property
    def is_responding_to_pings(self) -> bool:
        if self._last_ping is None:
            return False
        # Allow twice as much time as ping frequency to make sure boundary tests
        # are successful
        return (
            time.monotonic() - self._last_ping
        ) < GeckoConfig.PING_FREQUENCY_IN_SECONDS * 2

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
    def last_ping_at(self) -> Optional[datetime]:
        """The datetime of the last successful ping response or None"""
        return self._last_ping_at

    async def _ping_loop(self) -> None:
        _LOGGER.debug("Ping loop started")

        self._last_ping = time.monotonic()

        try:
            while self.isopen:

                assert self._protocol is not None
                ping_handler = await self._protocol.get(
                    lambda: GeckoPingProtocolHandler.request(parms=self.sendparms),
                    None,
                    1,
                )

                if ping_handler is not None:
                    self._last_ping = time.monotonic()
                    self._last_ping_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                    self._on_change()
                    await self._event_handler(
                        GeckoSpaEvent.RUNNING_PING_RECEIVED,
                        last_ping_at=self._last_ping_at,
                    )
                else:
                    await self._event_handler(
                        GeckoSpaEvent.RUNNING_PING_MISSED,
                        last_ping_at=self._last_ping_at,
                    )
                    if (
                        time.monotonic() - self._last_ping
                        > GeckoConfig.PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS
                    ):
                        await self._event_handler(
                            GeckoSpaEvent.RUNNING_PING_NO_RESPONSE,
                            last_ping_at=self._last_ping_at,
                        )

                # Ping every couple of seconds until we have had a response
                await config_sleep(
                    2
                    if self._last_ping_at is None
                    else GeckoConfig.PING_FREQUENCY_IN_SECONDS
                )

        except asyncio.CancelledError:
            _LOGGER.debug("Ping loop cancelled")
            raise

        except:  # noqa
            _LOGGER.exception("Exception in ping loop")
            raise

    def _get_status_block_handler_func(self) -> GeckoStatusBlockProtocolHandler:
        assert self._protocol is not None
        assert self.log_class is not None
        return GeckoStatusBlockProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(False),
            self.log_class.begin,
            self.log_class.end,
            parms=self.sendparms,
        )

    async def _refresh_loop(self) -> None:
        """The refresh loop is simply to ensure that our understanding
        of the live parts of the spastruct are always up-to-date. We
        shouldn't need to do this, but this is belt and braces stuff"""

        _LOGGER.debug("Refresh loop started")
        while self.isopen:
            await config_sleep(GeckoConfig.SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS)
            if not self.is_connected:
                continue
            if not self.is_responding_to_pings:
                continue
            if not await self.struct.get(
                self._protocol, self._get_status_block_handler_func
            ):
                await self._event_handler(
                    GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED
                )

            get_channel_handler = await self._protocol.get(
                self._get_channel_handler_func
            )
            if get_channel_handler is None:
                _LOGGER.error("Cannot get channel, protocol retry count exceeded")
                await self._event_handler(
                    GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED
                )
                continue

            self.channel = get_channel_handler.channel
            self.signal = get_channel_handler.signal_strength
            _LOGGER.debug("Refresh channel %s/%s", self.channel, self.signal)
            await self._event_handler(GeckoSpaEvent.RUNNING_SPA_PACK_REFRESHED)

    async def _async_on_partial_status_update(
        self,
        handler: GeckoAsyncPartialStatusBlockProtocolHandler,
        sender: tuple,
    ) -> None:
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])

    async def _on_async_set_value(self, pos, length, newvalue) -> None:
        assert self._protocol is not None
        if not self.is_connected:
            _LOGGER.warning("Cannot set value when spa not connected")
            return
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot set value when spa not responding to pings")
            return

        pack_command_handler = await self._protocol.get(
            lambda: GeckoPackCommandProtocolHandler.set_value(
                self._protocol.get_and_increment_sequence_counter(True),  # type: ignore
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
            _LOGGER.error("Cannot set value, protocol retry count exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED)

    def _on_set_value(self, pos, length, newvalue) -> None:
        self._taskman.add_task(
            self._on_async_set_value(pos, length, newvalue), "Set value task", "SPA"
        )

    @property
    def accessors(self) -> dict:
        return self.struct.accessors

    async def async_press(self, keypad) -> None:
        """Simulate a button press async"""
        assert self._protocol is not None
        if not self.is_connected:
            _LOGGER.warning("Cannot press keypad when spa not connected")
            return
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot press keypad when spa not responding to pings")
            return

        pack_command_handler = await self._protocol.get(
            lambda: GeckoPackCommandProtocolHandler.keypress(
                self._protocol.get_and_increment_sequence_counter(True),  # type: ignore
                self.pack_type,
                keypad,
                parms=self.sendparms,
            )
        )

        if pack_command_handler is None:
            _LOGGER.error("Cannot press keypad, protocol retry count exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED)

    def press(self, keypad) -> None:
        """Simulate a button press"""
        self._taskman.add_task(self.async_press(keypad), "Button press task", "SPA")

    def _get_watercare_handler_func(self) -> GeckoWatercareProtocolHandler:
        assert self._protocol is not None
        return GeckoWatercareProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(False),
            parms=self.sendparms,
        )

    async def _async_on_wcerr(
        self, handler: GeckoWatercareProtocolHandler, sender: tuple
    ) -> None:
        await self._event_handler(GeckoSpaEvent.RUNNING_SPA_WATER_CARE_ERROR)

    async def async_get_watercare(self) -> Optional[int]:
        if not self.is_connected:
            _LOGGER.warning("Cannot get watercare when spa not connected")
            return 0
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot get watercare when spa not responding to pings")
            return 0

        assert self._protocol is not None
        get_watercare_handler = await self._protocol.get(
            self._get_watercare_handler_func
        )

        if get_watercare_handler is None:
            _LOGGER.error("Cannot get watercare, protocol retry count exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED)
            return None

        return get_watercare_handler.mode

    async def async_set_watercare(self, new_mode) -> None:
        if not self.is_connected:
            _LOGGER.warning("Cannot set watercare when spa not connected")
            return
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot set watercare when spa not responding to pings")
            return

        assert self._protocol is not None
        set_watercare_handler = await self._protocol.get(
            lambda: GeckoWatercareProtocolHandler.set(
                self._protocol.get_and_increment_sequence_counter(False),  # type: ignore
                new_mode,
                parms=self.sendparms,
            )
        )

        if set_watercare_handler is None:
            _LOGGER.error("Cannot set version, protocol retry count exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED)

    def _get_reminders_handler_func(self) -> GeckoRemindersProtocolHandler:
        assert self._protocol is not None
        return GeckoRemindersProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(False),
            parms=self.sendparms,
        )

    async def async_get_reminders(self) -> List[Tuple]:
        if not self.is_connected:
            _LOGGER.warning("Cannot get reminders when spa not connected")
            return []
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot get reminders when spa not responding to pings")
            return []

        assert self._protocol is not None
        get_reminders_handler = await self._protocol.get(
            self._get_reminders_handler_func
        )

        if get_reminders_handler is None:
            _LOGGER.error("Cannot get reminders, protocol retry count exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED)
            return []

        return get_reminders_handler.reminders
