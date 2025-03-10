"""Bain Ultra class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.automation.heater import GeckoWaterHeaterAbstract
from geckolib.automation.number import GeckoNumber
from geckolib.automation.select import GeckoSelect
from geckolib.automation.switch import GeckoSwitch
from geckolib.const import GeckoConstants

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class BainUltra(GeckoWaterHeaterAbstract):
    """Bain Ultra support class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the Bain Ultra class."""
        super().__init__(facade, "Bath", "BAIN")
        if not facade.spa.struct.is_bain_ultra:
            return

        self.set_availability(is_available=True)

        self.onoff = GeckoSwitch(
            facade,
            GeckoConstants.KEY_BAIN_POWER_STATE,
            (
                "On/Off",
                GeckoConstants.KEY_BAIN_POWER_STATE,
                GeckoConstants.DEVICE_CLASS_SWITCH,
            ),
        )
        self.onoff.watch(self._on_change)
        # The spa pack didn't set Read/Write on the power property, but the BU client
        # wrote to it anyway, so we will too...
        self.facade.spa.accessors[GeckoConstants.KEY_BAIN_POWER_STATE].set_read_write(
            "ALL"
        )

        self.geysair = GeckoSwitch(
            facade,
            GeckoConstants.KEY_BAIN_GEYSAIR,
            (
                "Geysair",
                GeckoConstants.KEY_BAIN_GEYSAIR,
                GeckoConstants.DEVICE_CLASS_BLOWER,
            ),
        )
        self.geysair.watch(self._on_change)
        # The spa pack didn't set Read/Write on the geysair property, but the BU client
        # wrote to it anyway, so we will too...
        self.facade.spa.accessors[GeckoConstants.KEY_BAIN_GEYSAIR].set_read_write("ALL")

        self.backrest = GeckoSelect(
            facade, "Heated Backrest", GeckoConstants.KEY_BAIN_HEATER1
        )
        self.backrest.watch(self._on_change)
        self.backrest2 = GeckoSelect(
            facade, "2nd Heated Backrest", GeckoConstants.KEY_BAIN_HEATER2
        )
        self.backrest2.watch(self._on_change)

        self.bath_runtime = GeckoNumber(
            facade, "Duration", GeckoConstants.KEY_BAIN_DURATION, "min"
        )
        self.bath_runtime.native_max_value = 30.0
        self.bath_runtime.watch(self._on_change)
        self.bath_intensity = GeckoNumber(
            facade, "Intensity", GeckoConstants.KEY_BAIN_INTENSITY, "%"
        )
        self.bath_intensity.watch(self._on_change)

        self.drying_cycle = GeckoSelect(
            facade, "Drying Cycle", GeckoConstants.KEY_BAIN_DRYING_CYCLE
        )
        self.drying_cycle.watch(self._on_change)
        self.drying_cycle_delay = GeckoNumber(
            facade,
            "Drying Cycle Delay",
            GeckoConstants.KEY_BAIN_DRYING_CYCLE_DELAY,
            "min",
        )
        self.drying_cycle_delay.native_step = 5.0
        self.drying_cycle_delay.watch(self._on_change)

        self.drying_cycle_hour = GeckoNumber(
            facade, "Drying Cycle Hour", GeckoConstants.KEY_BAIN_DRYING_CYCLE_HOUR, "hr"
        )
        self.drying_cycle_hour.native_max_value = 23.0
        self.drying_cycle_hour.watch(self._on_change)

        self.drying_cycle_minute = GeckoNumber(
            facade,
            "Drying Cycle Minute",
            GeckoConstants.KEY_BAIN_DRYING_CYCLE_MINUTE,
            "min",
        )
        self.drying_cycle_minute.native_max_value = 59.0
        self.drying_cycle_minute.native_step = 5.0
        self.drying_cycle_minute.watch(self._on_change)

        self.chroma = GeckoSelect(facade, "Chroma", GeckoConstants.KEY_BAIN_CHROMA)
        has_chromo = self.facade.spa.accessors[GeckoConstants.KEY_BAIN_HAS_CHROMO]
        self.chroma.set_availability(is_available=has_chromo.value == "DELUXE")

    @property
    def switches(self) -> list[GeckoSwitch]:
        """Get a list of all the switches."""
        if self.is_available:
            return [self.onoff, self.geysair]
        return []

    @property
    def selects(self) -> list[GeckoSelect]:
        """Get a list of all the selects."""
        if self.is_available:
            return [self.backrest, self.backrest2]
        return []

    @property
    def current_operation(self) -> str:
        """Get the current operation."""
        if not self.onoff.is_on:
            return "Turned off"
        return f"Running, {self.bath_runtime} remaining"
