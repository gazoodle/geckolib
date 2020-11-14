""" Gecko Lights """

from .switches import GeckoSwitch


class GeckoLight(GeckoSwitch):
    """Lights are based on switches, but might have brightness and
    colours as options"""
