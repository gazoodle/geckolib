"""Gecko Keypads."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade


class GeckoKeypad(GeckoAutomationFacadeBase):
    """Keypad management class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the keypad class."""
        super().__init__(facade, "Keypad", "KEYPAD")

    def __str__(self) -> str:
        """Stringize the class."""
        return f"{self.name}: Not implemented yet"
