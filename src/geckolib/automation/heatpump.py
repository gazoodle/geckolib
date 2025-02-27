"""Automation heatpump class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.const import GeckoConstants

from .select import GeckoSelect

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade
    from geckolib.driver.accessor import (
        GeckoBoolStructAccessor,
    )

_LOGGER = logging.getLogger(__name__)


class GeckoHeatPump(GeckoSelect):
    """The heatpump mode."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the heatpump class."""
        super().__init__(facade, "Heat Pump", GeckoConstants.KEY_COOLZONE_MODE)

        if GeckoConstants.KEY_MODBUS_HEATPUMP_DETECTED not in self._spa.accessors:
            self.set_availability(is_available=False)
        else:
            modbus_heatpump_detected: GeckoBoolStructAccessor = self._spa.accessors[
                GeckoConstants.KEY_MODBUS_HEATPUMP_DETECTED
            ]
            if not modbus_heatpump_detected.value:
                self.set_availability(is_available=False)

        # Set of mappings of constants to UI options
        self.set_mapping(
            {
                "CHILL": "Cool",
                "INTERNAL_HEAT": "Electric",
                "HEAT_SAVER": "Eco Heat",
                "HEAT_W_BOOST": "Smart Heat",
                "AUTO_SAVER": "Eco Auto",
                "AUTO_W_BOOST": "Smart Auto",
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
