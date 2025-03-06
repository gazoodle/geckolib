"""
Abstract curses display class for use in asyncio app.

Thanks to https://gist.github.com/davesteele/8838f03e0594ef11c89f77a7bca91206
"""

import _curses
import asyncio
import curses
import inspect
import logging
from abc import ABC, abstractmethod
from collections.abc import Callable
from curses import ERR, KEY_MOUSE, KEY_RESIZE, curs_set, getmouse
from typing import Any, cast

from geckolib import GeckoAsyncTaskMan

_LOGGER = logging.getLogger(__name__)


class Button:
    """A button wrapper."""

    def __init__(  # noqa: PLR0913
        self,
        stdscr: _curses.window,
        y: int,
        x: int,
        text: str | list[str],
        char: str | None,
        command: Callable | tuple[Callable, Any] | None,
    ) -> None:
        """Initialize the button."""
        self.stdscr = stdscr
        self.y = y
        self.x = x
        self.text: list[str] = text if isinstance(text, list) else [text]
        self.char = char
        self.command = command

        self.width = max([len(t) for t in self.text]) + 4
        self.height = len(self.text) + 2
        self.window = None

    def _create_window(self) -> None:
        if self.window is None:
            self.window = self.stdscr.subwin(self.height, self.width, self.y, self.x)

    def make(self, attr: int = curses.A_NORMAL) -> None:
        """Make the curses objects."""
        self._create_window()
        if self.window is None:
            return
        self.window.erase()
        self.window.box()
        for idx, txt in enumerate(self.text):
            self.window.addstr(idx + 1, int((self.width - len(txt)) / 2), txt, attr)
        self.window.refresh()

    def is_in_button(self, y: int, x: int) -> bool:
        """Test if point is in the button."""
        self._create_window()
        if self.window is None:
            return False
        return self.window.enclose(y, x)

    def move(self, new_y: int, new_x: int) -> None:
        """Move the button to a new location."""
        self.y = new_y
        self.x = new_x
        if self.window is None:
            return
        self.window.mvderwin(new_y, new_x)
        self.window.mvwin(new_y, new_x)

    def __str__(self) -> str:
        """Stringize the button."""
        return (
            f"Button ({self.text} with '{self.char}') at ({self.y},"
            f" {self.x}, {self.height}, {self.width})"
        )


