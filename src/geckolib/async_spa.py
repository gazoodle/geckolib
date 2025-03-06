"""GeckoAsyncSpa class."""

import asyncio
import importlib
import logging
import socket
import time
from datetime import UTC, datetime
from functools import partial
from types import ModuleType
from typing import Any

from geckolib.driver.accessor import GeckoStructAccessor
from geckolib.driver.protocol.reminders import GeckoReminderType
from geckolib.driver.protocol.watercare import GeckoSetWatercareModeProtocolHandler

from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_taskman import GeckoAsyncTaskMan
from .config import (
    GeckoConfig,
    config_sleep,
    release_config_change_waiters,
    set_config_mode,
)
from .const import GeckoConstants
from .driver import (
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoAsyncStructure,
    GeckoAsyncUdpProtocol,
    GeckoConfigFileProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoGetWatercareModeProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoRFErrProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoUnhandledProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareErrorHandler,
    Observable,
)
from .spa_events import GeckoSpaEvent

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncSpa(Observable):
    """
    GeckoAsyncSpa class.

    Manage an instance of a spa, and is the main point of contact for control and
    monitoring. Uses the declarations found in pack/* to build an object that
    exposes the properties and capabilities of your spa. This class should only
    be used via a Facade which hides the implementation details.
    """

    def __init__(
        self,
        client_id: bytes,
        spa_descriptor: GeckoAsyncSpaDescriptor,
        taskman: GeckoAsyncTaskMan,
        event_handler: GeckoSpaEvent.CallBack,
    ) -> None:
        """Initialize the spa class."""
        super().__init__()

        self.client_id = client_id
        self.descriptor = spa_descriptor
        self._taskman = taskman
        self._event_handler: GeckoSpaEvent.CallBack = event_handler

        self._con_lost: asyncio.Event = asyncio.Event()
        self._transport: asyncio.BaseTransport | None = None
        self._protocol: GeckoAsyncUdpProtocol | None = None
        self._is_connected = False

        self.intouch_version_en = ""
        self.intouch_version_co = ""

        self.channel = 0
        self.signal = 0

        self.config_version = 0
        self.log_version = 0

        self.pack_type = ""

        self.pack = None
        self.version = ""
        self.config_number = 0

        self.struct: GeckoAsyncStructure = GeckoAsyncStructure(self.async_on_set_value)
        self._last_ping_at: datetime | None = None
        self._needs_reload: bool = False

    @property
    def sendparms(self) -> tuple:
        """Get send parms suitable for the send() API."""
        return (
            self.descriptor.destination[0],
            self.descriptor.destination[1],
            self.descriptor.identifier,
            self.client_id,
        )

    @property
    def is_connected(self) -> bool:
        """Is this spa connected."""
        return self._is_connected

    @property
    def revision(self) -> str:
        """Get the revision of the spa pack structure."""
        assert self.struct.pack_class is not None  # noqa: S101
        return self.struct.pack_class.revision

    def _get_version_handler_func(self) -> GeckoVersionProtocolHandler:
        assert self._protocol is not None  # noqa: S101
        return GeckoVersionProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    def _get_channel_handler_func(self) -> GeckoGetChannelProtocolHandler:
        assert self._protocol is not None  # noqa: S101
        return GeckoGetChannelProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    def _get_config_file_handler_func(self) -> GeckoConfigFileProtocolHandler:
        assert self._protocol is not None  # noqa: S101
        return GeckoConfigFileProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    async def _async_on_rferr(
        self, handler: GeckoRFErrProtocolHandler, _sender: tuple
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
            set_config_mode(active=False)

    async def _async_import_module(
        self, loop: asyncio.AbstractEventLoop, module: str
    ) -> ModuleType:
        return await loop.run_in_executor(
            None, partial(importlib.import_module, module)
        )

    async def _connect(self) -> None:
        loop = asyncio.get_running_loop()
        self._con_lost.clear()

        self._transport, _protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(
                self._taskman,
                self._con_lost,
                (self.descriptor.destination[0], self.descriptor.destination[1]),
            ),
            family=socket.AF_INET,
        )
        assert isinstance(_protocol, GeckoAsyncUdpProtocol)  # noqa: S101
        self._protocol = _protocol
        await config_sleep(
            GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS,
            "Async spa connect - after protocol creation",
        )

        await self._connect_install_task_handlers()

        if not await self._connect_get_version():
            return

        get_channel_handler = await self._protocol.get(self._get_channel_handler_func)
        if get_channel_handler is None:
            _LOGGER.error("Cannot get channel, protocol retry time exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_TIME_EXCEEDED
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
        await config_sleep(
            GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS,
            "Async spa connect - after channel",
        )

        config_file_handler = await self._protocol.get(
            self._get_config_file_handler_func,
            None,
            4,
        )
        if config_file_handler is None:
            _LOGGER.error("Cannot get file, protocol retry time exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_TIME_EXCEEDED
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
        await config_sleep(
            GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS,
            "Async spa connect - after files",
        )

        if not await self._connect_load_pack(plateform_key):
            return

        await self._event_handler(GeckoSpaEvent.CONNECTION_INITIAL_DATA_BLOCK_REQUEST)
        await config_sleep(
            GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS,
            "Async spa connect - after initial block request",
        )

        if not await self.struct.get(
            self._protocol,
            lambda: GeckoStatusBlockProtocolHandler.full_request(
                self._protocol.get_and_increment_sequence_counter(),
                parms=self.sendparms,
            ),
            5,
        ):
            _LOGGER.error("Cannot get full struct, protocol retry time exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_TIME_EXCEEDED
            )

            return

        await self.struct.check_for_accessories()

        _LOGGER.debug("Status block was completed, so spa can be connected")

        self.struct.build_accessors()

        self.pack = self.accessors[GeckoConstants.KEY_PACK_TYPE].value
        if GeckoConstants.KEY_PACK_CORE_ID in self.accessors:
            self.version = (
                f"{self.accessors[GeckoConstants.KEY_PACK_CORE_ID].value}"
                f" v{self.accessors[GeckoConstants.KEY_PACK_CORE_REV].value}"
                f".{self.accessors[GeckoConstants.KEY_PACK_CORE_REL].value}"
            )
        else:
            self.version = (
                f"{self.accessors[GeckoConstants.KEY_PACK_CONFIG_ID].value}"
                f"v{self.accessors[GeckoConstants.KEY_PACK_CONFIG_REV].value}"
                f".{self.accessors[GeckoConstants.KEY_PACK_CONFIG_REL].value}"
            )

        if GeckoConstants.KEY_CONFIG_NUMBER in self.accessors:
            self.config_number = self.accessors[GeckoConstants.KEY_CONFIG_NUMBER].value

        self._connect_listen_too_critical_changes()

        self._is_connected = True
        self._needs_reload = False
        await self._event_handler(GeckoSpaEvent.CONNECTION_SPA_COMPLETE)
        _LOGGER.debug("Spa connected")

    async def _connect_install_task_handlers(self) -> None:
        if self._protocol is None:
            return

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
        await config_sleep(
            GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS,
            "Async spa connect - before version ",
        )

    async def _connect_get_version(self) -> bool:
        version_handler = await self._protocol.get(self._get_version_handler_func)
        if version_handler is None:
            _LOGGER.error("Cannot get version, protocol retry time exceeded")
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_TIME_EXCEEDED
            )
            return False

        self.intouch_version_en = (
            f"{version_handler.en_build}"
            f" v{version_handler.en_major}.{version_handler.en_minor}"
        )
        self.intouch_version_co = (
            f"{version_handler.co_build}"
            f" v{version_handler.co_major}.{version_handler.co_minor}"
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
        await config_sleep(
            GeckoConstants.CONNECTION_STEP_PAUSE_IN_SECONDS,
            "Async spa connect - After version",
        )

        return True

    async def _connect_load_pack(self, plateform_key: str) -> bool:
        try:
            await self.struct.load_pack_class(plateform_key)
        except ModuleNotFoundError as ex:
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_CANNOT_FIND_SPA_PACK, ex.args
            )
            return False

        try:
            await self.struct.load_config_module(self.config_version)
        except ModuleNotFoundError as ex:
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_CANNOT_FIND_CONFIG_VERSION, ex.args
            )
            return False

        try:
            await self.struct.load_log_module(self.log_version)
        except ModuleNotFoundError as ex:
            await self._event_handler(
                GeckoSpaEvent.CONNECTION_CANNOT_FIND_LOG_VERSION, ex.args
            )

        self.pack_type = self.struct.pack_class.plateform_type
        _LOGGER.debug(
            "Got spa configuration Type %s - CFG %s/LOG %s, now ask for initial "
            "status block",
            self.pack_type,
            self.config_version,
            self.log_version,
        )
        return True

    def _connect_listen_too_critical_changes(self) -> None:
        # Listen to critical data changes for reload
        if "PackType" in self.accessors:
            self.accessors["PackType"].watch(self._on_critical_info_changed)
        if "PackConfID" in self.accessors:
            self.accessors["PackConfID"].watch(self._on_critical_info_changed)
        if "PackConfigLib" in self.accessors:
            self.accessors["PackConfigLib"].watch(self._on_critical_info_changed)
        if "PackStatusLib" in self.accessors:
            self.accessors["PackStatusLib"].watch(self._on_critical_info_changed)
        for output in self.struct.all_outputs:
            self.accessors[output].watch(self._on_critical_info_changed)
        if "InMix-PackType" in self.accessors:
            self.accessors["InMix-PackType"].watch(self._on_critical_info_changed)
        if "InMix-NumberOfZones" in self.accessors:
            self.accessors["InMix-NumberOfZones"].watch(self._on_critical_info_changed)

    async def connect(self) -> None:
        """Wrap the connection with exception safety."""
        try:
            await self._connect()
        except Exception:
            _LOGGER.exception("Exception during spa connection")
            raise

    async def disconnect(self) -> None:
        """Disconnect the spa from the async protocol."""
        self._is_connected = False
        await self._event_handler(GeckoSpaEvent.RUNNING_SPA_DISCONNECTED)
        self.struct.reset()
        self._taskman.cancel_key_tasks("SPA")
        if self._protocol is not None:
            self._protocol.disconnect()
            self._protocol = None
        self._transport = None
        self.unwatch_all()
        self._needs_reload = False

    def _on_critical_info_changed(
        self, _sender: Any, _old_value: Any, _new_value: Any
    ) -> None:
        self._needs_reload = True
        release_config_change_waiters()

    @property
    def isopen(self) -> bool:
        """Return True if the spa has a UDP socket with the in.touch EN module."""
        if self._protocol is None:
            return False
        return self._protocol.isopen

    @property
    def is_responding_to_pings(self) -> bool:
        """Is the remote end responding to pings."""
        if self._last_ping is None:
            return False
        # Allow twice as much time as ping frequency to make sure boundary tests
        # are successful
        return (
            time.monotonic() - self._last_ping
        ) < GeckoConfig.PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS

    async def _async_on_packet(
        self, handler: GeckoPacketProtocolHandler, _sender: tuple
    ) -> None:
        if handler.parms == self.sendparms:
            assert self._protocol is not None  # noqa: S101
            assert handler.packet_content is not None  # noqa: S101
            self._protocol.datagram_received(handler.packet_content, handler.parms)
        else:
            _LOGGER.warning(
                "Dropping packet from %s because it didn't match %s",
                handler.parms,
                self.sendparms,
            )

    @property
    def last_ping_at(self) -> datetime | None:
        """The datetime of the last successful ping response or None."""
        return self._last_ping_at

    async def _ping_loop(self) -> None:
        _LOGGER.debug("Ping loop started")

        self._last_ping = time.monotonic()

        try:
            while self.isopen:
                assert self._protocol is not None  # noqa: S101
                ping_handler = await self._protocol.get(
                    lambda: GeckoPingProtocolHandler.request(parms=self.sendparms)
                )

                if ping_handler is not None:
                    self._last_ping = time.monotonic()
                    self._last_ping_at = datetime.now(tz=UTC)
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
                    else GeckoConfig.PING_FREQUENCY_IN_SECONDS,
                    "Async spa ping loop",
                )

        except asyncio.CancelledError:
            _LOGGER.debug("Ping loop cancelled")
            raise

        except:
            _LOGGER.exception("Exception in ping loop")
            raise

        finally:
            _LOGGER.debug("Ping loop finished")

    def _get_status_block_handler_func(self) -> GeckoStatusBlockProtocolHandler:
        assert self._protocol is not None  # noqa: S101
        assert self.struct.log_class is not None  # noqa: S101
        return GeckoStatusBlockProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            self.struct.log_class.begin,
            self.struct.log_class.end,
            parms=self.sendparms,
        )

    async def _refresh_loop(self) -> None:
        """
        Refresh Loop.

        The refresh loop is simply to ensure that our understanding
        of the live parts of the spastruct are always up-to-date. We
        shouldn't need to do this, but this is belt and braces stuff
        """
        try:
            _LOGGER.debug("Refresh loop started")
            while self.isopen:
                time_to_doit = await config_sleep(
                    GeckoConfig.SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS,
                    "Async spa refresh handler ",
                )
                if self._needs_reload:
                    await self._event_handler(GeckoSpaEvent.RUNNING_SPA_NEEDS_RELOAD)
                    continue
                if not self.is_connected:
                    continue
                if not self.is_responding_to_pings:
                    continue
                if not time_to_doit:
                    continue

                if False:
                    # Removed because I don't think this is required now that ping
                    # is back to 2 seconds. Time will tell.
                    if not await self.struct.get(
                        self._protocol,
                        self._get_status_block_handler_func,
                        5,
                    ):
                        await self._event_handler(
                            GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED
                        )

                assert self._protocol is not None  # noqa: S101
                get_channel_handler = await self._protocol.get(
                    self._get_channel_handler_func
                )
                if get_channel_handler is None:
                    _LOGGER.error("Cannot get channel, protocol retry time exceeded")
                    await self._event_handler(
                        GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_TIME_EXCEEDED
                    )
                    continue

                self.channel = get_channel_handler.channel
                self.signal = get_channel_handler.signal_strength
                _LOGGER.debug("Refresh channel %s/%s", self.channel, self.signal)
                await self._event_handler(GeckoSpaEvent.RUNNING_SPA_PACK_REFRESHED)

        except asyncio.CancelledError:
            _LOGGER.debug("Refresh loop cancelled")
            raise

        except Exception:
            _LOGGER.exception("Refresh loop caught exception")
            raise

    async def _async_on_partial_status_update(
        self,
        handler: GeckoAsyncPartialStatusBlockProtocolHandler,
        _sender: tuple,
    ) -> None:
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])

    async def async_on_set_value(self, pos: int, length: int, newvalue: Any) -> None:
        """Set the data block to a specific value."""
        try:
            assert self._protocol is not None  # noqa: S101
            if not self.is_connected:
                _LOGGER.warning("Cannot set value when spa not connected")
                return
            if not self.is_responding_to_pings:
                _LOGGER.debug("Cannot set value when spa not responding to pings")
                return

            pack_command_handler = await self._protocol.get(
                lambda: GeckoPackCommandProtocolHandler.set_value(
                    self._protocol.get_and_increment_sequence_counter(command=True),
                    self.pack_type,
                    self.config_version,
                    self.log_version,
                    pos,
                    length,
                    newvalue,
                    parms=self.sendparms,
                )
            )

            if pack_command_handler is not None:
                self.struct.replace_status_block_segment(
                    pos, GeckoStructAccessor.pack_data(length, newvalue)
                )
            else:
                _LOGGER.error("Cannot set value, protocol retry time exceeded")
                await self._event_handler(
                    GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED
                )

        except asyncio.CancelledError:
            _LOGGER.debug("Async set value cancelled")
            raise
        except Exception:
            _LOGGER.exception("Async set value caught exception")
            raise

    @property
    def accessors(self) -> dict:
        """Get the accessors dictionary for this spa."""
        return self.struct.accessors

    async def async_press(self, keypad: int) -> None:
        """Simulate a button press async."""
        try:
            assert self._protocol is not None  # noqa: S101
            if not self.is_connected:
                _LOGGER.warning("Cannot press keypad when spa not connected")
                return
            if not self.is_responding_to_pings:
                _LOGGER.debug("Cannot press keypad when spa not responding to pings")
                return
            _LOGGER.info("Async press of key %d", keypad)

            pack_command_handler = await self._protocol.get(
                lambda: GeckoPackCommandProtocolHandler.keypress(
                    self._protocol.get_and_increment_sequence_counter(command=True),
                    self.pack_type,
                    keypad,
                    parms=self.sendparms,
                )
            )

            if pack_command_handler is None:
                _LOGGER.error("Cannot press keypad, protocol retry time exceeded")
                await self._event_handler(
                    GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED
                )
        except asyncio.CancelledError:
            _LOGGER.debug("Async press cancelled")
            raise
        except Exception:
            _LOGGER.exception("Async press caught exception")
            raise

    def _get_watercare_handler_func(self) -> GeckoGetWatercareModeProtocolHandler:
        assert self._protocol is not None  # noqa: S101
        return GeckoGetWatercareModeProtocolHandler.get(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    async def _async_on_wcerr(
        self, _handler: GeckoWatercareErrorHandler, _sender: tuple
    ) -> None:
        await self._event_handler(GeckoSpaEvent.RUNNING_SPA_WATER_CARE_ERROR)

    async def async_get_watercare_mode(self) -> int | None:
        """Get the watercare mode."""
        if not self.is_connected:
            _LOGGER.warning("Cannot get watercare when spa not connected")
            return 0
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot get watercare when spa not responding to pings")
            return 0
        assert self._protocol is not None  # noqa: S101
        get_watercare_handler = await self._protocol.get(
            self._get_watercare_handler_func
        )

        if get_watercare_handler is None:
            _LOGGER.error("Cannot get watercare mode, protocol retry time exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED)
            return None

        return get_watercare_handler.mode

    async def async_set_watercare_mode(self, new_mode: int) -> None:
        """Set the watercare more."""
        if not self.is_connected:
            _LOGGER.warning("Cannot set watercare when spa not connected")
            return
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot set watercare when spa not responding to pings")
            return
        assert self._protocol is not None  # noqa: S101
        set_watercare_handler = await self._protocol.get(
            lambda: GeckoSetWatercareModeProtocolHandler.set(
                self._protocol.get_and_increment_sequence_counter(),
                new_mode,
                parms=self.sendparms,
            )
        )
        if set_watercare_handler is None:
            _LOGGER.error("Cannot set watercare mode, protocol retry time exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED)
        else:
            _LOGGER.debug("Spa responded with %d", set_watercare_handler.mode)

    def _get_reminders_handler_func(self) -> GeckoRemindersProtocolHandler:
        assert self._protocol is not None  # noqa: S101
        return GeckoRemindersProtocolHandler.request(
            self._protocol.get_and_increment_sequence_counter(),
            parms=self.sendparms,
        )

    async def async_get_reminders(self) -> list[tuple]:
        """Get the reminders."""
        if not self.is_connected:
            _LOGGER.warning("Cannot get reminders when spa not connected")
            return []
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot get reminders when spa not responding to pings")
            return []

        assert self._protocol is not None  # noqa: S101
        get_reminders_handler = await self._protocol.get(
            self._get_reminders_handler_func
        )

        if get_reminders_handler is None:
            _LOGGER.error("Cannot get reminders, protocol retry time exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED)
            return []

        return get_reminders_handler.reminders

    async def async_set_reminders(
        self, reminders: list[tuple[GeckoReminderType, int]]
    ) -> None:
        """Set the reminders."""
        if not self.is_connected:
            _LOGGER.warning("Cannot set reminders when spa not connected")
            return
        if not self.is_responding_to_pings:
            _LOGGER.debug("Cannot set reminders when spa not responding to pings")
            return
        assert self._protocol is not None  # noqa: S101
        set_reminders_handler = await self._protocol.get(
            lambda: GeckoRemindersProtocolHandler.set(
                self._protocol.get_and_increment_sequence_counter(),
                reminders,
                parms=self.sendparms,
            )
        )

        if set_reminders_handler is None:
            _LOGGER.error("Cannot set reminders, protocol retry time exceeded")
            await self._event_handler(GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED)

    def get_snapshot_data(self) -> dict:
        """Get the snapshot data for this spa."""
        data = self.struct.get_snapshot_data()
        data.update(
            {
                "intouch version EN": self.intouch_version_en,
                "intouch version CO": self.intouch_version_co,
            }
        )
        return data
