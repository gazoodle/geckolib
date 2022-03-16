""" Shared command functionality """

import cmd
import logging

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
    """GeckoCmd is a shared command processor. It implements shared
    functionality between the Shell and the Simulator"""

    BANNER = None

    @classmethod
    def run(cls, first_commands=None):
        """Convenience function to run a command loop"""
        with cls(first_commands) as cmd:
            cmd.cmdloop()

    def __init__(self, first_commands=None):
        super().__init__()

        if self.BANNER is not None:
            print(self.BANNER)

        self.stream_logger = None
        self.file_logger = None
        self._init_logging()

        if first_commands is not None:
            for command in first_commands:
                self.onecmd(command)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def do_exit(self, _arg):
        """Exit this shell: exit"""
        return True

    def do_loglevel(self, arg):
        """Set the logging level : loglevel <ERROR|WARNING|INFO|DEBUG>"""
        for handler in logging.getLogger().handlers:
            handler.setLevel(arg)
        self._set_root_log_level()

    def do_logfile(self, arg):
        """Add a file logger to the system : logfile <filename>"""
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

    def _init_logging(self):
        self.stream_logger = logging.StreamHandler()
        self.stream_logger.setLevel(logging.WARNING)
        self.stream_logger.setFormatter(
            logging.Formatter("LOG> %(levelname)s %(message)s")
        )
        logging.getLogger().addHandler(self.stream_logger)
        self._set_root_log_level()

    def _set_root_log_level(self):
        # Set root log level
        logging.getLogger().setLevel(
            min(handler.level for handler in logging.getLogger().handlers)
        )

    def do_license(self, _arg):
        """Display the license details : license"""
        print(LICENSE)
