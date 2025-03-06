"""Gecko CURCH/CHCUR handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig

from .packet import GeckoPacketProtocolHandler

CURCH_VERB = b"CURCH"
CHCUR_VERB = b"CHCUR"
GETCHANNEL_FORMAT = ">BB"

_LOGGER = logging.getLogger(__name__)


class GeckoGetChannelProtocolHandler(GeckoPacketProtocolHandler):
    """Handle CURCH/CHCUR verbs."""

    @staticmethod
    def request(seq: int, **kwargs: Any) -> GeckoGetChannelProtocolHandler:
        """Generate request."""
        return GeckoGetChannelProtocolHandler(
            content=b"".join([CURCH_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(
        channel: int, signal_strength: int, **kwargs: Any
    ) -> GeckoGetChannelProtocolHandler:
        """Generate response."""
        return GeckoGetChannelProtocolHandler(
            content=b"".join(
                [
                    CHCUR_VERB,
                    struct.pack(
                        GETCHANNEL_FORMAT,
                        channel,
                        signal_strength,
                    ),
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)
        self.channel = self.signal_strength = None

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith((CURCH_VERB, CHCUR_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(CURCH_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list
        # Otherwise must be CHCUR
        (
            self.channel,
            self.signal_strength,
        ) = struct.unpack(GETCHANNEL_FORMAT, remainder)
        self._should_remove_handler = True
