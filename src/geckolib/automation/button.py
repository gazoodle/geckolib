"""GeckoButton class"""

import logging

from .base import GeckoAutomationBase

_LOGGER = logging.getLogger(__name__)


class GeckoButton(GeckoAutomationBase):
    """A button can be pressed ... that's it!"""

    def __init__(self, unique_id, name, parent_name, key):
        super().__init__(unique_id, name, parent_name, key)

    async def async_press(self):
        pass
