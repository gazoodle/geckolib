"""Energy base class."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from geckolib.automation.base import GeckoAutomationFacadeBase

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade


class GeckoPower(GeckoAutomationFacadeBase):
    """Base class for energy counting objects."""

    def __init__(self, facade: GeckoAsyncFacade, name: str, key: str) -> None:
        """Initialize the energy base class."""
        super().__init__(facade, name, key)
        self.power: float = 0.0

    @property
    @abstractmethod
    def is_on(self) -> bool:
        """Determine if this device is on or not."""

    @property
    def current_power(self) -> float:
        """Get powewr value for this device if it is on."""
        return self.power if self.is_on else 0.0
