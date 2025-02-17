"""Gecko Keypads."""

from __future__ import annotations

from typing import TYPE_CHECKING

from geckolib.automation.button import GeckoButton
from geckolib.automation.keypad_backlight import GeckoKeypadBacklight
from geckolib.const import GeckoConstants

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade


class GeckoKeypad(GeckoAutomationFacadeBase):
    """Keypad management class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the keypad class."""
        super().__init__(facade, "Keypad", "KEYPAD")

        self.backlight = GeckoKeypadBacklight(facade)

        self._buttons = []

        # Should we show eco mode button too?

        if self.facade.pump_1.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Pump 1", GeckoConstants.KEYPAD_PUMP_1)
            )
        if self.facade.pump_2.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Pump 2", GeckoConstants.KEYPAD_PUMP_2)
            )
        if self.facade.pump_3.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Pump 3", GeckoConstants.KEYPAD_PUMP_3)
            )
        if self.facade.pump_4.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Pump 4", GeckoConstants.KEYPAD_PUMP_4)
            )
        if self.facade.pump_5.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Pump 5", GeckoConstants.KEYPAD_PUMP_5)
            )
        if self.facade.blower.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Blower", GeckoConstants.KEYPAD_BLOWER)
            )
        if self.facade.waterfall.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Waterfall", GeckoConstants.KEYPAD_WATERFALL)
            )
        if self.facade.bubblegenerator.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Bubble Generator", GeckoConstants.KEYPAD_AUX)
            )

        if self.facade.light.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Light", GeckoConstants.KEYPAD_LIGHT)
            )
        if self.facade.light2.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Light 2", GeckoConstants.KEYPAD_LIGHT_120)
            )

        if self.facade.water_heater.is_available:
            self._buttons.append(
                GeckoButton(facade, "Key Temperature Up", GeckoConstants.KEYPAD_UP)
            )
            self._buttons.append(
                GeckoButton(facade, "Key Temperature Down", GeckoConstants.KEYPAD_DOWN)
            )

    @property
    def buttons(self) -> list[GeckoButton]:
        """Get the buttons that have any action."""
        return self._buttons

    def __str__(self) -> str:
        """Stringize the class."""
        return f"{self.name}:"
