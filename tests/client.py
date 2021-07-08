#!/usr/bin/python3
"""
    Sample client program for geckolib, searches for in.touch2 devices and
    then allows interaction with them
"""

from context import GeckoShell
import sys

# Run the shell with any extra arguments
GeckoShell.run(["logfile client.log"] + sys.argv[1:])
