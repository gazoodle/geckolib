# GeckoLib
Library to interface with Gecko Alliance spa pack systems via in.touch2

Written from the ground up using info gleaned from Wireshark captures to sniff 
the conversation between the iOS app and the inTouch2 home transmitter.

Designed to be used by home automation systems such as Home Assistant or openHAB

_This library is currently in Alpha, meaning that there may be large changes
in library shape, class definitions, behaviours etc as I client it in my ongoing
Home Assistant integration. This has now been released, in preview, and can be 
found at https://github.com/gazoodle/gecko-home-assistant, or from HACS by adding
a new integration and seaching for Gecko_

# Installation

This library is hosted on PyPI and can be installed with the following command-line

`pip install geckolib`

# GeckoShell usage

Once the library is installed, you should be able to start a Python interpreter session
by using the command `python3`, then executing the following commands

```python
>>> from geckolib import GeckoShell
>>> GeckoShell.run()


    <Disclaimer>
    :
    <snip/>
    :
    </Disclaimer>

Starting discovery process...Found 1 spas
Connecting to spa `Spa` at 10.1.2.3 ... connected!
Heater: Temperature 39.0°C, SetPoint 39.0°C, Operation Idle
Pump 1: OFF
Pump 2: OFF
Blower: OFF
Lights: OFF
WaterCare: Standard
Welcome to the Gecko shell. Type help or ? to list commands.

Spa$ 

```

This ought to find your spa on your local network. If it doesn't, please open an issue, you can
exercise some of your spa features using the commands below

```

Spa$ P1 HI
Spa$ P1 OFF

Spa$ LI ON
Spa$ LI OFF
```

You can get help on the GeckoShell module

```

Spa$ help

Documented commands (type help <topic>):
========================================
BL  P2      discover  get      list    refresh   snapshot  watercare
LI  about   download  help     live    set       state   
P1  config  exit      license  manage  setpoint  version 

Spa$ help watercare
Set the active watercare mode to one of ['Away From Home', 'Standard', 'Energy Saving', 'Super Energy Saving', 'Weekender'] : WATERCARE <mode>
Spa$ watercare Weekender

```

If you have more than one spa/device detected, you can use the `list` and `manage` commands

```

Starting discovery process...Found 2 spas
Welcome to the Gecko shell. Type help or ? to list commands.

(Gecko) list
1. Spa
2. Dummy Spa
(Gecko) manage 1
Connecting to spa `Spa` at 10.1.2.3 ... connected!
Heater: Temperature 39.0°C, SetPoint 39.0°C, Operation Idle
P1: OFF
P2: OFF
BL: OFF
LI: OFF
WaterCare: Standard
Spa$ 

```

If you want to get some diagnostics you can enable file logging at the start of the session

```python
>>> from geckolib import GeckoShell
>>> GeckoShell.run(["logfile client.log"])

  :
  :

```

or it can be used later after you've connected to your spa with the `logfile` command

```

Spa$ logfile client.log

```


The file `client.log` will contain diagnostic information that may be useful 
for tracking down issues

If you want to start the client and point it at a specific IP address (maybe you have your SPA on a different subnet), you can issue the discovery command as part of the launch parameters

```python
>>> from geckolib import GeckoShell
>>> GeckoShell.run(["logfile client.log", "discover 192.168.1.2"])

  :
  :

```

# Simulator Usage

It's best if you download the repo for using the simulator. Once you've done that, 
open a terminal to your repo test folder (./tests)

`python3 simulator.py`

You should see a prompt

```
Welcome to the Gecko simulator. Type help or ? to list commands.

(GeckoSim) 
```

You should load the default snapshot at this point

```
(GeckoSim) load snapshots/default.snapshot
(GeckoSim)
```

Now you can run the client program, or indeed your iOS or Android app and then 
attempt to connect to the simulator. At present it only supports loading another
snapshot to change the state. If the changes are too great, for example, if you've
loaded a completly different spa then the iOS and Android apps may be confused.

Best to click on the account icon and then reselect the test spa to get it to
reconnect from the start.

Also, at present the simulator doesn't respond to any commands issued from the
iOS and Android applications.

# API Usage

This first example is a trivial one to show how to minimally client this library

