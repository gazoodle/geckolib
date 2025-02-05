"""
Sample client program for geckolib.

Search for in.touch2 devices and then allows interaction with them
"""  # noqa: INP001

import logging
import sys
from pathlib import Path

from context import GeckoShell


def install_logging() -> None:
    """Everyone needs logging, you say when, you say where, you say how much."""
    Path("client.log").unlink(True)  # noqa: FBT003
    file_logger = logging.FileHandler("client.log")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(file_logger)
    logging.getLogger().setLevel(logging.DEBUG)


# Run the shell with any extra arguments
install_logging()
GeckoShell.run(sys.argv[1:])
