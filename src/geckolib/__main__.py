"""Main module. Supports python -m geckolib syntax."""

# ruff: noqa: T201

import logging
from pathlib import Path
from sys import argv

from geckolib import CUI, GeckoShell, GeckoSimulator


def usage() -> None:
    """Print usage."""
    print("Usage: python3 -m geckolib <shell|simulator|cui> [client args]")


def install_logging(command: str) -> None:
    """Everyone needs logging, you say when, you say where, you say how much."""
    Path(f"{command}.log").unlink(True)  # noqa: FBT003
    file_logger = logging.FileHandler(f"{command}.log")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(file_logger)
    logging.getLogger().setLevel(logging.DEBUG)


if len(argv) == 1:
    usage()
elif argv[1] == "shell":
    install_logging(argv[1])
    GeckoShell.run(argv[2:])
elif argv[1] == "simulator":
    install_logging(argv[1])
    GeckoSimulator.run(["load ../tests/snapshots/default.snapshot", "start"] + argv[2:])
elif argv[1] == "cui":
    install_logging(argv[1])
    CUI.launch()
else:
    usage()
