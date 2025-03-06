# GeckoLib

Async library to interface with Gecko Alliance spa pack systems via in.touch2

Written from the ground up using info gleaned from Wireshark captures to sniff
the conversation between the iOS app and the inTouch2 home transmitter.

Designed to be used by home automation systems such as Home Assistant or openHAB

_This library is now Beta, meaning that there are unlikely to be major changes
in library shape, class definitions, behaviours etc as I client it in my ongoing
Home Assistant integration. This has now been released, in preview, and can be
found at https://github.com/gazoodle/gecko-home-assistant, or from HACS by adding
a new integration and seaching for Gecko_

# Installation

This library is hosted on PyPI and can be installed with the following command-line

`pip install geckolib`

# CUI sample

_Work In Progress_

There is a complete async sample which uses the full API and shows how to
client the SpaManager class, react to events, discover devices and so on.
This can be run using `python3 -m geckolib cui`. On Windows you will need to
install the `curses` library.

It can also be used to diagnose issues with your Gecko client, test drive your
spa and investigate anything that the previous GeckoShell was able to do.



# GeckoShell usage

Once the library is installed, you should be able to start a Gecko shell with the
command `python3 -m geckolib shell`

```python

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

Diagnostics are created for each run, you can find them in the folder where the shell
was started in the file `shell.log`

If you want to start the client and point it at a specific IP address (maybe you have your SPA on a different subnet), you can issue the discovery command as part of the launch parameters

`python3 -m geckolib shell "discover 192.168.1.2"`

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

# Home Assistant integration

The best example of use is in the Home Assistant integration which can be
found here https://github.com/gazoodle/gecko-home-assistant

# Acknowledgements

- Inspired by https://github.com/chicago6061/in.touch2.
- Thanks to the folk at Gecko for building this system as a local device rather than mandating a cloud solution.
- Wireshark is an awesome tool for sniffing out what is going on on your network. Take a look one day, you might be horrified :-)

# License

https://www.gnu.org/licenses/gpl-3.0.html

# Todo

- Error handling (ongoing)
- Pythonize where possible
- More unit tests
- Add API documentation
- Tidy up support files. One class per file
- Add switch for winterizing
- Move to pytest unit test framework (replace all unittest fixtures and custom asserts)
- Use snapshots to generate some specific tests
- Add coverage to GitHub package workflow
- API set_config_mode needs to be per device rather than global
- Move localizable strings so that HA can handle itself
- Use MinSetpointG and MaxSetpointG if available
- Add a watt setting to pumps, heaters and so on so that the library can produce an instantaneous
  power consumption figure which ought to be able to integrate into HA's energy dashboard.
- Add ability to change the RF channel. The app sends a CHACH\xb4\x0c command, play in the simulator!
- When there are two spas loaded, the ping frequency seems to be too high. Is this related to the
  shared global config?
- Expose the master timeouts as configurations and the ud timeouts as controls
- Keep looking to see if there is a time sync mechanism
- Use the config ver and status ver check in simulator to make sure partial block updates are acceptable

# Recent discovery

There have been some issues with the library not getting updates from the spa, or other things not working
as well as they could, so I went back to basics, but this time I did some captures with two in.touch2 app
clients running at the same time. This was quite revealing. I pressed the light-on button on one of them
and then almost immediately, the other one updated, which isn't how the library currrently works.

Further investigation showed that the in.touch module seems to need the ping to be running around 2 seconds
otherwise it simply forgets about reporting changes to the client, so I needed to ensure that an idle spa
still maintains this. I know we changed this quite a while ago, probably to reduce logfile clutter, but if
it impacts the behaviour of the library, it needs changing. Anyway, it's back to 2 seconds always now. What
this also revealed was that we don't need to do the full structure refresh that we had been doing either
because that was to mitigate the missing change updates. Anyway, quite a big protocol change.


## Done/Fixed in 1.0.11
 - Refactor watercare handling to build full support
 - Change ping frequency to be 2 seconds always, see discovery above.
 - Updated the protocol queue to have two queues, one for normal protocol and one for commands
   per v0.4.6
 - Ensure that STATQ and SPACK commands are placed on the command queue
 - Refactor protocol retry mechanism to deal with busy in.touch modules
 - Desyncronize various protocol updates from their async wait mechanisms because this
   resulted in busy traffic immediately after a user demand causing the next one to go into
   a retry loop resulting in tardy updates in HA.
 - Protocol retry count removed because it is now intrinsic to retry operations every so
   often until the timeout period is exceeded.
 - Noticed that inMix updates seem to always send 7 x the number of zones worth of data
   based at 600 (which is the SpaPackStruct.xml's start location of the inMix log structure)
   so replicate this behaviour in the hope that it will drive the inMix modules correctly.

## Done/Fixed in 1.0.10
 - Handle TempNotValid error

## Done/Fixed in 1.0.9
 - Fixed broken EcoMode switch that 1.0.8 introduced
 - Added pump and blower sensors to show P[n] & BL device states because buttons now
   exclusively use UdP[n] for control.
 - Restore old min temperature, but use the pack config data if available to override.

## Done/Fixed in 1.0.8
 - Snapshots can be a full JSON file now
 - Working through various inMix and Mr.Steam issues
 - Trying to get Bain Ultra bath support too
 - Basic Mr.Steam support ready for testing

## Done/Fixed in 1.0.7
 - Move on with MrSteam device detection, it ought to load the facade cleanly now
 - Protect various select sub-classes from missing accessor during reconnection
 - More work on CUI

## Done/Fixed in 1.0.6
 - Fix error in pump is_on function if the state accessor wasn't created.
 - Bubble generator now tolerant of AuxAsBubbleGen being present and turned on, but no output set to AUX
 - Moving simulator, shell and CUI support to module main command.
 - CUI sample is work in progress, check-in needed for bug fix!

## Done/Fixed in 1.0.5
 - Fix DIV/0 in inMix RGB scaler

## Done/Fixed in 1.0.4
 - First version of inMix support. Only currenty handles RGB zones, no auto-modes or syncro.

## Done/Fixed in 1.0.3
 - Support setting of the remaining duration for reminders

## Done/Fixed in 1.0.2
 - Some progress toward support for MrSteam units
 - Refactoring to allow accessory modules such as inMix to be handled.
 - Library is now RUFF compliant, all typing hints are done.
 - Can connect to MrSteam without throwing any errors. This ought to be good to get some snapshots.
 - Rebuilt GeckoPump class to cleanly handle one, two or variable speed pumps
 - Spa manager will reload if critical data changed
 - Update light management to handle both Li and L120 light systems
 - Waterfall to new pattern, still might not reflect actual state if CP is on same circuit
 - Support bubble generator on the pack Aux port
 - Add keypad buttons for all available pumps, blowers, etc.

## BREAKING CHANGES 1.0.2
 - Blower is now a single speed pump, not a switch
 - Single speed pumps no longer support modes, it's either on or off
 - Pump modes are from the user demand list not the device control one, so previously
   "HIGH" was a pump mode, it is now "HI".

## Done/Fixed in 1.0.1
 - Add support for lock mode if it exists on the spa
 - Add support for standby mode
 - Add "Heating" binary sensor

## Done/Fixed in 1.0.0
 - Breaking change, removed all sync APIs
 - Require Python 3.13 as minimum version
 - Made unit tests pass after sync API removal
 - Refactor a bit of the protocol stack to DRY out some code
 - Added "Spa In Use" sensor
 - Added useful diagnostic functionality to shell and simulator
 - Added support for external heat sources

## Done/Fixed in 0.4.20
 - Remove deprecated constant, it's only available in Python 3.13 from warnings, we can re-add it
   adter this package is released.
 - Min Python requirement is 3.11

## Done/Fixed in 0.4.19

- Removed unprintable charater in RF Channel name
- Reworked packgen.py so that the code is RUFF compliant, working towards getting Github actions working
- Fixed simulator to load new HA snapshots
- Significant work on refactoring now with better async understanding
- Lots of RUFF updates
- Removed weird sleep constant that was the root of some CPU usaghe issues, hopefully this has
  gone now we're using a better async pattern.
- Shell and Simulator moving to async pattern in prep for deleting the sync API.
- Big refactor to help track down some obscure bugs, including a rare and hard to reproduce deadlock
- More robust pattern for transport socket usage hopefully clean-up potential
  leaking socket.
- Fixed lock issue when a command is being retried as the protocol lock
  is busy and the CUI won't exit until the timeout has been reached (this can
  be reproduced by making the simulator stop responding to watercare requests)
- Marked all sync APIs as deprecated
- Push this code to github and release it as it will be the last version that
  supports the sync API. It's getting too cluttered to maintain sync and async
  in the same codebase.

## Done/Fixed in 0.4.18

- Actually increment the version number and push to GIT before publishing. I might get the hang of
  this one day :-)

## Done/Fixed in 0.4.17

- Expose water heater internal sensors so they can be exposed in the home assistant integration

## Done/Fixed in 0.4.16

- Change min temperature from 15C to 8C
- Handle unnamed SPA (Issue #54)
- Prevent watercare from being out-of-range at the expense of knowing if it was ... it's more stable for users (#40)
- Fixed async importlib code from blocking by using loop executor

## Done/Fixed in 0.4.15

- Merged latest SpaPackStruct data from BenSeverson

## Done/Fixed in 0.4.9

- Merged pull to reduce asyncio sleep timeout to reduce processor usage

## Done/Fixed in 0.4.8

- Split radio strength & channel into two separate sensors
- Added some extra debugging around protocol sync lock
- Some unit_of_measurement values were the string "None" instead of the python keyword None
- Aggregate SpaPack error properties into a single text sensor
- Rebuild pack accessors from SpaStructPack.xml v36.1

## Done/Fixed in 0.4.7

- Merged fix for negative watercare values (thanks @EiNSTeiN-)
- Demote out-of-range spapack struct enum values to DEBUG and return "Unknown"
- Demote "No handler for xxxx" to DEBUG to declutter log files

## Done/Fixed in 0.4.6

- Going back to basics and watching the protocol from the iOS app, I noticed that
  the commands sent from the app don't use the same sequence numbers as the ones
  that are sent during connection, they run a loop around from 192-255 whereas the
  protocol ones go from 1-191 ... so replicate that behaviour in case it's confusing
  something in the system and adding to the instability of connections
- Moved protocol retry constants to GeckoConfig class
- Added 2 second pause between protocol retries to allow intouch2 EN module to settle
- Increased default timeout from 2 to 4 seconds
- Added radio channel and signal strength sensor

## Done/Fixed in 0.4.5

- Config change code could attempt to set result on a future that was already
  set leading to an unhandled exception that could result in the partial status
  update task being cancelled
- Disconnected facades now cleared out of the system correctly
- Added some more diagnostics to chase sporadic disconnects

## Done/Fixed in 0.4.4

- Moved config settings out of const class into their own class
- Added idle/active config settings and task loop for library to switch between
  idle and active config settings. An idle spa is one that is currently not processing
  any user demands, an active spa is one that has received a client request such as to
  change temp or turn on a pump. Active mode will stay on while any user demand is
  currently live.
- Replaced asyncio.sleep in various places with config_sleep which is aware of when
  the configuration values have changed which means that the loops currently waiting on
  these values stop waiting and can collect the new values.

## Done/Fixed in 0.4.2

- Fixed processor getting pegged at 100% but not using asyncio.sleep(0)
- Fixed simulator to respect names compatible with Windows
- Renamed some snapshots

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

# Thoughts and musings

The current facade control mechanism was based on my first experience with a single spa, and not much
community feedback which has now changed, I now think that I need to update it following a greater
understanding.

The first thing is that the intouch2 app only ever seems to send KEYPAD commands, and these are
handled by the spa and seem to be converted into UserDemand changes.

When the UserDemand property changes, the spa also seems to make other changes to the data structures
such as setting pump run times, light run times and so on, all of which we can see in the client
apps and the simulator.

I have recently done quite a bit of work in the simulator and client to remove the old sync code
and in doing so, I have refactored a good chunk of the base and got a better idea on how to improve
it.

Sometimes the intouch2 app shows the state of devices based on the timers for some reason, at
least if I change the UserDemand for the time then the app UI updates, but other times it responds
to when the UdP1/UdLi status changes. This needs more investigation!

In the current code, the possible values for the user demands is a direct copy of the info
that is in the SpaStruct.xml file, but if that was modified based on the information in the
Config accessors, then the facade could be more aware of single speed, two speed and variable
speed pumps that seem to be supported.

I've also recently updated the spa pack generator to include the structures for inMix and other
Gecko products so that I can look into how to drive those devices too.

# Version

Using Semantic versioning https://semver.org/
