# GeckoLib
Library to interface with Gecko Alliance spa pack systems via in.touch2

Written from the ground up using info gleaned from Wireshark captures to sniff the conversation 
between the iOS app and the inTouch2 home transmitter

# Usage

See the sample program client.py for information on how to use this library

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
 - Timeout retry of command to make it more robust on busy networks
 - Pythonize where possible
 - Limit buttons & devices to those available based on configuration (i.e. don't show P3 if not installed)
 - Download configuration so that a restore is possible
 - Factory reset spa pack if possible

 # Version
 v0.3.5
 Using Semantic versioning https://semver.org/
