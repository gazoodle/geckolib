""" Gecko Watercare """

from .base import GeckoAutomationBase
from ..driver import GeckoGetActiveWatercare, GeckoSetActiveWatercare
from ..const import GeckoConstants


class GeckoWaterCare(GeckoAutomationBase):
    """ Watercare manangement class """

    def __init__(self, facade):
        super().__init__(facade, "WaterCare", "WATERCARE")
        self.active_mode = None

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
        self._spa.send_request(GeckoSetActiveWatercare(new_mode))

    def update(self):
        get_wc = GeckoGetActiveWatercare()
        self._spa.send_request(get_wc)
        while get_wc.active_mode is None:
            if get_wc.aborted:
                raise TimeoutError()
        if self.active_mode != get_wc.active_mode:
            old_mode = self.active_mode
            self.active_mode = get_wc.active_mode
            self._on_change(self, old_mode, self.active_mode)

    def __str__(self):
        if self.active_mode is None:
            return f"{self.name}: Waiting..."
        return f"{self.name}: {GeckoConstants.WATERCARE_MODE_STRING[self.active_mode]}"
