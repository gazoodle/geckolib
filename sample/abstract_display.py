"""
Abstract curses display class for use in asyncio app.

Thanks to https://gist.github.com/davesteele/8838f03e0594ef11c89f77a7bca91206
"""  # noqa: INP001

import _curses
import asyncio
import curses
import logging
from abc import ABC, abstractmethod
from curses import ERR, KEY_MOUSE, KEY_RESIZE, curs_set, getmouse

from context_sample import GeckoAsyncTaskMan

_LOGGER = logging.getLogger(__name__)


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

    @abstractmethod
    def make_display(self) -> None:
        """Make a display."""

    @abstractmethod
    async def handle_char(self, char: int) -> None:
        """Handle a character."""

    @abstractmethod
    async def handle_mouse(self, mouse: tuple[int, int, int, int, int]) -> None:
        """Handle the mouse."""

    def refresh(self) -> None:
        """Refesh the display."""
        self._commands = {}
        self.stdscr.erase()
        self.make_display()
        self.stdscr.refresh()

    def set_exit(self) -> None:
        """Indicagte we can exit."""
        self.done_event.set()

    async def enqueue_input(self) -> None:
        """Get input and queue it up."""
        while not self.done_event.is_set():
            char = self.stdscr.getch()
            await self.queue.put(char)

    async def process_input(self) -> None:
        """Get queue data and process it."""
        try:
            while not self.done_event.is_set():
                char = await self.queue.get()
                if char == ERR:
                    # Do nothing and let the loop continue without sleeping continue
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

        except:
            _LOGGER.exception("Exception in input loop")
            raise

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
        width = max([len(t) for t in text])
        height = len(text)

        self.stdscr.addstr(y, x, f"┌{'─' * width}┐")
        for idx, line in enumerate(text):
            self.stdscr.addstr(y + idx, x, f"│ {line} │")
        self.stdscr.addstr(y + height, x, f"└{'─' * width}┘")
        return (y, x, height + 2, width + 2)

    def add_button(
        self, y: int, z: int, text: str | list[str], char: int | None, click: int
    ) -> None:
        """Add a button to the window."""
        pos = self.add_text_box(y, z, text)

    def add_line(self, y: int, x: int, text: str) -> None:
        """Add a text line."""
        self.stdscr.addstr(y, x, text)
