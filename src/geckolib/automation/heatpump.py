"""Automation heatpump class."""

import logging

from geckolib.automation.async_facade import GeckoAsyncFacade
from geckolib.driver.accessor import GeckoEnumStructAccessor

from .select import GeckoSelect

_LOGGER = logging.getLogger(__name__)


class GeckoHeatPump(GeckoSelect):
    """A select object can select between options and can report the current state."""

    def __init__(
        self, facade: GeckoAsyncFacade, name: str, accessor: GeckoEnumStructAccessor
    ) -> None:
        """Initialize the heatpump class."""
        super().__init__(facade, name, accessor)
        # Set of mappings of constants to UI options
        self.mapping = {
            "CHILL": "Cool",
            "INTERNAL_HEAT": "Electric",
            "HEAT_SAVER": "Eco Heat",
            "HEAT_W_BOOST": "Smart Heat",
            "AUTO_SAVER": "Eco Auto",
            "AUTO_W_BOOST": "Smart Auto",
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
