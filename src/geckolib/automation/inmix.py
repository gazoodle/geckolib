"""Gecko inMix accessory class."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.automation.power import GeckoPower

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoInMix(GeckoPower):
    """Gecko inMix support class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the inMix class."""
        super().__init__(facade, "inMix", "INMIX")
        if "InMix-PackType" in facade.spa.accessors:
            _LOGGER.info("Spa has an inMix accessory")
