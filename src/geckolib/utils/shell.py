"""GeckoShell class."""

# ruff: noqa: T201

import datetime
import logging
import sys
import traceback
from time import sleep
from typing import Any, Self

from geckolib import VERSION, GeckoConstants, GeckoPump
from geckolib.async_spa_manager import GeckoAsyncSpaMan
from geckolib.automation.base import GeckoAutomationBase, GeckoAutomationFacadeBase
from geckolib.config import release_config_change_waiters
from geckolib.driver.accessor import GeckoStructAccessor
from geckolib.spa_events import GeckoSpaEvent

from .shared_command import GeckoCmd

_LOGGER = logging.getLogger(__name__)


SHELL_UUID = "02ac6d28-42d0-41e3-ad22-274d0aa491da"


class GeckoShell(GeckoCmd, GeckoAsyncSpaMan):
    """Client shell to explore spa capabilities."""

    BANNER = """

        <Disclaimer>
        ----------------------------- USE AT YOUR OWN RISK -----------------------------

        This code will allow you to make changes to your spa configuration that is
        outside of what the app, top panel and side panel settings allow. I've not
        tested every setting and it might be that you prevent your spa pack from
        operating as it used to do.

        I strongly suggest dumping the configuration values with the "config" command
        and recording them somewhere safe.

        </Disclaimer>

    """

    def __init__(self) -> None:
        """Initialize the GeckoShell class."""
        self.spas = None
        GeckoAsyncSpaMan.__init__(self, SHELL_UUID)
        GeckoCmd.__init__(self, self)

        # Fill the watercare mode strings in.
        assert self.do_watercare.__doc__ is not None  # noqa: S101
        self.do_watercare.__func__.__doc__ = self.do_watercare.__doc__.format(
            GeckoConstants.WATERCARE_MODE_STRING
        )

        self.intro = "Welcome to the Gecko shell. Type help or ? to list commands.\n"
        self.prompt = "(Gecko) "

    async def __aenter__(self) -> Self:
        """Support 'with'."""
        _LOGGER.info("Async enter called on %s", self.__class__.__name__)
        await GeckoAsyncSpaMan.__aenter__(self)
        return self

    def _on_accessor_changed(
        self, accessor: GeckoStructAccessor, old_value: Any, new_value: Any
    ) -> None:
        print(f"accessor {accessor} changed from {old_value} to {new_value}")

    async def handle_event(self, event: GeckoSpaEvent, **_kwargs: object) -> None:  # noqa: PLR0912
        """Handle the event."""
        _LOGGER.debug("Handle event %s", event)
        if event == GeckoSpaEvent.CLIENT_FACADE_IS_READY:
            if self._spa is not None:
                self.structure = self._spa.struct
                for accessor in self.structure.accessors.values():
                    accessor.watch(self._on_accessor_changed)

        elif event == GeckoSpaEvent.CLIENT_FACADE_TEARDOWN:
            self.structure = None

        elif event == GeckoSpaEvent.LOCATING_STARTED:
            print("Starting discovery process...", end="", flush=True)

        elif event == GeckoSpaEvent.LOCATING_FINISHED:
            self.spas = self._spa_descriptors
            number_of_spas = len(self.spas)
            print(f"Found {number_of_spas} spas", flush=True)
            if number_of_spas == 0:
                _LOGGER.warning(
                    "Try using the iOS or Android app to confirm they are "
                    "functioning correctly"
                )
                sys.exit(1)
            if number_of_spas == 1:
                self.do_manage("1")
            else:
                print(self.prompt, end="", flush=True)

        elif event == GeckoSpaEvent.CONNECTION_FINISHED:
            assert self.facade is not None  # noqa: S101
            print(f"connected to {self.facade.name}!", flush=True)
            self.prompt = f"{self.facade.name}$ "

            # Build list of spa commands
            for device in self.facade.all_user_devices:
                if isinstance(device, GeckoPump):
                    func_name = f"do_{device.key}"

                    async def async_pump_command(
                        self: Self, arg: str, device: GeckoPump = device
                    ) -> None:
                        await self.pump_command(arg, device)

                    setattr(
                        GeckoShell,
                        func_name,
                        async_pump_command,
                    )
                    func_ptr = getattr(GeckoShell, func_name)
                    func_ptr.__doc__ = (
                        f"Set pump {device.name} mode: {device.key} <OFF|LO|HI>"
                    )
                else:
                    func_name = f"do_{device.key}"

                    async def async_device_command(
                        self: Self, arg: str, device: GeckoAutomationBase = device
                    ) -> None:
                        await self.device_command(arg, device)

                    setattr(
                        GeckoShell,
                        func_name,
                        async_device_command,
                    )
                    func_ptr = getattr(GeckoShell, func_name)
                    func_ptr.__doc__ = (
                        f"Turn device {device.name} ON or OFF: {device.key} <ON|OFF>"
                    )

            self.do_state("")
            print(self.prompt, end="", flush=True)

    def do_discover(self, arg: str) -> None:
        """
        Discover all the in.touch2 devices on your network.

        usage: discover [<ip address>].
        """
        if self.spas is not None:
            return
        self._spa_address = arg

    def do_list(self, _arg: str) -> None:
        """List the spas that are available to manage : list."""
        for idx, spa in enumerate(self.spas):
            print(f"{idx + 1}. {spa.name} ({spa.ipaddress})")

    def do_manage(self, arg: str) -> None:
        """Manage a named or numbered spa : manage 1."""
        spa_to_manage = int(arg)
        spa_descriptor = self.spas[spa_to_manage - 1]
        print(
            (
                f"Connecting to spa `{spa_descriptor.name}`"
                f" at {spa_descriptor.ipaddress} ... "
            ),
            end="",
            flush=True,
        )
        _LOGGER.debug(spa_descriptor)
        self._spa_identifier = spa_descriptor.identifier_as_string
        self._state_change.set()

    async def device_command(self, arg: str, device: GeckoAutomationFacadeBase) -> None:
        """Turn a device on or off."""
        print(f"Turn device {device.name} {arg}")
        if arg.lower() == "on":
            await device.async_turn_on()
        else:
            await device.async_turn_off()

    async def pump_command(self, arg: str, device: GeckoPump) -> None:
        """Set a pump mode <mode>."""
        print(f"Set pump {device.name} {arg}")
        try:
            await device.async_set_mode(arg)
        except Exception:  # noqa: BLE001
            traceback.print_exc()

    async def do_key(self, arg: str) -> None:
        """
        Press keypad button.

        Usage: key <keynum>. If keynum missing, then defaults to 1.
        """
        keypad = GeckoConstants.KEYPAD_PUMP_1
        if arg:
            try:
                keypad = int(arg)
            except ValueError:
                print("Numbers only please")
                print(self.prompt, end="", flush=True)
                return
        await self.facade.spa.async_press(keypad)

    def do_state(self, _arg: str) -> None:
        """Show the state of the managed spa : state."""
        if self.facade is None:
            print("Must be connected to a spa")
            return
        print(self.facade.water_heater)
        for pump in self.facade.pumps:
            print(pump)
        for blower in self.facade.blowers:
            print(blower)
        for light in self.facade.lights:
            print(light)
        if self.facade.reminders_manager.is_available:
            for reminder in self.facade.reminders_manager.reminders:
                print(reminder)
        if self.facade.water_care.is_available:
            print(self.facade.water_care)
        for sensor in [
            *self.facade.sensors,
            *self.facade.binary_sensors,
        ]:
            print(sensor)
        if self.facade.eco_mode is not None:
            print(self.facade.eco_mode)
        print(self.facade.error_sensor)
        if self.facade.ingrid.is_available:
            print(self.facade.ingrid)
        if self.facade.heatpump.is_available:
            print(self.facade.heatpump)
        if self.facade.inmix.is_available:
            print(self.facade.inmix)

    def monitor_get_states(self) -> list[str]:
        """Get the monitor states as a string list."""
        states = [
            self.facade.water_heater,
            *self.facade.pumps,
            *self.facade.blowers,
            *self.facade.lights,
            # *self.facade.reminders,
            self.facade.water_care,
            *self.facade.sensors,
            *self.facade.binary_sensors,
            self.facade.eco_mode,
        ]
        return [f"{state.monitor}" for state in states]

    def monitor_compare_states(self, states: list[str]) -> bool:
        """Compare the current monitor states."""
        local_state = self.monitor_get_states()
        return local_state != states

    def monitor_print_states(self, states: list[str]) -> None:
        """Print the monitor states out."""
        print(f"{datetime.datetime.now(tz=datetime.UTC)} : {' '.join(states)}")

    def do_monitor(self, _arg: str) -> None:
        """
        Monitor the state of the managed spa.

        Output a new line for each change

        usage: monitor.
        """
        if self.facade is None:
            print("Must be connected to a spa")
            return

        print("Monitoring spa ... CTRL+C to stop")
        current_state = []
        while True:
            try:
                if self.monitor_compare_states(current_state):
                    current_state = self.monitor_get_states()
                    self.monitor_print_states(current_state)
                sleep(1)
            except KeyboardInterrupt:
                print()
                print("Monitor stopped")
                break

    @property
    def version_strings(self) -> list[str]:
        """Get the version strings for the spa."""
        return [
            f"geckolib version {VERSION}",
            f"SpaPackStruct.xml revision {self.facade.spa.revision}",
            f"intouch version EN {self.facade.spa.intouch_version_en}",
            f"intouch version CO {self.facade.spa.intouch_version_co}",
            f"Spa pack {self.facade.spa.pack} {self.facade.spa.version}",
            f"Low level configuration # {self.facade.spa.config_number}",
            f"Config version {self.facade.spa.config_version}",
            f"Log version {self.facade.spa.log_version}",
            f"Pack type {self.facade.spa.pack_type}",
        ]

    def do_version(self, _arg: str) -> None:
        """Show the version information : version."""
        for version_str in self.version_strings:
            print(version_str)

    def do_about(self, _arg: str) -> None:
        """Display information about this client program and support library : about."""
        print()
        print(
            "GeckoShell: A python program using GeckoLib library to drive Gecko enabled"
            " devices with in.touch2 communication modules"
        )
        print(f"Library version v{VERSION}")

    async def do_watercare(self, arg: str) -> None:
        """Set the active watercare mode to one of {0} : WATERCARE <mode>."""
        try:
            await self.facade.water_care.async_set_mode(arg)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception setting watercare to '%s'", arg)

    async def do_setpoint(self, arg: str) -> None:
        """Set the spa setpoint temperature : setpoint <temp>."""
        await self.facade.water_heater.async_set_target_temperature(float(arg))

    def do_eco(self, arg: str) -> None:
        """Set the spa eco mode : eco on|off."""
        assert self.facade is not None  # noqa: S101
        assert self.facade.eco_mode is not None  # noqa: S101
        if arg.lower() == "off":
            self.facade.eco_mode.turn_off()
        else:
            self.facade.eco_mode.turn_on()

    def get_snapshot_data(self) -> dict:
        """Proxy for the spa."""
        assert self._facade is not None  # noqa: S101
        return self._facade.spa.get_snapshot_data()

    def do_refresh(self, _args: str) -> None:
        """Refresh the spa pack data."""
        release_config_change_waiters()
