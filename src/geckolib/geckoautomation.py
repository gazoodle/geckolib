#!/usr/bin/python3
'''
    Automation interface classes. Designed to abstract away the Gecko implementation details
    so that home automation systems can trivially utilise this library
'''
#
# Copyright (C) 2020, Gazoodle (https://github.com/gazoodle)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Inspiration from https://developers.home-assistant.io/docs/core/entity

#
# Automation interface facade classes for geckolib
#

import logging
from geckolib import GeckoConstants

# Module logger, uses the library name (at this time it was geckoautomation) and it
# is silent unless required ...
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

###################################################################################################
class GeckoAutomationBase:
    ''' Base of all the automation helper classes '''

    def __init__(self, facade, name):
        self._facade = facade
        self._spa = facade._spa
        self._name = name

    @property
    def name(self):
        ''' All automation items have a name '''
        return self._name

###################################################################################################
class GeckoSensor(GeckoAutomationBase):
    ''' Sensors wrap accessors state with extra units and device
        class properties '''

    def __init__(self, facade, name, accessor, unit_accessor=None):
        super().__init__(facade, name)
        self._accessor = accessor
        self._unit_of_measurement_accessor = unit_accessor
        self._device_class = None

    @property
    def state(self):
        ''' The state of the sensor '''
        return self._accessor.value

    @property
    def unit_of_measurement(self):
        ''' The unit of measurement for the sensor, or None '''
        if self._unit_of_measurement_accessor is None:
            return None
        return self._unit_of_measurement_accessor.value

    @property
    def device_class(self):
        ''' The device class '''
        return self._device_class

    @property
    def accessor(self):
        ''' Access the accessor member '''
        return self._accessor

###################################################################################################
class GeckoBinarySensor(GeckoSensor):
    ''' Binary sensors only have two states '''

###################################################################################################
class GeckoSwitch(GeckoAutomationBase):
    ''' A switch can turn something on or off, and can report the current state '''

    def __init__(self, facade, key, props):
        ''' props is a tuple of (name, keypad_button, state_key, device_class) '''
        super().__init__(facade, props[0])
        self.ui_key = key
        self._state_sensor = GeckoSensor(facade, "{0} State".format(props[0]),
                                         self._spa.accessors[props[2]])
        self._keypad_button = props[1]
        self.device_class = props[3]

    @property
    def is_on(self):
        ''' True if the device is ON, False otherwise '''
        return self._state_sensor.state != "OFF"

    def turn_on(self):
        ''' Turn the device ON, but does nothing if it is already ON '''
        logger.debug("%s turn ON", self.name)
        if self.is_on:
            logger.debug("%s request to turn ON ignored, it's already on!", self.name)
            return
        self._spa.press(self._keypad_button)

    def turn_off(self):
        ''' Turn the device OFF, but does nothing if it is already OFF '''
        logger.debug("%s turn OFF", self.name)
        if not self.is_on:
            logger.debug("%s request to turn OFF ignored, it's already off!", self.name)
            return
        self._spa.press(self._keypad_button)

    def __str__(self):
        return "{0}: {1}".format(self.name, self._state_sensor.state)

###################################################################################################
class GeckoPump(GeckoSwitch):
    ''' Pumps are based on switches, but might have variable speeds too '''

###################################################################################################
class GeckoBlower(GeckoSwitch):
    ''' Blowers are based on switches, but might have variable speeds too. They pump air,
        not water '''

###################################################################################################
class GeckoLight(GeckoSwitch):
    ''' Lights are based on switches, but might have brightness and colours as options '''

