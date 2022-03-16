#!/usr/bin/python3.9
""" Complete sample client

    This sample is built as a complete async client demonstrating all
    the code that might be needed in a full client of the library,
    e.g. in a home automation system.

    It was used to help develop the change from sync to async as
    this seems to be where all the HA integrations are going anyway

    I would have loved to have one library that could do both, but
    this was increasingly difficult to acheive and I was spending
    quite a bit of time in thread faff which is something that I'm
    sure is not needed in the async world ... time will tell

"""
import os
import logging
import asyncio

from cui import CUI
from curses import wrapper


_LOGGER = logging.getLogger(__name__)


def install_logging():
    """Everyone needs logging, you say when, you say where, you say how much"""
    os.remove("cui.log")
    file_logger = logging.FileHandler("cui.log")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(file_logger)
    logging.getLogger().setLevel(logging.DEBUG)


async def async_main(stdscr):
    """Async main manages the console UI"""
    async with CUI(stdscr):
        await asyncio.sleep(0)


def main(stdscr):
    """This main installs logging and then runs the async loop"""
    install_logging()
    asyncio.run(async_main(stdscr))


########################################################################################
#
#                                       Entry point
if __name__ == "__main__":
    wrapper(main)
