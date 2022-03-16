""" Gecko Reminders """

import logging
from datetime import datetime

from .base import GeckoAutomationBase
from ..driver import GeckoRemindersProtocolHandler

logger = logging.getLogger(__name__)


class GeckoReminders(GeckoAutomationBase):
    """ Reminders management """

    def __init__(self, facade):
        super().__init__(facade, "Reminders", "REMINDERS")

        self.active_reminders = None
        self._reminders_handler = None

    @property
    def reminders(self):
        """ return all reminders"""
        return self.active_reminders

    def _on_reminders(self, handler: GeckoRemindersProtocolHandler, socket, sender):
        """ call to from protocal handler. Will filter out only the active reminders"""
        self.active_reminders = []
        if handler.reminders is not None:
            # get actual time
            now = datetime.now()  # current date and time
            time = now.strftime("%d.%m.%Y, %H:%M:%S")
            self.active_reminders.append(tuple(("Time", time)))
            for reminder in handler.reminders:
                if reminder[0] != 'Invalid':
                    self.active_reminders.append(reminder)

    def update(self):
        self._reminders_handler = GeckoRemindersProtocolHandler.request(
            self._spa.get_and_increment_sequence_counter(),
            on_handled=self._on_reminders,
            parms=self._spa.sendparms,
            timeout=5,
            retry=2
        )

        self._spa.add_receive_handler(self._reminders_handler)
        self._spa.queue_send(self._reminders_handler, self._spa.sendparms)

    def __str__(self):
        if self.reminders is None:
            return f"{self.name}: Waiting..."
        return f"{self.name}: {self.reminders}"
