"""Gecko Pumps."""

from __future__ import annotations

import logging
from enum import Enum
from typing import TYPE_CHECKING

from geckolib.automation.power import GeckoPower
from geckolib.const import GeckoConstants

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade
    from geckolib.driver.accessor import GeckoStructAccessor

_LOGGER = logging.getLogger(__name__)


class GeckoPump(GeckoPower):
    """Pumps are similar to switches, but might have variable speeds too."""

    class PumpType(Enum):
        """Types of pump."""

        NONE = 0
        SINGLE_SPEED = 1
        TWO_SPEED = 2
        VARIABLE_SPEED = 3

    def __init__(self, facade: GeckoAsyncFacade, name: str, key: str) -> None:
        """Initialize the pump class."""
        super().__init__(facade, name, key)
        self.device_class = GeckoConstants.DEVICE_CLASS_PUMP
        self.pump_type = GeckoPump.PumpType.NONE
        self._state_accessor: GeckoStructAccessor | None = None

        if key in facade.spa.struct.connections:
            self.pump_type = GeckoPump.PumpType.SINGLE_SPEED
        if key.upper() in facade.spa.struct.connections:
            self.pump_type = GeckoPump.PumpType.SINGLE_SPEED

        # Look for P1H, P2H etc
        if f"{key}H" in facade.spa.struct.connections:
            self.pump_type = GeckoPump.PumpType.SINGLE_SPEED

        # Look for BLO
        if f"{key}O" in facade.spa.struct.connections:
            self.pump_type = GeckoPump.PumpType.SINGLE_SPEED

        # Look for P1L, P2L etc
        if f"{key}L" in facade.spa.struct.connections:
            if self.pump_type == GeckoPump.PumpType.NONE:
                self.pump_type = GeckoPump.PumpType.SINGLE_SPEED
            else:
                self.pump_type = GeckoPump.PumpType.TWO_SPEED

        udkey = f"Ud{key}"

        if key == "P1" and "Pump1AsVSP" in facade.spa.accessors:
            p1vsp = facade.spa.accessors["Pump1AsVSP"]
            if p1vsp.value is True:
                self.pump_type = GeckoPump.PumpType.VARIABLE_SPEED
                udkey = "UdVSP1"

        if key == "P3" and "Pump3AsVSP" in facade.spa.accessors:
            p3vsp = facade.spa.accessors["Pump3AsVSP"]
            if p3vsp.value is True:
                self.pump_type = GeckoPump.PumpType.VARIABLE_SPEED
                udkey = "UdVSP3"

        if self.pump_type != GeckoPump.PumpType.NONE and udkey in facade.spa.accessors:
            self._state_accessor = facade.spa.accessors[udkey]
            self._state_accessor.watch(self._on_change)
            self.set_availability(is_available=True)

    @property
    def is_on(self) -> bool:
        """Return True if the device is running, False otherwise."""
        if self._state_accessor is None:
            return False
        if (
            self._state_accessor.accessor_type
            == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE
        ):
            return self._state_accessor.value
        if (
            self._state_accessor.accessor_type
            == GeckoConstants.SPA_PACK_STRUCT_BYTE_TYPE
        ):
            return self._state_accessor.value > 0
        return self._state_accessor.value != "OFF"

    @property
    def is_variable_speed(self) -> bool:
        """Is this a variable speed pump."""
        return self.pump_type == GeckoPump.PumpType.VARIABLE_SPEED

    @property
    def modes(self) -> list[str]:
        """Get the pump modes."""
        if self._state_accessor is None or not self._state_accessor.items:
            return []
        return self._state_accessor.items

    @property
    def mode(self) -> str:
        """Get the pump mode."""
        if self._state_accessor is None:
            return "NA"
        return self._state_accessor.value

    @property
    def percentage(self) -> int:
        """Get the speed percentage."""
        return self._state_accessor.value

    async def async_turn_on(
        self,
        percentage: int | None = None,
        preset_mode: str | None = None,
    ) -> None:
        """Turn on the pump."""
        _LOGGER.info("Turn on pump %s with %s amd %s", self, percentage, preset_mode)
        if self.pump_type == GeckoPump.PumpType.VARIABLE_SPEED:
            if percentage is None:
                percentage = 100
            await self._state_accessor.async_set_value(percentage)
        else:
            if preset_mode is None:
                preset_mode = "HI"
            # Check that it is in the list of modes, otherwise we use "ON"
            if (
                self._state_accessor.items is not None
                and preset_mode not in self._state_accessor.items
            ):
                preset_mode = "ON"
            await self._state_accessor.async_set_value(preset_mode)

    async def async_turn_off(self) -> None:
        """Turn off the pump."""
        if self.pump_type == GeckoPump.PumpType.VARIABLE_SPEED:
            await self._state_accessor.async_set_value(0)
        else:
            await self._state_accessor.async_set_value("OFF")

    async def async_set_mode(self, mode: str) -> None:
        """Set the mode."""
        if self._state_accessor is not None:
            _LOGGER.debug("%s async set mode %s", self.name, mode)
            await self._state_accessor.async_set_value(mode)

    @property
    def state(self) -> str:
        """Get state."""
        if self.pump_type == GeckoPump.PumpType.VARIABLE_SPEED and self.mode == 0:
            return "OFF"
        return f"{self.mode}"

    def __str__(self) -> str:
        """Stringize class."""
        return f"{self.name}: {self.state}"

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        return f"{self.key}: {self.state}"
