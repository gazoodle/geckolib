"""Gecko Reminders."""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from geckolib.driver import GeckoRemindersProtocolHandler, GeckoReminderType

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

        self._active_reminders: list[GeckoReminders.Reminder] = []
        self._reminders_handler = None
        self._last_update = None

    @property
    def reminders(self) -> list[Reminder]:
        """Return all reminders."""
        return self._active_reminders

    def get_reminder(
        self, reminder_type: GeckoReminderType
    ) -> GeckoReminders.Reminder | None:
        """Get the reminder of the specified type, or None if not found."""
        for reminder in self.reminders:
            if reminder.reminder_type == reminder_type:
                return reminder
        return None

    @property
    def last_update(self) -> datetime | None:
        """Time of last reminder update."""
        return self._last_update

    def change_reminders(self, reminders: list[tuple]) -> None:
        """Call from async facade to update active reminders."""
        self._last_update = datetime.now(tz=UTC)
        self._active_reminders = []
        for reminder in reminders:
            if reminder[0] != GeckoReminderType.INVALID:
                self._active_reminders.append(GeckoReminders.Reminder(reminder))
        self._on_change(self)

    def _on_reminders(
        self, handler: GeckoRemindersProtocolHandler, _sender: tuple
    ) -> None:
        """Call to from protocal handler. Will filter out only the active reminders."""
        self._active_reminders = []
        if handler.reminders is not None:
            # get actual time
            now = datetime.now(tz=UTC)  # current date and time
            time = now.strftime("%d.%m.%Y, %H:%M:%S")
            self._active_reminders.append(("Time", time))
            for reminder in handler.reminders:
                if reminder[0] != GeckoReminderType.INVALID:
                    self._active_reminders.append(
                        (GeckoReminderType.to_string(reminder[0]), reminder[1])
                    )

        self._reminders_handler = None

    def obsolete_update(self) -> None:
        """Update the reminders."""
        self._reminders_handler = GeckoRemindersProtocolHandler.request(
            self._spa.get_and_increment_sequence_counter(),
            on_handled=self._on_reminders,
            parms=self._spa.sendparms,
        )

        self._spa.add_receive_handler(self._reminders_handler)
        self._spa.queue_send(self._reminders_handler, self._spa.sendparms)

    def __str__(self) -> str:
        """Stringize the class."""
        if self.reminders is None:
            return f"{self.name}: Waiting..."
        return f"{self.name}: {self.reminders}"