###################################################################################################
class GeckoWaterHeater(GeckoAutomationBase):
    ''' Water Heater object based on Home Assistant Entity Type WaterHeater '''

    TEMP_CELCIUS = "°C"
    TEMP_FARENHEIGHT = "°F"

    def __init__(self, facade):
        super().__init__(facade, "Heater")
        self._min_temp = 20
        self._max_temp = 40
        self._current_operation = "Idle"
        self._is_present = False

        # Attempt to locate the various items needed from the spa accessors
        self._temperature_unit_accessor = self._spa.accessors[GeckoConstants.KEY_TEMP_UNITS]
        if GeckoConstants.KEY_SETPOINT_G in self._spa.accessors:
            self._target_temperature_sensor = \
                GeckoSensor(facade,
                            "Target Temperature",
                            self._spa.accessors[GeckoConstants.KEY_SETPOINT_G],
                            self._temperature_unit_accessor)
            self._is_present = True
        if GeckoConstants.KEY_DISPLAYED_TEMP_G in self._spa.accessors:
            self._current_temperature_sensor = \
                GeckoSensor(facade,
                            "Current Temperature",
                            self._spa.accessors[GeckoConstants.KEY_DISPLAYED_TEMP_G],
                            self._temperature_unit_accessor)
            self._is_present = True

    @property
    def is_present(self):
        ''' Determine if the heater is present from the config '''
        return self._is_present

    @property
    def target_temperature(self):
        ''' Get the target temperature of the water '''
        return self._target_temperature_sensor.state

    def set_target_temperature(self, new_temperature):
        ''' Set the target temperature of the water '''
        self._target_temperature_sensor.accessor.value = new_temperature

    @property
    def min_temp(self):
        ''' Get the minimum temperature of the water heater '''
        return self._min_temp

    @property
    def max_temp(self):
        ''' Get the maximum temperature of the water heater '''
        return self._min_temp

    @property
    def current_temperature(self):
        ''' Get the current temperature of the water '''
        return self._current_temperature_sensor.state

    @property
    def temperature_unit(self):
        ''' Get the temperature units for the water heater '''
        if self._temperature_unit_accessor.value == "C":
            return self.TEMP_CELCIUS
        return self.TEMP_FARENHEIGHT

    def set_temperature_unit(self, new_unit):
        ''' Set the temperature units for the water heater '''
        if new_unit in (self.TEMP_FARENHEIGHT, "f", "F"):
            self._temperature_unit_accessor.value = "F"
        else:
            self._temperature_unit_accessor.value = "C"

    @property
    def current_operation(self):
        ''' Return the current operation of the water heater '''
        # Check the property bag to determine what is going on ...

        # Failing that, assume we know what is happening based on the temperature states ...
        return self._current_operation

    def format_temperature(self, temperature):
        ''' Format a temperature value to a printable string '''
        return "{0:.1f}{1}".format(temperature, self.temperature_unit)

    def __str__(self):
        if self._is_present:
            return "{0}: Temperature {1}, SetPoint {2}, Operation {3}".format(
                self.name,
                self.format_temperature(self.current_temperature),
                self.format_temperature(self.target_temperature),
                self.current_operation)
        return "{0}: Not present".format(self.name)

###################################################################################################
class GeckoKeypad(GeckoAutomationBase):
    ''' Keypad management class '''

    def __init__(self, facade):
        super().__init__(facade, "Keypad")

    def __str__(self):
        return "{0}: Not implemented yet".format(self.name)

###################################################################################################
class GeckoWaterCare(GeckoAutomationBase):
    ''' Watercare manangement class '''

    def __init__(self, facade):
        super().__init__(facade, "WaterCare")

    def __str__(self):
        return "{0}: Not implemented yet".format(self.name)

