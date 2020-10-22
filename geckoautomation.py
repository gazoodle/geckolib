#!/usr/bin/python3
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

# HISTORY
# =======
#
# 0.1.x       Oct 2020        -   Initial implementation
#
# Using Semantic versioning https://semver.org/

#
# Automation interface facade classes for geckolib
#

import logging
from geckolib import gecko_constants, gecko_manager

# Module logger, uses the library name (at this time it was geckoautomation) and it is silent unless required ...
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

#######################################################################
class GeckoFeatureNotAvailable(Exception):
    pass

#######################################################################
class GeckoAutomationBase:

    def __init__(self, facade, name):
        self._facade = facade
        self._spa = facade._spa
        self._name = name
    
    @property
    def name(self):
        return self._name

#######################################################################
class GeckoSensor(GeckoAutomationBase):
    
    def __init__(self, facade, name, accessor, unit_accessor = None ):
        super().__init__(facade, name)
        self._accessor = accessor
        self._unit_of_measurement_accessor = unit_accessor
        self._device_class = None

    @property
    def state(self):
        return self._accessor.value

    @property
    def unit_of_measurement(self):
        if self._unit_of_measurement_accessor is None:
            return None
        return self._unit_of_measurement_accessor.value

    @property
    def device_class(self):
        return self._device_class

#######################################################################
class GeckoBinarySensor(GeckoSensor):
    pass

#######################################################################
class GeckoSwitch(GeckoAutomationBase):

    def __init__(self, facade, key, props):
        ''' props is a tuple of (name, keypad_button, state_key, device_class) '''
        super().__init__(facade, props[0])
        self.ui_key = key
        self._state_sensor = GeckoSensor(facade, 
            "{0} State".format(props[0]),
            self._spa.accessors[props[2]])
        self._keypad_button = props[1]
        self.device_class = props[3]

    @property
    def is_on(self):
        return self._state_sensor.state != "OFF"

    def turn_on(self):
        logger.debug("%s turn ON" % self.name)
        if self.is_on: 
            logger.debug("%s request to turn ON ignored, it's already on!" % self.name)
            return
        self._spa.press(self._keypad_button)

    def turn_off(self):
        logger.debug("%s turn OFF" % self.name)
        if not self.is_on: 
            logger.debug("%s request to turn OFF ignored, it's already off!" % self.name)
            return
        self._spa.press(self._keypad_button)

    def __str__(self):
        return "{0}: {1}".format(self.name, self._state_sensor.state)        

#######################################################################
class GeckoPump(GeckoSwitch):
    pass

#######################################################################
class GeckoBlower(GeckoSwitch):
    pass

#######################################################################
class GeckoLight(GeckoSwitch):
    pass

#######################################################################
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
        self._temperature_unit_accessor = self._spa.accessors[gecko_constants.key_temp_units]
        if gecko_constants.key_setpoint_g in self._spa.accessors:
            self._target_temperature_sensor = GeckoSensor(facade, 
                "Target Temperature", 
                self._spa.accessors[gecko_constants.key_setpoint_g],
                self._temperature_unit_accessor)
            self._is_present = True
        if gecko_constants.key_displayed_temp_g in self._spa.accessors:
            self._current_temperature_sensor = GeckoSensor(facade,
                "Current Temperature",
                self._spa.accessors[gecko_constants.key_displayed_temp_g],
                self._temperature_unit_accessor)            
            self._is_present = True
    
    @property
    def is_present(self):
        return self._is_present

    @property
    def target_temperature(self):
        return self._target_temperature_sensor.state

    def set_target_temperature(self, new_temperature):
        self._target_temperature_sensor._accessor.value = new_temperature

    @property
    def min_temp(self):
        return self._min_temp

    @property
    def max_temp(self):
        return self._min_temp

    @property
    def current_temperature(self):
        return self._current_temperature_sensor.state

    @property
    def temperature_unit(self):
        if self._temperature_unit_accessor.value == "C":
            return self.TEMP_CELCIUS
        return self.TEMP_FARENHEIGHT

    def set_temperature_unit(self, new_unit):
        if new_unit == self.TEMP_FARENHEIGHT or new_unit == "f" or new_unit == "F":
            self._temperature_unit_accessor.value == "F"
        else:
            self._temperature_unit_accessor.value == "C"

    @property
    def current_operation(self):
        # Check the property bag to determine what is going on ...

        # Failing that, assume we know what is happening based on the temperature states ...
        return self._current_operation

    def format_temperature(self, temperature):
        return "{0:.1f}{1}".format(temperature, self.temperature_unit)

    def __str__(self):
        if self._is_present:
            return "{0}: Temperature {1}, SetPoint {2}, Operation {3}".format(
                self.name, 
                self.format_temperature(self.current_temperature),
                self.format_temperature(self.target_temperature),
                self.current_operation)
        return "{0}: Not present".format(self.name)

