"""Class to manage the clienting of a Gecko in.touch2 enabled device."""

from __future__ import annotations

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Self

from .async_locator import GeckoAsyncLocator
from .async_spa import GeckoAsyncSpa
from .async_taskman import GeckoAsyncTaskMan
from .automation import (
    GeckoAsyncFacade,
    GeckoAutomationBase,
)
from .const import GeckoConstants
from .spa_events import GeckoSpaEvent
from .spa_state import GeckoSpaState

if TYPE_CHECKING:
    from datetime import datetime

    from .async_spa_descriptor import GeckoAsyncSpaDescriptor

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncSpaMan(ABC, GeckoAsyncTaskMan):
    """
    GeckoAsyncSpaMan class.

    Manage the lifetime of a connection to a spa.

    This class is deliberately an abstract because you must provide your own
    implementation to manage the essential events that are required during operation
    """

    class ReconnectButton(GeckoAutomationBase):
        """Perform reconnect of the spa."""

        def __init__(self, spaman: GeckoAsyncSpaMan) -> None:
            """Initialize the reconnect butto n class."""
            super().__init__(
                spaman.unique_id, "Reconnect", spaman.spa_name, "RECONNECT"
            )
            self._spaman = spaman

        async def async_press(self) -> None:
            """Press the button."""
            await self._spaman.async_reset()

    class PingSensor(GeckoAutomationBase):
        """Sensor with the last ping time, or None."""

        def __init__(self, spaman: GeckoAsyncSpaMan) -> None:
            """Initialize the ping sensor."""
            super().__init__(spaman.unique_id, "Last Ping", spaman.spa_name, "PING")
            self._spaman: GeckoAsyncSpaMan = spaman
            assert self._spaman.spa is not None  # noqa: S101
            self._spaman.spa.watch(self._on_spa_change)
            self._last_ping_at: datetime | None = self._spaman.spa.last_ping_at

        @property
        def state(self) -> datetime | None:
            """The state of the sensor."""
            return self._last_ping_at

        @property
        def unit_of_measurement(self) -> None:
            """The unit of measurement for the sensor, or None."""
            return None

        @property
        def device_class(self) -> str:
            """Device class for the ping sensor."""
            return "timestamp"

        def _on_spa_change(self, *_args: Any) -> None:
            assert self._spaman.spa is not None  # noqa: S101
            if self._last_ping_at == self._spaman.spa.last_ping_at:
                return
            self._last_ping_at = self._spaman.spa.last_ping_at
            self._on_change()

        def __repr__(self) -> str:
            """Get string representation."""
            return f"{self.name}: {self.state}"

    class StatusSensor(GeckoAutomationBase):
        """Sensor with the current state."""

        def __init__(self, spaman: GeckoAsyncSpaMan) -> None:
            """Initialize the status sensor class."""
            super().__init__(spaman.unique_id, "Status", spaman.spa_name, "STATUS")
            self._spaman: GeckoAsyncSpaMan = spaman
            self._state = "Unknown"
            self._last_state = GeckoSpaState.IDLE
            self._last_event = GeckoSpaEvent.SPA_MAN_ENTER

        @property
        def state(self) -> str:
            """The state of the sensor."""
            return self._state

        @property
        def unit_of_measurement(self) -> None:
            """The unit of measurement for the sensor, or None."""
            return None

        @property
        def device_class(self) -> str:
            """Get the device class."""
            return "string"

        @property
        def last_event(self) -> GeckoSpaEvent:
            """Return the last event the sensor was notified of."""
            return self._last_event

        @property
        def spa_state(self) -> GeckoSpaState:
            """Returns the state of the spa at the time of the last event."""
            return self._last_state

        def on_event(self, event: GeckoSpaEvent) -> None:
            """Event handler."""
            self._last_event = event
            self._last_state = self._spaman.spa_state
            self._state = GeckoSpaState.to_string(self.spa_state)
            self._on_change()

        def __repr__(self) -> str:
            """Get string representation."""
            return f"{self.name}: {self.state}"

    class RadioConnectionSensor(GeckoAutomationBase):
        """Sensor with the current radio connection data."""

        def __init__(self, spaman: GeckoAsyncSpaMan) -> None:
            """Initialise the radio sensor class."""
            super().__init__(spaman.unique_id, "RF Signal", spaman.spa_name, "RADIO")
            self.signal: int = 0
            self.set_signal(spaman.spa.signal)

        def set_signal(self, signal: int) -> None:
            """Set signal nstrength."""
            self.signal = signal
            self.signal = min(self.signal, 100)

        @property
        def state(self) -> int:
            """The state of the sensor."""
            return self.signal

        @property
        def device_class(self) -> None:
            """Get the device class."""
            return None

        @property
        def unit_of_measurement(self) -> str:
            """The unit of measurement for the sensor, or None."""
            return "%"

        def __repr__(self) -> str:
            """Get the string representation."""
            return f"{self.name}: {self.state}{self.unit_of_measurement}"

    class RadioChannelSensor(GeckoAutomationBase):
        """Sensor with the current radio connection data."""

        def __init__(self, spaman: GeckoAsyncSpaMan) -> None:
            """Initialize the radio channel sensor."""
            super().__init__(spaman.unique_id, "RF Channel", spaman.spa_name, "CHANNEL")
            self.channel: int = 0
            self.set_channel(spaman.spa.channel)

        def set_channel(self, channel: int) -> None:
            """Set the radio channel."""
            self.channel = channel

        @property
        def state(self) -> int:
            """The state of the sensor."""
            return self.channel

        @property
        def device_class(self) -> None:
            """Get the device class."""
            return None

        @property
        def unit_of_measurement(self) -> None:
            """The unit of measurement for the sensor, or None."""
            return None

        def __repr__(self) -> str:
            """Get the string representation."""
            return f"{self.name}: {self.state}"

    def __init__(self, client_uuid: str, **kwargs: str) -> None:
        """
        Initialize a SpaMan class.

        The preferred pattern is to derive a class from SpaMan and then use it in
        an async with

        ```async with MySpaMan(client_uuid, **kwargs) as SpaMan:```

        If you leave **kwargs empty, then you are responsible for co-ordinating calls
        to methods such as async_locate_spas, async_connect_to_spa and async_connect.

        **kwargs can contain the following items

            spa_address:    The IP address of the spa. Useful if the spa is on a sub-net
            spa_identifier: The ID of a spa (as a string)
            spa_name:       The name of the spa. Useful for status feedback when spa
                            cannot be contacted

        If any of the **kwargs are provided then the spam manager will automatically
        run the sequence discover and connect
        """
        GeckoAsyncTaskMan.__init__(self)
        self._client_id = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)

        # Optional parameters as supplied from config
        self._spa_address: str | None = kwargs.get("spa_address")
        if self._spa_address == "":
            self._spa_address = None
        self._spa_identifier: str | None = kwargs.get("spa_identifier")
        if self._spa_identifier == "":
            self._spa_identifier = None
        self._spa_name: str | None = kwargs.get("spa_name")
        if self._spa_name == "":
            self._spa_name = None

        self._spa_descriptors: list[GeckoAsyncSpaDescriptor] | None = None
        self._has_descriptors = asyncio.Event()
        self._facade: GeckoAsyncFacade | None = None
        self._facade_state_known = asyncio.Event()
        self._spa: GeckoAsyncSpa | None = None
        self._state_change = asyncio.Event()
        self.set_spa_state(GeckoSpaState.IDLE)

        self._status_sensor: GeckoAsyncSpaMan.StatusSensor | None = None
        self._reconnect_button: GeckoAsyncSpaMan.ReconnectButton | None = None
        self._ping_sensor: GeckoAsyncSpaMan.PingSensor | None = None
        self._radio_sensor: GeckoAsyncSpaMan.RadioConnectionSensor | None = None
        self._channel_sensor: GeckoAsyncSpaMan.RadioChannelSensor | None = None

    ########################################################################
    #
    #   Usage helpers
    #

    async def __aenter__(self) -> Self:
        """Support 'with'."""
        await GeckoAsyncTaskMan.__aenter__(self)
        await self._handle_event(GeckoSpaEvent.SPA_MAN_ENTER)
        self.add_task(self._sequence_pump(), "Sequence Pump", "SPAMAN")
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        """Support 'with'."""
        self.cancel_key_tasks("SPAMAN")
        await self._handle_event(GeckoSpaEvent.SPA_MAN_EXIT, exc_info=exc_info)
        await GeckoAsyncTaskMan.__aexit__(self, exc_info)

    ########################################################################
    #
    #   Public methods
    #

    async def async_reset(self) -> None:
        """Reset the spa manager."""
        try:
            self._spa_descriptors = None
            self._has_descriptors.clear()
            if self._facade is not None:
                await self._facade.disconnect()
                self._facade = None
                self._facade_state_known.clear()
            if self._spa is not None:
                await self._spa.disconnect()
                self._spa = None
            self.set_spa_state(GeckoSpaState.IDLE)
        except Exception:
            _LOGGER.exception("Exception during reset")
            raise

    async def async_locate_spas(
        self, spa_address: str | None = None, spa_identifier: str | None = None
    ) -> list[GeckoAsyncSpaDescriptor] | None:
        """
        Locate spas on this network.

        This API will return a list of GeckoAsyncSpaDescriptor that were
        found on the network. If there are none found, then the return will be
        None. Events will be issued as the locating process proceeds
        """
        try:
            await self._handle_event(GeckoSpaEvent.LOCATING_STARTED)
            locator = GeckoAsyncLocator(
                self,
                self._handle_event,
                spa_address=spa_address,
                spa_identifier=spa_identifier,
            )
            await locator.discover()
            self._spa_descriptors = locator.spas
            self._has_descriptors.set()
            del locator

        finally:
            await self._handle_event(
                GeckoSpaEvent.LOCATING_FINISHED,
                spa_descriptors=self._spa_descriptors,
            )

        return self._spa_descriptors

    async def async_connect_to_spa(
        self, spa_descriptor: GeckoAsyncSpaDescriptor | None
    ) -> GeckoAsyncFacade | None:
        """
        Connect to spa.

        This API will connect to the specified spa using the supplied descriptor.
        """
        assert self._facade is None  # noqa: S101
        if spa_descriptor is None:
            await self._handle_event(GeckoSpaEvent.SPA_NOT_FOUND)
            return None

        try:
            self._spa_name = spa_descriptor.name
            if spa_descriptor.identifier is not None:
                self._spa_identifier = spa_descriptor.identifier_as_string
            await self._handle_event(GeckoSpaEvent.CONNECTION_STARTED)
            self._spa = GeckoAsyncSpa(
                self._client_id, spa_descriptor, self, self._handle_event
            )
            await self._spa.connect()
            # Check state now
            if self.spa_state == GeckoSpaState.SPA_READY:
                self._facade = GeckoAsyncFacade(self._spa, self)
                self._facade_state_known.set()

        finally:
            await self._handle_event(
                GeckoSpaEvent.CONNECTION_FINISHED, facade=self._facade
            )

        return self._facade

    async def async_connect(
        self, spa_identifier: str, spa_address: str | None = None
    ) -> GeckoAsyncFacade | None:
        """
        Connect to spa.

        This API will connect to the specified spa by doing a search with the
        supplied information. This is probably the API most commonly used by
        automation systems to avoid storing too much information in configuration
        """
        _LOGGER.debug("async_connect: ID:%s ADDR:%s", spa_identifier, spa_address)

        spa_descriptors = await self.async_locate_spas(spa_address, spa_identifier)

        assert spa_descriptors is not None  # noqa: S101
        if len(spa_descriptors) == 0:
            await self._handle_event(
                GeckoSpaEvent.SPA_NOT_FOUND,
                spa_address=spa_address,
                spa_identifier=spa_identifier,
            )
            return None

        return await self.async_connect_to_spa(spa_descriptors[0])

    async def async_set_spa_info(
        self,
        spa_address: str | None,
        spa_identifier: str | None,
        spa_name: str | None,
    ) -> None:
        """
        Set the spa information.

        Allows the sequence pump can run the locate and
        connect phases.
        """
        _LOGGER.debug(
            "set_spa_info: ADDR:%s ID:%s NAME:%s", spa_address, spa_identifier, spa_name
        )
        self._spa_address = spa_address
        self._spa_identifier = spa_identifier
        self._spa_name = spa_name
        await self.async_reset()

    async def wait_for_descriptors(self) -> None:
        """Wait for descriptors to be available."""
        await self._has_descriptors.wait()

    async def wait_for_facade(self) -> bool:
        """Wait for facade to be available."""
        await self._facade_state_known.wait()
        return self._facade is not None

    ########################################################################
    #
    #   Properties
    #

    @property
    def unique_id(self) -> str:
        """A unique id for the spa manager."""
        assert self._spa_identifier is not None  # noqa: S101
        return f"{self._spa_identifier.replace(':', '')}"

    @property
    def spa_name(self) -> str:
        """The name of the spa being managed."""
        assert self._spa_name is not None  # noqa: S101
        return self._spa_name

    @property
    def spa_descriptors(self) -> list[GeckoAsyncSpaDescriptor] | None:
        """Get a list of the discovered spas, or None."""
        return self._spa_descriptors

    @property
    def facade(self) -> GeckoAsyncFacade | None:
        """Get the connected facade, or None."""
        return self._facade

    @property
    def spa(self) -> GeckoAsyncSpa | None:
        """Get the spa, or None."""
        return self._spa

    @property
    def spa_state(self) -> GeckoSpaState:
        """Get the spa state."""
        return self._spa_state

    def set_spa_state(self, state: GeckoSpaState) -> None:
        """Set the spa state."""
        _LOGGER.debug("Spa state set to %s", state)
        self._spa_state = state
        self._state_change.set()

    @property
    def status_sensor(self) -> GeckoAsyncSpaMan.StatusSensor | None:
        """Get the status sensor."""
        return self._status_sensor

    @property
    def radio_sensor(self) -> GeckoAsyncSpaMan.RadioConnectionSensor | None:
        """Get the radio sensor."""
        return self._radio_sensor

    @property
    def channel_sensor(self) -> GeckoAsyncSpaMan.RadioChannelSensor | None:
        """Get the channel sensor."""
        return self._channel_sensor

    @property
    def reconnect_button(self) -> GeckoAsyncSpaMan.ReconnectButton | None:
        """Get the reconnect button."""
        return self._reconnect_button

    @property
    def ping_sensor(self) -> GeckoAsyncSpaMan.PingSensor | None:
        """Get the ping sensor."""
        return self._ping_sensor

    def __str__(self) -> str:
        """Get the stringized version."""
        return GeckoSpaState.to_string(self.spa_state)

    ########################################################################
    #
    #   Abstract methods
    #
    @abstractmethod
    async def handle_event(self, event: GeckoSpaEvent, **_kwargs: Any) -> None:
        """Handle the event."""

    ########################################################################
    #
    #   Private methods
    #

    async def _handle_event(self, event: GeckoSpaEvent, **kwargs: Any) -> None:  # noqa: PLR0912, PLR0915
        if (
            self._status_sensor is None
            and self._spa_identifier is not None
            and self._spa_name is not None
        ):
            self._status_sensor = GeckoAsyncSpaMan.StatusSensor(self)
            await self._handle_event(GeckoSpaEvent.CLIENT_HAS_STATUS_SENSOR)

        # Do any pre-processing of the event, such as setting the state or
        # updating the status line
        if event == GeckoSpaEvent.LOCATING_STARTED:
            self.set_spa_state(GeckoSpaState.LOCATING_SPAS)

        elif event == GeckoSpaEvent.LOCATING_FINISHED:
            self.set_spa_state(GeckoSpaState.LOCATED_SPAS)

        elif event == GeckoSpaEvent.SPA_NOT_FOUND:
            self._reconnect_button = GeckoAsyncSpaMan.ReconnectButton(self)
            await self._handle_event(GeckoSpaEvent.CLIENT_HAS_RECONNECT_BUTTON)
            self.set_spa_state(GeckoSpaState.ERROR_SPA_NOT_FOUND)

        elif event == GeckoSpaEvent.CONNECTION_STARTED:
            self.set_spa_state(GeckoSpaState.CONNECTING)
            self._reconnect_button = GeckoAsyncSpaMan.ReconnectButton(self)
            await self._handle_event(GeckoSpaEvent.CLIENT_HAS_RECONNECT_BUTTON)

        elif event == GeckoSpaEvent.CONNECTION_GOT_CHANNEL:
            self._ping_sensor = GeckoAsyncSpaMan.PingSensor(self)
            self._radio_sensor = GeckoAsyncSpaMan.RadioConnectionSensor(self)
            self._channel_sensor = GeckoAsyncSpaMan.RadioChannelSensor(self)
            await self._handle_event(GeckoSpaEvent.CLIENT_HAS_PING_SENSOR)

        elif event == GeckoSpaEvent.CONNECTION_SPA_COMPLETE:
            self.set_spa_state(GeckoSpaState.SPA_READY)

        elif event == GeckoSpaEvent.CONNECTION_FINISHED:
            if self._facade is not None:
                self.set_spa_state(GeckoSpaState.CONNECTED)
                await self._handle_event(GeckoSpaEvent.CLIENT_FACADE_IS_READY)

        elif event == GeckoSpaEvent.RUNNING_PING_NO_RESPONSE:
            if self.spa_state == GeckoSpaState.CONNECTED:
                self.set_spa_state(GeckoSpaState.ERROR_PING_MISSED)
                await self._handle_event(GeckoSpaEvent.CLIENT_FACADE_TEARDOWN)

        elif event == GeckoSpaEvent.RUNNING_PING_RECEIVED:
            if self.spa_state in (
                GeckoSpaState.ERROR_PING_MISSED,
                GeckoSpaState.ERROR_RF_FAULT,
                GeckoSpaState.ERROR_NEEDS_ATTENTION,
            ):
                await self.async_reset()

        elif event == GeckoSpaEvent.RUNNING_SPA_NEEDS_RELOAD:
            await self.async_reset()

        elif event == GeckoSpaEvent.ERROR_RF_ERROR:
            if self.spa_state == GeckoSpaState.CONNECTED:
                self.set_spa_state(GeckoSpaState.ERROR_RF_FAULT)
                await self._handle_event(GeckoSpaEvent.CLIENT_FACADE_TEARDOWN)

        elif event == GeckoSpaEvent.RUNNING_SPA_DISCONNECTED:
            if self.spa_state == GeckoSpaState.CONNECTED:
                self.set_spa_state(GeckoSpaState.IDLE)
                await self._handle_event(GeckoSpaEvent.CLIENT_FACADE_TEARDOWN)

        elif event == GeckoSpaEvent.RUNNING_SPA_PACK_REFRESHED:
            self._radio_sensor.set_signal(self._spa.signal)
            self._channel_sensor.set_channel(self._spa.channel)

        elif event in (
            GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_TIME_EXCEEDED,
            GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED,
            GeckoSpaEvent.ERROR_TOO_MANY_RF_ERRORS,
        ):
            self.set_spa_state(GeckoSpaState.ERROR_NEEDS_ATTENTION)

        elif event == GeckoSpaEvent.RUNNING_SPA_WATER_CARE_ERROR:
            assert self.facade is not None  # noqa: S101
            assert self._spa is not None  # noqa: S101
            self.facade.water_care.change_watercare_mode(
                await self._spa.async_get_watercare_mode()
            )

        if self._status_sensor is not None:
            self._status_sensor.on_event(event)

        # Call the abstract method to allow derived classes to do useful work
        # such as disconnecting handlers when the spa needs to reconnect
        # after protocol failure
        await self.handle_event(event, **kwargs)

        # Any post-processing goes here

    async def _sequence_pump(self) -> None:
        """
        SpaMan sequence pump loop.

        This class coordinates running the manager from the
        parameterized constructor and machine state.
        """
        _LOGGER.debug("SpaMan sequence pump started")

        try:
            while True:
                await self._state_change.wait()
                self._state_change.clear()

                if (
                    self.spa_state == GeckoSpaState.IDLE
                    and self._spa_descriptors is None
                ):
                    _LOGGER.debug("Sequence pump did locate")
                    await self.async_locate_spas(self._spa_address)

                if (
                    self.spa_state == GeckoSpaState.LOCATED_SPAS
                    and self._spa_identifier is not None
                    and self._facade is None
                ):
                    _LOGGER.debug("Sequence pump did connect")
                    if self._spa_descriptors is not None:
                        await self.async_connect_to_spa(
                            next(
                                (
                                    d
                                    for d in self._spa_descriptors
                                    if d.identifier_as_string == self._spa_identifier
                                ),
                                None,
                            )
                        )
                    else:
                        await self.async_connect(
                            self._spa_identifier, self._spa_address
                        )

        except asyncio.CancelledError:
            _LOGGER.debug("Spaman sequence pump cancelled")
            raise
        except Exception:
            _LOGGER.exception("Sequence pump caught exception")
            raise
