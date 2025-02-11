"""Gecko Blowers."""

from .switch import GeckoSwitch


class GeckoBlower(GeckoSwitch):
    """
    Blowers are based on switches.

    They might have variable speeds too. They pump air, not water.
    """
