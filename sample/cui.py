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
        self._last_char = None
        self._commands = {}

        self._facade = GeckoAsyncFacade(
            CLIENT_ID,
            spa_address=self._config.spa_address,
            spa_identifier=self._config.spa_id,
        )
        self._facade.watch(self._on_facade_changed)

    async def __aenter__(self):
        self.add_task(self._timer_loop(), "Timer")
        self.add_task(self._sequence_pump(), "Sequence pump")
        await self._facade.__aenter__()
        await self.run()
        return self

    async def __aexit__(self, *exc_info):
        await self._facade.__aexit__(exc_info)
        return await super().__aexit__(*exc_info)

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

    def _select_spa(self, spa):
        self._config.set_spa_id(spa.identifier_as_string)
        self._config.set_spa_address(spa.ipaddress)
        self._config.save()
        self._facade.set_spa_info(spa.identifier_as_string, spa.ipaddress)

    def _clear_spa(self):
        self._config.set_spa_id(None)
        self._config.set_spa_address(None)
        self._config.save()
        self._facade.set_spa_info(None, None)

    def make_title(self, maxy: int, maxx: int) -> None:
        title = "Gecko Async Sample App"
        self.stdscr.addstr(0, int((maxx - len(title)) / 2), title)

    def make_display(self) -> None:
        try:
            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.erase()
            self.stdscr.box()

            self.make_title(maxy, maxx)

            lines = []
            self._commands = {}

            if self._facade.is_ready:

                if self._facade.spa is not None:
                    lines.append(f"{self._facade.name} is ready")
                    lines.append("")
                    lines.append(f"{self._facade.water_heater}")
                    for pump in self._facade.pumps:
                        lines.append(f"{pump}")
                    for blower in self._facade.blowers:
                        lines.append(f"{blower}")
                    for light in self._facade.lights:
                        lines.append(f"{light}")
                    for reminder in self._facade.reminders:
                        lines.append(f"{reminder}")
                    lines.append(f"{self._facade.water_care}")
                    for sensor in [*self._facade.sensors, *self._facade.binary_sensors]:
                        lines.append(f"{sensor}")
                    lines.append(f"{self._facade.eco_mode}")

                elif self._facade.locator is not None:
                    if self._facade.locator.spas is not None:
                        for idx, spa in enumerate(self._facade.locator.spas, start=1):
                            lines.append(f"{idx}. {spa.name} at {spa.ipaddress}")
                            self._commands[
                                f"{idx}"
                            ] = lambda self=self, spa=spa: self._select_spa(spa)

            lines.append("")
            if self._facade.spa is not None:
                if self._facade.is_ready:
                    lines.append("Press 'b' to toggle blower")
                    if self._facade.blowers[0].is_on:
                        self._commands["b"] = lambda: {
                            self._facade.blowers[0].turn_off()
                        }
                    else:
                        self._commands["b"] = lambda: {
                            self._facade.blowers[0].turn_on()
                        }
                lines.append("Press 'r' to rescan")
                self._commands["r"] = self._clear_spa

            lines.append("Press 'q' to exit")
            self._commands["q"] = self.set_exit

            half = int(len(lines) / 2)

            for idx, line in enumerate(lines):
                self.stdscr.addstr(
                    int(maxy / 2) - half + idx, int((maxx - len(line)) / 2), line
                )

            self.stdscr.addstr(
                maxy - 2,
                1,
                f"{datetime.now():%x %X} - Status: {self._facade.status_line}",
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
        cmd = chr(char)
        if cmd in self._commands:
            self._commands[cmd]()
        self._last_char = char
