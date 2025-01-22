"""GeckoShell class."""

import datetime
import logging
import sys
import traceback

from geckolib import VERSION, GeckoConstants, GeckoPump
from geckolib.async_locator import GeckoAsyncLocator
from geckolib.async_spa import GeckoAsyncSpa
from geckolib.automation.async_facade import GeckoAsyncFacade
from geckolib.config import config_sleep
from geckolib.spa_events import GeckoSpaEvent

from .shared_command import GeckoCmd

_LOGGER = logging.getLogger(__name__)


SHELL_UUID = "02ac6d28-42d0-41e3-ad22-274d0aa491da"


class GeckoShell(GeckoCmd):
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
        self.facade = None

        super().__init__()

        self.do_watercare.__func__.__doc__ = self.do_watercare.__doc__.format(
            GeckoConstants.WATERCARE_MODE_STRING
        )

        self.intro = "Welcome to the Gecko shell. Type help or ? to list commands.\n"
        self.prompt = "(Gecko) "
        self.push_command("discover")

    async def __aexit__(self, *args: object) -> None:
        """Suport pythion 'with'."""
        if self.facade:
            await self.facade.disconnect()
            self.facade = None
        await super().__aexit__(args)

    async def _handle_event(self, event: GeckoSpaEvent, **kwargs) -> None:
        pass

    async def do_discover(self, arg) -> None:
        """Discover all the in.touch2 devices on your network : discover [<ip address>]."""
        if self.spas is not None:
            return

        print(
            "Starting discovery process...",
            end="",
            flush=True,
        )

        locator = GeckoAsyncLocator(
            self,
            self._handle_event,
            spa_address=arg,
        )
        await locator.discover()
        self.spas = locator.spas

        number_of_spas = len(self.spas)
        print("Found {0} spas".format(number_of_spas))
        if number_of_spas == 0:
            _LOGGER.warning(
                "Try using the iOS or Android app to confirm they are "
                "functioning correctly"
            )
            sys.exit(1)
        if number_of_spas == 1:
            self.push_command("manage 1")

    def do_list(self, _arg) -> None:
        """List the spas that are available to manage : list."""
        for idx, spa in enumerate(self.spas):
            print("{0}. {1}".format(idx + 1, spa.name))

    async def do_manage(self, arg) -> None:
        """Manage a named or numbered spa : manage 1."""
        spa_to_manage = int(arg)
        spa_descriptor = self.spas[spa_to_manage - 1]
        print(
            "Connecting to spa `{0}` at {1} ... ".format(
                spa_descriptor.name, spa_descriptor.ipaddress
            ),
            end="",
            flush=True,
        )

        spa = GeckoAsyncSpa(
            GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(SHELL_UUID).encode(
                GeckoConstants.MESSAGE_ENCODING
            ),
            spa_descriptor,
            self,
            self._handle_event,
        )
        await spa.connect()

        self.facade = GeckoAsyncFacade(spa, self)
        await self.facade.wait_for_one_update()
        print("connected!")
        self.prompt = "{0}$ ".format(self.facade.name)

        # Build list of spa commands
        for device in self.facade.all_user_devices:
            if isinstance(device, GeckoPump):
                func_name = "do_{0}".format(device.ui_key)
                setattr(
                    GeckoShell,
                    func_name,
                    lambda self, arg, device=device: self.pump_command(arg, device),
                )
                func_ptr = getattr(GeckoShell, func_name)
                func_ptr.__doc__ = "Set pump {0} mode: {1} <OFF|LO|HI>".format(
                    device.name, device.ui_key
                )
            else:
                func_name = "do_{0}".format(device.ui_key)
                setattr(
                    GeckoShell,
                    func_name,
                    lambda self, arg, device=device: self.device_command(arg, device),
                )
                func_ptr = getattr(GeckoShell, func_name)
                func_ptr.__doc__ = "Turn device {0} ON or OFF: {1} <ON|OFF>".format(
                    device.name, device.ui_key
                )

        self.push_command("state")

    def device_command(self, arg, device):
        """Turn a device on or off."""
        print("Turn device {0} {1}".format(device.name, arg))
        if arg.lower() == "on":
            device.turn_on()
        else:
            device.turn_off()

    def pump_command(self, arg, device):
        """Set a pump mode <mode>"""
        print("Set pump {0} {1}".format(device.name, arg))
        try:
            device.set_mode(arg)
        except Exception:
            traceback.print_exc()

    async def do_key(self, arg):
        """Press keyboard button 1."""
        await self.facade.spa.async_press(GeckoConstants.KEYPAD_PUMP_1)

    def do_state(self, _arg):
        """Show the state of the managed spa : state"""
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
        for reminder in self.facade.reminders_manager.reminders:
            print(reminder)
        print(self.facade.water_care)
        for sensor in [
            *self.facade.sensors,
            *self.facade.binary_sensors,
        ]:
            print(sensor)
        print(self.facade.eco_mode)
        print(self.facade.error_sensor)

    def monitor_get_states(self):
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

    def monitor_compare_states(self, states):
        local_state = self.monitor_get_states()
        return local_state != states

    def monitor_print_states(self, states):
        print(f"{datetime.datetime.now()} : {' '.join(states)}")

    async def do_monitor(self, _arg):
        """Monitor the state of the managed spa outputting a new line for each change : monitor"""
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
                await config_sleep(1)
            except KeyboardInterrupt:
                print("")
                print("Monitor stopped")
                break

    @property
    def version_strings(self):
        """Get the version strings for the spa"""
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

    def do_version(self, _arg):
        """Show the version information : version"""
        for version_str in self.version_strings:
            print(version_str)

    def do_accessors(self, _arg):
        """Display the data from the accessors : accessors"""
        print("Accessors")
        print("=========")
        print("")
        for key in self.facade.spa.accessors:
            print("   {0}: {1}".format(key, self.facade.spa.accessors[key].value))
        print("")

    def do_about(self, _arg):
        """Display information about this client program and support library : about"""
        print("")
        print(
            "GeckoShell: A python program using GeckoLib library to drive Gecko enabled"
            " devices with in.touch2 communication modules"
        )
        print("Library version v{0}".format(VERSION))

    def do_get(self, arg):
        """Get the value of the specified spa pack structure element : get <Element>"""
        try:
            print("{0} = {1}".format(arg, self.facade.spa.accessors[arg].value))
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception getting '%s'", arg)

    def do_peek(self, arg):
        """Get the byte value from the structure at the specified position : peek <pos>"""
        try:
            pos = int(arg)
            print(f"Byte at {pos} = {self.facade.spa.struct.status_block[pos]}")
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception peeking at '%s'", arg)

    def do_set(self, arg):
        """Set the value of the specified spa pack structure
        element : set <Element>=<value>"""
        try:
            key, val = arg.split("=")
            self.facade.spa.accessors[key].value = val
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception handling 'set %s'", arg)

    def do_watercare(self, arg):
        """Set the active watercare mode to one of {0} : WATERCARE <mode>"""
        try:
            self.facade.water_care.set_mode(arg)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception setting watercare to '%s'", arg)

    def do_setpoint(self, arg):
        """Set the spa setpoint temperature : setpoint <temp>"""
        self.facade.water_heater.set_target_temperature(float(arg))

    def do_eco(self, arg):
        """Set the spa eco mode : eco on|off"""
        if arg.lower() == "off":
            self.facade.eco_mode.turn_off()
        else:
            self.facade.eco_mode.turn_on()

    def do_snapshot(self, arg):
        """Take a snapshot of the spa data structure with a descriptive
        message : SNAPSHOT <desc>"""
        _LOGGER.info("Snapshot (%s)", arg)
        for ver_str in self.version_strings:
            _LOGGER.info(ver_str)
        _LOGGER.info([hex(b) for b in self.facade.spa.struct.status_block])
