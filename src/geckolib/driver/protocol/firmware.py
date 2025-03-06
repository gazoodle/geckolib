"""Gecko UPDTS/SUPDT handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig

from .packet import GeckoPacketProtocolHandler

UPDTS_VERB = b"UPDTS"
SUPDT_VERB = b"SUPDT"

_LOGGER = logging.getLogger(__name__)


class GeckoUpdateFirmwareProtocolHandler(GeckoPacketProtocolHandler):
    """Handle UPDTS/SUPDT."""

    @staticmethod
    def request(seq: int, **kwargs: Any) -> GeckoUpdateFirmwareProtocolHandler:
        """Generate the request."""
        return GeckoUpdateFirmwareProtocolHandler(
            content=b"".join([UPDTS_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(**kwargs: Any) -> GeckoUpdateFirmwareProtocolHandler:
        """Generate the response."""
        return GeckoUpdateFirmwareProtocolHandler(
            content=b"".join(
                [
                    SUPDT_VERB,
                    b"\x00",
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Is this verb handles."""
        return received_bytes.startswith((UPDTS_VERB, SUPDT_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(UPDTS_VERB):
            self._sequence = struct.unpack(">B", remainder[0:1])[0]
            return  # Stay in the handler list
        # Otherwise must be SUPDT
        self._should_remove_handler = True
