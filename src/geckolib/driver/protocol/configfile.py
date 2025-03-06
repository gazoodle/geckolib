"""Gecko FILES/SFILE handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig
from geckolib.const import GeckoConstants

from .packet import GeckoPacketProtocolHandler

SFILE_VERB = b"SFILE"
FILES_VERB = b"FILES"

_LOGGER = logging.getLogger(__name__)


class GeckoConfigFileProtocolHandler(GeckoPacketProtocolHandler):
    """Protocol handler class for FILES/SFILE."""

    @staticmethod
    def request(seq: int, **kwargs: Any) -> GeckoConfigFileProtocolHandler:
        """Generate the request."""
        return GeckoConfigFileProtocolHandler(
            content=b"".join([SFILE_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS * 3,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(
        plateform_key: str, config_version: int, log_version: int, **kwargs: Any
    ) -> GeckoConfigFileProtocolHandler:
        """Generate the response."""
        return GeckoConfigFileProtocolHandler(
            content=b"".join(
                [
                    FILES_VERB,
                    f",{plateform_key}_C{config_version:02}.xml,"
                    f"{plateform_key}_S{log_version:02}.xml".encode(
                        GeckoConstants.MESSAGE_ENCODING
                    ),
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs: Any) -> None:
        """Initialise the class."""
        super().__init__(**kwargs)
        self.plateform_key = self.config_version = self.log_version = None

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith((SFILE_VERB, FILES_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the command."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(SFILE_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list

        # Otherwise must be FILES
        config = (
            received_bytes[6:]
            .decode(GeckoConstants.MESSAGE_ENCODING)
            .replace(".xml", "")
            .split(",")
        )
        # Split the string around the underscore
        gecko_pack_config = config[0].split("_")
        gecko_pack_log = config[1].split("_")

        if gecko_pack_config[0] != gecko_pack_log[0]:
            msg = (
                f"Dissimilar platforms `{gecko_pack_config[0]}`"
                f" and `{gecko_pack_log[0]}`"
            )
            raise ValueError(msg)

        self.plateform_key = gecko_pack_config[0]
        if self.plateform_key == "MrSt":
            self.plateform_key = "MrSteam"
        self.config_version = int(gecko_pack_config[1][1:])
        self.log_version = int(gecko_pack_log[1][1:])
        self._should_remove_handler = True
