"""Gecko automation support for sensors."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from geckolib.driver import GeckoBoolStructAccessor
from geckolib.driver.accessor import GeckoStructAccessor

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoSensorBase(GeckoAutomationFacadeBase):
    """Base sensor allows non-accessor sensors to be implemented."""

    def __init__(
        self, facade: GeckoAsyncFacade, name: str, device_class: str | None = None
    ) -> None:
        """Initialize the sensor base."""
        super().__init__(facade, name, name.upper())
        self._device_class = device_class

    @property
    def state(self) -> Any | None:
        """The state of the sensor."""
        return None

    @property
    def unit_of_measurement(self) -> str | None:
        """The unit of measurement for the sensor, or None."""
        return None

    @property
    def device_class(self) -> str | None:
        """The device class."""
        return self._device_class

    def __repr__(self) -> str:
        """Get a string representation."""
        return f"{self.name}: {self.state}"


########################################################################################
class GeckoSensor(GeckoSensorBase):
    """
    Sensors wrapper.

    Take accessors state with extra units and device
    class properties
    """

    def __init__(
        self,
        facade: GeckoAsyncFacade,
        name: str,
        accessor: GeckoStructAccessor,
        unit_accessor: GeckoStructAccessor | str | None = None,
        device_class: str | None = None,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(facade, name, device_class)
        self._accessor = accessor
        # Bubble up change notification
        accessor.watch(self._on_change)
        self._unit_of_measurement_accessor = unit_accessor
        if isinstance(self._unit_of_measurement_accessor, GeckoStructAccessor):
            unit_accessor.watch(self._on_change)

    @property
    def state(self) -> Any:
        """The state of the sensor."""
        return self._accessor.value

    @property
    def unit_of_measurement(self) -> str | None:
        """The unit of measurement for the sensor, or None."""
        if isinstance(self._unit_of_measurement_accessor, GeckoStructAccessor):
            return self._unit_of_measurement_accessor.value
        return self._unit_of_measurement_accessor

    @property
    def accessor(self) -> GeckoStructAccessor:
        """Access the accessor member."""
        return self._accessor

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        return f"{self.accessor.tag}: {self.state}"


########################################################################################
class GeckoBinarySensor(GeckoSensor):
    """Binary sensors only have two states."""

    @property
    def is_on(self) -> bool:
        """Determine if the sensor is on or not."""
        state = self.state
        if isinstance(state, bool):
            return state
        if state == "":
            return False
        return state != "OFF"

    def __repr__(self) -> str:
        """Get string representation."""
        return f"{self.name}: {self.is_on}"


########################################################################################
class GeckoErrorSensor(GeckoSensorBase):
    """Error sensor aggregates all the error keys into a comma separated text string."""

    def __init__(
        self, facade: GeckoAsyncFacade, device_class: str | None = None
    ) -> None:
        """Initialise the error sensor class."""
        super().__init__(facade, "Error Sensor", device_class)
        self._state = "No errors or warnings"

        # Listen for changes to any of the error spapack accessors
        for accessor_key in facade.spa.struct.error_keys:
            accessor = facade.spa.struct.accessors[accessor_key]
            accessor.watch(self.update_state)

        # Force initial state
        self.update_state()

    @property
    def state(self) -> str:
        """The state of the sensor."""
        return self._state

    def update_state(
        self, _sender: Any = None, _old_value: Any = None, _new_value: Any = None
    ) -> None:
        """Update the state."""
        self._state = ""

        active_errors = [
            accessor
            for accessor_key, accessor in self.facade.spa.struct.accessors.items()
            if accessor_key in self.facade.spa.struct.error_keys
            and isinstance(accessor, GeckoBoolStructAccessor)
            and accessor.value is True
        ]

        if active_errors:
            self._state = ", ".join(err.tag for err in active_errors)
            _LOGGER.debug("Error sensor state is %s", self.state)
        else:
            self._state = "None"

        self._on_change(None, None, None)
