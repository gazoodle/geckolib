""" Gecko Reminders """
from __future__ import annotations

import logging
from datetime import datetime

from .base import GeckoAutomationFacadeBase
from ..driver import GeckoRemindersProtocolHandler, GeckoReminderType
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)


class GeckoReminders(GeckoAutomationFacadeBase):
    """Reminders management"""

    class Reminder:
        """A single reminder instance"""

        def __init__(self, rem: Tuple[GeckoReminderType, int]) -> None:
            self._type: GeckoReminderType = rem[0]
            self._days: int = rem[1]

        @property
        def type(self) -> GeckoReminderType:
            return self._type

        @property
        def description(self) -> str:
            return GeckoReminderType.to_string(self.type)

        @property
        def days(self) -> int:
            return self._days

        @property
        def monitor(self) -> str:
            return f"{datetime.now()}"

        def __str__(self):
            return (
                f"{self.description} due in {self.days} days"
                if self.days > 0
                else f"{self.description} due today"
                if self.days == 0
                else f"{self.description} overdue by {-self.days} days"
            )

    def __init__(self, facade):
        super().__init__(facade, "Reminders", "REMINDERS")

        self._active_reminders: List[GeckoReminders.Reminder] = []
        self._reminders_handler = None
        self._last_update = None

    @property
    def reminders(self):
        """return all reminders"""
        return self._active_reminders

    def get_reminder(
        self, reminder_type: GeckoReminderType
    ) -> Optional[GeckoReminders.Reminder]:
        """Get the reminder of the specified type, or None if not found"""
        for reminder in self.reminders:
            if reminder.type == reminder_type:
                return reminder
        return None

    @property
    def last_update(self) -> Optional[datetime]:
        """Time of last reminder update"""
        return self._last_update

    def change_reminders(self, reminders: List[Tuple]):
        """Called from async facade to update active reminders"""
        self._last_update = datetime.utcnow()
        self._active_reminders = []
        for reminder in reminders:
            if reminder[0] != GeckoReminderType.INVALID:
                self._active_reminders.append(GeckoReminders.Reminder(reminder))
        self._on_change(self)

    def _on_reminders(self, handler: GeckoRemindersProtocolHandler, sender):
        """call to from protocal handler. Will filter out only the active reminders"""
        self._active_reminders = []
        if handler.reminders is not None:
            # get actual time
            now = datetime.now()  # current date and time
            time = now.strftime("%d.%m.%Y, %H:%M:%S")
            self._active_reminders.append(tuple(("Time", time)))  # type: ignore
            for reminder in handler.reminders:
                if reminder[0] != GeckoReminderType.INVALID:
                    self._active_reminders.append(
                        tuple(
                            (GeckoReminderType.to_string(reminder[0]), reminder[1])
                        )  # type: ignore
                    )

        self._reminders_handler = None

    def update(self):
        self._reminders_handler = GeckoRemindersProtocolHandler.request(
            self._spa.get_and_increment_sequence_counter(False),
            on_handled=self._on_reminders,
            parms=self._spa.sendparms,
        )

        self._spa.add_receive_handler(self._reminders_handler)
        self._spa.queue_send(self._reminders_handler, self._spa.sendparms)

    def __str__(self):
        if self.reminders is None:
            return f"{self.name}: Waiting..."
        return f"{self.name}: {self.reminders}"
