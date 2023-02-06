""" Async Facade to hide implementation details """

from __future__ import annotations

import logging
import asyncio

from geckolib.automation.base import GeckoAutomationBase

from .blower import GeckoBlower
from ..const import GeckoConstants
from ..config import GeckoConfig, config_sleep, set_config_mode
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight
from .pump import GeckoPump
from .reminders import GeckoReminders
from .switch import GeckoSwitch
from .sensors import (
    GeckoSensor,
    GeckoBinarySensor,
    GeckoSensorBase,
    GeckoErrorSensor
)
from .watercare import GeckoWaterCare
from ..driver import Observable
from ..async_spa import GeckoAsyncSpa
from ..async_tasks import AsyncTasks

from typing import Optional, List

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncFacade(Observable):
    """Async facade"""

    def __init__(self, spa: GeckoAsyncSpa, taskman: AsyncTasks, **kwargs: str) -> None:
        """The facade is a thin automation-friendly client on the spa implementation."""
        Observable.__init__(self)

        self._spa: GeckoAsyncSpa = spa
        self._taskman: AsyncTasks = taskman

        # Declare all the class members
        self._sensors: List[GeckoSensorBase] = []
        self._binary_sensors: List[GeckoBinarySensor] = []
        self._pumps: List[GeckoPump] = []
        self._blowers: List[GeckoBlower] = []
        self._lights: List[GeckoLight] = []
        self._ecomode: Optional[GeckoSwitch] = None

        # Build the automation items
        self._reminders_manager = GeckoReminders(self)
        self._water_heater = GeckoWaterHeater(self)
        self._water_care = GeckoWaterCare(self)
        self._keypad = GeckoKeypad(self)
        self._scan_outputs()
        # Install change notifications
        for device in self.all_automation_devices:
            device.watch(self._on_change)
        # And notifications for active/idle items
        for device in self.all_config_change_devices:
            device.watch(self._on_config_device_change)

        self._taskman.add_task(self._facade_update(), "Facade update", "FACADE")
        self._ready = False

    async def disconnect(self) -> None:
        _LOGGER.debug("Disconnect facade")
        self._taskman.cancel_key_tasks("FACADE")
        for device in self.all_automation_devices:
            device.unwatch_all()

    def _on_config_device_change(self, *args) -> None:
        active_mode = False
        for device in self.all_config_change_devices:
            if device.is_on:  # type: ignore
                active_mode = True
        set_config_mode(active_mode)

    async def _facade_update(self) -> None:
        _LOGGER.debug("Facade update task started")
        try:
            while True:

                try:
                    if not self._spa.is_responding_to_pings:
                        continue

                    self._water_care.change_watercare_mode(
                        await self._spa.async_get_watercare()
                    )
                    self._reminders_manager.change_reminders(
                        await self._spa.async_get_reminders()
                    )
                    self._on_config_device_change()

                    # After we've been round here at least once, we're ready
                    self._ready = True

                finally:
                    wait_time = (
                        GeckoConfig.FACADE_UPDATE_FREQUENCY_IN_SECONDS
                        if self._spa.is_responding_to_pings
                        else GeckoConfig.PING_FREQUENCY_IN_SECONDS
                    )
                    await config_sleep(wait_time)

        except asyncio.CancelledError:
            _LOGGER.debug("Facade update loop cancelled")
            raise

    async def wait_for_one_update(self):
        while not self._ready:
            await asyncio.sleep(GeckoConstants.ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD)

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
        actual_devices = list(
            dict.fromkeys(
                [
                    device
                    for device in self._spa.struct.all_devices
                    for val in actual_connections.values()
                    if val.startswith(device)
                ]
            )
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

        self._error_sensor = GeckoErrorSensor(self)

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
    def unique_id(self) -> str:
        """A unique id for the facade"""
        return self._taskman.unique_id

    @property
    def name(self) -> str:
        """Get the spa name."""
        return self._taskman.spa_name

    @property
    def spa(self) -> GeckoAsyncSpa:
        """Get the spa implementation instance"""
        return self._spa

    @property
    def reminders_manager(self) -> GeckoReminders:
        """Get the reminders handler"""
        return self._reminders_manager

    @property
    def water_heater(self) -> GeckoWaterHeater:
        """Get the water heater handler"""
        return self._water_heater

    @property
    def water_care(self) -> GeckoWaterCare:
        """Get the water care handler"""
        return self._water_care

    @property
    def keypad(self) -> GeckoKeypad:
        """Get the keypad handler"""
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
        return self._sensors

    @property
    def binary_sensors(self) -> List[GeckoBinarySensor]:
        """Get the binary sensor list"""
        return self._binary_sensors

    @property
    def error_sensor(self) -> GeckoErrorSensor:
        """Get the error sensor"""
        return self._error_sensor

    @property
    def eco_mode(self) -> Optional[GeckoSwitch]:
        """Get the Eco Mode switch if available"""
        return self._ecomode

    @property
    def all_user_devices(self) -> List[GeckoAutomationBase]:
        """Get all the user controllable devices as a list"""
        return self._pumps + self._blowers + self._lights  # type: ignore

    @property
    def all_config_change_devices(self) -> List[GeckoAutomationBase]:
        """Get all devices that can cause config change"""
        return self._pumps + self._blowers  # type: ignore

    @property
    def all_automation_devices(self) -> List[GeckoAutomationBase]:
        """Get all the automation devices as a list"""
        return (
            self.all_user_devices
            + self.sensors  # type: ignore
            + self.binary_sensors  # type: ignore
            + [self.water_heater, self.water_care, self.reminders_manager]  # type: ignore
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
