""" Decorator classes """

from ..const import GeckoConstants
from .accessor import GeckoStructAccessor


class GeckoTemperatureDecorator(GeckoStructAccessor):
    """Class to decorate a temperature accessor so that the farenheight tenths, offset
    from freezing are handled"""

    def __init__(self, struct_, accessor):
        super().__init__(struct_, accessor.element)

    def _get_value(self, status_block=None):
        """ Get the temperature """
        # Internally, temp is in farenheight tenths, offset from freezing point
        temp = super()._get_value(status_block)
        units = self.struct.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        if units == "C":
            temp = temp / 18.0
        else:
            temp = (temp + 320) / 10.0
        return temp

    def _set_value(self, temp):
        """ Set the temperature """
        units = self.struct.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        if units == "C":
            temp = float(temp) * 18.0
        else:
            temp = (float(temp) * 10.0) - 320
        super()._set_value(int(temp))
