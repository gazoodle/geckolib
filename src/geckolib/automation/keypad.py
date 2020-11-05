""" Gecko Keypads """

from .base import GeckoAutomationBase


class GeckoKeypad(GeckoAutomationBase):
    """ Keypad management class """

    def __init__(self, facade):
        super().__init__(facade, "Keypad")

    def __str__(self):
        return "{0}: Not implemented yet".format(self.name)
