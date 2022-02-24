""" Complete sample client CUI - Console User Interface

    All the code to drive the CUI is in this file, it should only
    talk to the facade as it is the example of how to integrate
    geckolib into an automation system

"""

import asyncio
import curses
import _curses
import logging
import time
from datetime import datetime
from abstract_display import AbstractDisplay
from config import Config
from context import AsyncTasks, GeckoAsyncFacade, GeckoAsyncLocator

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "1eca3a27-9b00-476a-9645-d13f4b1f9b56"


_LOGGER = logging.getLogger(__name__)


def main_menu(stdscr):
    k = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()
    stdscr.border(0)
    # curses.mousemask(1)

    # Start colors in curses
    # curses.start_color()
    # curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    # curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while k != ord("q"):

        # Initialization
        stdscr.erase()

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


class CUI(AbstractDisplay, AsyncTasks):
    def __init__(self, stdscr: "_curses._CursesWindow"):
        AbstractDisplay.__init__(self, stdscr)
        AsyncTasks.__init__(self)

        # Enable mouse events
        curses.mousemask(1)

        self._config = Config()

        self._last_update = time.monotonic()
        self._counter = 0
        self._last_char = None

        self._facade = GeckoAsyncFacade(
            CLIENT_ID,
            spa_address=self._config.spa_address,
            spa_identifier=self._config.spa_id,
        )
        self._facade.watch(self._on_facade_changed)

    async def __aenter__(self):
        # self.add_task(self._counter_loop(), "Counter")
        # self.add_task(self._timer_loop(), "Timer")
        self.add_task(self._sequence_pump(), "Sequence pump")
        await self._facade.__aenter__()
        await self.run()
        return self

    async def __aexit__(self, *exc_info):
        await self._facade.__aexit__(exc_info)
        return await super().__aexit__(*exc_info)

    async def _counter_loop(self) -> None:
        while True:
            self._counter = self._counter + 1
            self.make_display()
            await asyncio.sleep(5)

    async def _timer_loop(self) -> None:
        while True:
            self.make_display()
            await asyncio.sleep(1)

    async def _sequence_pump(self) -> None:
        while True:
            # If we don't have a config ID, then trigger a find
            # if self._config.spa_id is None:
            #    if self._facade.locator is None:
            #        await self._facade.discover()
            #        _LOGGER.debug("Discovery complete")
            await asyncio.sleep(0)

    def _on_facade_changed(self, *args) -> None:
        self.make_display()

    def make_title(self, maxy: int, maxx: int) -> None:
        title = "Gecko Async Sample App"
        self.stdscr.addstr(0, int((maxx - len(title)) / 2), title)

    def make_display(self) -> None:
        try:
            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.erase()
            self.stdscr.box()

            self.make_title(maxy, maxx)

            msg1 = "Resize at will"
            msg2 = "Press 'q' to exit"
            msg3 = f"It is now {datetime.now()}"

            self.stdscr.addstr(int(maxy / 2) - 1, int((maxx - len(msg1)) / 2), msg1)
            self.stdscr.addstr(int(maxy / 2), int((maxx - len(msg3)) / 2), msg3)
            self.stdscr.addstr(int(maxy / 2) + 1, int((maxx - len(msg2)) / 2), msg2)
            self.stdscr.addstr(
                maxy - 2,
                1,
                f"Hello {self._counter}, Status: {self._facade.status_line}, char: {self._last_char}",
            )

        except _curses.error:
            # If window gets too small, we won't output anything
            _LOGGER.warning("Screen too small")
            self.stdscr.erase()

        self.stdscr.refresh()

        # window = curses.newwin(5, 20, 10, 10)
        # window.box()
        # window.addstr(2, 2, "Window")
        # window.refresh()

    def handle_char(self, char: int) -> None:
        if chr(char) == "q":
            self.set_exit()
        self._last_char = char
