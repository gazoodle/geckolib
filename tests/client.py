#!/usr/bin/python3
"""
    Sample client program for geckolib, searches for in.touch2 devices and
    then allows interaction with them
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from geckolib import GeckoShell  # noqa: E402

# Run the shell
GeckoShell.run(["logfile client.log"])
