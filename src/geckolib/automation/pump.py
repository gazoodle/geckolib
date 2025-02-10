"""Gecko Pumps."""

import logging

from geckolib.automation.power import GeckoPower

from ..const import GeckoConstants
from .sensors import GeckoSensor

_LOGGER = logging.getLogger(__name__)


class GeckoPump(GeckoPower):
    """Pumps are similar to switches, but might have variable speeds too."""

    def __init__(self, facade, key, props, user_demand):
        """Props is a tuple of (name, keypad_button, state_key, device_class)."""
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
        """Return True if the device is running, False otherwise."""
        if (
            self._state_sensor.accessor.accessor_type
            == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE
        ):
            return self._state_sensor.state
        return self._state_sensor.state != "OFF"

    @property
    def modes(self):
        """Get the pump modes."""
        return self._user_demand["options"]

    @property
    def mode(self):
        """Get the pump mode."""
        return self._state_sensor.state

    async def async_set_mode(self, mode) -> None:
        """Set the mode."""
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
