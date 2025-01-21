"""
Spa simulator program for geckolib: Pretends to be a spa on the network,
used by integration tests to prevent regression
"""

from context import GeckoSimulator
from pathlib import Path


Path("simulator.log").unlink(True)
GeckoSimulator.run(["logfile simulator.log", "start"])
