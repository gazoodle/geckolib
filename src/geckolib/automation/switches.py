""" Automation switches """

import logging

from .base import GeckoAutomationBase
from .sensors import GeckoSensor

logger = logging.getLogger(__name__)


class GeckoSwitch(GeckoAutomationBase):
    """ A switch can turn something on or off, and can report the current state """

    def __init__(self, facade, key, props):
        """ props is a tuple of (name, keypad_button, state_key, device_class) """
        super().__init__(facade, props[0], key)
        self.ui_key = key
        self._state_sensor = GeckoSensor(
            facade, f"{props[0]} State", self._spa.accessors[props[2]]
        )
        self._state_sensor.watch(self._on_change)
        self._keypad_button = props[1]
        self.device_class = props[3]

    @property
    def is_on(self):
        """ True if the device is ON, False otherwise """
        return self._state_sensor.state != "OFF"

    def turn_on(self):
        """ Turn the device ON, but does nothing if it is already ON """
        logger.debug("%s turn ON", self.name)
        if self.is_on:
            logger.debug("%s request to turn ON ignored, it's already on!", self.name)
            return
        self._spa.press(self._keypad_button)

    def turn_off(self):
        """ Turn the device OFF, but does nothing if it is already OFF """
        logger.debug("%s turn OFF", self.name)
        if not self.is_on:
            logger.debug("%s request to turn OFF ignored, it's already off!", self.name)
            return
        self._spa.press(self._keypad_button)

    def state_sensor(self):
        return self._state_sensor

    def __str__(self):
        return f"{self.name}: {self._state_sensor.state}"
