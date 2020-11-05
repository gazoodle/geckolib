""" GeckoShell class """

import cmd
import sys
import logging

from .. import GeckoManager, GeckoConstants, GeckoFacade

logger = logging.getLogger(__name__)

LICENSE = """
#
#   Copyright (C) 2020, Gazoodle (https://github.com/gazoodle)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""

DISCLAIMER = """

    <Disclaimer>
    --------------------------------- USE AT YOUR OWN RISK ---------------------------------

    This code will allow you to make changes to your spa configuration that is outside
    of what the app, top panel and side panel settings allow. I've not tested every setting
    and it might be that you prevent your spa pack from operating as it used to do.

    Configuration is declared in the file SpaPackStruct.xml which is downloaded the first
    time you run this program. Settings marked as RW="ALL" seem to indicate that any process
    can write them, so you ought to be able to revert the settings to their original ones.

    I strongly suggest dumping the configuration values with the "config" command and recording
    them somewhere safe.

    </Disclaimer>

"""


class GeckoShell(cmd.Cmd):
    """ GeckoShell is a client application to drive the geckolib automation interface """

    def run():  # pylint: disable=no-method-argument
        """ Convenience function to run a shell command loop """
        print(DISCLAIMER)
        shell = GeckoShell()
        try:
            shell.cmdloop()
        finally:
            del shell

    def __init__(self):
        super().__init__()

        self.manager = GeckoManager("02ac6d28-42d0-41e3-ad22-274d0aa491da")
        self.spa = None
        self.facade = None

        self.do_watercare.__func__.__doc__ = self.do_watercare.__doc__.format(
            GeckoConstants.WATERCARE_MODE_STRING
        )

        self.intro = "Welcome to the Gecko shell. Type help or ? to list commands.\n"
        self.prompt = "(Gecko) "
        self.onecmd("discover")

    def __del__(self):
        self.manager.finish()

    def do_exit(self, arg):
        """Exit this shell: EXIT"""
        del arg
        print("Thank you for using the Gecko shell")
        return True

    def do_discover(self, arg):
        """Discover all the in.touch2 devices on your network : DISCOVER"""
        del arg
        print(
            "Starting discovery process...",
            end="",
            flush=True,
        )
        self.manager.discover()
        number_of_spas = len(self.manager.spas)
        print("Found {0} spas".format(number_of_spas))
        if number_of_spas == 0:
            logger.warning(
                "Try using the iOS or Android app to confirm they are functioning correctly"
            )
            sys.exit(1)
        if number_of_spas == 1:
            self.onecmd("manage 1")

    def do_list(self, arg):
        """List the spas that are available to manage : LIST """
        del arg
        for idx, spa in enumerate(self.manager.spas):
            print("{0}. {1}".format(idx + 1, spa.name))

    def do_manage(self, arg):
        """Manage a named or numbered spa : MANAGE 1"""
        spa_to_manage = int(arg)
        self.spa = self.manager.spas[spa_to_manage - 1]
        print(
            "Connecting to spa `{0}` at {1} ... ".format(
                self.spa.name, self.spa.ipaddress
            ),
            end="",
            flush=True,
        )
        self.spa.connect()
        self.facade = GeckoFacade(self.spa)
        print("connected!")
        self.prompt = "{0}$ ".format(self.spa.name)

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
        """Show the state of the managed spa"""
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

    def get_version_strings(self):  # pylint: disable=redefined-outer-name
        """ Get the version strings for the spa """
        return [
            "SpaPackStruct.xml revision {0}".format(
                self.manager.spa_pack_struct_revision
            ),
            "intouch version EN {0}".format(self.spa.intouch_version_en),
            "intouch version CO {0}".format(self.spa.intouch_version_co),
            "Spa pack {0} {1}".format(self.spa.pack, self.spa.version),
            "Low level configuration # {0}".format(self.spa.config_number),
            "Config version {0}".format(self.spa.config_version),
            "Log version {0}".format(self.spa.log_version),
            "Pack type {0}".format(self.spa.pack_type),
        ]

    def do_version(self, arg):
        """Show the version information"""
        del arg
        for version_str in self.get_version_strings():
            print(version_str)

    def do_config(self, arg):
        """Display the configuration data from the spa"""
        del arg
        print("Configuration Settings")
        print("======================")
        print("")
        for element in self.spa.config_xml.findall("./*"):
            if "Pos" in element.attrib:
                continue
            print(element.tag)
            print("-" * len(element.tag))
            for child in element.findall("./*"):
                print(
                    "  {0}: {1}".format(child.tag, self.spa.accessors[child.tag].value)
                )
            print("")

    def do_live(self, arg):
        """Display the live settings from the spa"""
        del arg
        print("Live Settings")
        print("=============")
        print("")
        for element in self.spa.log_xml.findall("./*"):
            print(element.tag)
            print("-" * len(element.tag))
            for child in element.findall("./*"):
                print(
                    "  {0}: {1}".format(child.tag, self.spa.accessors[child.tag].value)
                )
            print("")

    def do_about(self, arg):
        """Display information about this client program and support library"""
        del arg
        print("")
        print(
            "client.py: A python program using GeckoLib library to drive Gecko enabled"
            " devices with in.touch2 communication modules"
        )
        print("Library version {0}".format(self.manager.version))

    def do_license(self, arg):
        """Display the license details"""
        del arg
        print(LICENSE)

    def do_download(self, arg):
        """Download the SpaPackStruct.xml from Gecko"""
        del arg
        self.manager.download()

    def do_refresh(self, arg):
        """Refresh the live data from your spa"""
        del arg
        self.spa.refresh()

    def do_get(self, arg):
        """Get the value of the specified spa pack structure element"""
        try:
            print("{0} = {1}".format(arg, self.spa.accessors[arg].value))
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception getting '%s'", arg)

    def do_set(self, arg):
        """Set the value of the specified spa pack structure element"""
        try:
            key, val = arg.split("=")
            self.spa.accessors[key].value = val
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception handling setting %s=%s", key, val)

    def do_watercare(self, arg):
        """Set the active watercare mode to one of {0} : WATERCARE <mode>"""
        try:
            self.facade.water_care.set_mode(arg)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception setting watercare to '%s'", arg)

    def do_setpoint(self, arg):
        """Set the spa setpoint temperature"""
        self.facade.water_heater.set_target_temperature(float(arg))

    def do_snapshot(self, arg):
        """Take a snapshot of the spa data structure with a descriptive message: SNAPSHOT <desc>"""
        logger.info("Snapshot (%s)", arg)
        for ver_str in self.get_version_strings():
            logger.info(ver_str)
        logger.info([hex(b) for b in self.spa.status_block])
