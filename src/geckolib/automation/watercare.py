""" Gecko Watercare """

import logging
from .base import GeckoAutomationBase

from ..driver import GeckoWatercareProtocolHandler
from ..const import GeckoConstants

_LOGGER = logging.getLogger(__name__)


class GeckoWaterCare(GeckoAutomationBase):
    """ Watercare manangement class """

    def __init__(self, facade):
        super().__init__(facade, "WaterCare", "WATERCARE")
        self.active_mode = None
        self._water_care_handler = None

    @property
    def mode(self):
        """ Return the active water care mode """
        return self.active_mode

    @property
    def modes(self):
        """ Return all the possible water care modes """
        return GeckoConstants.WATERCARE_MODE_STRING

    def set_mode(self, new_mode):
        """Set the active watercare mode to new_mode.
        new_mode can be a string, in which case the value must be a member of
        GeckoConstants.WATERCARE_MODE_STRING, or it can be an integer from
        GeckoConstants.WATERCARE_MODE
        """
        if isinstance(new_mode, str):
            new_mode = GeckoConstants.WATERCARE_MODE_STRING.index(new_mode)
        self._spa.queue_send(
            GeckoWatercareProtocolHandler.set(
                self._spa.get_and_increment_sequence_counter(),
                new_mode,
                parms=self._spa.sendparms,
            ),
            self._spa.sendparms,
        )

    def _on_watercare(self, handler, socket, sender):
        if self.active_mode != handler.mode:
            old_mode = self.active_mode
            self.active_mode = handler.mode
            self._on_change(self, old_mode, self.active_mode)
        self._water_care_handler = None

    def update(self):
        if self._water_care_handler is not None:
            return

        self._water_care_handler = GeckoWatercareProtocolHandler.request(
            self._spa.get_and_increment_sequence_counter(),
            on_handled=self._on_watercare,
            parms=self._spa.sendparms,
        )
        self._spa.add_receive_handler(self._water_care_handler)
        self._spa.queue_send(self._water_care_handler, self._spa.sendparms)

    def __str__(self):
        if self.active_mode is None:
            return f"{self.name}: Waiting..."
        return f"{self.name}: {GeckoConstants.WATERCARE_MODE_STRING[self.active_mode]}"
