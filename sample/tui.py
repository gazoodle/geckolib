""" Complete sample client TUI - Textual User Interface

    All the code to drive the TUI is in this file, it should only
    talk to the facade as it is the example of how to integrate
    geckolib into an automation system

"""

import curses
import logging


_LOGGER = logging.getLogger(__name__)


def init_tui():
    _LOGGER.debug("Init curses library")
