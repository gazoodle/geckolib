""" Facade to hide implementation details """

import logging
import threading

from .blower import GeckoBlower
from ..const import GeckoConstants
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight
from .pump import GeckoPump
from .sensors import GeckoSensor, GeckoBinarySensor
from .watercare import GeckoWaterCare
from ..driver import Observable

logger = logging.getLogger(__name__)


class GeckoFacade(Observable):
    """Facade to abstract the Gecko implementation details and present an interface suitable
    for consumption by automation systems, e.g. Home Assistant. This class and all the
    output and state objects maintain their state locally so there should be no need to
    poll"""

    def __init__(self, spa):
        super().__init__()
        self._spa = spa
        self._sensors = []
        self._binary_sensors = []
        self._water_heater = None
        self._water_care = None
        self._keypad = None
        self._update_thread = threading.Thread(
            target=self._update_thread_func, daemon=True
        )
        self._update_thread.start()
        self._facade_ready = False
        self._spa.on_connected = self._on_connected

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self._spa:
            self._spa.complete()
            self._spa = None
        if self._update_thread:
            self._update_thread.join()

    def _on_connected(self, spa):
        logger.debug("Facade knows spa is connected")
        self._water_heater = GeckoWaterHeater(self)
        self._water_care = GeckoWaterCare(self)
        self._keypad = GeckoKeypad(self)
        self.scan_outputs()
        # Install change notifications
        for device in self.all_automation_devices:
            device.watch(self._on_change)
        logger.debug("Facade is now ready")
        self._facade_ready = True

    def complete(self):
        """ Finish using this facade if not used in a `with` statement """
        self.__exit__()

    @property
    def is_connected(self):
        if not self._spa.is_connected:
            return False
        return self._facade_ready

    def wait(self, timeout):
        self.spa.wait(timeout)

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
        actual_devices = set(
            [
                device
                for device in all_devices
                for val in actual_connections.values()
                if val.startswith(device)
            ]
        )
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
        # Actual user devices are those where the actual device has a corresponding
        # user demand
        self.actual_user_devices = [
            { "device": device, "user_demand" : { "demand": self._spa.accessors[f"{ud}"].tag, "options": self._spa.accessors[f"{ud}"].items } }
            for device in actual_devices
            for ud in user_demands
            if f"Ud{device}".upper() == ud.upper()
        ]
        logger.debug("Actual user devices are %s", self.actual_user_devices)

        # These keys can be used to determine the actual state ...
        # Key       Desc        Outputs         Keypad      Direct Drive
        # P1 ...    Pump 1      Out1A->P1H      1           <Doesn't work as expected>
        # Pn ...    Pump n      Out?A/B->PnH/L  n                     ""

        # Fix for issue#1 https://github.com/gazoodle/geckolib/issues/1
        # self.actual_user_devices.append("Waterfall")
        # Remove unknown device classes
        self.actual_user_devices = [
            handled_device
            for handled_device in self.actual_user_devices
            if handled_device["device"] in GeckoConstants.DEVICES
        ]
        logger.debug("Handled user devices are %s", self.actual_user_devices)


        self._pumps = [
            GeckoPump(self, device["device"], GeckoConstants.DEVICES[device["device"]], device["user_demand"])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device["device"]][3] == GeckoConstants.DEVICE_CLASS_PUMP
        ]

        self._blowers = [
            GeckoBlower(self, device["device"], GeckoConstants.DEVICES[device["device"]])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device["device"]][3] == GeckoConstants.DEVICE_CLASS_BLOWER
        ]

        self._lights = [
            GeckoLight(self, device["device"], GeckoConstants.DEVICES[device["device"]])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device["device"]][3] == GeckoConstants.DEVICE_CLASS_LIGHT
        ]

        self._sensors = [
            GeckoSensor(self, sensor[0], self._spa.accessors[sensor[1]])
            for sensor in GeckoConstants.SENSORS
            if sensor[1] in self._spa.accessors
        ]

        self._binary_sensors = [
            GeckoBinarySensor(
                self, binary_sensor[0], self._spa.accessors[binary_sensor[1]]
            )
            for binary_sensor in GeckoConstants.BINARY_SENSORS
            if binary_sensor[1] in self._spa.accessors
        ]

    @property
    def unique_id(self):
        """ A unique id for the facade """
        return f"{self.identifier.replace(':', '')}"

    @property
    def name(self):
        """ Get the spa name """
        return self._spa.descriptor.name

    @property
    def identifier(self):
        """ Get the spa identifier """
        return self._spa.descriptor.identifier_as_string

    @property
    def spa(self):
        """ Get the spa implementation class """
        return self._spa

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
    def pumps(self) -> [GeckoPump]:
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
    def sensors(self):
        """ Get the sensor list """
        return self._sensors

    @property
    def binary_sensors(self):
        """ Get the binary sensor list """
        return self._binary_sensors

    @property
    def all_user_devices(self):
        """ Get all the user controllable devices as a list """
        return self._pumps + self._blowers + self._lights

    @property
    def all_automation_devices(self):
        """ Get all the automation devices as a list """
        return (
            self.all_user_devices
            + self.sensors
            + self.binary_sensors
            + [self.water_heater, self.water_care, self.keypad]
        )

    def get_device(self, key):
        """ Get an automation device from the key """
        for device in self.all_automation_devices:
            if device.key == key:
                return device
        return None

    @property
    def devices(self):
        """Get a list of automation device keys. Keys can be passed to get_device
        to find the specific device"""
        return [device.key for device in self.all_automation_devices]

    @property
    def reminders(self):
        """ Get the reminders list """
        return []

    def _update_thread_func(self):
        while self.spa.isopen:
            if self._water_care is None:
                self.spa.wait(0.1)
                continue
            self.water_care.update()
            if self._water_care.active_mode is None:
                self.spa.wait(0.1)
                continue
            self.spa.wait(GeckoConstants.FACADE_UPDATE_FREQUENCY_IN_SECONDS)

        logger.info("Facade update thread finished")
