""" GeckoShell class """

import sys
import logging
from .shared_command import GeckoCmd
from .. import GeckoConstants, GeckoLocator, VERSION

logger = logging.getLogger(__name__)


SHELL_UUID = "02ac6d28-42d0-41e3-ad22-274d0aa491da"


class GeckoShell(GeckoCmd):
    """GeckoShell is a client application to drive the geckolib automation
    interface"""

    BANNER = """

        <Disclaimer>
        ----------------------------- USE AT YOUR OWN RISK -----------------------------

        This code will allow you to make changes to your spa configuration that is
        outside of what the app, top panel and side panel settings allow. I've not
        tested every setting and it might be that you prevent your spa pack from
        operating as it used to do.

        Configuration is declared in the file SpaPackStruct.xml which is downloaded the
        first time you run this program. Settings marked as RW="ALL" seem to indicate
        that any process can write them, so you ought to be able to revert the settings
        to their original ones.

        I strongly suggest dumping the configuration values with the "config" command
        and recording them somewhere safe.

        </Disclaimer>

    """

    def __init__(self, first_commands=None):
        self.spas = None
        self.facade = None

        super().__init__(first_commands)

        self.do_watercare.__func__.__doc__ = self.do_watercare.__doc__.format(
            GeckoConstants.WATERCARE_MODE_STRING
        )

        self.intro = "Welcome to the Gecko shell. Type help or ? to list commands.\n"
        self.prompt = "(Gecko) "
        self.onecmd("discover")

    def __exit__(self, *args):
        super().__exit__(args)
        if self.facade:
            self.facade.complete()

    def do_discover(self, arg):
        """Discover all the in.touch2 devices on your network : discover [<ip address>]"""
        if self.spas is not None:
            return

        print(
            "Starting discovery process...",
            end="",
            flush=True,
        )

        with GeckoLocator(SHELL_UUID, static_ip=arg) as locator:
            self.spas = locator.spas

        number_of_spas = len(self.spas)
        print("Found {0} spas".format(number_of_spas))
        if number_of_spas == 0:
            logger.warning(
                "Try using the iOS or Android app to confirm they are "
                "functioning correctly"
            )
            sys.exit(1)
        if number_of_spas == 1:
            self.onecmd("manage 1")

    def do_list(self, arg):
        """List the spas that are available to manage : list"""
        del arg
        for idx, spa in enumerate(self.spas):
            print("{0}. {1}".format(idx + 1, spa.name))

    def do_manage(self, arg):
        """Manage a named or numbered spa : manage 1"""
        spa_to_manage = int(arg)
        spa = self.spas[spa_to_manage - 1]
        print(
            "Connecting to spa `{0}` at {1} ... ".format(spa.name, spa.ipaddress),
            end="",
            flush=True,
        )
        self.facade = spa.get_facade()
        print("connected!")
        self.prompt = "{0}$ ".format(self.facade.name)

        # Build list of spa commands
        for device in self.facade.all_user_devices:
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

        self.onecmd("state")

    def device_command(self, arg, device):
        """Turn a device on or off"""
        print("Turn device {0} {1}".format(device.name, arg))
        if arg.lower() == "on":
            device.turn_on()
        else:
            device.turn_off()

    def do_state(self, arg):
        """Show the state of the managed spa : state"""
        del arg
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
        for reminder in self.facade.reminders:
            print(reminder)
        print(self.facade.water_care)
        for sensor in [*self.facade.sensors, *self.facade.binary_sensors]:
            print(sensor)

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

    def do_version(self, arg):
        """Show the version information : version"""
        del arg
        for version_str in self.version_strings:
            print(version_str)

    def do_config(self, arg):
        """Display the configuration data from the spa : config"""
        del arg
        print("Configuration Settings")
        print("======================")
        print("")
        for element in self.facade.spa.config_xml.findall("./*"):
            if "Pos" in element.attrib:
                continue
            print(element.tag)
            print("-" * len(element.tag))
            for child in element.findall("./*"):
                print(
                    "  {0}: {1}".format(
                        child.tag, self.facade.spa.accessors[child.tag].value
                    )
                )
            print("")

    def do_live(self, arg):
        """Display the live settings from the spa : live"""
        del arg
        print("Live Settings")
        print("=============")
        print("")
        for element in self.facade.spa.log_xml.findall("./*"):
            print(element.tag)
            print("-" * len(element.tag))
            for child in element.findall("./*"):
                print(
                    "  {0}: {1}".format(
                        child.tag, self.facade.spa.accessors[child.tag].value
                    )
                )
            print("")

    def do_about(self, arg):
        """Display information about this client program and support library : about"""
        del arg
        print("")
        print(
            "GeckoShell: A python program using GeckoLib library to drive Gecko enabled"
            " devices with in.touch2 communication modules"
        )
        print("Library version v{0}".format(VERSION))

    def do_refresh(self, arg):
        """Refresh the live data from your spa : refresh"""
        del arg
        self.facade.spa.refresh()

    def do_get(self, arg):
        """Get the value of the specified spa pack structure element : get <Element>"""
        try:
            print("{0} = {1}".format(arg, self.facade.spa.accessors[arg].value))
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception getting '%s'", arg)

    def do_set(self, arg):
        """Set the value of the specified spa pack structure
        element : set <Element>=<value>"""
        try:
            key, val = arg.split("=")
            self.facade.spa.accessors[key].value = val
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception handling setting %s=%s", key, val)

    def do_watercare(self, arg):
        """Set the active watercare mode to one of {0} : WATERCARE <mode>"""
        try:
            self.facade.water_care.set_mode(arg)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception setting watercare to '%s'", arg)

    def do_setpoint(self, arg):
        """Set the spa setpoint temperature : setpoint <temp>"""
        self.facade.water_heater.set_target_temperature(float(arg))

    def do_snapshot(self, arg):
        """Take a snapshot of the spa data structure with a descriptive
        message : SNAPSHOT <desc>"""
        logger.info("Snapshot (%s)", arg)
        for ver_str in self.version_strings:
            logger.info(ver_str)
        logger.info([hex(b) for b in self.facade.spa.struct.status_block])
