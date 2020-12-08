#!/usr/bin/python3
"""
    Spa simulator program for geckolib: Pretends to be a spa on the network,
    used by integration tests to prevent regression
"""

from context import GeckoSimulator

GeckoSimulator.run(["logfile simulator.log", "start"])
