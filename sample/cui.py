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
from context_sample import (  # type: ignore
    GeckoAsyncSpaMan,
    GeckoSpaEvent,
    GeckoAsyncSpaDescriptor,
    GeckoConstants,
    GeckoConfig,
)
from typing import Optional

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

        self._last_update = time.monotonic()
        self._last_char = None
        self._commands = {}
        self._watching_ping_sensor = False

        # Various flags based on the SpaMan events to simulate an
        # automation client
        self._can_use_facade = False

    async def __aenter__(self):
        await GeckoAsyncSpaMan.__aenter__(self)
        self.add_task(self._timer_loop(), "Timer", "CUI")
        await self.async_set_spa_info(
            self._config.spa_address, self._config.spa_id, self._config.spa_name
        )
        await self.run()
        return self

    async def __aexit__(self, *exc_info):
        return await GeckoAsyncSpaMan.__aexit__(self, *exc_info)

    async def _timer_loop(self) -> None:
        while True:
            self.make_display()
            await asyncio.sleep(1)

    async def handle_event(self, event: GeckoSpaEvent, **kwargs) -> None:
        # Always rebuild the UI when there is an event
        _LOGGER.debug(f"{event} : {self.spa_state}")
        if event == GeckoSpaEvent.CLIENT_FACADE_IS_READY:
            self._can_use_facade = True
        elif event in (
            GeckoSpaEvent.CLIENT_FACADE_TEARDOWN,
            GeckoSpaState.ERROR_NEEDS_ATTENTION,
        ):
            self._can_use_facade = False

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

    async def _select_next_watercare_mode(self) -> None:
        assert self.facade is not None
        assert self.facade.water_care is not None
        new_mode = (self.facade.water_care.active_mode + 1) % len(
            GeckoConstants.WATERCARE_MODE
        )
        await self.facade.water_care.async_set_mode(new_mode)

    def make_title(self, maxy: int, maxx: int) -> None:
        title = "Gecko Async Sample App"
        self.stdscr.addstr(0, int((maxx - len(title)) / 2), title)

    async def increase_temp(self):
        await self.facade.water_heater.async_set_target_temperature(
            self.facade.water_heater.target_temperature + 0.5
        )

    async def decrease_temp(self):
        await self.facade.water_heater.async_set_target_temperature(
            self.facade.water_heater.target_temperature - 0.5
        )

    def make_display(self) -> None:
        try:
            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.erase()
            self.stdscr.box()

            self.make_title(maxy, maxx)

            lines = []
            self._commands = {}

            if self._can_use_facade:

                assert self.facade is not None
                lines.append(f"{self.facade.name} is ready")
                lines.append("")
                lines.append(f"{self.facade.water_heater}")
                for pump in self.facade.pumps:
                    lines.append(f"{pump}")
                for blower in self.facade.blowers:
                    lines.append(f"{blower}")
                for light in self.facade.lights:
                    lines.append(f"{light}")
                for reminder in self.facade.reminders_manager.reminders:
                    lines.append(f"{reminder}")
                lines.append(f"{self.facade.water_care}")
                for sensor in [
                    *self.facade.sensors,
                    *self.facade.binary_sensors,
                ]:
                    lines.append(f"{sensor}")
                lines.append(f"{self.facade.eco_mode}")
                lines.append(f"{self.ping_sensor}")
                lines.append(f"{self.radio_sensor}")
                lines.append(f"{self.channel_sensor}")
                lines.append(f"{self.facade.error_sensor}")

            else:

                if self.spa_state == GeckoSpaState.LOCATED_SPAS:

                    if self.spa_descriptors is not None:
                        # If the _spas property is available, that means we've got
                        # a list of spas that we can choose from
                        for idx, spa in enumerate(self.spa_descriptors, start=1):
                            lines.append(f"{idx}. {spa.name} at {spa.ipaddress}")
                            self._commands[f"{idx}"] = (self._select_spa, spa)

                        if len(self.spa_descriptors) == 0:
                            lines.append("No spas were found on your network")

                elif self.spa_state == GeckoSpaState.CONNECTED:
                    lines.append(f"{self.spa_name} connecting")
                    lines.append(f"{self.ping_sensor}")
                    lines.append(f"{self.radio_sensor}")
                    lines.append(f"{self.channel_sensor}")
                    lines.append("")

                elif self.spa_state == GeckoSpaState.ERROR_RF_FAULT:

                    lines.append(f"{self.spa_name} not ready")
                    lines.append(f"{self.ping_sensor}")
                    lines.append(f"{self.radio_sensor}")
                    lines.append(f"{self.channel_sensor}")
                    lines.append("")
                    lines.append(
                        "Lost contact with your spa, it looks as if it is turned off"
                    )

                elif self.spa_state == GeckoSpaState.ERROR_PING_MISSED:

                    lines.append(f"{self.spa_name} not ready")
                    lines.append(f"{self.ping_sensor}")
                    lines.append(f"{self.radio_sensor}")
                    lines.append(f"{self.channel_sensor}")
                    lines.append("")
                    lines.append(
                        "Lost contact with your intouch2 module, please investigate"
                    )

            lines.append("")

            if self._can_use_facade:
                assert self.facade is not None
                if self.facade.blowers:
                    lines.append("Press 'b' to toggle blower")
                    if self.facade.blowers[0].is_on:
                        self._commands["b"] = self.facade.blowers[0].async_turn_off
                    else:
                        self._commands["b"] = self.facade.blowers[0].async_turn_on
                if self.facade.pumps:
                    lines.append("Press 'p' to toggle pump 1")
                    if self.facade.pumps[0].mode == "OFF":
                        self._commands["p"] = (
                            self.facade.pumps[0].async_set_mode,
                            "HI",
                        )
                    else:
                        self._commands["p"] = (
                            self.facade.pumps[0].async_set_mode,
                            "OFF",
                        )

                lines.append("Press '+' to increase setpoint")
                self._commands["+"] = self.increase_temp
                lines.append("Press '-' to decrease setpoint")
                self._commands["-"] = self.decrease_temp
                lines.append("Press 'w' to select next watercare mode")
                self._commands["w"] = self._select_next_watercare_mode

            lines.append("Press 'r' to reconnect")
            self._commands["r"] = self.async_reset
            if self._config.spa_id is not None:
                lines.append("Press 's' to scan for spas")
                self._commands["s"] = self._clear_spa
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
                f"{datetime.now():%x %X} - {self}",
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
