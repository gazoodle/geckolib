"""Async Facade to hide implementation details."""

from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Any

from geckolib.automation.base import GeckoAutomationBase
from geckolib.automation.bubblegen import GeckoBubbleGenerator
from geckolib.automation.heatpump import GeckoHeatPump
from geckolib.automation.ingrid import GeckoInGrid
from geckolib.automation.inmix import GeckoInMix
from geckolib.automation.lockmode import GeckoLockMode
from geckolib.automation.mrsteam import MrSteam
from geckolib.automation.waterfall import GeckoWaterfall
from geckolib.config import GeckoConfig, config_sleep, set_config_mode
from geckolib.const import GeckoConstants
from geckolib.driver import Observable

from .blower import GeckoBlower
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight, GeckoLightL120, GeckoLightLi
from .pump import GeckoPump
from .reminders import GeckoReminders
from .sensors import GeckoBinarySensor, GeckoErrorSensor, GeckoSensor, GeckoSensorBase
from .switch import GeckoStandby, GeckoSwitch
from .watercare import GeckoWaterCare

if TYPE_CHECKING:
    from geckolib.async_spa import GeckoAsyncSpa
    from geckolib.async_taskman import GeckoAsyncTaskMan
    from geckolib.automation.power import GeckoPower

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncFacade(Observable):
    """Async facade."""

    class SpaInUseSensor(GeckoAutomationBase):
        """Sensor with idle/active state."""

        def __init__(self, facade: GeckoAsyncFacade) -> None:
            """Initializd the in-use sensor."""
            super().__init__(facade.unique_id, "Spa In Use", facade.name, "INUSE")
            self._facade: GeckoAsyncFacade = facade
            self._in_use: bool = False

        @property
        def is_on(self) -> bool:
            """Determine if the sensor is on or not."""
            state = self.state
            if isinstance(state, bool):
                return state
            if state == "":
                return False
            return state != "OFF"

        @property
        def state(self) -> bool:
            """The state of the sensor."""
            return self._in_use

        @property
        def device_class(self) -> str | None:
            """The device class."""
            return None

        @property
        def unit_of_measurement(self) -> str | None:
            """The unit of measurement for the sensor, or None."""
            return None

        def set_in_use(self, *, in_use: bool) -> None:
            """Set the internal flag."""
            self._in_use = in_use
            self._on_change()

        def __repr__(self) -> str:
            """Get string representation of the class."""
            return f"{self.name}: {self.state}"

    def __init__(
        self, spa: GeckoAsyncSpa, taskman: GeckoAsyncTaskMan, **_kwargs: str
    ) -> None:
        """
        Initialize the facade.

        This is a thin automation-friendly client on the spa implementation.
        """
        Observable.__init__(self)

        self._spa: GeckoAsyncSpa = spa
        self._taskman: GeckoAsyncTaskMan = taskman

        spa.struct.build_connections()

        # Declare all the items that a spa might have. If they are
        # available for this configuration, they will be marked as such.
        self.pump_1: GeckoPump = GeckoPump(self, "Pump 1", "P1")
        self.pump_2: GeckoPump = GeckoPump(self, "Pump 2", "P2")
        self.pump_3: GeckoPump = GeckoPump(self, "Pump 3", "P3")
        self.pump_4: GeckoPump = GeckoPump(self, "Pump 4", "P4")
        self.pump_5: GeckoPump = GeckoPump(self, "Pump 5", "P5")

        self.blower: GeckoBlower = GeckoBlower(self)
        self.waterfall: GeckoWaterfall = GeckoWaterfall(self)
        self.bubblegenerator: GeckoBubbleGenerator = GeckoBubbleGenerator(self)

        self.light: GeckoLightLi = GeckoLightLi(self)
        self.light2: GeckoLightL120 = GeckoLightL120(self)

        self._heatpump: GeckoHeatPump = GeckoHeatPump(self)
        self._ingrid: GeckoInGrid = GeckoInGrid(self)
        self._lockmode: GeckoLockMode = GeckoLockMode(self)

        self._inmix: GeckoInMix = GeckoInMix(self)

        self._mrsteam: MrSteam = MrSteam(self)

        #################

        # Declare all the class members
        self._sensors: list[GeckoSensorBase] = []
        self._binary_sensors: list[GeckoBinarySensor] = []
        self._pumps: list[GeckoPump] = []
        self._blowers: list[GeckoBlower] = []
        self._lights: list[GeckoLight] = []
        self._ecomode: GeckoSwitch | None = None
        self._standby: GeckoStandby | None = None

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
        self._ready = asyncio.Event()

        self._spa_in_use_sensor = GeckoAsyncFacade.SpaInUseSensor(self)

    async def disconnect(self) -> None:
        """Disconnect the facade."""
        try:
            _LOGGER.debug("Disconnect facade")
            self._taskman.cancel_key_tasks("FACADE")
            for device in self.all_automation_devices:
                device.unwatch_all()
        except Exception:
            _LOGGER.exception("During facade disconnect")

    def _on_config_device_change(self, *_args: Any) -> None:
        in_use = False
        for device in self.all_config_change_devices:
            if device.is_on:
                in_use = True
        set_config_mode(active=in_use)
        self._spa_in_use_sensor.set_in_use(in_use=in_use)

    async def _facade_update(self) -> None:
        _LOGGER.debug("Facade update task started")
        try:
            do_check = True
            while True:
                # Only want to do the protocol work if timeout, otherwise we run
                # the risk of swamping the spa when we're making operational changes
                wait_time = GeckoConfig.FACADE_UPDATE_FREQUENCY_IN_SECONDS
                if not self._spa.is_responding_to_pings:
                    wait_time = GeckoConfig.PING_FREQUENCY_IN_SECONDS
                elif do_check:
                    if self._water_care.is_available:
                        _LOGGER.debug("Facade update: Get watercare mode")
                        self._water_care.change_watercare_mode(
                            await self._spa.async_get_watercare_mode()
                        )
                    if self._reminders_manager.is_available:
                        _LOGGER.debug("Facade update: Get reminders")
                        self._reminders_manager.change_reminders(
                            await self._spa.async_get_reminders()
                        )
                    self._on_config_device_change()

                    # After we've been round here at least once, we're ready
                    self._ready.set()

                do_check = await config_sleep(wait_time, "Async facade update loop")
                _LOGGER.debug("Facade update, wait over. do_check=%s", f"{do_check}")

        except asyncio.CancelledError:
            _LOGGER.debug("Facade update loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("Facade update loop caught execption")
            raise

    async def wait_for_one_update(self) -> None:
        """Wait until the first update has occurred."""
        await self._ready.wait()

    def _scan_outputs(self) -> None:
        """Scan the spa outputs to decide what user options are available."""
        if self._spa is None:
            return

        self._pumps: list[GeckoPump] = [
            pump
            for pump in [
                self.pump_1,
                self.pump_2,
                self.pump_3,
                self.pump_4,
                self.pump_5,
                self.waterfall,
                self.bubblegenerator,
            ]
            if pump.is_available
        ]

        self._blowers = [blower for blower in [self.blower] if blower.is_available]

        self._lights = [
            light for light in [self.light, self.light2] if light.is_available
        ]

        #######

        self._sensors = [
            GeckoSensor(self, sensor[0], self._spa.accessors[sensor[1]])
            for sensor in GeckoConstants.SENSORS
            if sensor[1] in self._spa.accessors
        ]

        if self.pump_1.is_available:
            self._sensors.append(
                GeckoSensor(self, "Pump 1 State", self.spa.accessors["P1"])
            )
        if self.pump_2.is_available:
            self._sensors.append(
                GeckoSensor(self, "Pump 2 State", self.spa.accessors["P2"])
            )
        if self.pump_3.is_available:
            self._sensors.append(
                GeckoSensor(self, "Pump 3 State", self.spa.accessors["P3"])
            )
        if self.pump_4.is_available:
            self._sensors.append(
                GeckoSensor(self, "Pump 4 State", self.spa.accessors["P4"])
            )
        if self.pump_5.is_available:
            self._sensors.append(
                GeckoSensor(self, "Pump 5 State", self.spa.accessors["P5"])
            )
        if self.blower.is_available:
            self._sensors.append(
                GeckoSensor(self, "Blower State", self.spa.accessors["BL"])
            )
        if self.waterfall.is_available:
            self._sensors.append(
                GeckoSensor(self, "Waterfall State", self.spa.accessors["Waterfall"])
            )

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
                    GeckoConstants.KEY_ECON_ACTIVE,
                    GeckoConstants.DEVICE_CLASS_SWITCH,
                ),
            )

        if GeckoConstants.KEY_STANDBY in self._spa.accessors:
            self._standby = GeckoStandby(self)

    @property
    def unique_id(self) -> str:
        """A unique id for the facade."""
        return self._taskman.unique_id

    @property
    def name(self) -> str:
        """Get the spa name."""
        return self._taskman.spa_name

    @property
    def spa(self) -> GeckoAsyncSpa:
        """Get the spa implementation instance."""
        return self._spa

    @property
    def mrsteam(self) -> MrSteam:
        """Get the Mr.Steam object."""
        return self._mrsteam

    @property
    def reminders_manager(self) -> GeckoReminders:
        """Get the reminders handler."""
        return self._reminders_manager

    @property
    def water_heater(self) -> GeckoWaterHeater:
        """Get the water heater handler."""
        return self._water_heater

    @property
    def water_care(self) -> GeckoWaterCare:
        """Get the water care handler."""
        return self._water_care

    @property
    def keypad(self) -> GeckoKeypad:
        """Get the keypad handler."""
        return self._keypad

    @property
    def pumps(self) -> list[GeckoPump]:
        """Get the pumps list."""
        return self._pumps

    @property
    def blowers(self) -> list[GeckoBlower]:
        """Get the blowers list."""
        return self._blowers

    @property
    def lights(self) -> list[GeckoLight]:
        """Get the lights list."""
        return self._lights

    @property
    def switches(self) -> list[GeckoSwitch]:
        """Get the switches."""
        if self.mrsteam.is_available:
            return self.mrsteam.switches
        switches = []
        if self.eco_mode is not None:
            switches.append(self.eco_mode)
        if self.standby is not None:
            switches.append(self.standby)
        return switches

    @property
    def sensors(self) -> list[GeckoSensorBase]:
        """Get the sensor list."""
        return self._sensors

    @property
    def binary_sensors(self) -> list[GeckoBinarySensor]:
        """Get the binary sensor list."""
        return self._binary_sensors

    @property
    def error_sensor(self) -> GeckoErrorSensor:
        """Get the error sensor."""
        return self._error_sensor

    @property
    def eco_mode(self) -> GeckoSwitch | None:
        """Get the Eco Mode switch if available."""
        return self._ecomode

    @property
    def heatpump(self) -> GeckoHeatPump:
        """Get the heat pump if available."""
        return self._heatpump

    @property
    def ingrid(self) -> GeckoInGrid:
        """Get the inGrid handler if available."""
        return self._ingrid

    @property
    def lockmode(self) -> GeckoLockMode:
        """Get the lockmode handler."""
        return self._lockmode

    @property
    def standby(self) -> GeckoStandby | None:
        """Get the standby switch if available."""
        return self._standby

    @property
    def inmix(self) -> GeckoInMix:
        """Get the inMix handler."""
        return self._inmix

    @property
    def spa_in_use_sensor(self) -> GeckoAsyncFacade.SpaInUseSensor:
        """Get the spa in use sensor."""
        return self._spa_in_use_sensor

    @property
    def all_user_devices(self) -> list[GeckoAutomationBase]:
        """Get all the user controllable devices as a list."""
        return list(self._pumps + self._blowers + self._lights)

    @property
    def all_config_change_devices(self) -> list[GeckoPower]:
        """Get all devices that can cause config change."""
        return list(self._pumps + self._blowers + self._lights)

    @property
    def all_automation_devices(self) -> list[GeckoAutomationBase]:
        """Get all the automation devices as a list."""
        extras = []
        extras.extend(self.all_user_devices)
        extras.extend(self.sensors)
        extras.extend(self.binary_sensors)
        extras.append(self.water_heater)
        extras.append(self.water_care)
        extras.append(self.reminders_manager)
        extras.append(self.keypad)
        if self.eco_mode is not None:
            extras.append(self.eco_mode)
        if self.heatpump is not None:
            extras.append(self.heatpump)
        if self.ingrid is not None:
            extras.append(self.ingrid)
        return extras

    def get_device(self, key: str) -> GeckoAutomationBase | None:
        """Get an automation device from the key, or None if not found."""
        for device in self.all_automation_devices:
            if device.key == key:
                return device
        return None

    @property
    def devices(self) -> list[str]:
        """
        Get a list of automation device keys.

        Keys can be passed to get_device to find the specific device.
        """
        return [device.key for device in self.all_automation_devices]

    @property
    def taskmanager(self) -> GeckoAsyncTaskMan:
        """The facade's task manager."""
        return self._taskman
