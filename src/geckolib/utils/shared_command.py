"""Shared command functionality."""

# ruff: noqa: T201

import fnmatch
import glob
import logging
import os
from typing import TYPE_CHECKING

from geckolib.async_taskman import GeckoAsyncTaskMan
from geckolib.const import GeckoConstants

from .async_command import AsyncCmd

if TYPE_CHECKING:
    from geckolib.driver import GeckoStructAccessor
    from geckolib.driver.async_spastruct import GeckoAsyncStructure

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


class GeckoCmd(AsyncCmd):
    """
    Shared command processor.

    Implements shared functionality between the Shell and the Simulator

    This version is now async.
    """

    BANNER = None

    @classmethod
    def run(cls, first_commands: list[str] | None = None) -> None:
        """Run command loop."""
        with cls() as cmd:  # type: ignore  # noqa: PGH003
            if first_commands is not None:
                for command in first_commands:
                    cmd.push_command(command)
            cmd.cmdloop()

    def __init__(self, taskman: GeckoAsyncTaskMan) -> None:
        """Initialize the command class."""
        super().__init__()
        self._taskman = taskman

        if self.BANNER is not None:
            print(self.BANNER)

        self.stream_logger = None
        self.file_logger = None
        self._init_logging()

        self.structure: GeckoAsyncStructure | None = None
        self.running_set_command: bool = False

    def push_command(self, cmd: str) -> None:
        """Add a command to the queue."""
        self.cmdqueue.append(cmd)

    def do_loglevel(self, arg: str) -> None:
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

    def do_get(self, arg: str) -> None:
        """
        Get the value of the specified spa pack structure element.

        Usage: get <Element>
        """
        if self.structure is None:
            print("No access to the spa structure")
            return
        try:
            print(self.structure.accessors[arg].diag_info())
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception getting '%s'", arg)

    def _accessor_list(self, pattern: str) -> list[str]:
        if self.structure is None:
            return []
        keys = self.structure.accessors.keys()
        if not pattern:
            pattern = ""
        if not pattern.endswith("?"):
            pattern = pattern + "*"
        return fnmatch.filter(keys, pattern)

    def complete_get(
        self, text: str, _line: int, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the get command."""
        return self._accessor_list(text)

    def do_accessors(self, pattern: str) -> None:
        """
        Display the values from the accessors.

        Usage: accessors [pattern] where pattern is case sensitive
        text with * and ? wildcards
        """
        if self.structure is None:
            print("No access to the spa structure")
            return
        print("Accessors")
        print("=========")
        print()
        for key in self._accessor_list(pattern):
            print(f"   {self.structure.accessors[key]!r}")
        print()

    def complete_accessors(
        self, text: str, _line: int, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the accessors command."""
        return self._accessor_list(text)

    def do_peek(self, arg: str) -> None:
        """
        Get the byte value from the structure at the specified position.

        Usage: peek <pos>
        """
        if self.structure is None:
            print("No access to the spa structure")
            return
        try:
            pos = int(arg)
            print(
                f"Byte at {pos} = {self.structure.status_block[pos]} (\\x{self.structure.status_block[pos]:x})"  # noqa: E501
            )
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception peeking at '%s'", arg)

    async def do_set(self, arg: str) -> None:
        """
        Set the value of the specified spa pack structure element.

        Usage: set <Element>=<value>
        """
        if self.structure is None:
            print("No access to the spa structure")
            return
        self.running_set_command = True
        try:
            key, val = arg.split("=")
            await self.structure.accessors[key].async_set_value(val)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception handling 'set %s'", arg)
        finally:
            self.running_set_command = False

    def complete_set(
        self, text: str, _line: int, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the set command."""
        if "=" not in text:
            return self._accessor_list(text)
        key, val = text.split("=")
        if self.structure is None:
            return []
        if key not in self.structure.accessors:
            return []
        accessor: GeckoStructAccessor = self.structure.accessors[key]
        if accessor.accessor_type != GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            return []
        return [f"{key}={item}" for item in accessor.items if item.startswith(val)]

    def do_hexdump(self, _arg: str) -> None:
        """Hex dump of the raw structure status block."""
        if self.structure is None:
            print("No access to the spa structure")
            return

        width = 16
        data = self.structure.status_block

        lines = []
        for i in range(0, len(data), width):
            chunk = data[i : i + width]
            hex_values = " ".join(f"{b:02x}" for b in chunk)
            # Split hex values into two parts with an extra space in the middle
            left_hex = hex_values[:23]  # 8 hex octets + 7 spaces = 23 characters
            right_hex = hex_values[23:]  # The rest
            formatted_hex = f"{left_hex} {right_hex}"
            printable = "".join((chr(b) if 32 <= b < 127 else ".") for b in chunk)  # noqa: PLR2004
            lines.append(f"{i:08x}  {formatted_hex:<{width * 3 + 1}}  {printable}")

        print("Status block")
        print("\n".join(lines))

    def do_snapshot(self, arg: str) -> None:
        """
        Take a snapshot of the spa data structure.

        Supply an option description to help identify
        the state of the spa at this time.

        usage: snapshot <desc>
        """
        data = self.get_snapshot_data()
        if arg:
            data["Description"] = arg
        _LOGGER.info(f"SNAPSHOT ========{data}========")  # noqa: G004
        print(data)

    def _complete_path(self, path: str) -> list[str]:
        if os.path.isdir(path):  # noqa: PTH112
            return glob.glob(os.path.join(path, "*"))  # noqa: PTH118, PTH207
        return glob.glob(path + "*")  # noqa: PTH207

    def do_pack(self, _args: str) -> None:
        """List pack info."""
        print(f"Outputs {self.structure.all_outputs}")
        print(f"Connections: {self.structure.connections}")
        print(f"All Devices: {self.structure.all_devices}")
        print(f"Error Keys: {self.structure.error_keys}")
        print(f"User Demands: {self.structure.user_demands}")
