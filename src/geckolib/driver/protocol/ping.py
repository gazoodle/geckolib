"""Gecko APING handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig

from .packet import GeckoPacketProtocolHandler

PING_VERB = b"APING"

_LOGGER = logging.getLogger(__name__)


class GeckoPingProtocolHandler(GeckoPacketProtocolHandler):
    """Ping handler class."""

    @staticmethod
    def request(**kwargs: Any) -> GeckoPingProtocolHandler:
        """Build a PING request class."""
        return GeckoPingProtocolHandler(
            content=PING_VERB, timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS, **kwargs
        )

    @staticmethod
    def response(**kwargs: Any) -> GeckoPingProtocolHandler:
        """Build a PING response class."""
        return GeckoPingProtocolHandler(
            content=b"".join([PING_VERB, b"\x00"]), **kwargs
        )

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Check if this class can handle the packet bytes."""
        return received_bytes.startswith(PING_VERB)

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the packet bytes."""
        remainder = received_bytes[5:]
        if len(remainder) > 0:
            self._sequence = struct.unpack(">B", remainder)[0]
