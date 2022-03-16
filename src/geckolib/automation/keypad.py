""" Gecko Keypads """

from .base import GeckoAutomationFacadeBase


class GeckoKeypad(GeckoAutomationFacadeBase):
    """Keypad management class"""

    def __init__(self, facade):
        super().__init__(facade, "Keypad", "KEYPAD")

    def __str__(self):
        return f"{self.name}: Not implemented yet"
