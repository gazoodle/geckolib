""" Snapshot helper """

import logging
import re
import os
from datetime import datetime

_LOGGER = logging.getLogger(__name__)

# Match "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Snapshot (Heating)",
RE_SNAPSHOT = r"(\d+-\d+-\d+\s+\d+:\d+:\d+).*Snapshot \((.*)\)"
# Match "INFO:geckolib.utils.shell:Snapshot (EconomyModeActive)",
RE_SNAPSHOT_ALT = r"Snapshot \((.*)\)"
# Match "Spa pack inXM 186 v3.0"
RE_SPA_PACK = r"Spa pack (.*) (\d+) v(\d+)\.(\d+)"
# Match "intouch version EN 88 v15.0"
RE_INTOUCH_EN = r"intouch version EN (\d+) v(\d+)\.(\d+)"
# Match "intouch version CO 89 v11.0"
RE_INTOUCH_CO = r"intouch version CO (\d+) v(\d+)\.(\d+)"
# Match "Config version 9"
RE_CONFIG_VERSION = r"Config version (\d+)"
# Match "Log version 9"
RE_LOG_VERSION = r"Log version (\d+)"
# Match "['0x5', '0x1', ... '0x0']"
RE_DATA_DUMP = r"\[('.*')\]"


class GeckoSnapshot:
    def __init__(self):
        self._lines = []
        self._name = None
        self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._pack_type = None
        self._pack_conf_id = None
        self._pack_conf_rev = None
        self._pack_conf_rel = None
        self._intouch_CO = None
        self._intouch_EN = None
        self._config_version = None
        self._log_version = None
        self._bytes = b""

    def parse(self, line: str):
        # Always bag the lines
        self._lines.append(line)
        # Search the interesting ones ...
        match = re.search(RE_SNAPSHOT, line, re.DOTALL)
        if match:
            (self._timestamp, self._name) = match.groups()
        match = re.search(RE_SNAPSHOT_ALT, line, re.DOTALL)
        if match:
            (self._name,) = match.groups()
        match = re.search(RE_SPA_PACK, line, re.DOTALL)
        if match:
            (
                self._pack_type,
                self._pack_conf_id,
                self._pack_conf_rev,
                self._pack_conf_rel,
            ) = match.groups()
        match = re.search(RE_INTOUCH_EN, line, re.DOTALL)
        if match:
            self._intouch_EN = match.groups()
        match = re.search(RE_INTOUCH_CO, line, re.DOTALL)
        if match:
            self._intouch_CO = match.groups()
        match = re.search(RE_CONFIG_VERSION, line, re.DOTALL)
        if match:
            self._config_version = match.group(1)
        match = re.search(RE_LOG_VERSION, line, re.DOTALL)
        if match:
            self._log_version = match.group(1)
        match = re.search(RE_DATA_DUMP, line, re.DOTALL)
        if match:
            self._bytes = bytes(
                bytearray([int(b.strip()[1:-1], 16) for b in match.group(1).split(",")])
            )
            print(self._bytes)

    @property
    def name(self):
        return self._name

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def packtype(self):
        return self._pack_type

    @property
    def spapack(self):
        return (
            f"{self._pack_type} {self._pack_conf_id}"
            f" v{self._pack_conf_rev}.{self._pack_conf_rel}"
        )

    @property
    def filename(self):
        return f"{self._pack_type}-{self.name}-{self.timestamp}.snapshot"

    @property
    def intouch_EN(self):
        return tuple(int(i) for i in self._intouch_EN)

    @property
    def intouch_CO(self):
        return tuple(int(i) for i in self._intouch_CO)

    @property
    def config_version(self):
        return int(self._config_version)

    @property
    def log_version(self):
        return int(self._log_version)

    @property
    def bytes(self):
        return self._bytes

    def save(self, path):
        """Save this snapshot into the path specified"""
        with open(os.path.join(path, self.filename), "w") as f:
            f.writelines(self._lines)

    def __repr__(self):
        return f"{self.name} ({self.timestamp}) for {self.packtype}"

    @staticmethod
    def parse_log_file(file: str):
        snapshots = []

        snapshot = None

        with open(file) as f:
            for line in f:
                if "Snapshot" in line:
                    snapshot = GeckoSnapshot()
                if snapshot:
                    if "INFO" in line:
                        snapshot.parse(line)
                    else:
                        snapshots.append(snapshot)
                        snapshot = None

        # Handle dangling snapshot
        if snapshot is not None:
            snapshots.append(snapshot)

        return snapshots
