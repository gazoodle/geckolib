"""
Spa simulator program for geckolib.

Pretends to be a spa on the network,
used by integration tests to prevent regression
"""  # noqa: INP001

import logging
import sys
from pathlib import Path

from context import GeckoSimulator


def install_logging() -> None:
    """Everyone needs logging, you say when, you say where, you say how much."""
    Path("simulator.log").unlink(True)  # noqa: FBT003
    file_logger = logging.FileHandler("simulator.log")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(file_logger)
    logging.getLogger().setLevel(logging.DEBUG)


install_logging()
GeckoSimulator.run(["load snapshots/default.snapshot", "start"] + sys.argv[1:])
