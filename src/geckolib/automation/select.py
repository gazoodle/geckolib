"""Automation selection class."""  # noqa: A005

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoSelect(GeckoAutomationFacadeBase):
    """A select object can select between options and can report the current state."""

    def __init__(self, facade: GeckoAsyncFacade, name: str, tag: str) -> None:
        """Initialize the select class."""
        super().__init__(facade, name, tag)
        self._accessor = None
        if tag in facade.spa.accessors:
            self._accessor = facade.spa.accessors[tag]
            self._accessor.watch(self._on_change)
            self.set_availability(is_available=True)

    @property
    def state(self) -> str:
        """Get the current state."""
        if self._accessor is None:
            return "Unknown"
        return self._accessor.value

    async def async_set_state(self, new_state: str) -> None:
        """Set the state of the select entity."""
        if self._accessor is None:
            _LOGGER.warning("%s can't set state with no accessor.", self)
            return
        _LOGGER.debug("%s async set state %s", self.name, new_state)
        await self._accessor.async_set_value(new_state)

    @property
    def states(self) -> list[str]:
        """Get the possible states."""
        if self._accessor is None:
            return []
        return self._accessor.items

    def __str__(self) -> str:
        """Stringize the class."""
        return f"{self.name}: {self.state}"

    @property
    def monitor(self) -> str:
        """Get monitore string."""
        return f"{self.key}: {self.state}"
