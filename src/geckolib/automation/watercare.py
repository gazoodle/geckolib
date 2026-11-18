"""Gecko Watercare."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.const import GeckoConstants
from geckolib.driver.protocol.watercare import (
    GeckoScheduleDay,
    GeckoWatercareSchedule,
    GeckoWatercareScheduleManager,
    GeckoWatercareScheduleType,
)

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoWaterCare(GeckoAutomationFacadeBase):
    """Watercare manangement class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize watercare class."""
        super().__init__(facade, "WaterCare", "WATERCARE")
        self.active_mode: int | None = None
        self._schedules = GeckoWatercareScheduleManager()
        if facade.spa.struct.is_spa_pack:
            self.set_availability(is_available=True)

    @property
    def mode(self) -> int | None:
        """Return the active water care mode."""
        return self.active_mode

    @property
    def modes(self) -> list[str]:
        """Return all the possible water care modes."""
        return GeckoConstants.WATERCARE_MODE_STRING

    @property
    def state(self) -> str:
        """Return the current state."""
        if self.mode is None:
            return "Unknown"
        return GeckoConstants.WATERCARE_MODE_STRING[self.mode]

    @property
    def states(self) -> list[str]:
        """Return all the states."""
        return self.modes

    async def async_set_state(self, new_mode: str | int) -> None:
        """Set the state. Support select style objects."""
        await self.async_set_mode(new_mode)

    async def async_set_mode(self, new_mode: str | int) -> None:
        """
        Set the active watercare mode to new_mode.

        new_mode can be a string, in which case the value must be a member of
        GeckoConstants.WATERCARE_MODE_STRING, or it can be an integer from
        GeckoConstants.WATERCARE_MODE
        """
        if isinstance(new_mode, str):
            new_mode = GeckoConstants.WATERCARE_MODE_STRING.index(new_mode)
        await self._spa.async_set_watercare_mode(new_mode)
        self.change_watercare_mode(new_mode)

    def change_watercare_mode(self, new_mode: int) -> None:
        """Change the watercare mode."""
        if self.active_mode != new_mode:
            old_mode = self.active_mode
            self.active_mode = new_mode
            self._on_change(self, old_mode, self.active_mode)

    @property
    def schedules(self) -> list[GeckoWatercareSchedule]:
        """Get the schedules for all the watercare modes."""
        return list(self._schedules.schedules)

    def schedules_for_mode(self, mode: int | str) -> list[GeckoWatercareSchedule]:
        """Get the schedules for one watercare mode, in the order the spa has them."""
        if isinstance(mode, str):
            mode = GeckoConstants.WATERCARE_MODE_STRING.index(mode)
        return self._schedules.for_mode(mode)

    def change_schedules(self, schedules: list[GeckoWatercareSchedule]) -> None:
        """Change the known schedules, and tell the watchers if they differ."""
        if self._schedules.schedules != schedules:
            old_schedules = self.schedules
            self._schedules = GeckoWatercareScheduleManager(schedules)
            self._on_change(self, old_schedules, self.schedules)

    async def async_refresh_schedules(self) -> None:
        """Get the schedules from the spa."""
        schedules = await self._spa.async_get_watercare_schedules()
        if schedules is not None:
            self.change_schedules(schedules)

    async def async_add_schedule(  # noqa: PLR0913
        self,
        mode: int | str,
        schedule_type: GeckoWatercareScheduleType,
        start_day: int,
        start_hour: int,
        start_minute: int,
        stop_hour: int,
        stop_minute: int,
        stop_day: int | None = None,
    ) -> bool:
        """
        Add a schedule to a watercare mode.

        If `stop_day` is not given, `start_day` may be a single day or one of the
        GeckoScheduleDay conveniences WEEKDAY, WEEKEND or EVERYDAY.
        """
        if isinstance(mode, str):
            mode = GeckoConstants.WATERCARE_MODE_STRING.index(mode)
        if stop_day is None:
            start_day, stop_day = GeckoScheduleDay.day_range(start_day)
        schedule = GeckoWatercareSchedule(
            mode,
            schedule_type,
            self._schedules.next_number(mode, schedule_type),
            start_day,
            stop_day,
            start_hour,
            start_minute,
            stop_hour,
            stop_minute,
        )
        added = await self._spa.async_add_watercare_schedule(schedule)
        # The spa is the source of truth for numbering, so always re-read
        await self.async_refresh_schedules()
        return added

    async def async_modify_schedule(self, schedule: GeckoWatercareSchedule) -> bool:
        """Modify an existing schedule, which is identified by its mode/type/number."""
        modified = await self._spa.async_modify_watercare_schedule(schedule)
        await self.async_refresh_schedules()
        return modified

    async def async_delete_schedule(self, schedule: GeckoWatercareSchedule) -> bool:
        """Delete a schedule, which is identified by its mode/type/number."""
        deleted = await self._spa.async_delete_watercare_schedule(schedule)
        await self.async_refresh_schedules()
        return deleted

    def __str__(self) -> str:
        """Stringise the class."""
        if not self.is_available:
            return f"{self.name}: Unavailable"
        if self.active_mode is None:
            return f"{self.name}: Waiting..."
        if self.active_mode < 0 or self.active_mode > len(
            GeckoConstants.WATERCARE_MODE_STRING
        ):
            return f"Unknown Water care mode (index:{self.active_mode})"
        return f"{self.name}: {GeckoConstants.WATERCARE_MODE_STRING[self.active_mode]}"

    @property
    def monitor(self) -> str:
        """Get monitor string."""
        if not self.is_available:
            return "WC: None"
        if self.active_mode is None:
            return "WC: ?"
        return f"WC: {self.active_mode}"
