"""Automation switches"""

import logging

from geckolib.driver.accessor import GeckoEnumStructAccessor

from ..const import GeckoConstants
from .base import GeckoAutomationFacadeBase
from .sensors import GeckoSensor

_LOGGER = logging.getLogger(__name__)


class GeckoSwitch(GeckoAutomationFacadeBase):
    """A switch can turn something on or off, and can report the current state."""

    def __init__(self, facade, key, props):
        """Props is a tuple of (name, keypad_button, state_key, device_class)."""
        super().__init__(facade, props[0], key)
        self.ui_key = key
        self._accessor = self._spa.accessors[props[2]]
        self._state_sensor = GeckoSensor(facade, f"{props[0]} State", self._accessor)
        self._state_sensor.watch(self._on_change)
        self._keypad_button = props[1]
        self.device_class = props[3]

    @property
    def is_on(self) -> bool:
        """True if the device is ON, False otherwise"""
        if self._accessor.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            return self._state_sensor.state
        return self._state_sensor.state != "OFF"

    async def async_turn_on(self) -> None:
        """Turn the device ON, but does nothing if it is already ON."""
        _LOGGER.debug("%s async turn ON", self.name)
        if self.is_on:
            _LOGGER.debug("%s request to turn ON ignored, it's already on!", self.name)
            return
        if self._keypad_button != 0:
            await self._spa.async_press(self._keypad_button)
            return
        _LOGGER.debug("Set async state on accessor")
        await self._accessor.async_set_value(True)

    async def async_turn_off(self) -> None:
        """Turn the device OFF, but does nothing if it is already OFF."""
        _LOGGER.debug("%s async turn OFF", self.name)
        if not self.is_on:
            _LOGGER.debug(
                "%s request to turn OFF ignored, it's already off!", self.name
            )
            return
        if self._keypad_button != 0:
            await self._spa.async_press(self._keypad_button)
            return
        _LOGGER.debug("Set async state on accessor")
        await self._accessor.async_set_value(False)

    def state_sensor(self):
        return self._state_sensor

    def __str__(self):
        return f"{self.name}: {self._state_sensor.state}"

    @property
    def monitor(self):
        return f"{self.ui_key}: {self._state_sensor.state}"


class GeckoStandby(GeckoAutomationFacadeBase):
    """Standby switch."""

    def __init__(self, facade):
        """Initialize the standby switch."""
        super().__init__(facade, "Standby", GeckoConstants.KEY_STANDBY)
        self._accessor: GeckoEnumStructAccessor = self._spa.accessors[
            GeckoConstants.KEY_STANDBY
        ]
        self._accessor.watch(self._on_change)

    @property
    def is_on(self) -> bool:
        """True if the device is ON, False otherwise."""
        return self._accessor.value == "OFF"

    async def async_turn_on(self) -> None:
        """Turn on standby mode."""
        await self._accessor.async_set_value("OFF")

    async def async_turn_off(self) -> None:
        """Turn off standby mode."""
        await self._accessor.async_set_value("NOT_SET")

    def __str__(self):
        return f"{self.name}: {self.is_on}"

    @property
    def monitor(self):
        return f"{self.ui_key}: {self.is_on}"