```python
""" Sample client demonstrating use of geckolib """

import time

from geckolib import GeckoLocator

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "a2d936db-4e95-4e4d-82bc-b4225fa99739"

print("Locating spas on your network")
with GeckoLocator(CLIENT_ID) as locator:

    print(f"Connecting to first spa {locator.spas[0]}")
    with locator.spas[0].get_facade() as facade:

        print(facade.water_heater)

        print("Turning pump 1 on")
        facade.pumps[0].set_mode('HI')

        time.sleep(5)

        print("Turning pump 1 off")
        facade.pumps[0].set_mode('OFF')
        time.sleep(2)
```

A more complex example 

```python
""" Real world sample client demonstrating use of geckolib

Python async suffers like many interpreted languages with function
colour see:

http://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/

To avoid this, the geckolib is written using synchronous functions and
methodologies, but using threading to manage the I/O portions. Where
appropriate, state flags are exposed so that you can use async clients
to ensure that your host is still responsive and I don't have to maintain
two versions of the library ... ugh!"""

import time

from geckolib import GeckoLocator

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "a2d936db-4e95-4e4d-82bc-b4225fa99739"

# First up, lets locate all the spas on your network
print("Locating spas on your network ", end="", flush=True)
locator = GeckoLocator(CLIENT_ID)
locator.start_discovery()

# We can perform other operations while this is progressing, like output a dot
while not locator.has_had_enough_time:
    # Could also be `await asyncio.sleep(1)`
    locator.wait(1)
    print(".", end="", flush=True)

locator.complete()

# Report how many we've found
print(f" found {len(locator.spas)} spas")

if len(locator.spas) == 0:
    raise RuntimeError("Cannot continue as there were no spas detected")

# Grasp info about your spa, this is often the integration phase in your
# automation system, sometimes you can store binary identifiers, sometimes
# you can't ...
persistent_spa_identifier = locator.spas[0].identifier_as_string
print(f"Using spa identifier {persistent_spa_identifier}")

# Some time later, when we want to start the automation system but don't
# want to choose the spa again, we do something like this ...
facade = GeckoLocator.find_spa(CLIENT_ID, persistent_spa_identifier).get_facade(False)

# Now we have a facade, wait for it to be connected
print(f"Connecting to {facade.name} ", end="", flush=True)
while not facade.is_connected:
    # Could also be `await asyncio.sleep(1)`
    facade.wait(1)
    print(".", end="", flush=True)
print(" connected")

# Do some things with the facade
print(f"Water heater : {facade.water_heater}")


def pump_1_change(sender, old_value, new_value):
    print(f"Pump 1 changed from {old_value} to {new_value}")


# Watch pump 1 for changes and report on them
facade.pumps[0].watch(pump_1_change)

print("Turn pump 1 on")
facade.pumps[0].set_mode('HI')

time.sleep(5)

print("Turning pump 1 off")
facade.pumps[0].set_mode('OFF')

time.sleep(2)
facade.complete()
```

# Acknowledgements

 - Inspired by https://github.com/chicago6061/in.touch2.
 - Thanks to the folk at Gecko for building this system as a local device rather than mandating a cloud solution.
 - Wireshark is an awesome tool for sniffing out what is going on on your network. Take a look one day, you might be horrified :-)

# License
https://www.gnu.org/licenses/gpl-3.0.html

# Todo

 - Reminders
 - Spa state (errors)
 - Error handling
 - Better timeout/retry for multiple commands
 - Pythonize where possible
 - Download configuration so that a restore is possible
 - Factory reset spa pack if possible
 - APIs to support integration into automation systems (Ongoing)
    * HVAC (Heating/Cooling/Setpoint/Modes)
    * States (Pumps/Blowers/Lights)
    * Support Devices States (Circulation Pump/Ozone/Filters)
    * Operations (Pumps/Blowers/Lights)
    * Warnings/Errors
    * Reminders
    * Diagnostics
 - More unit tests
 - Show which parts of the status block are addressed by the SpaPackStruct.xml
   so we can inspect the remainder to see if there is anything useful in there.
 - Handle other device types such as Waterfall
 - Handle multi/variable speed pumps
 - Connection retry needed when pings fail
 - A missing spa is an unusual event not a critical failure, retry connection
 - Find mechanism to get more recent SpaPackStruct.xml.
   o V19 available from Gecko
   o V24 can be dug out of Android APK assemblies using some C#
   o V28 is obfuscated in latest version (Xamarin compression apparently)
   o V33 is downloaded from https portal, investigation ongoing.
   Contact initiated with Gecko .. still ongoing.
 - Handle inMix for lighting control

