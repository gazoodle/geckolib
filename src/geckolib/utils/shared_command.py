"""Shared command functionality."""

import asyncio
import cmd
import logging
import sys
from enum import member
from importlib.metadata import files
from typing import Self

from geckolib.async_taskman import GeckoAsyncTaskMan
from geckolib.config import set_config_mode

_LOGGER = logging.getLogger(__name__)

LICENSE = """
#
#   Copyright (C) 2020, Gazoodle (https://github.com/gazoodle)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""


class GeckoCmd(cmd.Cmd):
    """
    Shared command processor.

    Implements shared functionality between the Shell and the Simulator

    This version is now async.
    """

    BANNER = None

    @classmethod
    def run(cls, first_commands: list[str] | None = None) -> None:
        """Run command loop."""
        asyncio.run(cls.async_run(first_commands))

    @classmethod
    async def async_run(cls, first_commands: list[str] | None = None) -> None:
        _LOGGER.debug("*** Shell %s started ***", cls.__name__)
        set_config_mode(True)
        async with cls() as cmd:
            if first_commands is not None:
                for command in first_commands:
                    cmd.push_command(command)
            await cmd.cmdloop()
        _LOGGER.debug("*** Shell %s stopped ***", cls.__name__)

    def __init__(self, taskman: GeckoAsyncTaskMan) -> None:
        """Initialize the command class."""
        cmd.Cmd.__init__(self)
        self._taskman = taskman

        if self.BANNER is not None:
            print(self.BANNER)

        self.stream_logger = None
        self.file_logger = None
        self._init_logging()

    async def __aenter__(self) -> Self:
        """Async enter for with statement."""
        await GeckoAsyncTaskMan.__aenter__(self)
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        """Support for 'with'."""
        await GeckoAsyncTaskMan.__aexit__(self, exc_info)

    def push_command(self, cmd: str) -> None:
        """Add a command to the queue."""
        self.cmdqueue.append(cmd)

    def do_exit(self, _arg: str) -> bool:
        """Exit this shell: exit."""
        return True

    def do_loglevel(self, arg) -> None:
        """Set the logging level : loglevel <ERROR|WARNING|INFO|DEBUG>."""
        for handler in logging.getLogger().handlers:
            handler.setLevel(arg)
        self._set_root_log_level()

    def do_logfile(self, arg: str) -> None:
        """Add a file logger to the system : logfile <filename>."""
        if self.file_logger is not None:
            print("There is already a file logger installed")
            return
        self.file_logger = logging.FileHandler(arg)
        self.file_logger.setLevel(logging.DEBUG)
        self.file_logger.setFormatter(
            logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        )
        logging.getLogger().addHandler(self.file_logger)
        self._set_root_log_level()

    async def do_async(self, arg: str) -> None:
        """Async test function."""
        print("Start async task, wait for 1 second")
        await asyncio.sleep(1)
        print("Async sleep complete")

    def _init_logging(self) -> None:
        self.stream_logger = logging.StreamHandler()
        self.stream_logger.setLevel(logging.WARNING)
        self.stream_logger.setFormatter(
            logging.Formatter("LOG> %(levelname)s %(message)s")
        )
        logging.getLogger().addHandler(self.stream_logger)
        self._set_root_log_level()

    def _set_root_log_level(self) -> None:
        # Set root log level
        logging.getLogger().setLevel(
            min(handler.level for handler in logging.getLogger().handlers)
        )

    def do_license(self, _arg: str) -> None:
        """Display the license details : license."""
        print(LICENSE)

    def emptyline(self) -> None:
        """Call when an empty line is entered in response to the prompt."""

    async def onecmd(self, line: str) -> bool:
        """
        Async single command.

        Interpret the argument as though it had been typed in response to the prompt.

        This may be overridden, but should not normally need to be;
        see the precmd() and postcmd() methods for useful execution hooks.
        The return value is a flag indicating whether interpretation of
        commands by the interpreter should stop.

        Support async commands.
        """
        _LOGGER.debug("Handle command `%s`", line)
        cmd, arg, line = self.parseline(line)
        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default(line)
        self.lastcmd = line
        if line == "EOF":
            self.lastcmd = ""
        if cmd == "":
            return self.default(line)
        func = getattr(self, "do_" + cmd, None)
        if func is None:
            return self.default(line)
        if asyncio.iscoroutinefunction(func):
            return await func(arg)
        return func(arg)

    async def _input(self, string: str) -> str:
        _LOGGER.debug("Prompt is %s", string)
        await asyncio.get_event_loop().run_in_executor(
            None, lambda s=string: sys.stdout.write(s + " ")
        )

        await asyncio.get_event_loop().run_in_executor(None, sys.stdout.flush)

        return await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)

    async def cmdloop(self, intro=None):
        """
        Async command loop.

        Repeatedly issue a prompt, accept input, parse an initial prefix
        off the received input, and dispatch to action methods, passing them
        the remainder of the line as argument.
        """
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                import readline

                self.old_completer = readline.get_completer()
                readline.set_completer(self.complete)
                if readline.backend == "editline":
                    if self.completekey == "tab":
                        # libedit uses "^I" instead of "tab"
                        command_string = "bind ^I rl_complete"
                    else:
                        command_string = f"bind {self.completekey} rl_complete"
                else:
                    command_string = f"{self.completekey}: complete"
                readline.parse_and_bind(command_string)
            except ImportError:
                pass
        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                self.stdout.write(str(self.intro) + "\n")
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0)
                else:
                    if self.use_rawinput:
                        try:
                            line = await self._input(self.prompt)
                        except EOFError:
                            line = "EOF"
                    else:
                        self.stdout.write(self.prompt)
                        self.stdout.flush()
                        line = self.stdin.readline()
                        if not len(line):
                            line = "EOF"
                        else:
                            line = line.rstrip("\r\n")
                line = self.precmd(line)
                stop = await self.onecmd(line)
                stop = self.postcmd(stop, line)
            self.postloop()
        finally:
            if self.use_rawinput and self.completekey:
                try:
                    import readline

                    readline.set_completer(self.old_completer)
                except ImportError:
                    pass
