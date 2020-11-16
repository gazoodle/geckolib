# GeckoLib
Library to interface with Gecko Alliance spa pack systems via in.touch2

Written from the ground up using info gleaned from Wireshark captures to sniff 
the conversation between the iOS app and the inTouch2 home transmitter.

Designed to be used by home automation systems such as Home Assistant or openHAB

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

Spa$ P1 ON
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

If you have more than one spa/device detected, you can use the `list` and `manage` command

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


# API Usage

```python

""" Simple client demonstrating use of geckolib """

import time
from geckolib import GeckoLocator   # pylint: disable=import-error,wrong-import-position

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "a2d936db-4e95-4e4d-82bc-b4225fa99739"

print("Locating spas on your network")
with GeckoLocator(CLIENT_ID) as locator:

    print("Connecting to first spa")
    with locator.spas[0].get_facade() as facade:

        print(facade.water_heater)

        print("Turning pump 1 on")
        facade.pumps[0].turn_on()

        time.sleep(5)

        print("Turning pump 1 off")
        facade.pumps[0].turn_off()
        time.sleep(2)


```

# Acknowledgements

 - Inspired by https://github.com/chicago6061/in.touch2.
 - Thanks to the folk at Gecko for building this system as a local device rather than mandating a cloud solution.
 - Wireshark is an awesome tool for sniffing out what is going on on your network. Take a look one day, you might be horrified :-)

# License
https://www.gnu.org/licenses/gpl-3.0.html

# Todo

 - Reminders
 - Spa state (heating/cooling/errors)
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
 - Async APIs
 - Turn on/off log file in GeckoShell
 - Make GeckoGetStatus handle missing and out-of-sequence as this is a major 
   cause of delays during spa connection
 - Write simulator module and use that to investigate comms from the app for 
   features that I don't have
 - Sometimes in.touch2 doesn't report back to this library resulting in missing 
   changes
 - Deal with this: 
     UnicodeEncodeError: 'latin-1' codec can't encode character '\u0101' in position 108: ordinal not in range(256)


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
