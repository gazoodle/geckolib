#!/usr/bin/python3
"""
    Sample client program for geckolib, searches for in.touch2 devices and
    then allows interaction with them
"""

import logging
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from geckolib import GeckoShell  # pylint: disable=import-error,wrong-import-position

# Set logging
stm_log = logging.StreamHandler()
stm_log.setLevel(logging.WARNING)
stm_log.setFormatter(logging.Formatter("%(message)s"))
logging.basicConfig(
    level=logging.DEBUG,  # Uncomment this line to get detailed information
    # level=logging.WARNING, # Uncomment this line to keep log files small
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("client.log"), stm_log],
)
logger = logging.getLogger(__name__)

# Run the shell
GeckoShell.run()