###################################################################################################
class GeckoFacade:
    ''' Facade to abstract the Gecko implementation details and present an interface suitable
        for consumption by automation systems, e.g. Home Assistant '''

    def __init__(self, spa):
        self._spa = spa
        self._sensors = []
        self._water_heater = GeckoWaterHeater(self)
        self._water_care = GeckoWaterCare(self)
        self._keypad = GeckoKeypad(self)
        self.scan_outputs()

    def scan_outputs(self):
        ''' Scan the spa outputs to decide what user options are available '''
        # Get list of outputs from the configuration
        all_outputs = [element.tag
                       for xpath
                       in GeckoConstants.PACK_OUTPUTS_XPATHS
                       for element
                       in self._spa.config_xml.findall(xpath)]
        logger.debug("All outputs are %s", all_outputs)
        # Workout what (if anything) the outputs are connected to
        all_output_connections = {output: self._spa.accessors[output].value for output
                                  in all_outputs}
        logger.debug("Output connections are %s", all_output_connections)
        # Reduce the dictionary to those that are not set to NA (Not Applicable)
        actual_connections = {tag: val for (tag, val)
                              in all_output_connections.items() if val != "NA"}
        logger.debug("Actual connections are %s", actual_connections)
        # Get collection of possible devices, including lights
        all_devices = [element.tag for element
                       in self._spa.log_xml.findall(GeckoConstants.SPA_PACK_DEVICE_XPATH)] + ['LI']
        logger.debug("All devices are %s", all_devices)
        # If any of the actual connection values starts with any of the devices,
        # then the device is present
        actual_devices = [device for device in all_devices for val
                          in actual_connections.values() if val.startswith(device)]
        logger.debug("Actual devices are %s", actual_devices)
        # User devices are those that have a Ud in the tag name
        user_demands = [element.tag for element
                        in self._spa.log_xml.findall(GeckoConstants.SPA_PACK_USER_DEMANDS)
                        if element.tag.startswith("Ud")]
        logger.debug("Possible user demands are %s", user_demands)
        # Actual user devices are those where the actual device has a corresponding user demand
        self.actual_user_devices = [device for device in actual_devices for ud in user_demands
                                    if "Ud{0}".format(device).upper() == ud.upper()]
        logger.debug("Actual user devices are %s", self.actual_user_devices)
        # These keys can be used to determine the actual state ...
        # Key       Desc        Outputs         Keypad      Direct Drive
        # P1 ...    Pump 1      Out1A->P1H      1           <Doesn't work as expected ...>
        # Pn ...    Pump n      Out?A/B->PnH/L  n                     ""

        # Fix for issue#1 https://github.com/gazoodle/geckolib/issues/1
        # self.actual_user_devices.append("Waterfall")
        # Remove unknown device classes
        self.actual_user_devices = [handled_device for handled_device in self.actual_user_devices
                                    if handled_device in GeckoConstants.DEVICES]
        logger.debug("Handled user devices are %s", self.actual_user_devices)

        self._pumps = [GeckoPump(self, device, GeckoConstants.DEVICES[device])
                       for device in self.actual_user_devices
                       if GeckoConstants.DEVICES[device][3] == GeckoConstants.DEVICE_CLASS_PUMP]

        self._blowers = [GeckoBlower(self, device, GeckoConstants.DEVICES[device])
                         for device in self.actual_user_devices
                         if GeckoConstants.DEVICES[device][3] == GeckoConstants.DEVICE_CLASS_BLOWER]

        self._lights = [GeckoLight(self, device, GeckoConstants.DEVICES[device])
                        for device in self.actual_user_devices
                        if GeckoConstants.DEVICES[device][3] == GeckoConstants.DEVICE_CLASS_LIGHT]

    @property
    def water_heater(self):
        ''' Get the water heater handler '''
        return self._water_heater

    @property
    def water_care(self):
        ''' Get the water care handler '''
        return self._water_care

    @property
    def keypad(self):
        ''' Get the keypad handler '''
        return self._keypad

    @property
    def pumps(self):
        ''' Get the pumps list '''
        return self._pumps

    @property
    def blowers(self):
        ''' Get the blowers list '''
        return self._blowers

    @property
    def lights(self):
        ''' Get the lights list '''
        return self._lights

    @property
    def all_user_devices(self):
        ''' Get all the devices as a list '''
        return self._pumps + self._blowers + self._lights

    @property
    def reminders(self):
        ''' Get the reminders list '''
        return []
