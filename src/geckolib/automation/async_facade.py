""" Async Facade to hide implementation details """

import logging
import asyncio

from .blower import GeckoBlower
from ..const import GeckoConstants
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight
from .pump import GeckoPump
from .switches import GeckoSwitch
from .sensors import GeckoSensor, GeckoBinarySensor
from .watercare import GeckoWaterCare
from ..driver import Observable
from ..async_locator import GeckoAsyncLocator
from ..async_spa import GeckoAsyncSpa, GeckoSpaConnectionState
from ..async_tasks import AsyncTasks

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncFacade(Observable, AsyncTasks):
    """Async facade"""

    def __init__(self, client_uuid, **kwargs):
        """The Facade is an automation friendly class that manages the interaction between
        a client program and the low-level protocol of a Gecko Alliance spa equipped with
        an in.touch2 module. Ideally there should be no need to import anything other than
        this class, constructed in an appropriate fashion.

        First time:
            ```async with GeckoAsyncFacade(CLIENT_UUID) as facade:```

            ```facade.spas``` contains a list of spas found on the local network, or None

        Subnet usage:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_address="1.2.3.4") as facade:```

            ```facade.spas``` contains either one spa found at the above address pr None

        Connection to known spa:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_identifier="SPA01:02:03:04:05:06") as facade:```

            Will discover this spa on the network and then instigate connection to it,
            ```facade``` has various methods and properties suitable for automation,
            including status

        Connection to known spa at specific address:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_identifier="SPA01:02:03:04:05:06", spa_address="1.2.3.4") as facade:```

            Will connect to this spa on the network at the specified addres.
            ```facade``` has various methods and properties suitable for automation,
            including status
        """
        Observable.__init__(self)
        AsyncTasks.__init__(self)
        self.client_id = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)

        self._spa_address = kwargs.get("spa_address", None)
        if self._spa_address == "":
            self._spa_address = None
        self._spa_identifier = kwargs.get("spa_identifier", None)
        if self._spa_identifier == "":
            self._spa_identifier = None

        _LOGGER.debug(
            "Facade started with UUID: %s ID:%s ADDR:%s",
            self.client_id,
            self._spa_identifier,
            self._spa_address,
        )

        self._sensors = []
        self._binary_sensors = []
        self._water_heater = None
        self._water_care = None
        self._pumps = None
        self._keypad = None
        self._ecomode = None

        self._spa = None
        self._locator = None
        self._ready = False

    async def __aenter__(self):
        self.add_task(self._facade_pump(), "Facade pump")
        return self

    async def __aexit__(self, *exc_info):
        await AsyncTasks.__aexit__(self, exc_info)

    def set_spa_info(self, spa_id, spa_address):
        self._spa_identifier = spa_id
        self._spa_address = spa_address
        self._locator = None
        self._spa = None
        self._ready = False

    async def _facade_pump(self):
        _LOGGER.debug("Facade pump started %s", self)
        while True:

            try:
                # If the facade is ready for action, the pump does nothing
                if self._ready:
                    continue

                # Always run a discovery, it builds the descriptor needed
                if self._locator is None:
                    self._locator = GeckoAsyncLocator(
                        self,
                        spa_address=self._spa_address,
                        spa_identifier=self._spa_identifier,
                    )
                    self._locator.watch(self._on_change)
                    await self._locator.discover()

                # It is possible for the UI to clear the locator, if so we
                # must start this loop again
                if self._locator is None:
                    continue

                # If there was no identifier specified, then we've completed
                # discovery and the facade is ready
                if self._spa_identifier is None:
                    _LOGGER.debug(
                        "Facade is ready as there was no spa identifier, and we should have scanned for them"
                    )
                    self._ready = True
                    continue

                # Check condition where we didn't find any spa but expected to
                if self._locator.spas is None:
                    _LOGGER.error(
                        "Failed to find spa %s at %s",
                        self._spa_identifier,
                        self._spa_address,
                    )
                    self._ready = True
                    continue

                spa = self._locator.spas[0]

                if self._spa is None:
                    self._spa = GeckoAsyncSpa(self.client_id, spa, self)
                    self._spa.watch(self._on_change)
                    await self._spa.connect()

                    # The UI can again clear this, so deal with it
                    if self._spa is None:
                        continue
                    if self._spa.connection_state != GeckoSpaConnectionState.CONNECTED:
                        continue

                    _LOGGER.debug("Facade knows spa is connected")

                    self._water_heater = GeckoWaterHeater(self)
                    self._water_care = GeckoWaterCare(self)
                    self._keypad = GeckoKeypad(self)
                    self.scan_outputs()
                    # Install change notifications
                    for device in self.all_automation_devices:
                        device.watch(self._on_change)

                    self.water_care.change_watercare_mode(
                        await self.spa.async_get_watercare()
                    )

                    _LOGGER.debug("Facade is now ready")
                    self._ready = True
                    self._on_change(self, False, True)

            finally:
                # Keep everything running
                await asyncio.sleep(0)

    async def ready(self):
        while not self._ready:
            await asyncio.sleep(0)

    def scan_outputs(self):
        """Scan the spa outputs to decide what user options are available"""
        _LOGGER.debug("All outputs are %s", self._spa.struct.all_outputs)
        # Workout what (if anything) the outputs are connected to
        all_output_connections = {
            output: self._spa.accessors[output].value
            for output in self._spa.struct.all_outputs
        }
        _LOGGER.debug("Output connections are %s", all_output_connections)
        # Reduce the dictionary to those that are not set to NA (Not Applicable)
        actual_connections = {
            tag: val for (tag, val) in all_output_connections.items() if val != "NA"
        }
        _LOGGER.debug("Actual connections are %s", actual_connections)

        _LOGGER.debug("All devices are %s", self._spa.struct.all_devices)
        # If any of the actual connection values starts with any of the devices,
        # then the device is present
        actual_devices = set(
            [
                device
                for device in self._spa.struct.all_devices
                for val in actual_connections.values()
                if val.startswith(device)
            ]
        )
        _LOGGER.debug("Actual devices are %s", actual_devices)

        _LOGGER.debug("Possible user demands are %s", self._spa.struct.user_demands)
        # Actual user devices are those where the actual device has a corresponding
        # user demand
        self.actual_user_devices = [
            {
                "device": device,
                "user_demand": {
                    "demand": self._spa.accessors[f"{ud}"].tag,
                    "options": self._spa.accessors[f"{ud}"].items,
                },
            }
            for device in actual_devices
            for ud in self._spa.struct.user_demands
            if f"Ud{device}".upper() == ud.upper()
        ]
        _LOGGER.debug("Actual user devices are %s", self.actual_user_devices)

        # These keys can be used to determine the actual state ...
        # Key       Desc        Outputs         Keypad      Direct Drive
        # P1 ...    Pump 1      Out1A->P1H      1           <Doesn't work as expected>
        # Pn ...    Pump n      Out?A/B->PnH/L  n                     ""

        # Fix for issue#1 https://github.com/gazoodle/geckolib/issues/1
        # self.actual_user_devices.append("Waterfall")
        # Remove unknown device classes
        self.actual_user_devices = [
            handled_device
            for handled_device in self.actual_user_devices
            if handled_device["device"] in GeckoConstants.DEVICES
        ]
        _LOGGER.debug("Handled user devices are %s", self.actual_user_devices)

        self._pumps = [
            GeckoPump(
                self,
                device["device"],
                GeckoConstants.DEVICES[device["device"]],
                device["user_demand"],
            )
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device["device"]][3]
            == GeckoConstants.DEVICE_CLASS_PUMP
        ]

        self._blowers = [
            GeckoBlower(
                self, device["device"], GeckoConstants.DEVICES[device["device"]]
            )
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device["device"]][3]
            == GeckoConstants.DEVICE_CLASS_BLOWER
        ]

        self._lights = [
            GeckoLight(self, device["device"], GeckoConstants.DEVICES[device["device"]])
            for device in self.actual_user_devices
            if GeckoConstants.DEVICES[device["device"]][3]
            == GeckoConstants.DEVICE_CLASS_LIGHT
        ]

        self._sensors = [
            GeckoSensor(self, sensor[0], self._spa.accessors[sensor[1]])
            for sensor in GeckoConstants.SENSORS
            if sensor[1] in self._spa.accessors
        ]

        self._binary_sensors = [
            GeckoBinarySensor(
                self, binary_sensor[0], self._spa.accessors[binary_sensor[1]]
            )
            for binary_sensor in GeckoConstants.BINARY_SENSORS
            if binary_sensor[1] in self._spa.accessors
        ]

        if GeckoConstants.KEY_ECON_ACTIVE in self._spa.accessors:
            self._ecomode = GeckoSwitch(
                self,
                GeckoConstants.KEY_ECON_ACTIVE,
                (
                    GeckoConstants.ECON_ACTIVE_DESCRIPTION,
                    GeckoConstants.KEYPAD_ECOMODE,
                    GeckoConstants.KEY_ECON_ACTIVE,
                    GeckoConstants.DEVICE_CLASS_SWITCH,
                ),
            )

    @property
    def is_ready(self):
        return self._ready

    @property
    def unique_id(self):
        """A unique id for the facade"""
        return f"{self.identifier.replace(':', '')}"

    @property
    def name(self):
        """Get the spa name"""
        return self._spa.descriptor.name

    @property
    def identifier(self):
        """Get the spa identifier"""
        return self._spa.descriptor.identifier_as_string

    @property
    def spa(self):
        """Get the spa implementation class"""
        return self._spa

    @property
    def locator(self) -> GeckoAsyncLocator:
        return self._locator

    @property
    def water_heater(self):
        """Get the water heater handler"""
        return self._water_heater

    @property
    def water_care(self):
        """Get the water care handler"""
        return self._water_care

    @property
    def keypad(self):
        """Get the keypad handler"""
        return self._keypad

    @property
    def pumps(self) -> [GeckoPump]:
        """Get the pumps list"""
        return self._pumps

    @property
    def blowers(self):
        """Get the blowers list"""
        return self._blowers

    @property
    def lights(self):
        """Get the lights list"""
        return self._lights

    @property
    def sensors(self):
        """Get the sensor list"""
        return self._sensors

    @property
    def binary_sensors(self):
        """Get the binary sensor list"""
        return self._binary_sensors

    @property
    def eco_mode(self):
        """Get the Eco Mode switch"""
        return self._ecomode

    @property
    def all_user_devices(self):
        """Get all the user controllable devices as a list"""
        return self._pumps + self._blowers + self._lights

    @property
    def all_automation_devices(self):
        """Get all the automation devices as a list"""
        return (
            self.all_user_devices
            + self.sensors
            + self.binary_sensors
            + [self.water_heater, self.water_care, self.keypad, self.eco_mode]
        )

    def get_device(self, key):
        """Get an automation device from the key"""
        for device in self.all_automation_devices:
            if device.key == key:
                return device
        return None

    @property
    def devices(self):
        """Get a list of automation device keys. Keys can be passed to get_device
        to find the specific device"""
        return [device.key for device in self.all_automation_devices]

    @property
    def reminders(self):
        """Get the reminders list"""
        return []

    @property
    def status_line(self) -> str:
        """Get a human readable status line showing the current state of the facade"""
        if self._spa is not None:
            return self._spa.status_line
        if self._locator is not None:
            return self._locator.status_line
        return "Initializing"
