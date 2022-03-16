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

# Async support

The core of the library has been rewritten to be async based. This is for several
reasons;

1. Home Assistant, my main client of the library prefers this pattern. I'd like to
   get away from the "can't connect", "not supported" pattern and have the spa
   connect immediately to the facade (which will do the handshake to the actual spa
   asynchronously so that connection state can be shown in the UI if required).
   This will improve HA startup performance and allow me to control
   the retry connection pattern in the library without having to burden the HA
   integration with this (HA doesn't like protocol in integrations)
2. I've done loads of multi-threaded programming in my life and think I'm familiar
   with almost all kinds of problems this brings, but ... why bother when this isn't
   necessary
3. While trying to implement a feature that supports occasionally disconnected
   spas without generating reams of logging, I realized that I was fighting against
   the previous architecture, so it's time to refactor that.
4. Every day is a school day. I've not seriously explored Python's async support :-)

Currently this isn't a breaking change, the sync library still has the functionality
that it always had (albeit with some major refactoring). There is a completely parallel
API and class set to support async clients.

I'll update the HA integration to use the async version as it's much faster to start
and it has more functionality. I know there are other automation clients using this
library, so the sync API and classes will stay here for a while until those clients have
had a chance to use the new async code, but I will deprecate them at some point,
probably when the library goes to v1.0.0

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

# Async API Usage

```python
""" Sample client demonstrating async use of geckolib """

import asyncio
import logging

from geckolib import GeckoAsyncSpaMan, GeckoSpaEvent  # type: ignore

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "a2d936db-4e95-4e4d-82bc-b4225fa99739"
# Replace with your spa IP address if on a sub-net
SPA_ADDRESS = None


class SampleSpaMan(GeckoAsyncSpaMan):
    """Sample spa man implementation"""

    async def handle_event(self, event: GeckoSpaEvent, **kwargs) -> None:
        # Uncomment this line to see events generated
        # print(f"{event}: {kwargs}")
        pass


async def main() -> None:

    async with SampleSpaMan(CLIENT_ID, spa_address=SPA_ADDRESS) as spaman:
        print("Looking for spas on your network ...")

        # Wait for descriptors to be available
        await spaman.wait_for_descriptors()

        if len(spaman.spa_descriptors) == 0:
            print("**** There were no spas found on your network.")
            return

        spa_descriptor = spaman.spa_descriptors[0]
        print(f"Connecting to {spa_descriptor.name} at {spa_descriptor.ipaddress} ...")
        await spaman.async_set_spa_info(
            spa_descriptor.ipaddress,
            spa_descriptor.identifier_as_string,
            spa_descriptor.name,
        )

        # Wait for the facade to be ready
        await spaman.wait_for_facade()

        print(spaman.facade.water_heater)

        print("Turning pump 1 on")
        await spaman.facade.pumps[0].async_set_mode("HI")

        await asyncio.sleep(5)

        print("Turning pump 1 off")
        await spaman.facade.pumps[0].async_set_mode("OFF")

        await asyncio.sleep(5)


if __name__ == "__main__":
    # Install logging
    stream_logger = logging.StreamHandler()
    stream_logger.setLevel(logging.DEBUG)
    stream_logger.setFormatter(
        logging.Formatter("%(asctime)s> %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(stream_logger)
    logging.getLogger().setLevel(logging.INFO)

    asyncio.run(main())
```

This should output something like this

```
Looking for spas on your network ...
2022-03-16 07:05:12,842> INFO Found 1 spas ... [My Spa(SPA00:01:02:03:04:05)]
Connecting to My Spa at 10.0.0.123 ...
Heater: Temperature 36.0°C, SetPoint 36.0°C, Real SetPoint 36.0°C, Operation Idle
Turning pump 1 on
2022-03-16 07:05:19,292> INFO Value for UdP2 changed from OFF to HI
2022-03-16 07:05:19,479> INFO Value for P2 changed from OFF to HIGH
2022-03-16 07:05:19,480> INFO Value for UdPumpTime changed from 0 to 45
Turning pump 1 off
2022-03-16 07:05:25,049> INFO Value for UdP2 changed from HI to OFF
2022-03-16 07:05:25,236> INFO Value for P2 changed from HIGH to OFF
2022-03-16 07:05:25,236> INFO Value for UdPumpTime changed from 45 to 0

```

# Complete sample

