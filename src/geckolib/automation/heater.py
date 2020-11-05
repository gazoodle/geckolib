""" Gecko Water Heaters """

from .base import GeckoAutomationBase
from .sensors import GeckoSensor
from ..const import GeckoConstants


class GeckoWaterHeater(GeckoAutomationBase):
    """ Water Heater object based on Home Assistant Entity Type WaterHeater """

    TEMP_CELCIUS = "°C"
    TEMP_FARENHEIGHT = "°F"

    def __init__(self, facade):
        super().__init__(facade, "Heater")
        self._min_temp = 20
        self._max_temp = 40
        self._current_operation = "Idle"
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

    @property
    def is_present(self):
        """ Determine if the heater is present from the config """
        return self._is_present

    @property
    def target_temperature(self):
        """ Get the target temperature of the water """
        return self._target_temperature_sensor.state

    def set_target_temperature(self, new_temperature):
        """ Set the target temperature of the water """
        self._target_temperature_sensor.accessor.value = new_temperature

    @property
    def min_temp(self):
        """ Get the minimum temperature of the water heater """
        return self._min_temp

    @property
    def max_temp(self):
        """ Get the maximum temperature of the water heater """
        return self._min_temp

    @property
    def current_temperature(self):
        """ Get the current temperature of the water """
        return self._current_temperature_sensor.state

    @property
    def temperature_unit(self):
        """ Get the temperature units for the water heater """
        if self._temperature_unit_accessor.value == "C":
            return self.TEMP_CELCIUS
        return self.TEMP_FARENHEIGHT

    def set_temperature_unit(self, new_unit):
        """ Set the temperature units for the water heater """
        if new_unit in (self.TEMP_FARENHEIGHT, "f", "F"):
            self._temperature_unit_accessor.value = "F"
        else:
            self._temperature_unit_accessor.value = "C"

    @property
    def current_operation(self):
        """ Return the current operation of the water heater """
        # Check the property bag to determine what is going on ...

        # Failing that, assume we know what is happening based on the temperature states ...
        return self._current_operation

    def format_temperature(self, temperature):
        """ Format a temperature value to a printable string """
        return "{0:.1f}{1}".format(temperature, self.temperature_unit)

    def __str__(self):
        if self._is_present:
            return "{0}: Temperature {1}, SetPoint {2}, Operation {3}".format(
                self.name,
                self.format_temperature(self.current_temperature),
                self.format_temperature(self.target_temperature),
                self.current_operation,
            )
        return "{0}: Not present".format(self.name)
