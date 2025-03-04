"""Gecko Water Heaters."""

from __future__ import annotations

import logging
from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from geckolib.automation.power import GeckoPower
from geckolib.const import GeckoConstants

from .sensors import GeckoBinarySensor, GeckoSensor

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoWaterHeaterAbstract(GeckoPower):
    """Abstract base for water heaters."""

    TEMP_CELCIUS = "°C"
    TEMP_FARENHEIGHT = "°F"

    @property
    @abstractmethod
    def current_operation(self) -> str:
        """Get the current operation."""

    @property
    @abstractmethod
    def temperature_unit(self) -> str:
        """Get the temperature unit."""

    @property
    @abstractmethod
    def current_temperature(self) -> float:
        """Get the current temperature."""

    @property
    @abstractmethod
    def target_temperature(self) -> float:
        """Get the target temperature."""

    @property
    @abstractmethod
    def min_temp(self) -> float:
        """Get the min temp."""

    @property
    @abstractmethod
    def max_temp(self) -> float:
        """Get the max temp."""


class GeckoWaterHeater(GeckoWaterHeaterAbstract):
    """Water Heater object based on Home Assistant Entity Type Climate."""

    MIN_TEMP_C = 15
    MAX_TEMP_C = 40
    MIN_TEMP_F = 59
    MAX_TEMP_F = 104

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the water heater class."""
        super().__init__(facade, "Heater", "HEAT")

        self._current_temperature_sensor = None
        self._target_temperature_sensor = None
        self._real_setpoint_sensor = None
        self._temperature_unit_accessor = None
        self._heating_action_sensor = None
        self._cooling_action_sensor = None
        self._min_temp_sensor = None
        self._max_temp_sensor = None
        self._temp_not_valid_sensor = None

        # Attempt to locate the various items needed from the spa accessors
        self._temperature_unit_accessor = self._spa.accessors[
            GeckoConstants.KEY_TEMP_UNITS
        ]
        if GeckoConstants.KEY_SETPOINT_G in self._spa.accessors:
            self._target_temperature_sensor = GeckoSensor(
                facade,
                "Target Temperature",
                self._spa.accessors[GeckoConstants.KEY_SETPOINT_G],
                self._temperature_unit_accessor,
            )
            self.set_availability(is_available=True)
        if GeckoConstants.KEY_DISPLAYED_TEMP_G in self._spa.accessors:
            self._current_temperature_sensor = GeckoSensor(
                facade,
                "Current Temperature",
                self._spa.accessors[GeckoConstants.KEY_DISPLAYED_TEMP_G],
                self._temperature_unit_accessor,
            )
            self.set_availability(is_available=True)
        if GeckoConstants.KEY_REAL_SETPOINT_G in self._spa.accessors:
            self._real_setpoint_sensor = GeckoSensor(
                facade,
                "Real Target Temperature",
                self._spa.accessors[GeckoConstants.KEY_REAL_SETPOINT_G],
                self._temperature_unit_accessor,
            )
            self.set_availability(is_available=True)

        self._heating_action_sensor = self._cooling_action_sensor = None
        if GeckoConstants.KEY_HEATING in self._spa.accessors:
            self._heating_action_sensor = GeckoBinarySensor(
                self.facade, "Heating", self._spa.accessors[GeckoConstants.KEY_HEATING]
            )
        if GeckoConstants.KEY_COOLINGDOWN in self._spa.accessors:
            self._cooling_action_sensor = GeckoBinarySensor(
                self.facade,
                "Cooling",
                self._spa.accessors[GeckoConstants.KEY_COOLINGDOWN],
            )
        if GeckoConstants.KEY_MIN_SETPOINT_G in self._spa.accessors:
            self._min_temp_sensor = GeckoSensor(
                self.facade,
                "Min Temperature",
                self._spa.accessors[GeckoConstants.KEY_MIN_SETPOINT_G],
                self._temperature_unit_accessor,
            )
        if GeckoConstants.KEY_MAX_SETPOINT_G in self._spa.accessors:
            self._max_temp_sensor = GeckoSensor(
                self.facade,
                "Max Temperature",
                self._spa.accessors[GeckoConstants.KEY_MAX_SETPOINT_G],
                self._temperature_unit_accessor,
            )
        if GeckoConstants.KEY_TEMP_NOT_VALID in self._spa.accessors:
            self._temp_not_valid_sensor = GeckoSensor(
                self.facade,
                "Temp Not Valid",
                self._spa.accessors[GeckoConstants.KEY_TEMP_NOT_VALID],
            )

        # Setup change observers
        for sensor in [
            self._current_temperature_sensor,
            self._target_temperature_sensor,
            self._real_setpoint_sensor,
            self._temperature_unit_accessor,
            self._heating_action_sensor,
            self._cooling_action_sensor,
            self._min_temp_sensor,
            self._max_temp_sensor,
            self._temp_not_valid_sensor,
        ]:
            if sensor is not None:
                sensor.watch(self._on_change)

        self._on_change(None, None, None)

    @property
    def target_temperature_sensor(self) -> GeckoSensor:
        """Get the target temperature sensor object."""
        return self._target_temperature_sensor

    @property
    def target_temperature(self) -> float:
        """Get the target temperature of the water."""
        return self._target_temperature_sensor.state

    async def async_set_target_temperature(self, new_temperature: float) -> None:
        """Set the target temperature of the water."""
        await self._target_temperature_sensor.accessor.async_set_value(new_temperature)

    @property
    def real_target_temperature(self) -> float:
        """Get the real target temperature (takes eco mode into account)."""
        if self._real_setpoint_sensor is not None:
            return self._real_setpoint_sensor.state
        return self.target_temperature

    @property
    def real_target_temperature_sensor(self) -> GeckoSensor:
        """Get the real target temperature sensor (takes eco mode into account)."""
        return self._real_setpoint_sensor

    @property
    def min_temp(self) -> float:
        """Get the minimum temperature of the water heater."""
        if self._min_temp_sensor is not None:
            return self._min_temp_sensor.state
        return (
            self.MIN_TEMP_C
            if self._temperature_unit_accessor.value == "C"
            else self.MIN_TEMP_F
        )

    @property
    def max_temp(self) -> float:
        """Get the maximum temperature of the water heater."""
        if self._max_temp_sensor is not None:
            return self._max_temp_sensor.state
        return (
            self.MAX_TEMP_C
            if self._temperature_unit_accessor.value == "C"
            else self.MAX_TEMP_F
        )

    @property
    def current_temperature(self) -> float:
        """Get the current temperature of the water."""
        return self._current_temperature_sensor.state

    @property
    def temperature_unit(self) -> str:
        """Get the temperature units for the water heater."""
        if self._temperature_unit_accessor.value == "C":
            return self.TEMP_CELCIUS
        return self.TEMP_FARENHEIGHT

    @property
    def current_temperature_sensor(self) -> GeckoSensor:
        """Get the current temperature sensor object."""
        return self._current_temperature_sensor

    async def async_set_temperature_unit(self, new_unit: str) -> None:
        """Set the temperature units for the water heater."""
        if new_unit in (self.TEMP_FARENHEIGHT, "f", "F"):
            await self._temperature_unit_accessor.async_set_value("F")
        else:
            await self._temperature_unit_accessor.async_set_value("C")

    @property
    def current_operation(self) -> str:  # noqa: PLR0911
        """Return the current operation of the water heater."""
        # If we have both sensors, then these are the arbiters
        if (
            self._heating_action_sensor is not None
            and self._cooling_action_sensor is not None
        ):
            if self._heating_action_sensor.is_on:
                return GeckoConstants.WATER_HEATER_HEATING
            if self._cooling_action_sensor.is_on:
                return GeckoConstants.WATER_HEATER_COOLING
            return GeckoConstants.WATER_HEATER_IDLE

        # Otherwise, we take what we can get
        if (
            self._heating_action_sensor is not None
            and self._heating_action_sensor.is_on
        ):
            return GeckoConstants.WATER_HEATER_HEATING
        if (
            self._cooling_action_sensor is not None
            and self._cooling_action_sensor.is_on
        ):
            return GeckoConstants.WATER_HEATER_COOLING

        # Finally, it's down to the actual temperatures
        if self.current_temperature < self.real_target_temperature:
            return GeckoConstants.WATER_HEATER_HEATING
        if self.current_temperature > self.real_target_temperature:
            return GeckoConstants.WATER_HEATER_COOLING
        return GeckoConstants.WATER_HEATER_IDLE

    def format_temperature(self, temperature: float) -> str:
        """Format a temperature value to a printable string."""
        return f"{temperature:.1f}{self.temperature_unit}"

    def __str__(self) -> str:
        """Stringize the class."""
        if self.is_available:
            return (
                f"{self.name}: Temperature "
                f"{self.format_temperature(self.current_temperature)}, SetPoint "
                f"{self.format_temperature(self.target_temperature)}, Real SetPoint "
                f"{self.format_temperature(self.real_target_temperature)}, Operation "
                f"{self.current_operation}"
            )
        return f"{self.name}: Not present"

    def _on_change(
        self, sender: Any = None, old_value: Any = None, new_value: Any = None
    ) -> None:
        if self._temp_not_valid_sensor is not None:
            self.set_availability(is_available=not self._temp_not_valid_sensor.state)
        return super()._on_change(sender, old_value, new_value)

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        return (
            f"HTR: {self.format_temperature(self.current_temperature)}"
            f" SET: {self.format_temperature(self.real_target_temperature)}"
        )
