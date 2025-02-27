"""Gecko Reminders."""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from geckolib.driver import GeckoReminderType

from .base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

logger = logging.getLogger(__name__)


class GeckoReminders(GeckoAutomationFacadeBase):
    """Reminders management."""

    class Reminder:
        """A single reminder instance."""

        def __init__(self, rem: tuple[GeckoReminderType, int]) -> None:
            """Initialize a single reminder."""
            self._reminder_type: GeckoReminderType = rem[0]
            self._days: int = rem[1]

        @property
        def reminder_type(self) -> GeckoReminderType:
            """Get the reminder type."""
            return self._reminder_type

        @property
        def description(self) -> str:
            """Get the reminder description."""
            return GeckoReminderType.to_string(self.reminder_type)

        @property
        def days(self) -> int:
            """Get the remaining days."""
            return self._days

        def set_days(self, days: int) -> None:
            """Set the remaining days."""
            self._days = days

        @property
        def monitor(self) -> str:
            """Get the monitor string."""
            return f"{datetime.now(tz=UTC)}"

        def __str__(self) -> str:
            """Stringize the reminder."""
            return (
                f"{self.description} due in {self.days} days"
                if self.days > 0
                else f"{self.description} due today"
                if self.days == 0
                else f"{self.description} overdue by {-self.days} days"
            )

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the reminders class."""
        super().__init__(facade, "Reminders", "REMINDERS")

        self._all_reminders: list[GeckoReminders.Reminder] = []
        self._reminders_handler = None
        self._last_update = None
        if not facade.spa.struct.is_mr_steam:
            self.set_availability(is_available=True)

    @property
    def reminders(self) -> list[Reminder]:
        """Return active reminders."""
        return [
            reminder
            for reminder in self._all_reminders
            if reminder.reminder_type != GeckoReminderType.INVALID
        ]

    def get_reminder(
        self, reminder_type: GeckoReminderType
    ) -> GeckoReminders.Reminder | None:
        """Get the reminder of the specified type, or None if not found."""
        for reminder in self._all_reminders:
            if reminder.reminder_type == reminder_type:
                return reminder
        return None

    async def set_reminder(self, reminder_type: GeckoReminderType, days: int) -> None:
        """Set the remaining days for the specified reminder type."""
        for reminder in self._all_reminders:
            if reminder.reminder_type == reminder_type:
                reminder.set_days(days)
        await self.facade.spa.async_set_reminders(
            [
                (reminder.reminder_type, reminder.days)
                for reminder in self._all_reminders
            ]
        )
        self._on_change(self)

    @property
    def last_update(self) -> datetime | None:
        """Time of last reminder update."""
        return self._last_update

    def change_reminders(self, reminders: list[tuple]) -> None:
        """Call from async facade to update active reminders."""
        self._last_update = datetime.now(tz=UTC)
        self._all_reminders = [
            GeckoReminders.Reminder(reminder) for reminder in reminders
        ]
        self._on_change(self)

    def __str__(self) -> str:
        """Stringize the class."""
        if self.reminders is None:
            return f"{self.name}: Waiting..."
        return f"{self.name}: {self.reminders}"
