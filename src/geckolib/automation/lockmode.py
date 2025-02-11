"""Automation lockmode class."""

import logging

from geckolib.automation.async_facade import GeckoAsyncFacade
from geckolib.driver.accessor import GeckoEnumStructAccessor

from .select import GeckoSelect

_LOGGER = logging.getLogger(__name__)


class GeckoLockMode(GeckoSelect):
    """A select object can select between options and can report the current state."""

    def __init__(
        self, facade: GeckoAsyncFacade, name: str, accessor: GeckoEnumStructAccessor
    ) -> None:
        """Initialize the heatpump class."""
        super().__init__(facade, name, accessor)
        # Set of mappings of constants to UI options
        self.mapping = {
            "UNLOCK": "Unlocked",
            "PARTIAL": "Partial Lock",
            "FULL": "Full Lock",
        }
        self.reverse = {v: k for k, v in self.mapping.items()}

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
