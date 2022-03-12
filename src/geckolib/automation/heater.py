""" Gecko Water Heaters """

from .base import GeckoAutomationFacadeBase
from .sensors import GeckoSensor, GeckoBinarySensor
from ..const import GeckoConstants


class GeckoWaterHeater(GeckoAutomationFacadeBase):
    """Water Heater object based on Home Assistant Entity Type Climate"""

    TEMP_CELCIUS = "°C"
    TEMP_FARENHEIGHT = "°F"

    MIN_TEMP_C = 15
    MAX_TEMP_C = 40
    MIN_TEMP_F = 59
    MAX_TEMP_F = 104

    def __init__(self, facade):
        super().__init__(facade, "Heater", "HEAT")
        self._is_present = False

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
            self._is_present = True
        if GeckoConstants.KEY_DISPLAYED_TEMP_G in self._spa.accessors:
            self._current_temperature_sensor = GeckoSensor(
                facade,
                "Current Temperature",
                self._spa.accessors[GeckoConstants.KEY_DISPLAYED_TEMP_G],
                self._temperature_unit_accessor,
            )
            self._is_present = True
        if GeckoConstants.KEY_REAL_SETPOINT_G in self._spa.accessors:
            self._real_setpoint_sensor = GeckoSensor(
                facade,
                "Real Target Temperature",
                self._spa.accessors[GeckoConstants.KEY_REAL_SETPOINT_G],
                self._temperature_unit_accessor,
            )
            self._is_present = True

        self._heating_action_sensor = self._cooling_action_sensor = None
        if GeckoConstants.KEY_HEATING in self._spa.accessors:
            self._heating_action_sensor = GeckoBinarySensor(
                self, "Heating", self._spa.accessors[GeckoConstants.KEY_HEATING]
            )
        if GeckoConstants.KEY_COOLINGDOWN in self._spa.accessors:
            self._cooling_action_sensor = GeckoBinarySensor(
                self, "Cooling", self._spa.accessors[GeckoConstants.KEY_COOLINGDOWN]
            )

        # Setup change observers
        for sensor in [
            self._current_temperature_sensor,
            self._target_temperature_sensor,
            self._real_setpoint_sensor,
            self._temperature_unit_accessor,
            self._heating_action_sensor,
            self._cooling_action_sensor,
        ]:
            if sensor is not None:
                sensor.watch(self._on_change)

    @property
    def is_present(self):
        """Determine if the heater is present from the config"""
        return self._is_present

    @property
    def target_temperature(self):
        """Get the target temperature of the water"""
        return self._target_temperature_sensor.state

    def set_target_temperature(self, new_temperature):
        """Set the target temperature of the water"""
        self._target_temperature_sensor.accessor.value = new_temperature

    async def async_set_target_temperature(self, new_temperature):
        """Set the target temperature of the water"""
        await self._target_temperature_sensor.accessor.async_set_value(new_temperature)

    @property
    def real_target_temperature(self):
        """Get the real target temperature (takes economy mode into account)"""
        return self._real_setpoint_sensor.state

    @property
    def min_temp(self):
        """Get the minimum temperature of the water heater"""
        return (
            self.MIN_TEMP_C
            if self._temperature_unit_accessor.value == "C"
            else self.MIN_TEMP_F
        )

    @property
    def max_temp(self):
        """Get the maximum temperature of the water heater"""
        return (
            self.MAX_TEMP_C
            if self._temperature_unit_accessor.value == "C"
            else self.MAX_TEMP_F
        )

    @property
    def current_temperature(self):
        """Get the current temperature of the water"""
        return self._current_temperature_sensor.state

    @property
    def temperature_unit(self):
        """Get the temperature units for the water heater"""
        if self._temperature_unit_accessor.value == "C":
            return self.TEMP_CELCIUS
        return self.TEMP_FARENHEIGHT

    def set_temperature_unit(self, new_unit):
        """Set the temperature units for the water heater"""
        if new_unit in (self.TEMP_FARENHEIGHT, "f", "F"):
            self._temperature_unit_accessor.value = "F"
        else:
            self._temperature_unit_accessor.value = "C"

    async def async_set_temperature_unit(self, new_unit):
        """Set the temperature units for the water heater"""
        if new_unit in (self.TEMP_FARENHEIGHT, "f", "F"):
            await self._temperature_unit_accessor.async_set_value("F")
        else:
            await self._temperature_unit_accessor.async_set_value("C")

    @property
    def current_operation(self):
        """Return the current operation of the water heater"""

        # If we have both sensors, then these are the arbiters
        if (
            self._heating_action_sensor is not None
            and self._cooling_action_sensor is not None
        ):
            if self._heating_action_sensor.is_on:
                return GeckoConstants.WATER_HEATER_HEATING
            elif self._cooling_action_sensor.is_on:
                return GeckoConstants.WATER_HEATER_COOLING
            else:
                return GeckoConstants.WATER_HEATER_IDLE

        # Otherwise, we take what we can get
        if self._heating_action_sensor is not None:
            if self._heating_action_sensor.is_on:
                return GeckoConstants.WATER_HEATER_HEATING
        if self._cooling_action_sensor is not None:
            if self._cooling_action_sensor.is_on:
                return GeckoConstants.WATER_HEATER_COOLING

        # Finally, it's down to the actual temperatures
        if self.current_temperature < self.real_target_temperature:
            return GeckoConstants.WATER_HEATER_HEATING
        elif self.current_temperature > self.real_target_temperature:
            return GeckoConstants.WATER_HEATER_COOLING
        return GeckoConstants.WATER_HEATER_IDLE

    def format_temperature(self, temperature):
        """Format a temperature value to a printable string"""
        return f"{temperature:.1f}{self.temperature_unit}"

    def __str__(self):
        if self._is_present:
            return (
                f"{self.name}: Temperature "
                f"{self.format_temperature(self.current_temperature)}, SetPoint "
                f"{self.format_temperature(self.target_temperature)}, Real SetPoint "
                f"{self.format_temperature(self.real_target_temperature)}, Operation "
                f"{self.current_operation}"
            )
        return f"{self.name}: Not present"

    @property
    def monitor(self):
        return f"HTR: {self.format_temperature(self.current_temperature)} SET: {self.format_temperature(self.real_target_temperature)}"
