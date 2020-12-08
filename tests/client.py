#!/usr/bin/python3
"""
    Sample client program for geckolib, searches for in.touch2 devices and
    then allows interaction with them
"""

from context import GeckoShell

# Run the shell
GeckoShell.run(["logfile client.log"])