## Done/Fixed in 0.3.20
 - Merge changes for variable speed pumps. Thanks https://github.com/los93sol
 - Prevent new "pump" command showing in help UI

## Done/Fixed in 0.3.19
 - Ensure STATP changes are cleared after processing rather than accumulating for-all-time! Thanks https://github.com/maegibbons

## Done/Fixed in 0.3.18
 - Added some more snapshots
 - Attempt to handle spas that return unsupported config/log versions
 - Add ability to provide an IP address to the library

## Done/Fixed in 0.3.17
 - Attempt to fix urllib3 requirement in pip install. It was in the wrong place

## Done/Fixed in 0.3.16
 - More robust to missed packets during spa connection
 - Mechanism to access raw pack values from the facade, e.g. facade.pumps[0].state_sensor.accessor.raw_value
 - Add API to facade to get device by key, e.g. facade.get_device("P1") will return the first pump. 
 - Add property to facade to get all device keys; facade.devices

## Done/Fixed in 0.3.15
 - Trying out Github publish actions

## Done/Fixed in 0.3.14
 - Added SmartWinterMode sensors
 - Added Filter Clean/Purge sensors

## Done/Fixed in 0.3.13
 - Move MrSteam handling on so that we can get a proper structure dump

## Done/Fixed in 0.3.12
 - UnicodeEncodeError: 'latin-1' codec can't encode character '\u0101' in position 108: ordinal not in range(256)
 - Massive refactor of protocol handlers to make building a simulator easier
 - Changes to allow library to be more suitable for async clients
 - Ping frequency returned to 15 seconds
 - Simulator added to allow investigation using snapshots sent in from other folk
 - Heating state fixed to show heating/cooling as appropriate
 - Issue #1 Waterfall now recognised and responding to button press
 - Issue #3 P1 Twice - deduped the device list
 - Issue #8 The library should be able to provide temp and heater usage stats now
 - Issue #9 Water Heater current operation should now be working correctly

## Done/Fixed in 0.3.11
 - Ping frequency set to 45 seconds
 - Reset method to GeckoReponse class to handle retries in GeckoGetStatus class
 - Add mechanism to locate a spa in the locator class based on it's identifier
 - Set worker threads to daemon mode
 - Re-structure for better lifetime management and easier clienting
 - Merged PR from dukey32123 supplying waterfall constants ... need to find keypad code too.
 - flake8 and black formatting and tidy-up
 - Observable added to propagate change notification so we can be cliented as a 
   local-push integration in Home Assistant
 - Moved all the functionality out of client.py and put it into GeckoShell class

## Done/Fixed in 0.3.10
 - Try upload to PiPY

## Done/Fixed in 0.3.9
 - Message encoding -> latin1 from utf-8 to avoid mangling raw bytes. This fixes
   the turning pump 2 off when turning pump 1 on using `set UdP2=HI` then 
   `set UdP1=HI`. There must be a better way to do this without switching between
   strings and bytes ...
 - Major source restructure to get ready for PyPI package
 - Moved to pyproject.toml/setup.cfg for modern Python library
 - Updated README.md with better examples

## Done/Fixed in 0.3.8
 - Restructure code to be in line with Python library style
 - Code auto formatted with Black
 - Most pylint warnings/issues fixed
 - Unit tests added for GeckoStructAccessor
 - Watercare handled
 - Client.py program restructured to use python Cmd class

## Done/Fixed in 0.3.7
 - Deal with unhandled devices

## Done/Fixed in 0.3.6
 - Limit buttons & devices to those available based on configuration (i.e. don't show P3 if not installed)
 - Dump state block & intro sequence so we can build a simulator
 - Deal with temp decorators that might not be present on different modules
 - Automation interface added
 - Timeout retry of command to make it more robust on busy networks

 # Version
 Using Semantic versioning https://semver.org/
