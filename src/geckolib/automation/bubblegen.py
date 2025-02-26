"""Gecko Bubble generator on Aux."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .pump import GeckoPump

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade


class GeckoBubbleGenerator(GeckoPump):
    """Blowers are based on pumps."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the bubble generator."""
        super().__init__(facade, "Bubble Generator", "Aux")
        if self.is_available and "AuxAsBubbleGen" in self.facade.spa.accessors:
            self.set_availability(
                is_available=self.facade.spa.accessors["AuxAsBubbleGen"].value
            )
