#!/usr/bin/python3
"""
    Spa simulator program for geckolib: Pretends to be a spa on the network,
    used by integration tests to prevent regression
"""

import logging

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from geckolib import (  # pylint: disable=import-error,wrong-import-position
    GeckoConstants,
    GeckoManager,
    GeckoFacade,
)

# Setup logging
stm_log = logging.StreamHandler()
stm_log.setLevel(logging.WARNING)
stm_log.setFormatter(logging.Formatter("%(message)s"))
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("client.log"), stm_log],
)
logger = logging.getLogger(__name__)

manager = GeckoManager("18a25f07-f5b4-4fce-b93d-f86600e40f6b")
print("Simulator started")

while True:
    m = GeckoManager("one")
    f = GeckoFacade(m.spas[0])
    x = GeckoConstants.device_class_blower
