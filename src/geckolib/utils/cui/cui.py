"""
Complete sample client CUI - Console User Interface.

All the code to drive the CUI is in this file, it should only
talk to the facade as it is the example of how to integrate
geckolib into an automation system.
"""

import _curses
import asyncio
import curses
import curses.textpad
import logging
from datetime import UTC, datetime
from typing import Any, Self

from geckolib import (
    GeckoAsyncSpaDescriptor,
    GeckoAsyncSpaMan,
    GeckoConstants,
    GeckoSpaEvent,
)
from geckolib.automation.light import GeckoLight
from geckolib.automation.pump import GeckoPump
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
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
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
        self._lines: list[str | tuple[str, int]] = []

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
            raise
        except Exception:
            _LOGGER.exception("Timer loop caught exception")
            raise

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

    async def _device_click(self, device: GeckoPump | GeckoLight) -> None:
        _LOGGER.debug("Device %s clicked", device)
        try:
            if device.is_on:
                await device.async_turn_off()
            else:
                await device.async_turn_on()
        except Exception:
            _LOGGER.exception("Exception during click")

    def _located_spas(self, maxy: int, maxx: int) -> None:
        if self.spa_descriptors is None:
            return

        no_of_spas = len(self.spa_descriptors)
        if no_of_spas == 0:
            self._lines.append(
                (
                    "No spas were found on your network",
                    curses.color_pair(1),
                )
            )
            return

        buttons_height = no_of_spas * 3

        for idx, spa in enumerate(self.spa_descriptors):
            button_text = f"{idx + 1}. {spa.name} at {spa.ipaddress}"
            self.add_button(
                int((maxy - buttons_height) / 2) + (idx * 3),
                int(maxx / 2) - int(len(button_text) / 2) - 2,
                button_text,
                f"{idx + 1}",
                (self._select_spa, spa),
            )

    def _spa_problem(self) -> None:
        self._lines.append((f"{self.spa_name} not ready", curses.color_pair(1)))
        self._lines.append("")
        self._lines.append(f"{self.ping_sensor}")
        self._lines.append(f"{self.radio_sensor}")
        self._lines.append(f"{self.channel_sensor}")
        self._lines.append("")

        if self.spa_state == GeckoSpaState.ERROR_RF_FAULT:
            self._lines.append(
                (
                    "Lost contact with your spa, it looks as if it is turned off",
                    curses.color_pair(1),
                )
            )
        if self.spa_state == GeckoSpaState.ERROR_PING_MISSED:
            self._lines.append(
                (
                    "Lost contact with your intouch2 module, please investigate",
                    curses.color_pair(1),
                )
            )

    def _build_facade_ui(self, _maxy: int, maxx: int) -> None:  # noqa: PLR0912
        if self.facade is None:
            return
        curx = 2
        cury = 1
        button_line = []

        for device in list(
            self.facade.pumps
            + self.facade.blowers
            + self.facade.lights
            + self.facade.switches
        ):
            device_button = self.add_button(
                cury,
                curx,
                [device.name, device.state],
                None,
                (self._device_click, device),
            )
            if device_button.x + device_button.width > maxx - 2:
                delta = int(((maxx - 2) - curx) / 2)
                for moveit in button_line:
                    moveit.move(moveit.y, moveit.x + delta)
                button_line = []
                curx = 2
                cury += 4
                device_button.move(cury, curx)
            curx += device_button.width + 1
            button_line.append(device_button)

        delta = int(((maxx - 2) - curx) / 2)
        for moveit in button_line:
            moveit.move(moveit.y, moveit.x + delta)

        if self.facade.mrsteam.is_available:
            self._lines.append("We have a Mr Steam unit")
            self._lines.append("")

        if self.facade.water_heater.is_available:
            self._lines.append(f"{self.facade.water_heater}")
        if self.facade.inmix.is_available:
            self._lines.extend(f"{zone}" for zone in self.facade.inmix.zones)
            if self.facade.inmix.syncro.is_available:
                self._lines.append(f"{self.facade.inmix.syncro}")
        if self.facade.reminders_manager.is_available:
            self._lines.extend(
                f"{reminder}" for reminder in self.facade.reminders_manager.reminders
            )
        # if self.facade.water_care.is_available:
        if self.facade.water_care.is_available:
            self._lines.append(f"{self.facade.water_care}")
        if self.facade.heatpump.is_available:
            self._lines.append(f"{self.facade.heatpump}")
        if self.facade.ingrid.is_available:
            self._lines.append(f"{self.facade.ingrid}")
        if self.facade.lockmode.is_available:
            self._lines.append(f"{self.facade.lockmode}")
        self._lines.extend(
            f"{sensor}"
            for sensor in [
                *self.facade.sensors,
                *self.facade.binary_sensors,
            ]
        )
        if self.facade.eco_mode is not None:
            self._lines.append(f"{self.facade.eco_mode}")
        self._lines.append(
            f"{self.ping_sensor} (Responding: {self._spa.is_responding_to_pings})"
        )
        self._lines.append(f"{self.radio_sensor}")
        self._lines.append(f"{self.channel_sensor}")
        self._lines.append(f"{self.facade.error_sensor}")
        self._lines.append(f"{self.facade.spa_in_use_sensor}")

    def make_display(self) -> None:
        """Make a display."""
        try:
            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.box()

            title = (
                f"{self.facade.name} is ready"
                if self._can_use_facade
                else "Gecko Async Sample App"
            )
            self.stdscr.addstr(0, int((maxx - len(title)) / 2), title)

            self._lines = []

            if self._can_use_facade:
                self._build_facade_ui(maxy, maxx)

            elif self.spa_state == GeckoSpaState.LOCATED_SPAS:
                self._located_spas(maxy, maxx)

            elif self.spa_state in (
                GeckoSpaState.ERROR_RF_FAULT,
                GeckoSpaState.ERROR_PING_MISSED,
                GeckoSpaState.ERROR_NEEDS_ATTENTION,
            ):
                self._spa_problem()

            self._lines.append("")

            if self._can_use_facade:
                assert self.facade is not None  # noqa: S101
                self._lines.append("Press '+' to increase setpoint")
                self._commands["+"] = self.increase_temp
                self._lines.append("Press '-' to decrease setpoint")
                self._commands["-"] = self.decrease_temp
                self._lines.append("Press 'w' to select next watercare mode")
                self._commands["w"] = self._select_next_watercare_mode

            #       ┌──────┐
            #       │ eXit │
            #       └──────┘
            _exit_button = self.add_button(
                maxy - 4, maxx - 10, "eXit", "x", self.set_exit
            )

            #       ┌─────────┐    ┌─────────────┐
            #       │ Re-scan │ or │ Re-connnect │
            #       └─────────┘    └─────────────┘
            reset_text = (
                "Re-scan"
                if self.spa_state
                in (
                    GeckoSpaState.LOCATING_SPAS,
                    GeckoSpaState.LOCATED_SPAS,
                )
                and self._config.spa_id is None
                else "Re-connect"
            )
            _reset_button = self.add_button(
                maxy - 4,
                _exit_button.x - len(reset_text) - 5,
                reset_text,
                "r",
                self.async_reset,
            )

            #       ┌───────────┐
            #       │ Clear Spa │
            #       └───────────┘
            if self._config.spa_id is not None:
                _clear_spa = self.add_button(
                    maxy - 4, _reset_button.x - 14, "Clear Spa", "c", self._clear_spa
                )

            # Lines of data centred

            half = int(len(self._lines) / 2)

            for idx, line in enumerate(self._lines):
                attr: int = curses.A_NORMAL
                text: str = line
                if isinstance(line, tuple):
                    attr = int(line[1])
                    text = line[0]
                self.stdscr.addstr(
                    int(maxy / 2) - half + idx, int((maxx - len(text)) / 2), text, attr
                )

            # Status liine
            self.stdscr.addstr(
                maxy - 2,
                1,
                f"{datetime.now(tz=UTC):%x %X} - {self}",
            )

        except _curses.error:
            # If window gets too small, we won't output anything
            _LOGGER.warning("Window too small")
            self.stdscr.erase()
            self.stdscr.addstr("Window too small")

        except Exception:
            _LOGGER.exception("During make display")