There is also a complete async sample which can be found in the repo under
the /sample folder. This can be run using `python3 complete.py`. Full path
https://github.com/gazoodle/geckolib/tree/main/sample

# Home Assistant integration

The best example of use is in the Home Assistant integration which can be
found here https://github.com/gazoodle/gecko-home-assistant

# Sync API Usage

**WARNING** Sync functionality will be removed in a future release,
examples removed from README

# Acknowledgements

- Inspired by https://github.com/chicago6061/in.touch2.
- Thanks to the folk at Gecko for building this system as a local device rather than mandating a cloud solution.
- Wireshark is an awesome tool for sniffing out what is going on on your network. Take a look one day, you might be horrified :-)

# License

https://www.gnu.org/licenses/gpl-3.0.html

# Todo

- Reminders
- Spa state (errors)
- Error handling (ongoing)
- Pythonize where possible
- APIs to support integration into automation systems (Ongoing)
  - Warnings/Errors
  - Reminders
  - Diagnostics
- More unit tests
- Handle other device types such as Waterfall
- Handle inMix for lighting control
- Add API documentation
- RF signal strength for EN(Home) -> CO(Spa)
- Merge reminders branch from @kalinrow
- List property for User demands in pack classes
- List property for errors in pack classes
- Tidy up support files. One class per file
- Full sweep for typing hints - Ongoing
- Add sensor for reminders
- Add sensor for errors
- Add switch for winterizing
- Add sensor for RF signal strength
- Add ability to set hours so we can implement a crude clock sync mechanism
- Think about a way to provide access to behaviour refresh frequencies so that
  it can be customised
- Look into getting shell & simulator using async API so that there are no
  internal dependencies on the sync code any longer
- Move to pytest unit test framework
- Use snapshots to generate some specific tests
- Build some documentation
- Add coverage to GitHub package workflow
- There is a lock issue when a command is being retried as the protocol lock
  is busy and the CUI won't exit until the timeout has been reached (this can
  be reproduced by making the simulator stop responding to watercare requests)

## Done/Fixed in 0.4.1

- Updated README with simple async example
- Pull in reminders PR from @kalinrow - Thanks!
- Add unit tests for reminders
- Add async version of reminders - slightly different API as sync version returns
  time as first reminder
- Updated various clients to use reminders

## Done/Fixed in 0.4.0

- Supports both sync and async clients. The sync clients ought to be backward
  compatible but there has been a huge chunk of refactoring to get the async
  built and even though I've run all the tests and clients, it's possible there
  are issues
- Sensor for connection status is available early in facade lifetime
- Ping sensor available after spa begins connection sequence
- Re-added readline library to simulator as it was doing auto-complete for snapshot
  loading and was useful when testing, but added it inside a try/catch block so
  it won't upset Windows clients
- Manage ping failure and RF errors with retry mechanism
- Watercare regular refresh from facade
- Create Spa manager class to run the connection logic so that clients get cleanup
  opportunity when reconnections are needed
- Handle disconnected spas, ping failures, RF errors and so on
- Simulator can get/set accessors for experimentation

## Done/Fixed in 0.3.24

- Fix error found by Github workflow
- Added extra logging into to find out more about issue #28
- Removed readline library as it isn't supported on Windows and it wasn't really doing anything
- Added some extra doc for issue #18
- Added RFERR handler to client and simulator to start investigations
- Handle Watercare index out of range
- Accessors can now deal with Time type entries
- Added diag.py to aid tracking issue#27
- Added eco mode control to facade and shell
- Temperature accessor in new generator as it doesn't need to be handled at runtime
- Removed decorators.py

## Done/Fixed in 0.3.23

- Demoted some INFO logging to DEBUG to reduce HA log file clutter

## Done/Fixed in 0.3.22

- Increase connection timeout to help with laggy tubs and busy networks
- Watercare setting updated locally rather than wait for tub response to
  improve HA UI responsiveness
- Fast locator for static IP

## Done/Fixed in 0.3.21

- Demoted some benign debugging data that clutters log files
- Replaced "config" and "live" with "accessors" commands in shell to reduce direct access to XML
- Added "monitor" command in shell to give a live view of changes from other sources e.g. control panel or app
- Removed runtime reliance on SpaPackStruct.xml, this is replaced by the python code in driver/pack/\*
- Accessor can handle byte, word, bool value updates if provided as a string (i.e. GeckoShell set command)

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
