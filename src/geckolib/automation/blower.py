""" Gecko Blowers """

from .switches import GeckoSwitch


class GeckoBlower(GeckoSwitch):
    """Blowers are based on switches, but might have variable speeds too. They pump air,
    not water"""
