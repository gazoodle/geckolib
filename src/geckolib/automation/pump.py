""" Gecko Pumps """

import logging

from .base import GeckoAutomationBase
from .sensors import GeckoSensor

logger = logging.getLogger(__name__)

class GeckoPump(GeckoAutomationBase):
    """ Pumps are similar to switches, but might have variable speeds too """

    def __init__(self, facade, key, props, user_demand):
        """ props is a tuple of (name, keypad_button, state_key, device_class) """
        super().__init__(facade, props[0], key)
        self.ui_key = key
        self._state_sensor = GeckoSensor(
            facade, f"{props[0]} State", self._spa.accessors[props[2]]
        )
        self._state_sensor.watch(self._on_change)
        self._keypad_button = props[1]
        self.device_class = props[3]
        self._user_demand = user_demand

    @property
    def modes(self):
        return self._user_demand["options"]

    @property
    def mode(self):
        return self._state_sensor.state

    def set_mode(self, mode):        
        try:
            logger.debug("%s set mode %s", self.name, mode)
            self.facade.spa.accessors[self._user_demand["demand"]].value = mode
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception handling setting %s=%s", key, val)

    def __str__(self):
        return f"{self.name}: {self._state_sensor.state}"
