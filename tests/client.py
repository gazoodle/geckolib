"""
Sample client program for geckolib.

Search for in.touch2 devices and then allows interaction with them
"""  # noqa: INP001

import sys
from pathlib import Path

from context import GeckoShell

# Run the shell with any extra arguments
Path("client.log").unlink(True)
GeckoShell.run(["logfile client.log"] + sys.argv[1:])
