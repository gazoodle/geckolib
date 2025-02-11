"""Automation selection class."""  # noqa: A005

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade
    from geckolib.driver.accessor import GeckoEnumStructAccessor

_LOGGER = logging.getLogger(__name__)


class GeckoSelect(GeckoAutomationFacadeBase):
    """A select object can select between options and can report the current state."""

    def __init__(
        self, facade: GeckoAsyncFacade, name: str, accessor: GeckoEnumStructAccessor
    ) -> None:
        """Initialize the select class."""
        super().__init__(facade, name, accessor.tag)
        self._accessor = accessor
        self._accessor.watch(self._on_change)

    @property
    def state(self) -> str:
        """Get the current state."""
        return self._accessor.value

    async def async_set_state(self, new_state: str) -> None:
        """Set the state of the select entity."""
        _LOGGER.debug("%s async set state %s", self.name, new_state)
        await self._accessor.async_set_value(new_state)

    @property
    def states(self) -> list[str]:
        """Get the possible states."""
        return self._accessor.items

    def __str__(self) -> str:
        """Stringize the class."""
        return f"{self.name}: {self.state}"

    @property
    def monitor(self) -> str:
        """Get monitore string."""
        return f"{self.ui_key}: {self.state}"
