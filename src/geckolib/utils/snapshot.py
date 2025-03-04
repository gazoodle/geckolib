"""Snapshot helper."""

from __future__ import annotations

import ast
import logging
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from geckolib.driver import GeckoStatusBlockProtocolHandler

_LOGGER = logging.getLogger(__name__)


class GeckoSnapshot:
    """Snapshot helper class."""

    def __init__(self) -> None:
        """Initialize the snapshot."""
        self._lines = []
        self._name = None
        self._timestamp = datetime.now(tz=UTC).strftime("%Y-%m-%d %H:%M:%S")
        self._pack_type: str = ""
        self._pack_conf_id = None
        self._pack_conf_rev = None
        self._pack_conf_rel = None
        self._intouch_CO = ()
        self._intouch_EN = ()
        self._config_version = None
        self._log_version = None
        self._bytes = b""
        self._status_block_handler = GeckoStatusBlockProtocolHandler()
        self._status_block_segments = []

        self._funcs = [
            #
            #   Snapshot set
            #
            # Match "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Snapshot (Heating)", # noqa: E501
            (r"(\d+-\d+-\d+\s+\d+:\d+:\d+).*Snapshot \((.*)\)", self._re_snapshot),
            # Match "INFO:geckolib.utils.shell:Snapshot (EconomyModeActive)",
            (r"Snapshot \((.*)\)", self._re_snapshot_alt),
            # Match "Spa pack inXM 186 v3.0"
            (r"Spa pack (.*) (\d+) v(\d+)\.(\d+)", self._re_spa_pack),
            # Match "intouch version EN 88 v15.0"
            (r"intouch version EN (\d+) v(\d+)\.(\d+)", self._re_intouch_en),
            # Match "intouch version CO 89 v11.0"
            (r"intouch version CO (\d+) v(\d+)\.(\d+)", self._re_intouch_co),
            # Match "Config version 9"
            (r"Config version (\d+)", self._re_config_version),
            # Match "Log version 9"
            (r"Log version (\d+)", self._re_log_version),
            # Match "['0x5', '0x1', ... '0x0']"
            (r"\[([0-9A-Fa-fx\\' ,]*)\]", self._re_data),
            #
            #   Connection set
            #
            # Match "PackType adjusted data = inYT"
            (r"PackType adjusted data = (\w+)", self._re_spa_pack_type),
            # Match "PackConfID @ 297, Word raw data = 163"
            (r"PackConfID @ 297, Word raw data = (\d+)", self._re_spa_pack_id),
            # Match "PackConfRev @ 299, Byte raw data = 4"
            (r"PackConfRev @ 299, Byte raw data = (\d+)", self._re_spa_pack_rev),
            # Match "PackConfRel @ 300, Byte raw data = 0"
            (r"PackConfRel @ 300, Byte raw data = (\d+)", self._re_spa_pack_rel),
            # Match "Got software version 70 v14.0/69 v11.0"
            (
                r"Got software version (\d+) v(\d+).(\d+)/(\d+) v(\d+).(\d+)",
                self._re_software_version,
            ),
            # Match "Got spa configuration Type 10 - CFG 61/LOG 61"
            (
                r"Got spa configuration Type (\d+) - CFG (\d+)/LOG (\d+)",
                self._re_config_and_log,
            ),
            # Match "STATV\x15\x16'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS>"  # noqa: E501
            (r"(STATV.*)</DATAS>", self._re_data_segment),
            # Match "INFO SNAPSHOT ========{ ... }========"
            (r"SNAPSHOT ========({.*})========", self._re_json_liine),
        ]

    def _re_snapshot(self, groups: tuple[str | Any, ...]) -> None:
        (self._timestamp, self._name) = groups

    def _re_snapshot_alt(self, groups: tuple[str | Any, ...]) -> None:
        (self._name,) = groups

    def _re_spa_pack(self, groups: tuple[str | Any, ...]) -> None:
        (
            self._pack_type,
            self._pack_conf_id,
            self._pack_conf_rev,
            self._pack_conf_rel,
        ) = groups

    def _re_spa_pack_type(self, groups: tuple[str | Any, ...]) -> None:
        (self._pack_type,) = groups

    def _re_spa_pack_id(self, groups: tuple[str | Any, ...]) -> None:
        (hex_id,) = groups
        self._pack_conf_id = f"{int(hex_id, 16)}"

    def _re_spa_pack_rev(self, groups: tuple[str | Any, ...]) -> None:
        (self._pack_conf_rev,) = groups

    def _re_spa_pack_rel(self, groups: tuple[str | Any, ...]) -> None:
        (self._pack_conf_rel,) = groups

    def _re_intouch_en(self, groups: tuple[str | Any, ...]) -> None:
        self._intouch_EN = groups

    def _re_intouch_co(self, groups: tuple[str | Any, ...]) -> None:
        self._intouch_CO = groups

    def _re_software_version(self, groups: tuple[str | Any, ...]) -> None:
        self._intouch_EN = (groups[0], groups[1], groups[2])
        self._intouch_CO = (groups[3], groups[4], groups[5])

    def _re_config_version(self, groups: tuple[str | Any, ...]) -> None:
        (self._config_version,) = groups

    def _re_log_version(self, groups: tuple[str | Any, ...]) -> None:
        (self._log_version,) = groups

    def _re_config_and_log(self, groups: tuple[str | Any, ...]) -> None:
        (type_, self._config_version, self._log_version) = groups

    def _re_data(self, groups: tuple[str | Any, ...]) -> None:
        self._bytes = bytes(
            bytearray([int(b.strip()[1:-1], 16) for b in groups[0].split(",")])
        )

    def _re_data_segment(self, groups: tuple[str | Any, ...]) -> None:
        data = groups[0].replace("'", "\\x27")
        bytes_ = ast.literal_eval(f"b'{data}'")
        self._status_block_handler.handle(bytes_, None)
        self._status_block_segments.append(self._status_block_handler.data)
        if self._status_block_handler.next == 0:
            self._bytes = b"".join(self._status_block_segments)

    def _re_json_liine(self, groups: tuple[str | Any, ...]) -> None:
        self._parse_json(groups[0])

    def parse(self, line: str) -> None:
        """Parse a snapshot line."""
        # Always bag the lines
        self._lines.append(line)

        for fn in self._funcs:
            match = re.search(fn[0], line, re.DOTALL)
            if match:
                fn[1](match.groups())

    @property
    def name(self) -> str | None:
        """Get the snapshot name."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set the snapshot name."""
        self._name = name

    @property
    def timestamp(self) -> str | None:
        """Get the snapshot timestamp."""
        return self._timestamp

    @property
    def packtype(self) -> str:
        """Get the snapshot packtype."""
        return self._pack_type

    @property
    def spapack(self) -> str:
        """Get the spapack."""
        return (
            f"{self._pack_type} {self._pack_conf_id}"
            f" v{self._pack_conf_rev}.{self._pack_conf_rel}"
        )

    @property
    def filename(self) -> str:
        """Generate snapshot filename."""
        fixed_timestamp = f"{self.timestamp}".replace(":", "_").replace(" ", "-")
        return f"{self._pack_type}-{self.name}-{fixed_timestamp}.snapshot"

    @property
    def intouch_EN(self) -> tuple[int, ...]:  # noqa: N802
        """Get the intouch_EN versions."""
        return tuple(int(i) for i in self._intouch_EN)

    @property
    def intouch_EN_str(self) -> str:  # noqa: N802
        """Get the EN version as a string."""
        tup = self._intouch_EN
        if len(tup) == 3:  # noqa: PLR2004
            return f"{tup[0]} v{tup[1]}.{tup[2]}"
        return ""

    @property
    def intouch_CO(self) -> tuple[int, ...]:  # noqa: N802
        """Get the intouch_CO versions."""
        return tuple(int(i) for i in self._intouch_CO)

    @property
    def intouch_CO_str(self) -> str:  # noqa: N802
        """Get the CO version as a string."""
        tup = self.intouch_CO
        if len(tup) == 3:  # noqa: PLR2004
            return f"{tup[0]} v{tup[1]}.{tup[2]}"
        return ""

    @property
    def config_version(self) -> int:
        """Get the config version."""
        return int(self._config_version)

    @property
    def log_version(self) -> int:
        """Get the log version."""
        return int(self._log_version)

    @property
    def bytes(self) -> bytes:
        """Get the structure bytes."""
        return self._bytes

    def save(self, path: str) -> None:
        """Save this snapshot into the path specified."""
        with (Path(path) / Path(self.filename)).open("w") as f:
            f.writelines(self._lines)

    def __repr__(self) -> str:
        """Get string representagtion."""
        return f"{self.name} ({self.timestamp}) for {self.packtype}"

    @staticmethod
    def parse_log_file(file: str) -> list[GeckoSnapshot]:  # noqa: PLR0912
        """Parse a log file into one or more snapshots."""
        snapshots = []

        snapshot = None
        connection = None

        if file.endswith(".json"):
            with Path(file).open() as f:
                json = "".join(f.readlines())
                snapshot = GeckoSnapshot.parse_json(json)
        else:
            with Path(file).open() as f:
                for line in f:
                    if line.startswith("{"):
                        snapshot = GeckoSnapshot.parse_json(line)
                    elif "Snapshot" in line:
                        snapshot = GeckoSnapshot()

                    if snapshot:
                        if "INFO" in line:
                            snapshot.parse(line)
                        else:
                            snapshots.append(snapshot)
                            snapshot = None

                    if "Starting spa connection handshake..." in line:
                        connection = GeckoSnapshot()
                        connection.set_name("Connection found")
                    if connection:
                        if "Spa is connected" in line:
                            connection.parse(line)
                            snapshots.append(connection)
                            connection = None
                        else:
                            connection.parse(line)

        # Handle dangling snapshot
        if snapshot is not None:
            snapshots.append(snapshot)
        if connection is not None:
            snapshots.append(connection)

        return snapshots

    def _parse_json(self, json: str) -> None:
        snap = ast.literal_eval(json)
        self.parse(f"Spa pack {snap['Spa pack']}")
        self.parse(f"intouch version EN {snap['intouch version EN']}")
        self.parse(f"intouch version CO {snap['intouch version CO']}")
        self._config_version = snap["Config version"]
        self._log_version = snap["Log version"]
        self._bytes = bytes(
            bytearray([int(b.strip()[2:], 16) for b in snap["Status Block"]])
        )
        self._timestamp = datetime.fromisoformat(snap["Snapshot UTC Time"])

    @staticmethod
    def parse_json(json: str) -> GeckoSnapshot:
        """Parse a JSON snapshot."""
        snapshot = GeckoSnapshot()
        snapshot._parse_json(json)
        return snapshot

    @staticmethod
    def create(pack_type: str, config_version: str, log_version: str) -> GeckoSnapshot:
        """Create a blank snapshot."""
        snapshot = GeckoSnapshot()

        snapshot.parse(f"Spa pack {pack_type} 186 v3.0")
        snapshot.parse("intouch version EN 88 v15.0")
        snapshot.parse("intouch version CO 89 v11.0")

        snapshot._config_version = config_version
        snapshot._log_version = log_version
        snapshot._bytes = bytearray(1024)

        return snapshot

    def is_compatible(self, other: GeckoSnapshot) -> bool:
        """Determine if this snapshot is compatible with the other."""
        if self.spapack != other.spapack:
            return False
        if self.packtype != other.packtype:
            return False
        if self.config_version != other.config_version:
            return False
        return self.log_version == other.log_version
