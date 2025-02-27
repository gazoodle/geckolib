"""Automation inGrid class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.const import GeckoConstants

from .select import GeckoSelect

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade
    from geckolib.driver.accessor import GeckoBoolStructAccessor

_LOGGER = logging.getLogger(__name__)


class GeckoInGrid(GeckoSelect):
    """The inGrid mode."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the inGrid class."""
        super().__init__(facade, "Heating Management", GeckoConstants.KEY_COOLZONE_MODE)
        if GeckoConstants.KEY_INGRID_DETECTED not in self._spa.accessors:
            self.set_availability(is_available=False)
        else:
            in_grid_detected: GeckoBoolStructAccessor = self._spa.accessors[
                GeckoConstants.KEY_INGRID_DETECTED
            ]
            if not in_grid_detected.value:
                self.set_availability(is_available=False)
        # Set of mappings of constants to UI options
        self.set_mapping(
            {
                "INTERNAL_HEAT": "Electrical heater",
                "HEAT_SAVER": "External heater",
                "BOTH_HEAT": "Both",
                "HEAT_W_BOOST": "Smart",
            }
        )

    @property
    def state(self) -> str:
        """Get the current state via the mapping."""
        if self._accessor is None:
            return "(Unknown)"
        return self.mapping[self._accessor.value]

    async def async_set_state(self, new_state: str) -> None:
        """Set the state of the select entity."""
        if self._accessor is None:
            _LOGGER.warning("%s can't set state with no accessor", self)
            return
        if new_state in self.reverse:
            new_state = self.reverse[new_state]
        await self._accessor.async_set_value(new_state)

    @property
    def states(self) -> list[str]:
        """Get the possible states."""
        if self._accessor is None:
            return []
        return list(self.mapping.values())
