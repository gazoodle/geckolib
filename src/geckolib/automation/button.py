"""GeckoButton class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoButton(GeckoAutomationFacadeBase):
    """A button can be pressed ... that's it."""

    def __init__(self, facade: GeckoAsyncFacade, name: str, keypad: int) -> None:
        """Inirtialize the button class."""
        super().__init__(facade, name, f"KEYPAD{keypad}")
        self._keypad: int = keypad

    async def async_press(self) -> None:
        """Press the button."""
        await self.facade.spa.async_press(self._keypad)
