""" Gecko automation support for sensors """

from .base import GeckoAutomationFacadeBase


class GeckoSensorBase(GeckoAutomationFacadeBase):
    """Base sensor allows non-accessor sensors to be implemented"""

    def __init__(self, facade, name, device_class=None):
        super().__init__(facade, name, name.upper())
        self._device_class = device_class

    @property
    def state(self):
        """The state of the sensor"""
        return None

    @property
    def unit_of_measurement(self):
        """The unit of measurement for the sensor, or None"""
        return None

    @property
    def device_class(self):
        """The device class"""
        return self._device_class

    def __repr__(self):
        return f"{self.name}: {self.state}"


########################################################################################
class GeckoSensor(GeckoSensorBase):
    """Sensors wrap accessors state with extra units and device
    class properties"""

    def __init__(self, facade, name, accessor, unit_accessor=None, device_class=None):
        super().__init__(facade, name, device_class)
        self._accessor = accessor
        # Bubble up change notification
        accessor.watch(self._on_change)
        self._unit_of_measurement_accessor = unit_accessor
        if unit_accessor:
            unit_accessor.watch(self._on_change)

    @property
    def state(self):
        """The state of the sensor"""
        return self._accessor.value

    @property
    def unit_of_measurement(self):
        """The unit of measurement for the sensor, or None"""
        if self._unit_of_measurement_accessor is None:
            return None
        return self._unit_of_measurement_accessor.value

    @property
    def accessor(self):
        """Access the accessor member"""
        return self._accessor

    @property
    def monitor(self):
        return f"{self.accessor.tag}: {self.state}"


########################################################################################
class GeckoBinarySensor(GeckoSensor):
    """Binary sensors only have two states"""

    @property
    def is_on(self):
        """Determine if the sensor is on or not"""
        state = self.state
        if isinstance(state, bool):
            return state
        if state == "":
            return False
        return state != "OFF"


########################################################################################
class GeckoFacadeStatusSensor(GeckoSensorBase):
    """String sensor for facade status"""

    def __init__(self, facade, name, device_class=None):
        super().__init__(facade, name, device_class)

        self._last_status = self.facade.status_line
        self.facade.watch(self._on_facade_change)

    def _on_facade_change(self, _sender, _old_value, _new_value):
        current_status = self.facade.status_line
        if not current_status == self._last_status:
            old_status = self._last_status
            self._last_status = current_status
            self._on_change(self, old_status, current_status)

    @property
    def state(self):
        """The state of the sensor"""
        return f"{self._last_status}"


########################################################################################
class GeckoFacadePingSensor(GeckoSensorBase):
    """datetime sensor for facade ping"""

    def __init__(self, facade, name, device_class=None):
        super().__init__(facade, name, device_class)
        self._last_ping_at = self.facade.spa.last_ping_at
        self.facade.watch(self._on_facade_change)

    def _on_facade_change(self, _sender, _old_value, _new_value):
        current_ping_at = self.facade.spa.last_ping_at
        if not current_ping_at == self._last_ping_at:
            old_last_ping_at = self._last_ping_at
            self._last_ping_at = current_ping_at
            self._on_change(self, old_last_ping_at, current_ping_at)

    @property
    def state(self):
        """The state of the sensor"""
        return self._last_ping_at