#######################################################################
class GeckoKeypad(GeckoAutomationBase):

    def __init__(self, facade):
        super().__init__(facade, "Keypad")

    def __str__(self):
        return "{0}: Not implemented yet".format(self.name)

#######################################################################
class GeckoWaterCare(GeckoAutomationBase):

    def __init__(self, facade):
        super().__init__(facade, "WaterCare")

    def __str__(self):
        return "{0}: Not implemented yet".format(self.name)

#######################################################################
class GeckoFacade(GeckoAutomationBase):
    
    def __init__(self, spa):
        self._spa = spa
        self._sensors = []
        self._water_heater = GeckoWaterHeater(self)
        self._water_care = GeckoWaterCare(self)
        self._keypad = GeckoKeypad(self)
        self.scan_outputs()
        
    def scan_outputs(self):
        # Get list of outputs from the configuration
        all_outputs = [ element.tag for xpath in gecko_constants.pack_outputs_xpaths for element in self._spa.config_xml.findall(xpath) ]
        logger.debug("All outputs are %s" % all_outputs )
        # Workout what (if anything) the outputs are connected to
        all_output_connections = { output: self._spa.accessors[output].value for output in all_outputs }
        logger.debug("Output connections are %s" % all_output_connections)
        # Reduce the dictionary to those that are not set to NA (Not Applicable)
        actual_connections = { tag: val for (tag,val) in all_output_connections.items() if val != "NA" }
        logger.debug("Actual connections are %s" % actual_connections)
        # Get collection of possible devices, including lights
        all_devices = [ element.tag for element in self._spa.log_xml.findall(gecko_constants.spa_pack_device_xpath) ] + ['LI']
        logger.debug("All devices are %s" % all_devices)
        # If any of the actual connection values starts with any of the devices, then the device is present
        actual_devices = [ device for device in all_devices for val in actual_connections.values() if val.startswith(device) ]
        logger.debug("Actual devices are %s" % actual_devices)
        # User devices are those that have a Ud in the tag name
        user_demands = [ element.tag for element in self._spa.log_xml.findall(gecko_constants.spa_pack_user_demands) if element.tag.startswith("Ud") ]
        logger.debug("Possible user demands are %s" % user_demands)
        # Actual user devices are those where the actual device has a corresponding user demand
        self.actual_user_devices = [ device for device in actual_devices for ud in user_demands if "Ud{0}".format(device).upper() == ud.upper() ]
        logger.debug("Actual user devices are %s" % self.actual_user_devices)
        # These keys can be used to determine the actual state ...
        # Key       Desc        Outputs         Keypad      Direct Drive
        # P1 ...    Pump 1      Out1A->P1H      1           <Doesn't work as expected ...>
        # Pn ...    Pump n      Out?A/B->PnH/L  n                     ""

        self._pumps = [ GeckoPump(self, device, gecko_constants.devices[device])
            for device in self.actual_user_devices
            if gecko_constants.devices[device][3] == gecko_constants.device_class_pump]

        self._blowers = [ GeckoBlower(self, device, gecko_constants.devices[device])
            for device in self.actual_user_devices
            if gecko_constants.devices[device][3] == gecko_constants.device_class_blower]

        self._lights = [ GeckoLight(self, device, gecko_constants.devices[device])
            for device in self.actual_user_devices
            if gecko_constants.devices[device][3] == gecko_constants.device_class_light]

    @property
    def water_heater(self):
        return self._water_heater

    @property
    def water_care(self):
        return self._water_care

    @property
    def keypad(self):
        return self._keypad

    @property
    def pumps(self):
        return self._pumps

    @property
    def blowers(self):
        return self._blowers

    @property
    def lights(self):
        return self._lights

    @property
    def all_user_devices(self):
        return self._pumps + self._blowers + self._lights

    @property
    def reminders(self):
        return []
