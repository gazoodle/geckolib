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

# API Usage

```python

""" Sample Client """

import sys
import os
import time

from geckolib import GeckoManager, GeckoFacade   # pylint: disable=import-error,wrong-import-position

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "a2d936db-4e95-4e4d-82bc-b4225fa99739"

class SampleClient:
    """ Sample client class to demonstrate how to use geckolib """

    def __init__(self):
        self.manager = GeckoManager(CLIENT_ID)
        self.facade = None

    def __del__(self):
        self.manager.finish()

    def connect_to_first_spa(self):
        """ Connect the client to the first spa that it encounters """
        self.manager.discover()
        self.manager.spas[0].connect()
        self.facade = GeckoFacade(self.manager.spas[0])

    def pump_1_on(self):
        """ Turn the first pump on """
        self.facade.pumps[0].turn_on()

    def pump_1_off(self):
        """ Turn the first pump off """
        self.facade.pumps[0].turn_off()

    @property
    def get_current_temperature(self):
        """ Get the current temperature of the spa """
        return self.facade.water_heater.current_temperature

cli = SampleClient()
cli.connect_to_first_spa()
print("Spa temp is {0}".format(cli.get_current_temperature))

print("Turning pump 1 on")
cli.pump_1_on()

time.sleep(5)

print("Turning pump 1 off")
cli.pump_1_off()
time.sleep(2)

del cli

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
    * Operations (Pumps/Blowers/Lights)
    * Warnings/Errors
    * Reminders
    * Diagnostics
 - Support installtools/requirements.txt to ensure all libraries are present
 - More unit tests
 - Show which parts of the status block are addressed by the SpaPackStruct.xml
   so we can inspect the remainder to see if there is anything useful in there.
 - Handle other device types such as Waterfall
 - Handle multi/variable speed pumps
 - Async APIs
 - Turn on/off log file in GeckoShell

## Done/Fixed in 0.3.11
 - Ping frequency set to 45 seconds

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
