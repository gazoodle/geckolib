# GeckoLib
Library to interface with Gecko Alliance spa pack systems via in.touch2

Written from the ground up using info gleaned from Wireshark captures to sniff the conversation between the iOS app and the inTouch2 home transmitter.

Designed to be used by home automation systems such as Home Assistant or openHAB

# Usage

1. Download the repo
2. `python3 client.py`

This ought to find your spa on your network. If it doesn't, please open an issue and include the 
exception. I may need the client.log file but please don't post this as it contains network specific
information. If I need it, please PM it to me

Once this is complete, you can try to turn on or off pumps, blowers, lights

3. `P1 ON` etc
4. `LI ON` etc

Check that the pumps, blowers and lights go on/off as expected

5. `state` will show the current state of the spa
6. `help` will show a list of possible commands. It's not very robust at present :-)
7. `snapshot <description>` will dump a snapshot of the spa data into the log file
8. `exit` will exit the client program

# Troubleshooting

- Ensure all support libraries are present (will move to python library standard in a future release)
- Might need to `pip install urllib3`
- Check the log file `client.log`

# API

(Coming soon)



# Acknowledgements

 - Inspired by https://github.com/chicago6061/in.touch2.
 - Thanks to the folk at Gecko for building this system as a local device rather than mandating a cloud solution.
 - Wireshark is an awesome tool for sniffing out what is going on on your network. Take a look one day, you might be horrified :-)

# License
https://www.gnu.org/licenses/gpl-3.0.html

# Todo

 - Water care settings
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
 - Unit tests to make sure EnumAccessors are working as expected ... odd things 
   happen at present
 - Show which parts of the status block are addressed by the SpaPackStruct.xml
   so we can inspect the remainder to see if there is anything useful in there.
 - Handle other device types such as Waterfall

## Done/Fixed in 0.3.7
 - Deal with unhandled devices

## Done/Fixed in 0.3.6
 - Limit buttons & devices to those available based on configuration (i.e. don't show P3 if not installed)
 - Dump state block & intro sequence so we can build a simulator
 - Deal with temp decorators that might not be present on different modules
 - Automation interface added
 - Timeout retry of command to make it more robust on busy networks

 # Version
 v0.3.7
 Using Semantic versioning https://semver.org/
