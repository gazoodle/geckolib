"""Automation number class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.driver.accessor import GeckoStructAccessor

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoNumber(GeckoAutomationFacadeBase):
    """A number object can input a value in a range and can report the current state."""

    def __init__(
        self,
        facade: GeckoAsyncFacade,
        name: str,
        tag: str,
        unit_accessor: GeckoStructAccessor | str | None = None,
    ) -> None:
        """Initialize the number class."""
        super().__init__(facade, name, tag)
        self._accessor = None
        if tag in facade.spa.accessors:
            self._accessor = facade.spa.accessors[tag]
            self._accessor.watch(self._on_change)
            self.set_availability(is_available=True)
        self.native_min_value: float = 0.0
        self.native_max_value: float = 100.0
        self._unit_accessor = unit_accessor
        if isinstance(self._unit_accessor, GeckoStructAccessor):
            self._unit_accessor.watch(self._on_change)

    @property
    def native_value(self) -> float:
        """Get the current value."""
        if self._accessor is None:
            return 0.0
        return self._accessor.value

    async def async_set_native_value(self, new_value: float) -> None:
        """Set the value of the number entity."""
        if self._accessor is None:
            _LOGGER.warning("%s can't set value with no accessor.", self)
            return
        _LOGGER.debug("%s async set value %f", self.name, new_value)
        await self._accessor.async_set_value(int(new_value))

    @property
    def native_unit_of_measurement(self) -> str | None:
        """The unit of measurement for the sensor, or None."""
        if isinstance(self._unit_accessor, GeckoStructAccessor):
            return self._unit_accessor.value
        return self._unit_accessor

    def __str__(self) -> str:
        """Stringize the class."""
        return f"{self.name}: {self.native_value}"

    @property
    def monitor(self) -> str:
        """Get monitore string."""
        return f"{self.key}: {self.native_value}"
