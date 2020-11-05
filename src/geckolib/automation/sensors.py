""" Gecko automation support for sensors """

from .base import GeckoAutomationBase


class GeckoSensor(GeckoAutomationBase):
    """Sensors wrap accessors state with extra units and device
    class properties"""

    def __init__(self, facade, name, accessor, unit_accessor=None):
        super().__init__(facade, name)
        self._accessor = accessor
        self._unit_of_measurement_accessor = unit_accessor
        self._device_class = None

    @property
    def state(self):
        """ The state of the sensor """
        return self._accessor.value

    @property
    def unit_of_measurement(self):
        """ The unit of measurement for the sensor, or None """
        if self._unit_of_measurement_accessor is None:
            return None
        return self._unit_of_measurement_accessor.value

    @property
    def device_class(self):
        """ The device class """
        return self._device_class

    @property
    def accessor(self):
        """ Access the accessor member """
        return self._accessor


###################################################################################################
class GeckoBinarySensor(GeckoSensor):
    """ Binary sensors only have two states """
