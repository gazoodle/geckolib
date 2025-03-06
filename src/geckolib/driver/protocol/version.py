"""Gecko AVERS/SVERS handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig

from .packet import GeckoPacketProtocolHandler

AVERS_VERB = b"AVERS"
SVERS_VERB = b"SVERS"
VERSION_FORMAT = ">HBBHBB"

_LOGGER = logging.getLogger(__name__)


class GeckoVersionProtocolHandler(GeckoPacketProtocolHandler):
    """Version handler class."""

    @staticmethod
    def request(seq: int, **kwargs: Any) -> GeckoVersionProtocolHandler:
        """Generate a request."""
        return GeckoVersionProtocolHandler(
            content=b"".join([AVERS_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(
        intouch_EN: tuple,  # noqa: N803
        intouch_CO: tuple,  # noqa: N803
        **kwargs: Any,
    ) -> GeckoVersionProtocolHandler:
        """Generate a response."""
        return GeckoVersionProtocolHandler(
            content=b"".join(
                [
                    SVERS_VERB,
                    struct.pack(
                        VERSION_FORMAT,
                        *intouch_EN,
                        *intouch_CO,
                    ),
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the version handler class."""
        super().__init__(**kwargs)
        self.en_build = self.en_major = self.en_minor = None
        self.co_build = self.co_major = self.co_minor = None

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith((AVERS_VERB, SVERS_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(AVERS_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return
        # Otherwise must be SVERS
        (
            self.en_build,
            self.en_major,
            self.en_minor,
            self.co_build,
            self.co_major,
            self.co_minor,
        ) = struct.unpack(VERSION_FORMAT, remainder)
        self._should_remove_handler = True
