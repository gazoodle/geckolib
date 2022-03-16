""" Abstract curses display class for use in asyncio app - Thanks to https://gist.github.com/davesteele/8838f03e0594ef11c89f77a7bca91206 """

import asyncio
from abc import ABC, abstractmethod
from curses import ERR, KEY_RESIZE, curs_set
from context import GeckoConstants  # type: ignore

import _curses


class AbstractDisplay(ABC):
    def __init__(self, stdscr: "_curses._CursesWindow"):
        self.stdscr = stdscr
        self.done: bool = False

    @abstractmethod
    def make_display(self) -> None:
        pass

    @abstractmethod
    async def handle_char(self, char: int) -> None:
        pass

    def set_exit(self) -> None:
        self.done = True

    async def run(self) -> None:
        curs_set(0)
        self.stdscr.nodelay(True)

        self.make_display()

        while not self.done:
            char = self.stdscr.getch()
            if char == ERR:
                await asyncio.sleep(GeckoConstants.ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD)
            elif char == KEY_RESIZE:
                self.make_display()
            else:
                await self.handle_char(char)
