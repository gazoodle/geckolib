""" Facade to hide implementation details """

import logging

from .blower import GeckoBlower
from ..const import GeckoConstants
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight
from .pump import GeckoPump
from .watercare import GeckoWaterCare

logger = logging.getLogger(__name__)


class GeckoFacade:
    """Facade to abstract the Gecko implementation details and present an interface suitable
    for consumption by automation systems, e.g. Home Assistant"""

    def __init__(self, spa):
        self._spa = spa
        self._sensors = []
        self._water_heater = GeckoWaterHeater(self)
        self._water_care = GeckoWaterCare(self)
        self._keypad = GeckoKeypad(self)
        self.scan_outputs()

    def scan_outputs(self):
        """ Scan the spa outputs to decide what user options are available """
        # Get list of outputs from the configuration
        all_outputs = [
            element.tag
            for xpath in GeckoConstants.PACK_OUTPUTS_XPATHS
            for element in self._spa.config_xml.findall(xpath)
        ]
        logger.debug("All outputs are %s", all_outputs)
        # Workout what (if anything) the outputs are connected to
        all_output_connections = {
            output: self._spa.accessors[output].value for output in all_outputs
        }
        logger.debug("Output connections are %s", all_output_connections)
        # Reduce the dictionary to those that are not set to NA (Not Applicable)
        actual_connections = {
            tag: val for (tag, val) in all_output_connections.items() if val != "NA"
        }
        logger.debug("Actual connections are %s", actual_connections)
        # Get collection of possible devices, including lights
        all_devices = [
            element.tag
            for element in self._spa.log_xml.findall(
                GeckoConstants.SPA_PACK_DEVICE_XPATH
            )
        ] + ["LI"]
        logger.debug("All devices are %s", all_devices)
        # If any of the actual connection values starts with any of the devices,
        # then the device is present
        actual_devices = [
            device
            for device in all_devices
            for val in actual_connections.values()
            if val.startswith(device)
        ]
        logger.debug("Actual devices are %s", actual_devices)
        # User devices are those that have a Ud in the tag name
        user_demands = [
            element.tag
            for element in self._spa.log_xml.findall(
                GeckoConstants.SPA_PACK_USER_DEMANDS
            )
            if element.tag.startswith("Ud")
        ]
        logger.debug("Possible user demands are %s", user_demands)
        # Actual user devices are those where the actual device has a corresponding user demand
        self.actual_user_devices = [
            device
            for device in actual_devices
            for ud in user_demands
            if "Ud{0}".format(device).upper() == ud.upper()
        ]
        logger.debug("Actual user devices are %s", self.actual_user_devices)
        # These keys can be used to determine the actual state ...
        # Key       Desc        Outputs         Keypad      Direct Drive
        # P1 ...    Pump 1      Out1A->P1H      1           <Doesn't work as expected ...>
        # Pn ...    Pump n      Out?A/B->PnH/L  n                     ""

        # Fix for issue#1 https://github.com/gazoodle/geckolib/issues/1
        # self.actual_user_devices.append("Waterfall")
        # Remove unknown device classes
        self.actual_user_devices = [
            handled_device
            for handled_device in self.actual_user_devices
            if handled_device in GeckoConstants.DEVICES
        ]
        logger.debug("Handled user devices are %s", self.actual_user_devices)

        self._pumps = [
            GeckoPump(self, device, GeckoConstants.DEVICES[device])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device][3] == GeckoConstants.DEVICE_CLASS_PUMP
        ]

        self._blowers = [
            GeckoBlower(self, device, GeckoConstants.DEVICES[device])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device][3] == GeckoConstants.DEVICE_CLASS_BLOWER
        ]

        self._lights = [
            GeckoLight(self, device, GeckoConstants.DEVICES[device])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device][3] == GeckoConstants.DEVICE_CLASS_LIGHT
        ]

    @property
    def water_heater(self):
        """ Get the water heater handler """
        return self._water_heater

    @property
    def water_care(self):
        """ Get the water care handler """
        return self._water_care

    @property
    def keypad(self):
        """ Get the keypad handler """
        return self._keypad

    @property
    def pumps(self):
        """ Get the pumps list """
        return self._pumps

    @property
    def blowers(self):
        """ Get the blowers list """
        return self._blowers

    @property
    def lights(self):
        """ Get the lights list """
        return self._lights

    @property
    def all_user_devices(self):
        """ Get all the devices as a list """
        return self._pumps + self._blowers + self._lights

    @property
    def reminders(self):
        """ Get the reminders list """
        return []
