"""Abstract curses display class for use in asyncio app."""

"""Thanks to https://gist.github.com/davesteele/8838f03e0594ef11c89f77a7bca91206"""

import _curses
import asyncio
from abc import ABC, abstractmethod
from curses import ERR, KEY_RESIZE, curs_set

from context_sample import GeckoConstants  # type: ignore


class AbstractDisplay(ABC):
    """Abstract display class."""

    def __init__(self, stdscr: "_curses._CursesWindow") -> None:  # type: ignore
        """Initialize the class."""
        self.stdscr = stdscr
        self.done_event = asyncio.Event()
        self.queue = asyncio.Queue(5)

    @abstractmethod
    def make_display(self) -> None:
        """Make a display."""

    @abstractmethod
    async def handle_char(self, char: int) -> None:
        """Handle a character."""

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
        while not self.done_event.is_set():
            char = await self.queue.get()
            if char == ERR:
                # Do nothing and let the loop continue without sleeping continue
                pass
            elif char == KEY_RESIZE:
                self.make_display()
            else:
                await self.handle_char(char)
            self.queue.task_done()

    async def run(self) -> None:
        """Run the display class."""
        curs_set(0)
        self.stdscr.nodelay(True)

        self.make_display()

        input_task = asyncio.create_task(self.enqueue_input())
        process_task = asyncio.create_task(self.process_input())

        await asyncio.gather(input_task, process_task)
