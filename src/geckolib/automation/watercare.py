"""Gecko Watercare."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.const import GeckoConstants

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoWaterCare(GeckoAutomationFacadeBase):
    """Watercare manangement class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize watercare class."""
        super().__init__(facade, "WaterCare", "WATERCARE")
        self.active_mode: int | None = None
        if not facade.spa.struct.is_mr_steam:
            self.set_availability(is_available=True)

    @property
    def mode(self) -> int | None:
        """Return the active water care mode."""
        return self.active_mode

    @property
    def modes(self) -> list[str]:
        """Return all the possible water care modes."""
        return GeckoConstants.WATERCARE_MODE_STRING

    @property
    def state(self) -> str:
        """Return the current state."""
        if self.mode is None:
            return "Unknown"
        return GeckoConstants.WATERCARE_MODE_STRING[self.mode]

    @property
    def states(self) -> list[str]:
        """Return all the states."""
        return self.modes

    async def async_set_state(self, new_mode: str | int) -> None:
        """Set the state. Support select style objects."""
        await self.async_set_mode(new_mode)

    async def async_set_mode(self, new_mode: str | int) -> None:
        """
        Set the active watercare mode to new_mode.

        new_mode can be a string, in which case the value must be a member of
        GeckoConstants.WATERCARE_MODE_STRING, or it can be an integer from
        GeckoConstants.WATERCARE_MODE
        """
        if isinstance(new_mode, str):
            new_mode = GeckoConstants.WATERCARE_MODE_STRING.index(new_mode)
        await self._spa.async_set_watercare_mode(new_mode)
        self.change_watercare_mode(new_mode)

    def change_watercare_mode(self, new_mode: int) -> None:
        """Change the watercare mode."""
        if self.active_mode != new_mode:
            old_mode = self.active_mode
            self.active_mode = new_mode
            self._on_change(self, old_mode, self.active_mode)

    def __str__(self) -> str:
        """Stringise the class."""
        if not self.is_available:
            return f"{self.name}: Unavailable"
        if self.active_mode is None:
            return f"{self.name}: Waiting..."
        if self.active_mode < 0 or self.active_mode > len(
            GeckoConstants.WATERCARE_MODE_STRING
        ):
            return f"Unknown Water care mode (index:{self.active_mode})"
        return f"{self.name}: {GeckoConstants.WATERCARE_MODE_STRING[self.active_mode]}"

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        if not self.is_available:
            return "WC: None"
        if self.active_mode is None:
            return "WC: ?"
        return f"WC: {self.active_mode}"
