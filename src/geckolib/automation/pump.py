""" Gecko Pumps """

import logging

from ..const import GeckoConstants
from .base import GeckoAutomationFacadeBase
from .sensors import GeckoSensor

_LOGGER = logging.getLogger(__name__)


class GeckoPump(GeckoAutomationFacadeBase):
    """Pumps are similar to switches, but might have variable speeds too"""

    def __init__(self, facade, key, props, user_demand):
        """props is a tuple of (name, keypad_button, state_key, device_class)"""
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
    def is_on(self):
        """True if the device is running, False otherwise"""
        if self._state_sensor.accessor.type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            return self._state_sensor.state
        return self._state_sensor.state != "OFF"

    @property
    def modes(self):
        return self._user_demand["options"]

    @property
    def mode(self):
        return self._state_sensor.state

    def set_mode(self, mode):
        try:
            _LOGGER.debug("%s set mode %s", self.name, mode)
            self.facade.spa.accessors[self._user_demand["demand"]].value = mode
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception(
                "Exception handling setting %s=%s", self._user_demand["demand"], mode
            )

    async def async_set_mode(self, mode):
        try:
            _LOGGER.debug("%s async set mode %s", self.name, mode)
            await self.facade.spa.accessors[
                self._user_demand["demand"]
            ].async_set_value(mode)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception(
                "Exception handling setting %s=%s", self._user_demand["demand"], mode
            )

    def __str__(self):
        return f"{self.name}: {self._state_sensor.state}"

    @property
    def monitor(self):
        return f"{self.ui_key}: {self._state_sensor.state}"
