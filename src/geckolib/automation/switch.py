"""Automation switches."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.automation.power import GeckoPower
from geckolib.const import GeckoConstants

from .base import GeckoAutomationFacadeBase
from .sensors import GeckoSensor

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade
    from geckolib.driver.accessor import GeckoEnumStructAccessor

_LOGGER = logging.getLogger(__name__)


class GeckoSwitch(GeckoPower):
    """A switch can turn something on or off, and can report the current state."""

    def __init__(self, facade: GeckoAsyncFacade, key: str, props: tuple) -> None:
        """Props is a tuple of (name, keypad_button, state_key, device_class)."""
        super().__init__(facade, props[0], key)
        if key in self._spa.accessors:
            self._accessor = self._spa.accessors[key]
        else:
            self._accessor = self._spa.accessors[props[1]]
        self._state_sensor = GeckoSensor(facade, f"{props[0]} State", self._accessor)
        self._state_sensor.watch(self._on_change)
        self.device_class = props[2]

    @property
    def is_on(self) -> bool:
        """True if the device is ON, False otherwise."""
        if self._accessor.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            return self._state_sensor.state
        return self._state_sensor.state != "OFF"

    async def async_turn_on(self) -> None:
        """Turn the device ON, but does nothing if it is already ON."""
        _LOGGER.debug("%s async turn ON", self.name)
        if self.is_on:
            _LOGGER.debug("%s request to turn ON ignored, it's already on!", self.name)
            return
        _LOGGER.debug("Set async state on accessor")
        if self._accessor.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            await self._accessor.async_set_value(True)  # noqa: FBT003
        else:
            await self._accessor.async_set_value("ON")

    async def async_turn_off(self) -> None:
        """Turn the device OFF, but does nothing if it is already OFF."""
        _LOGGER.debug("%s async turn OFF", self.name)
        if not self.is_on:
            _LOGGER.debug(
                "%s request to turn OFF ignored, it's already off!", self.name
            )
            return
        _LOGGER.debug("Set async state on accessor")
        if self._accessor.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            await self._accessor.async_set_value(False)  # noqa: FBT003
        else:
            await self._accessor.async_set_value("OFF")

    def state_sensor(self) -> GeckoSensor:
        """Get the state sensor."""
        return self._state_sensor

    @property
    def state(self) -> str:
        """Get the switch state."""
        if self._accessor.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            return "ON" if self._state_sensor.state else "OFF"
        return self._state_sensor.state

    def __str__(self) -> str:
        """Stringize."""
        return f"{self.name}: {self._state_sensor.state}"

    @property
    def monitor(self) -> str:
        """Get a monitor string."""
        return f"{self.key}: {self._state_sensor.state}"


class GeckoStandby(GeckoAutomationFacadeBase):
    """Standby switch."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
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

    @property
    def state(self) -> str:
        """Get the standby state."""
        return f"{self.is_on}"

    def __str__(self) -> str:
        """Stringize the class."""
        return f"{self.name}: {self.is_on}"

    @property
    def monitor(self) -> str:
        """Get the monitor string."""
        return f"{self.key}: {self.is_on}"
