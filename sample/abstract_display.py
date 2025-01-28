"""
Abstract curses display class for use in asyncio app.

Thanks to https://gist.github.com/davesteele/8838f03e0594ef11c89f77a7bca91206
"""

import _curses
import asyncio
import logging
from abc import ABC, abstractmethod
from curses import ERR, KEY_RESIZE, curs_set

from context_sample import GeckoAsyncTaskMan

_LOGGER = logging.getLogger(__name__)


class AbstractDisplay(ABC):
    """Abstract display class."""

    def __init__(self, stdscr: _curses.window) -> None:
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
        try:
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

        self.make_display()

        taskman.add_task(self.enqueue_input(), "Input gather", "CUI")
        taskman.add_task(self.process_input(), "Process input", "CUI")
        await self.done_event.wait()
        taskman.cancel_key_tasks("CUI")
