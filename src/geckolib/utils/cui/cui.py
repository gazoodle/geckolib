"""
Complete sample client CUI - Console User Interface.

All the code to drive the CUI is in this file, it should only
talk to the facade as it is the example of how to integrate
geckolib into an automation system.
"""  # noqa: INP001

import _curses
import asyncio
import curses
import curses.textpad
import inspect
import logging
from datetime import UTC, datetime
from typing import Any, Self

from geckolib import (
    GeckoAsyncSpaDescriptor,
    GeckoAsyncSpaMan,
    GeckoConstants,
    GeckoSpaEvent,
)
from geckolib.config import config_sleep
from geckolib.spa_state import GeckoSpaState

from .abstract_display import AbstractDisplay
from .config import Config

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "1eca3a27-9b00-476a-9645-d13f4b1f9b56"


_LOGGER = logging.getLogger(__name__)


class CUI(AbstractDisplay, GeckoAsyncSpaMan):
    """The console UI implementation."""

    @staticmethod
    def launch() -> None:
        """Launch the CUI."""
        curses.wrapper(CUI.main)

    @staticmethod
    def main(stdscr: curses.window) -> None:
        """Run the async loop."""
        asyncio.run(
            CUI.async_main(stdscr),
        )

    @staticmethod
    async def async_main(stdscr: curses.window) -> None:
        """Async main manages the console UI."""
        task = asyncio.current_task()
        if task is not None:
            task.set_name("CUI main")
            async with CUI(stdscr):
                pass

    def __init__(self, stdscr: _curses.window) -> None:
        """Initialize the CUI class."""
        AbstractDisplay.__init__(self, stdscr)
        GeckoAsyncSpaMan.__init__(self, CLIENT_ID)

        self._config = Config()
        self._spas: GeckoAsyncSpaDescriptor | None = None

        # Various flags based on the SpaMan events to simulate an
        # automation client
        self._can_use_facade = False

    async def __aenter__(self) -> Self:
        """Async enter for with statement."""
        await GeckoAsyncSpaMan.__aenter__(self)
        self.add_task(self._timer_loop(), "Timer", "CUI")
        await self.async_set_spa_info(
            self._config.spa_address, self._config.spa_id, self._config.spa_name
        )
        await self.run(self)
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        """Async exit."""
        return await GeckoAsyncSpaMan.__aexit__(self, *exc_info)

    async def _timer_loop(self) -> None:
        try:
            while True:
                self.refresh()
                await config_sleep(1, "CUI Timer")
        except asyncio.CancelledError:
            _LOGGER.debug("Timer loop cancelled")
        except Exception:
            _LOGGER.exception("Timer loop caught exception")

    async def handle_event(self, event: GeckoSpaEvent, **_kwargs: Any) -> None:
        """Rebuild the UI when there is an event."""
        try:
            _LOGGER.debug(f"{event} : {self.spa_state}")  # noqa: G004
            if event == GeckoSpaEvent.CLIENT_FACADE_IS_READY:
                self._can_use_facade = True
            elif event in (
                GeckoSpaEvent.CLIENT_FACADE_TEARDOWN,
                GeckoSpaState.ERROR_NEEDS_ATTENTION,
            ):
                self._can_use_facade = False

            self.refresh()
        except Exception:
            _LOGGER.exception("Exception in handle event")

    async def _select_spa(self, spa: GeckoAsyncSpaDescriptor) -> None:
        self._config.set_spa_id(spa.identifier_as_string)
        self._config.set_spa_address(spa.ipaddress)
        self._config.set_spa_name(spa.name)
        self._config.save()
        await self.async_set_spa_info(spa.ipaddress, spa.identifier_as_string, spa.name)

    async def _clear_spa(self) -> None:
        """Clear spa data."""
        self._config.set_spa_id(None)
        self._config.set_spa_address(None)
        self._config.set_spa_name(None)
        self._config.save()
        await self.async_set_spa_info(None, None, None)

    async def _select_next_watercare_mode(self) -> None:
        assert self.facade is not None  # noqa: S101
        assert self.facade.water_care is not None  # noqa: S101
        new_mode = (self.facade.water_care.active_mode + 1) % len(
            GeckoConstants.WATERCARE_MODE
        )
        await self.facade.water_care.async_set_mode(new_mode)

    async def increase_temp(self) -> None:
        """Increase the setpoint."""
        await self.facade.water_heater.async_set_target_temperature(
            self.facade.water_heater.target_temperature + 0.5
        )

    async def decrease_temp(self) -> None:
        """Decrease the setpoint."""
        await self.facade.water_heater.async_set_target_temperature(
            self.facade.water_heater.target_temperature - 0.5
        )

    async def key_press(self, keypad: int) -> None:
        """Simulate keypress."""
        await self.facade.spa.async_press(keypad)
        self.make_display()

    def make_display(self) -> None:  # noqa: PLR0912, PLR0915
        """Make a display."""
        try:
            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.box()

            title = "Gecko Async Sample App"
            self.stdscr.addstr(0, int((maxx - len(title)) / 2), title)

            lines = []

            if self._can_use_facade:
                assert self.facade is not None  # noqa: S101
                lines.append(f"{self.facade.name} is ready")
                lines.append("")
                lines.append(f"{self.facade.water_heater}")
                lines.extend(f"{pump}" for pump in self.facade.pumps)
                lines.extend(f"{blower}" for blower in self.facade.blowers)
                lines.extend(f"{light}" for light in self.facade.lights)
                if self.facade.inmix.is_available:
                    lines.extend(f"{zone}" for zone in self.facade.inmix.zones)
                    if self.facade.inmix.syncro.is_available:
                        lines.append(f"{self.facade.inmix.syncro}")
                lines.extend(
                    f"{reminder}"
                    for reminder in self.facade.reminders_manager.reminders
                )
                lines.append(f"{self.facade.water_care}")
                if self.facade.heatpump.is_available:
                    lines.append(f"{self.facade.heatpump}")
                if self.facade.ingrid.is_available:
                    lines.append(f"{self.facade.ingrid}")
                if self.facade.lockmode.is_available:
                    lines.append(f"{self.facade.lockmode}")
                if self.facade.standby is not None:
                    lines.append(f"{self.facade.standby}")
                lines.extend(
                    f"{sensor}"
                    for sensor in [
                        *self.facade.sensors,
                        *self.facade.binary_sensors,
                    ]
                )
                lines.append(f"{self.facade.eco_mode}")
                lines.append(
                    f"{self.ping_sensor} (Responding: {self._spa.is_responding_to_pings})"  # noqa: E501
                )
                lines.append(f"{self.radio_sensor}")
                lines.append(f"{self.channel_sensor}")
                lines.append(f"{self.facade.error_sensor}")
                lines.append(f"{self.facade.spa_in_use_sensor}")

            elif self.spa_state == GeckoSpaState.LOCATED_SPAS:
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
                assert self.facade is not None  # noqa: S101
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
                    lines.append("Press '1' to simulate keypad 1 press")
                    self._commands["1"] = (self.key_press, GeckoConstants.KEYPAD_PUMP_1)

                lines.append("Press '+' to increase setpoint")
                self._commands["+"] = self.increase_temp
                lines.append("Press '-' to decrease setpoint")
                self._commands["-"] = self.decrease_temp
                lines.append("Press 'w' to select next watercare mode")
                self._commands["w"] = self._select_next_watercare_mode

            lines.append("Press 'r' to reset")
            self._commands["r"] = self.async_reset
            if self._config.spa_id is not None:
                lines.append("Press 's' to scan for spas")
                self._commands["s"] = self._clear_spa
            lines.append("Press 'f' to flash the screen")
            self._commands["f"] = curses.flash

            exit_button = self.add_button(
                maxy - 4, maxx - 10, "eXit", "x", self.set_exit
            )

            half = int(len(lines) / 2)

            for idx, line in enumerate(lines):
                self.stdscr.addstr(
                    int(maxy / 2) - half + idx, int((maxx - len(line)) / 2), line
                )

            self.stdscr.addstr(
                maxy - 2,
                1,
                f"{datetime.now(tz=UTC):%x %X} - {self}",
            )

            # self.stdscr.addstr(5, 2, "+----------+  ╔══════════╗  ┌──────────┐")
            # self.stdscr.addstr(6, 2, "| A Button |  ║ B Button ║  │ C Button │")
            # self.stdscr.addstr(7, 2, "+----------+  ╚══════════╝  └──────────┘")

            # self.add_line(1, 100, "[Line]")

            # self.add_text_box(1, 50, "Hello")
            # self.add_text_box(1, 80, ["One", "Two"])

            # subwin = self.stdscr.subwin(5, 30, 20, 80)
            # subwin.erase()
            # subwin.box()
            # tb = curses.textpad.Textbox(subwin)
            # tb.edit()
            # subwin.addstr(1, 1, "Box Hi!")

            b = self.add_button(
                1, 2, "Click Me!", "c", lambda: _LOGGER.debug("Clicked")
            )
            if self._can_use_facade:
                self.add_button(
                    1,
                    b.width + 4,
                    ["Pump 1", self.facade.pump_1.mode],
                    None,
                    (self.key_press, GeckoConstants.KEYPAD_PUMP_1),
                )

        except _curses.error:
            # If window gets too small, we won't output anything
            _LOGGER.warning("Window too small")
            self.stdscr.erase()
            self.stdscr.addstr("Window too small")
