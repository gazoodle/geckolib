"""Mr.Steam class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.automation.heater import GeckoWaterHeaterAbstract
from geckolib.automation.number import GeckoNumber
from geckolib.automation.sensors import GeckoSensor
from geckolib.automation.switch import GeckoSwitch
from geckolib.const import GeckoConstants

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class MrSteam(GeckoWaterHeaterAbstract):
    """Mr.Steam support class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the MrSteam class."""
        super().__init__(facade, "Steamer", "MRSTEAM")
        if not facade.spa.struct.is_mr_steam:
            return

        self.set_availability(is_available=True)

        self.onoff = GeckoSwitch(
            facade,
            GeckoConstants.KEY_MRSTEAM_USER_MODE,
            (
                "On/Off",
                GeckoConstants.KEY_MRSTEAM_USER_MODE,
                GeckoConstants.DEVICE_CLASS_SWITCH,
            ),
        )
        self.onoff.watch(self._on_change)

        self.aroma = GeckoSwitch(
            facade,
            GeckoConstants.KEY_MRSTEAM_USER_AROMA,
            (
                "Aroma",
                GeckoConstants.KEY_MRSTEAM_USER_AROMA,
                GeckoConstants.DEVICE_CLASS_SWITCH,
            ),
        )
        self.aroma.watch(self._on_change)

        self.chroma = GeckoSwitch(
            facade,
            GeckoConstants.KEY_MRSTEAM_USER_CHROMA,
            (
                "Chroma",
                GeckoConstants.KEY_MRSTEAM_USER_CHROMA,
                GeckoConstants.DEVICE_CLASS_SWITCH,
            ),
        )
        self.chroma.watch(self._on_change)

        self.setpoint_accessor = self._spa.accessors[
            GeckoConstants.KEY_MRSTEAM_USER_SETPOINT_G
        ]
        self.setpoint_accessor.watch(self._on_change)
        self.temp_unt_accesor = self._spa.accessors[GeckoConstants.KEY_TEMP_UNITS]
        self.min_temp_accessor = self._spa.accessors[GeckoConstants.KEY_MIN_SETPOINT_G]
        self.max_temp_accessor = self._spa.accessors[GeckoConstants.KEY_MAX_SETPOINT_G]

        self.user_runtime = GeckoNumber(
            facade, "Runtime", GeckoConstants.KEY_MRSTEAM_USER_RUNTIME, "min"
        )
        self.user_runtime.watch(self._on_change)
        if GeckoConstants.KEY_MRSTEAM_MAX_RUNTIME in self._spa.accessors:
            max_runtime = self._spa.accessors[GeckoConstants.KEY_MRSTEAM_MAX_RUNTIME]
            self.user_runtime.native_max_value = max_runtime.value

        self.remaining_runtime = GeckoSensor(
            facade,
            "Remaining Runtime",
            self._spa.accessors[GeckoConstants.KEY_MRSTEAM_REMAINING_RUNTIME],
            "min",
        )
        self.remaining_runtime.watch(self._on_change)

    @property
    def switches(self) -> list[GeckoSwitch]:
        """Get a list of all the switches."""
        if self.is_available:
            return [self.onoff, self.aroma, self.chroma]
        return []

    @property
    def current_operation(self) -> str:
        """Get the current operation."""
        if not self.onoff.is_on:
            return "Turned off"
        return f"Running, {self.remaining_runtime.state}m remaining"

    @property
    def temperature_unit(self) -> str:
        """Get the temperature unit."""
        if self.temp_unt_accesor.value == "C":
            return self.TEMP_CELCIUS
        return self.TEMP_FARENHEIGHT

    @property
    def current_temperature(self) -> float:
        """Get the current temperature."""
        return self.setpoint_accessor.value

    @property
    def target_temperature(self) -> float:
        """Get the target temperature."""
        return self.setpoint_accessor.value

    @property
    def min_temp(self) -> float:
        """Get the min temp."""
        return self.min_temp_accessor.value

    @property
    def max_temp(self) -> float:
        """Get the max temp."""
        return self.max_temp_accessor.value

    async def async_set_target_temperature(self, new_temperature: float) -> None:
        """Set the target temperature of the water."""
        await self.setpoint_accessor.async_set_value(new_temperature)
