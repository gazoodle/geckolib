"""Automation selection class."""

import logging

from geckolib.const import GeckoConstants
from geckolib.driver.accessor import GeckoEnumStructAccessor

from .base import GeckoAutomationFacadeBase

_LOGGER = logging.getLogger(__name__)


class GeckoSelect(GeckoAutomationFacadeBase):
    """A select object can select between options and can report the current state."""

    def __init__(self, facade, name, accessor: GeckoEnumStructAccessor):
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

    def __str__(self):
        return f"{self.name}: {self.state}"

    @property
    def monitor(self):
        return f"{self.ui_key}: {self.state}"
