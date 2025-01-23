"""
Complete sample client.

This sample is built as a complete async client demonstrating all
the code that might be needed in a full client of the library,
e.g. in a home automation system.

It was used to help develop the change from sync to async as
this seems to be where all the HA integrations are going anyway

I would have loved to have one library that could do both, but
this was increasingly difficult to acheive and I was spending
quite a bit of time in thread faff which is something that I'm
sure is not needed in the async world ... time will tell.
"""

import asyncio
import curses
import logging
from pathlib import Path

from cui import CUI


def install_logging() -> None:
    """Everyone needs logging, you say when, you say where, you say how much."""
    Path("cui.log").unlink(True)
    file_logger = logging.FileHandler("cui.log")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(file_logger)
    logging.getLogger().setLevel(logging.DEBUG)


async def async_main(stdscr: curses.window) -> None:
    """Async main manages the console UI."""
    task = asyncio.current_task()
    task.set_name("CUI main")
    async with CUI(stdscr):
        pass


def main(stdscr: curses.window) -> None:
    """Install logging and then runs the async loop."""
    install_logging()
    asyncio.run(
        async_main(stdscr),
    )


########################################################################################
#
#                                       Entry point
if __name__ == "__main__":
    curses.wrapper(main)