class AbstractDisplay(ABC):
    """Abstract display class."""

    def __init__(self, stdscr: _curses.window) -> None:
        """Initialize the class."""
        self.stdscr = stdscr
        self.done_event = asyncio.Event()
        self.queue = asyncio.Queue(5)

        # Enable mouse events
        curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

        # https://stackoverflow.com/questions/56300134/how-to-enable-mouse-movement-events-in-curses#64809709
        print("\033[?1003h")  # enable mouse tracking with the XTERM API  # noqa: T201
        # https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Mouse-Tracking

        # Temp waiting to get replaced
        self._commands = {}
        self._buttons: list[Button] = []

        self._last_x = 0
        self._last_y = 0
        self._last_button = None

    @abstractmethod
    def make_display(self) -> None:
        """Make a display."""

    async def execute(self, func: Any) -> None:
        """Execute a function, or unpack and execute a function tuple."""
        try:
            if func is None:
                return
            if isinstance(func, Button):
                await self.execute(cast(Button, func).command)
                return
            if inspect.iscoroutinefunction(func):
                await func()
            elif isinstance(func, tuple):
                func, *parms = func
                if inspect.iscoroutinefunction(func):
                    await func(*parms)
                else:
                    func(*parms)
            else:
                func()
        except Exception:
            _LOGGER.exception("Exception during execute %s", func)
            raise

    async def handle_char(self, char: int) -> None:
        """Handle a command character."""
        cmd = chr(char)
        if cmd in self._commands:
            await self.execute(self._commands[cmd])

    def _get_button(self, y: int, x: int) -> Button | None:
        for button in self._buttons:
            if button.is_in_button(y, x):
                return button
        return None

    async def handle_mouse(self, mouse: tuple[int, int, int, int, int]) -> None:
        """Handle the mouse events."""
        _id, x, y, z, bstate = mouse
        self._last_x = x
        self._last_y = y
        button = self._get_button(y, x)
        if button is not None:
            if (
                bstate & curses.BUTTON1_PRESSED == curses.BUTTON1_PRESSED
                or bstate & curses.BUTTON1_CLICKED == curses.BUTTON1_CLICKED
                or bstate & curses.BUTTON1_DOUBLE_CLICKED
                == curses.BUTTON1_DOUBLE_CLICKED
            ):
                await self.execute(button.command)

            if button is not self._last_button:
                button.make(curses.A_BOLD)
                self._last_button = button

        elif self._last_button is not None:
            self._last_button.make()
            self._last_button = None

    def refresh(self) -> None:
        """Refesh the display."""
        self._commands = {}
        self._buttons = []
        self._last_button = None
        self.stdscr.erase()
        self.make_display()
        for button in self._buttons:
            button.make(
                curses.A_BOLD
                if button.is_in_button(self._last_y, self._last_x)
                else curses.A_NORMAL
            )
        self.stdscr.refresh()

    def set_exit(self) -> None:
        """Indicate we can exit."""
        self.done_event.set()

    async def enqueue_input(self) -> None:
        """Get input and queue it up."""
        try:
            while not self.done_event.is_set():
                char = self.stdscr.getch()
                await self.queue.put(char)
        except asyncio.CancelledError:
            _LOGGER.debug("CUI enqueue loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("CUI enqueue loop caught exception")
            raise

    async def process_input(self) -> None:
        """Get queue data and process it."""
        try:
            while not self.done_event.is_set():
                try:
                    char = await self.queue.get()
                    if char == ERR:
                        # Do nothing and let the loop continue without sleeping
                        pass
                    elif char == KEY_RESIZE:
                        self.refresh()
                    elif char == KEY_MOUSE:
                        await self.handle_mouse(getmouse())
                    else:
                        await self.handle_char(char)
                    self.queue.task_done()

                except asyncio.CancelledError:
                    _LOGGER.debug("Input loop cancelled")
                    raise

                except Exception:
                    _LOGGER.exception("Exception in input loop, ignored and continuing")

        finally:
            _LOGGER.debug("Input loop finished")

    async def run(self, taskman: GeckoAsyncTaskMan) -> None:
        """Run the display class."""
        curs_set(0)
        self.stdscr.nodelay(True)  # noqa: FBT003

        self.refresh()

        taskman.add_task(self.enqueue_input(), "Input gather", "CUI")
        taskman.add_task(self.process_input(), "Process input", "CUI")
        await self.done_event.wait()
        taskman.cancel_key_tasks("CUI")

    def add_text_box(
        self, y: int, x: int, text: str | list[str]
    ) -> tuple[int, int, int, int]:
        """Add a text box."""
        if isinstance(text, str):
            text = [text]
        width = max([len(t) for t in text]) + 2
        height = len(text)

        self.stdscr.addstr(y, x, f"┌{'─' * width}┐")
        for idx, line in enumerate(text):
            self.stdscr.addstr(y + 1 + idx, x, f"│ {line} │")
        self.stdscr.addstr(y + 1 + height, x, f"└{'─' * width}┘")
        return (y, x, height + 2, width + 2)

    def add_button(
        self,
        y: int,
        x: int,
        text: str | list[str],
        char: str | None,
        command: Callable | tuple[Callable, Any] | None,
    ) -> Button:
        """Add a button to the window."""
        button = Button(self.stdscr, y, x, text, char, command)
        self._buttons.append(button)
        if char is not None:
            self._commands[char] = button
        return button

    def add_line(self, y: int, x: int, text: str) -> None:
        """Add a text line."""
        self.stdscr.addstr(y, x, text)
