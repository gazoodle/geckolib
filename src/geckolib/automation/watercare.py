""" Gecko Watercare """

import logging
from .base import GeckoAutomationFacadeBase

from ..driver import GeckoWatercareProtocolHandler
from ..const import GeckoConstants

_LOGGER = logging.getLogger(__name__)


class GeckoWaterCare(GeckoAutomationFacadeBase):
    """Watercare manangement class"""

    def __init__(self, facade):
        super().__init__(facade, "WaterCare", "WATERCARE")
        self.active_mode = None
        self._water_care_handler = None

    @property
    def mode(self):
        """Return the active water care mode"""
        return self.active_mode

    @property
    def modes(self):
        """Return all the possible water care modes"""
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
                self._spa.get_and_increment_sequence_counter(False),
                new_mode,
                parms=self._spa.sendparms,
            ),
            self._spa.sendparms,
        )
        if new_mode != self.active_mode:
            self.active_mode = new_mode

    async def async_set_mode(self, new_mode):
        """Set the active watercare mode to new_mode.
        new_mode can be a string, in which case the value must be a member of
        GeckoConstants.WATERCARE_MODE_STRING, or it can be an integer from
        GeckoConstants.WATERCARE_MODE
        """
        if isinstance(new_mode, str):
            new_mode = GeckoConstants.WATERCARE_MODE_STRING.index(new_mode)
        await self._spa.async_set_watercare(new_mode)
        self.change_watercare_mode(new_mode)

    def _on_watercare(self, handler, sender):
        if self.active_mode != handler.mode:
            old_mode = self.active_mode
            self.active_mode = handler.mode
            self._on_change(self, old_mode, self.active_mode)
        self._water_care_handler = None

    def update(self):
        if self._water_care_handler is not None:
            return

        self._water_care_handler = GeckoWatercareProtocolHandler.request(
            self._spa.get_and_increment_sequence_counter(False),
            on_handled=self._on_watercare,
            parms=self._spa.sendparms,
        )
        self._spa.add_receive_handler(self._water_care_handler)
        self._spa.queue_send(self._water_care_handler, self._spa.sendparms)

    def change_watercare_mode(self, new_mode):
        if self.active_mode != new_mode:
            old_mode = self.active_mode
            self.active_mode = new_mode
            self._on_change(self, old_mode, self.active_mode)

    def __str__(self):
        if self.active_mode is None:
            return f"{self.name}: Waiting..."
        if self.active_mode < 0 or self.active_mode > len(
            GeckoConstants.WATERCARE_MODE_STRING
        ):
            return f"Unknown Water care mode (index:{self.active_mode})"
        return f"{self.name}: {GeckoConstants.WATERCARE_MODE_STRING[self.active_mode]}"

    @property
    def monitor(self):
        if self.active_mode is None:
            return "WC: ?"
        return f"WC: {self.active_mode}"
