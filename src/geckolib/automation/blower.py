"""Gecko Blowers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .pump import GeckoPump

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade


class GeckoBlower(GeckoPump):
    """Blowers are based on pumps."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the blower."""
        super().__init__(facade, "Blower", "BL")
