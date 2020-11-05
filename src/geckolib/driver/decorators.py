""" Decorator classes """

from ..const import GeckoConstants


class GeckoTemperatureDecorator:
    """Class to decorate a temperature accessor so that the farenheight tenths, offset
    from freezing are handled"""

    def __init__(self, spa, accessor):
        self.spa = spa
        self.accessor = accessor

    @property
    def value(self):
        """ Get the temperature """
        # Internally, temp is in farenheight tenths, offset from freezing point
        temp = self.accessor.value
        units = self.spa.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        if units == "C":
            temp = temp / 18.0
        else:
            temp = (temp + 320) / 10.0
        return temp

    @value.setter
    def value(self, temp):
        """ Set the temperature """
        units = self.spa.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        if units == "C":
            temp = float(temp) * 18.0
        else:
            temp = (float(temp) * 10.0) - 320
        self.accessor.value = int(temp)
