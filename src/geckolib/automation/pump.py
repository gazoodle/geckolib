"""Gecko Pumps."""

from __future__ import annotations

import logging
from enum import Enum
from typing import TYPE_CHECKING

from geckolib.automation.power import GeckoPower
from geckolib.const import GeckoConstants

from .sensors import GeckoSensor

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoPump(GeckoPower):
    """Pumps are similar to switches, but might have variable speeds too."""

    def __init__(
        self,
        facade: GeckoAsyncFacade,
        key: str,
        props: tuple[str, int, str, str],
        user_demand: dict,
    ) -> None:
        """Props is a tuple of (name, keypad_button, state_key, device_class)."""
        super().__init__(facade, props[0], key)
        self._state_sensor = GeckoSensor(
            facade, f"{props[0]} State", self._spa.accessors[props[2]]
        )
        self._state_sensor.watch(self._on_change)
        self._keypad_button = props[1]
        self.device_class = props[3]
        self._user_demand = user_demand

    @property
    def is_on(self) -> bool:
        """Return True if the device is running, False otherwise."""
        if (
            self._state_sensor.accessor.accessor_type
            == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE
        ):
            return self._state_sensor.state
        return self._state_sensor.state != "OFF"

    @property
    def modes(self) -> list[str]:
        """Get the pump modes."""
        return self._user_demand["options"]

    @property
    def mode(self) -> str:
        """Get the pump mode."""
        return self._state_sensor.state

    async def async_set_mode(self, mode: str) -> None:
        """Set the mode."""
        try:
            _LOGGER.debug("%s async set mode %s", self.name, mode)
            await self.facade.spa.accessors[
                self._user_demand["demand"]
            ].async_set_value(mode)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception(
                "Exception handling setting %s=%s", self._user_demand["demand"], mode
            )

    def __str__(self) -> str:
        """Stringize class."""
        return f"{self.name}: {self._state_sensor.state}"

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        return f"{self.key}: {self._state_sensor.state}"


class GeckoNewPump(GeckoPower):
    """Pumps are similar to switches, but might have variable speeds too."""

    class PumpType(Enum):
        """Types of pump."""

        NONE = 0
        SINGLE_SPEED = 1
        TWIN_SPEED = 2
        VARIABLE_SPEED = 3

    def __init__(self, facade: GeckoAsyncFacade, name: str, key: str) -> None:
        """Initialize the pump class."""
        super().__init__(facade, name, key)
        self.device_class = GeckoConstants.DEVICE_CLASS_PUMP
        self.pump_type = GeckoNewPump.PumpType.NONE

        if key in facade.connections:
            pass

    @property
    def is_on(self) -> bool:
        """Return True if the device is running, False otherwise."""
        if not self.is_available:
            return False
        self.a = "ex"
        return True

    @property
    def modes(self) -> list[str]:
        """Get the pump modes."""
        return []

    @property
    def mode(self) -> str:
        """Get the pump mode."""
        return ""

    async def async_set_mode(self, mode: str) -> None:
        """Set the mode."""
        _LOGGER.debug("%s async set mode %s", self.name, mode)

    def __str__(self) -> str:
        """Stringize class."""
        return f"{self.name}: {self.mode}"

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        return f"{self.key}: {self.mode}"


class GeckoPump1(GeckoNewPump):
    """Pump 1."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize Pump1 class."""
        super().__init__(facade, "Pump 1", "P1")
