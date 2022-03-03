""" Async Facade to hide implementation details """

from __future__ import annotations

import logging
import asyncio
import gc

from geckolib.automation.base import GeckoAutomationBase

from .blower import GeckoBlower
from ..const import GeckoConstants
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight
from .pump import GeckoPump
from .switches import GeckoSwitch
from .sensors import (
    GeckoSensor,
    GeckoBinarySensor,
    GeckoFacadeStatusSensor,
    GeckoFacadePingSensor,
    GeckoSensorBase,
)
from .watercare import GeckoWaterCare
from ..driver import Observable
from ..async_locator import GeckoAsyncLocator
from ..async_spa import GeckoAsyncSpa, GeckoSpaConnectionState
from ..async_tasks import AsyncTasks

from typing import Optional, List

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncFacade(Observable, AsyncTasks):
    """Async facade"""

    def __init__(self, client_uuid: str, **kwargs: str) -> None:
        """The Facade is an automation friendly class that manages the interaction
        between a client program and the low-level protocol of a Gecko Alliance spa
        equipped with an in.touch2 module. Ideally there should be no need to import
        anything other than this class, constructed in an appropriate fashion.

        First time:
            ```async with GeckoAsyncFacade(CLIENT_UUID) as facade:```

            ```facade.spas``` contains a list of spas found on the local network,
            or None

        Subnet usage:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_address="1.2.3.4")``` as facade:```

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
        """  # noqa
        Observable.__init__(self)
        AsyncTasks.__init__(self)
        self.client_id = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)

        self._spa_address: Optional[str] = kwargs.get("spa_address", None)
        if self._spa_address == "":
            self._spa_address = None
        self._spa_identifier: Optional[str] = kwargs.get("spa_identifier", None)
        if self._spa_identifier == "":
            self._spa_identifier = None
        # spa_name is only used for a very brief period during startup
        self._spa_name: Optional[str] = kwargs.get("spa_name", None)
        if self._spa_name == "":
            self._spa_name = None

        _LOGGER.debug(
            "Facade started with UUID:%r ID:%s ADDR:%s",
            self.client_id,
            self._spa_identifier,
            self._spa_address,
        )

        self._spa: Optional[GeckoAsyncSpa] = None
        self._locator: Optional[GeckoAsyncLocator] = None

        self._facade_status_sensor = GeckoFacadeStatusSensor(self, "Status", "string")
        self._facade_ping_sensor: Optional[GeckoFacadePingSensor] = None

        self._sensors: List[GeckoSensorBase] = []
        self._binary_sensors: List[GeckoBinarySensor] = []
        self._water_heater: Optional[GeckoWaterHeater] = None
        self._water_care: Optional[GeckoWaterCare] = None
        self._pumps: List[GeckoPump] = []
        self._blowers: List[GeckoBlower] = []
        self._lights: List[GeckoLight] = []
        self._keypad: Optional[GeckoKeypad] = None
        self._ecomode: Optional[GeckoSwitch] = None

        self._ready = False

    async def __aenter__(self) -> GeckoAsyncFacade:
        self.add_task(self._facade_pump(), "Facade pump", "FACADE")
        self.add_task(self._facade_health_monitor(), "Facade health monitor", "FACADE")
        self.add_task(self._facade_update(), "Facade update", "FACADE")
        return self

    async def __aexit__(self, *exc_info) -> None:
        await AsyncTasks.__aexit__(self, exc_info)

    def set_spa_info(self, spa_id, spa_address) -> None:
        self._spa_identifier = spa_id
        self._spa_address = spa_address
        self._locator = None
        self._spa = None
        self._ready = False

    async def reconnect_spa(self) -> None:
        if self._spa is None:
            return
        for device in self.all_automation_devices:
            device.unwatchall()
        self._spa.disconnect()
        self._spa = None
        self._ready = False
        gc.collect()

    async def _facade_health_monitor(self) -> None:
        _LOGGER.debug("Facade health monitor started")
        while True:

            try:

                if self._spa is None:
                    continue

                if self._spa.connection_state == GeckoSpaConnectionState.PING_RESTORED:
                    _LOGGER.info(
                        "Facade health monitor reconnecting spa after ping restored"
                    )
                    await self.reconnect_spa()

            finally:
                await asyncio.sleep(
                    GeckoConstants.FACADE_HEALTH_MONITOR_DUTY_CYCLE_IN_SECONDS
                )

    async def _facade_pump(self) -> None:
        _LOGGER.debug("Facade pump started %s", self)
        while True:

            try:
                # If the facade is ready for action, the pump does nothing
                if self._ready:
                    continue

                # Always run a discovery if needed, it builds the descriptor
                # required for spa connection
                if self._locator is None:
                    self._locator = GeckoAsyncLocator(
                        self,
                        spa_address=self._spa_address,
                        spa_identifier=self._spa_identifier,
                    )
                    self._locator.watch(self._on_change)
                    await self._locator.discover()

                # It is possible for the locator to get cleared
                if self._locator is None:
                    continue

                # If there was no identifier specified, then we've completed
                # discovery and the facade is ready - won't connect to any spa
                # at this stage
                if self._spa_identifier is None:
                    _LOGGER.debug(
                        (
                            "Facade is ready as there was no spa identifier, "
                            "and we have already scanned for them"
                        )
                    )
                    self._ready = True
                    continue

                # Condition where we didn't find any spa but we expected to
                if self._locator.spas is None:
                    _LOGGER.error(
                        "Failed to find spa %s at %s",
                        self._spa_identifier,
                        self._spa_address,
                    )
                    self._ready = True
                    continue

                # There ought to be only one spa at this point
                assert len(self._locator.spas) == 1
                spa_descriptor = self._locator.spas[0]

                # So now we start the spa connection process
                if self._spa is None:
                    self._spa = GeckoAsyncSpa(self.client_id, spa_descriptor, self)
                    self._spa.watch(self._on_change)
                    self._facade_ping_sensor = GeckoFacadePingSensor(
                        self, "Last Ping", "date"
                    )
                    await self._spa.connect()

                    # The spa can be cleared so we have to cope with this state
                    if self._spa is None:
                        continue

                    # The connection phase completed or timed-out, but we're not
                    # in a connected state, so we cannot continue around this loop
                    if self._spa.connection_state != GeckoSpaConnectionState.CONNECTED:
                        continue

                    _LOGGER.debug(
                        "Facade knows spa is connected, build automation helpers"
                    )
                    self._water_heater = GeckoWaterHeater(self)
                    self._water_care = GeckoWaterCare(self)
                    self._keypad = GeckoKeypad(self)
                    self._scan_outputs()

                    # Install change notifications
                    for device in self.all_automation_devices:
                        device.watch(self._on_change)

                    # Run an inital watercare process
                    self._water_care.change_watercare_mode(
                        await self._spa.async_get_watercare()
                    )

                    _LOGGER.debug("Facade is now ready")
                    self._ready = True
                    # Report that state
                    self._on_change(self, False, True)

            finally:
                # Keep everything running
                await asyncio.sleep(0)

    async def _facade_update(self) -> None:
        _LOGGER.debug("Facade health monitor started")
        while True:

            try:
                if not self._ready:
                    continue

                assert self._water_care is not None
                assert self._spa is not None

                self._water_care.change_watercare_mode(
                    await self._spa.async_get_watercare()
                )

            finally:
                await asyncio.sleep(GeckoConstants.FACADE_UPDATE_FREQUENCY_IN_SECONDS)

    async def ready(self) -> None:
        """Coroutine to allow waiting for facade to be ready"""
        while not self._ready:
            await asyncio.sleep(0)

    def _scan_outputs(self) -> None:
        """Scan the spa outputs to decide what user options are available"""

        assert self._spa is not None
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

        self._sensors = [  # type: ignore
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
    def is_ready(self) -> bool:
        """Returns True if the facade is fully ready"""
        return self._ready

    @property
    def unique_id(self) -> str:
        """A unique id for the facade"""
        return f"{self.identifier.replace(':', '')}"

    @property
    def name(self) -> str:
        """Get the spa name.

        Will return the most up-to-date name if available (i.e. the spa has
        responded to an initial handshake.

        If this is not available, it will use a name given during initial
        setup (which might be out of date)

        If this isn't available, it will use the spa identifier, which is
        very unhelpful,

        If none of the above is available, it will return an emtpy string
        """
        if self._spa is not None:
            # If we have a spa, then get it from the descriptor name
            return self._spa.descriptor.name
        elif self._spa_name is not None:
            # Otherwise, if we have an initial spa name, use that
            return self._spa_name
        elif self._spa_identifier:
            # Not the best option, we use the identifier
            return self.identifier
        else:
            # Finally we got nothing ...
            return ""

    @property
    def identifier(self) -> str:
        """Get the spa identifier"""
        assert self._spa_identifier is not None
        return self._spa_identifier

    @property
    def spa(self) -> Optional[GeckoAsyncSpa]:
        """Get the spa implementation instance"""
        return self._spa

    @property
    def locator(self) -> Optional[GeckoAsyncLocator]:
        """Get the spa locator implementation instance"""
        return self._locator

    @property
    def water_heater(self) -> Optional[GeckoWaterHeater]:
        """Get the water heater handler if available"""
        return self._water_heater

    @property
    def water_care(self) -> Optional[GeckoWaterCare]:
        """Get the water care handler if available"""
        return self._water_care

    @property
    def keypad(self) -> Optional[GeckoKeypad]:
        """Get the keypad handler if available"""
        return self._keypad

    @property
    def pumps(self) -> List[GeckoPump]:
        """Get the pumps list"""
        return self._pumps

    @property
    def blowers(self) -> List[GeckoBlower]:
        """Get the blowers list"""
        return self._blowers

    @property
    def lights(self) -> List[GeckoLight]:
        """Get the lights list"""
        return self._lights

    @property
    def sensors(self) -> List[GeckoSensorBase]:
        """Get the sensor list"""
        all_sensors = list(self._sensors)
        all_sensors.append(self._facade_status_sensor)
        if self._facade_ping_sensor is not None:
            all_sensors.append(self._facade_ping_sensor)
        return all_sensors

    @property
    def binary_sensors(self) -> List[GeckoBinarySensor]:
        """Get the binary sensor list"""
        return self._binary_sensors

    @property
    def eco_mode(self) -> Optional[GeckoSwitch]:
        """Get the Eco Mode switch if available"""
        return self._ecomode

    @property
    def facade_status_sensor(self) -> GeckoFacadeStatusSensor:
        """Get the facade status sensor"""
        return self._facade_status_sensor

    @property
    def facade_ping_sensor(self) -> Optional[GeckoFacadePingSensor]:
        """Get the facade ping sensor"""
        return self._facade_ping_sensor

    @property
    def all_user_devices(self) -> List[GeckoAutomationBase]:
        """Get all the user controllable devices as a list"""
        return self._pumps + self._blowers + self._lights  # type:ignore

    @property
    def all_automation_devices(self) -> List[GeckoAutomationBase]:
        """Get all the automation devices as a list"""
        return (
            self.all_user_devices
            + self.sensors  # type: ignore
            + self.binary_sensors  # type: ignore
            + [self.water_heater, self.water_care]  # type: ignore
            + [self.keypad, self.eco_mode]  # type: ignore
        )

    def get_device(self, key) -> Optional[GeckoAutomationBase]:
        """Get an automation device from the key, or None if not found"""
        for device in self.all_automation_devices:
            if device.key == key:
                return device
        return None

    @property
    def devices(self) -> List[str]:
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
