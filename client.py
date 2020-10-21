#!/usr/bin/python3
LICENSE = '''
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
'''

#   HISTORY
#   =======
#
#   0.1.x       Oct 2020        -   Proof of concept code
#   0.2.x       Oct 2020        -   Initial development
#   0.3.x       Oct 2020        -   Created GitHub repo and readied for initial experimental release
#
#   Using Semantic versioning https://semver.org/


import logging
import sys
import traceback

from geckolib import gecko_constants, gecko_manager

# Set logging
stm_log = logging.StreamHandler()
stm_log.setLevel(logging.WARNING)
stm_log.setFormatter(logging.Formatter("%(message)s"))
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s", handlers=[
    logging.FileHandler("client.log"),
    stm_log])
logger = logging.getLogger(__name__)

manager = gecko_manager('02ac6d28-42d0-41e3-ad22-274d0aa491da')
version = "0.3.6"

print("""

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

    """)

try:
    print("Starting discovery ...")
    manager.discover()

    if len(manager.spas) == 0:
        logger.warn("Try using the iOS or Android app to confirm they are functioning correctly")
        exit(1)

    print("Found {0} spas".format(len(manager.spas)))
    spa_to_manage = 0

    if len(manager.spas) > 1:
        index = 1
        for spa in manager.spas:
            print("{0}. {1}".format(index, spa.name))
            index += 1
        spa_to_manage = int(input("Which spa do you want to manage ? "))-1

    spa = manager.spas[spa_to_manage]
    print('Connecting to spa `{0}` at {1} ... '.format(spa.name, spa.ipaddress),end='',flush=True)
    spa.connect()
    print("connected!")
    print(spa.get_simple_state())

    while True:
        inp = input("{0}$ ".format(spa.name))
        cmd = inp.lower()
        logger.info("Handle command %s" % inp)
        if cmd == "exit" or cmd == "quit":
            exit(0)

        elif cmd == "help":
            print("")
            print("+++++++++++++++++++ Help +++++++++++++++++++")
            print("")
            print("exit             - Exit this program")
            print("state            - Show the state of the spa")
            print("version          - Show version information")
            print("config           - Dump the spa configuration")
            print("live             - Dump the spa real-time status")
            #print("on <d>          - Turn device <d> on. Where <d> is one of {0}".format(spa.get_devices()))
            #print("off <d>         - Turn device <d> off. Where <d> is one of {0}".format(spa.get_devices()))
            print("get <key>        - Get the value of SpaPackStruct key <key>")
            print("set <key>=<val>  - Set the value of SpaPackStrung key <key> to <val>")
            print("press <btn>      - Press button <btn>. Where <btn> is one of {0}".format(spa.get_buttons()))
            print("setpoint <temp>  - Set the setpoint temperature to <temp>")
            print("refresh          - Force the live status block to refresh")
            print("download         - Download SpaPackStruct.xml even if it already exists")
            print("license          - Show the license details")
            print("about            - About this program")
            print("")

        elif cmd == "state":
            print(spa.get_simple_state())

        elif cmd == "version":
            print("SpaPackStruct.xml revision {0}".format(manager.spa_pack_struct_revision))
            print("intouch version EN {0}".format(spa.intouch_version_EN))
            print("intouch version CO {0}".format(spa.intouch_version_CO))
            print("Spa pack {0} {1}".format(spa.pack, spa.version))
            print("Low level configuration # {0}".format(spa.config_number))

        elif cmd == "config":
            print("Configuration Settings")
            print("======================")
            print("")
            for el in spa.config_xml.findall("./*"):
                if "Pos" in el.attrib:
                    continue
                print(el.tag)
                print('-'*len(el.tag))
                for c in el.findall("./*"):
                    print("  {0}: {1}".format(c.tag, spa.accessors[c.tag].value))
                print("")

        elif cmd == "live":
            print("Live Settings")
            print("=============")
            print("")
            for el in spa.log_xml.findall("./*"):
                print(el.tag)
                print('-'*len(el.tag))
                for c in el.findall("./*"):
                    print("  {0}: {1}".format(c.tag, spa.accessors[c.tag].value))
                print("")

        elif cmd.startswith("press "):
            cmd = cmd[6:]
            for button in gecko_constants.buttons:
                if button[0].lower() == cmd:
                    spa.press(button[2])

        elif cmd.startswith("setpoint "):
            cmd = cmd[9:]
            spa.accessors['SetpointG'].value = float(cmd)

        elif cmd.startswith("get "):
            key = inp[4:]
            try:
                print("{0} = {1}".format(key, spa.accessors[key].value))
            except:
                (ex,ty,tb) = sys.exc_info()
                print("{0}: {1}".format(ex,ty))
                traceback.print_tb(tb)

        elif cmd.startswith("set "):
            try:
                key, val = inp[4:].split("=")
                spa.accessors[key].value = val
            except:
                (ex,ty,tb) = sys.exc_info()
                print("{0}: {1}".format(ex,ty))
                traceback.print_tb(tb)

        elif cmd == "refresh":
            spa.refresh()

        elif cmd == "download":
            manager.download()

        elif cmd == "license":
            print(LICENSE)

        elif cmd == "about":
            print("")
            print("client.py: A python program using GeckoLib library to drive Gecko enabled devices with in.touch2 communication modules")
            print("Client version {0}".format(version))
            print("Library version {0}".format(manager.version))

        else:
            print("Unknown command. Try 'help'!")

finally:
    manager.finish()
