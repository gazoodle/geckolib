""" Gecko automation support for sensors """

import logging
from typing import Any
from .base import GeckoAutomationFacadeBase
from ..driver import GeckoBoolStructAccessor

_LOGGER = logging.getLogger(__name__)

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
class GeckoErrorSensor(GeckoSensorBase):
    """Error sensor aggregates all the error keys into a comma separated text string"""
    def __init__(self, facade, device_class=None):
        super().__init__(facade, "Error Sensor", device_class)
        self._state = "No errors or warnings"

        # Listen for changes to any of the error spapack accessors
        for accessor_key in facade.spa.struct.error_keys:
            accessor = facade.spa.struct.accessors[accessor_key]
            accessor.watch(self.update_state)

        # Force initial state
        self.update_state()

    @property
    def state(self):
        """The state of the sensor"""
        return self._state

    def update_state(self, sender: Any = None, old_value: Any = None, new_value: Any = None
    ) -> None:
        self._state = ""

        active_errors = [accessor for accessor_key, accessor in self.facade.spa.struct.accessors.items()
                 if accessor_key in self.facade.spa.struct.error_keys
                 and isinstance(accessor, GeckoBoolStructAccessor)
                 and accessor.value == True]

        if active_errors:
            self._state = ", ".join(err.tag for err in active_errors)
            _LOGGER.debug("Error sensor state is %s", self.state)
        else:
            self._state = "None"
