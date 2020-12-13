""" Snapshot helper """
import ast
import logging
import re
import os
from datetime import datetime
from ..driver import GeckoStatusBlockProtocolHandler

_LOGGER = logging.getLogger(__name__)


class GeckoSnapshot:
    def __init__(self):
        self._lines = []
        self._name = None
        self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._pack_type = None
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
            # Match "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Snapshot (Heating)", # noqa : E501
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
        ]

    def _re_snapshot(self, groups):
        (self._timestamp, self._name) = groups

    def _re_snapshot_alt(self, groups):
        (self._name,) = groups

    def _re_spa_pack(self, groups):
        (
            self._pack_type,
            self._pack_conf_id,
            self._pack_conf_rev,
            self._pack_conf_rel,
        ) = groups

    def _re_spa_pack_type(self, groups):
        (self._pack_type,) = groups

    def _re_spa_pack_id(self, groups):
        (hex_id,) = groups
        self._pack_conf_id = f"{int(hex_id,16)}"

    def _re_spa_pack_rev(self, groups):
        (self._pack_conf_rev,) = groups

    def _re_spa_pack_rel(self, groups):
        (self._pack_conf_rel,) = groups

    def _re_intouch_en(self, groups):
        self._intouch_EN = groups

    def _re_intouch_co(self, groups):
        self._intouch_CO = groups

    def _re_software_version(self, groups):
        self._intouch_EN = (groups[0], groups[1], groups[2])
        self._intouch_CO = (groups[3], groups[4], groups[5])

    def _re_config_version(self, groups):
        (self._config_version,) = groups

    def _re_log_version(self, groups):
        (self._log_version,) = groups

    def _re_config_and_log(self, groups):
        (type_, self._config_version, self._log_version) = groups

    def _re_data(self, groups):
        self._bytes = bytes(
            bytearray([int(b.strip()[1:-1], 16) for b in groups[0].split(",")])
        )

    def _re_data_segment(self, groups):
        data = groups[0].replace("'", "\\x27")
        bytes_ = ast.literal_eval(f"b'{data}'")
        self._status_block_handler.handle(None, bytes_, None)
        self._status_block_segments.append(self._status_block_handler.data)
        if self._status_block_handler.next == 0:
            self._bytes = b"".join(self._status_block_segments)

    def parse(self, line: str):
        # Always bag the lines
        self._lines.append(line)

        for fn in self._funcs:
            match = re.search(fn[0], line, re.DOTALL)
            if match:
                fn[1](match.groups())

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
        connection = None

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

                if "Starting spa connection handshake..." in line:
                    connection = GeckoSnapshot()
                    connection._name = "Connection found"
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
