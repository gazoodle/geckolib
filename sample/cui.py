""" Complete sample client CUI - Console User Interface

    All the code to drive the CUI is in this file, it should only
    talk to the facade as it is the example of how to integrate
    geckolib into an automation system

"""

import asyncio
import curses
import _curses
import inspect
import logging
import time
from datetime import datetime
from abstract_display import AbstractDisplay
from config import Config
from context import (  # type: ignore
    GeckoAsyncSpaMan,
    GeckoSpaEvent,
    GeckoAsyncSpaDescriptor,
)
from typing import Optional

from geckolib.automation.async_facade import GeckoAsyncFacade
from geckolib.spa_state import GeckoSpaState

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "1eca3a27-9b00-476a-9645-d13f4b1f9b56"


_LOGGER = logging.getLogger(__name__)


class CUI(AbstractDisplay, GeckoAsyncSpaMan):
    def __init__(self, stdscr: "_curses._CursesWindow"):
        AbstractDisplay.__init__(self, stdscr)
        GeckoAsyncSpaMan.__init__(self, CLIENT_ID)

        # Enable mouse events
        curses.mousemask(1)

        self._config = Config()
        self._spas: Optional[GeckoAsyncSpaDescriptor] = None
        self._facade: Optional[GeckoAsyncFacade] = None

        self._last_update = time.monotonic()
        self._last_char = None
        self._commands = {}
        self._watching_ping_sensor = False

    async def __aenter__(self):
        await GeckoAsyncSpaMan.__aenter__(self)
        self.add_task(self._timer_loop(), "Timer", "CUI")
        await self.async_set_spa_info(
            self._config.spa_address, self._config.spa_id, self._config.spa_name
        )
        # self.add_task(self._sequence_pump(), "Sequence pump", "CUI")
        await self.run()
        return self

    async def __aexit__(self, *exc_info):
        return await GeckoAsyncSpaMan.__aexit__(self, *exc_info)

    async def _timer_loop(self) -> None:
        while True:
            self.make_display()
            await asyncio.sleep(1)

    async def _ssequence_pump(self) -> None:
        while True:
            if False:
                if self.spa_state == GeckoSpaState.IDLE:
                    if self._config.spa_id is None:
                        # If we don't have a config ID, then trigger a find
                        self._spas = await self.async_locate_spas()
                    elif self._facade is None:
                        # If we have an id, but no facade, try a connection
                        self._facade = await self.async_connect(
                            spa_address=self._config.spa_address,
                            spa_identifier=self._config.spa_id,
                        )

            if False:
                if self._config.spa_id is None and self._spas is None:
                    # If we don't have a config ID, then trigger a find
                    self._spas = await self.async_locate_spas()

                elif self._config.spa_id is not None and self._facade is None:
                    # If we have an id, but no facade, try a connection
                    self._facade = await self.async_connect(
                        spa_address=self._config.spa_address,
                        spa_identifier=self._config.spa_id,
                    )

            await asyncio.sleep(0)

    async def handle_event(self, event: GeckoSpaEvent, **kwargs) -> None:
        # Always rebuild the UI when there is an event
        self.make_display()

    async def _select_spa(self, spa):
        self._config.set_spa_id(spa.identifier_as_string)
        self._config.set_spa_address(spa.ipaddress)
        self._config.set_spa_name(spa.name)
        self._config.save()
        await self.async_set_spa_info(spa.ipaddress, spa.identifier_as_string, spa.name)

    async def _clear_spa(self):
        self._config.set_spa_id(None)
        self._config.set_spa_address(None)
        self._config.set_spa_name(None)
        self._config.save()
        await self.async_set_spa_info(None, None, None)

    def make_title(self, maxy: int, maxx: int) -> None:
        title = "Gecko Async Sample App"
        self.stdscr.addstr(0, int((maxx - len(title)) / 2), title)

    async def increase_temp(self):
        await self._facade.water_heater.async_set_target_temperature(
            self._facade.water_heater.target_temperature + 0.5
        )

    async def decrease_temp(self):
        await self._facade.water_heater.async_set_target_temperature(
            self._facade.water_heater.target_temperature - 0.5
        )

    def make_display(self) -> None:
        try:
            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.erase()
            self.stdscr.box()

            self.make_title(maxy, maxx)

            lines = []
            self._commands = {}

            if self.spa_state == GeckoSpaState.IDLE:

                if self.spa_descriptors is not None:
                    # If the _spas property is available, that means we've got
                    # a list of spas that we can choose from
                    for idx, spa in enumerate(self.spa_descriptors, start=1):
                        lines.append(f"{idx}. {spa.name} at {spa.ipaddress}")
                        self._commands[f"{idx}"] = (self._select_spa, spa)

                    if len(self.spa_descriptors) == 0:
                        lines.append("No spas were found on your network")

            elif self._facade is not None:
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
                for sensor in [
                    *self._facade.sensors,
                    *self._facade.binary_sensors,
                ]:
                    lines.append(f"{sensor}")
                lines.append(f"{self._facade.eco_mode}")

            if False:
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
                        for sensor in [
                            *self._facade.sensors,
                            *self._facade.binary_sensors,
                        ]:
                            lines.append(f"{sensor}")
                        lines.append(f"{self._facade.eco_mode}")

                    elif self._facade.locator is not None:
                        if self._facade.locator.spas is not None:
                            for idx, spa in enumerate(
                                self._facade.locator.spas, start=1
                            ):
                                lines.append(f"{idx}. {spa.name} at {spa.ipaddress}")
                                self._commands[
                                    f"{idx}"
                                ] = lambda self=self, spa=spa: self._select_spa(spa)
                        else:
                            lines.append("Press 's' to scan for spas")
                            self._commands["s"] = self._clear_spa

            else:

                # Spa isn't ready yet, but ...
                if False:
                    if not self._facade.name == "":
                        lines.append(f"{self._facade.name} is connecting")
                        lines.append("")
                    lines.append(f"{self._facade.facade_status_sensor.state}")

            lines.append("")
            if False:
                if self._facade.spa is not None:
                    if self._facade.is_ready:
                        lines.append("Press 'b' to toggle blower")
                        if self._facade.blowers[0].is_on:
                            self._commands["b"] = self._facade.blowers[0].async_turn_off
                        else:
                            self._commands["b"] = self._facade.blowers[0].async_turn_on

                        lines.append("Press '+' to increase setpoint")
                        self._commands["+"] = self.increase_temp
                        lines.append("Press '-' to decrease setpoint")
                        self._commands["-"] = self.decrease_temp

                    lines.append("Press 's' to rescan")
                    self._commands["s"] = self._clear_spa
                    lines.append("Press 'r' to reconnect to spa")
                    self._commands["r"] = self._facade.reconnect_spa

            if self.spa_state == GeckoSpaState.ERROR_SPA_NOT_FOUND:
                lines.append("Press 'r' to reconnect")
                self._commands["r"] = self.async_reset

            if self._config.spa_id is not None:
                lines.append("Press 's' to scan for spas")
                self._commands["s"] = self._clear_spa
            # if self.spa_state == GeckoSpaState.CONNECTED:
            #    lines.append("Press 'r' to reconnect to spa")
            #    self._commands["r"] = self._facade.reconnect_spa
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
                f"{datetime.now():%x %X} - Status: {self}",
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

    async def handle_char(self, char: int) -> None:
        cmd = chr(char)
        if cmd in self._commands:
            func = self._commands[cmd]
            if inspect.iscoroutinefunction(func):
                await func()
            elif isinstance(func, tuple):
                func, *parms = func
                if inspect.iscoroutinefunction(func):
                    await func(*parms)
            else:
                func()
        self._last_char = char
