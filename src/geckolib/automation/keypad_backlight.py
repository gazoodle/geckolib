"""Automation keypad backlight class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .select import GeckoSelect

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoKeypadBacklight(GeckoSelect):
    """The keypad backlight value."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the backlight class."""
        super().__init__(facade, "Keypad Backlight", "KeypadBacklightColor")
        # Set of mappings of constants to UI options
        self.set_mapping(
            {
                "OFF": "Off",
                "RED": "Red",
                "GREEN": "Green",
                "YELLOW": "Yellow",
                "BLUE": "Blue",
                "MAGENTA": "Magenta",
                "CYAN": "Cyan",
                "WHITE": "White",
            }
        )

    @property
    def state(self) -> str:
        """Get the current state via the mapping."""
        return self.mapping[self._accessor.value]

    async def async_set_state(self, new_state: str) -> None:
        """Set the state of the select entity."""
        if new_state in self.reverse:
            new_state = self.reverse[new_state]
        await self._accessor.async_set_value(new_state)

    @property
    def states(self) -> list[str]:
        """Get the possible states."""
        return list(self.mapping.values())
