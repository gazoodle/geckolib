"""Gecko RFERR handlers."""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import Any

from .packet import GeckoPacketProtocolHandler

RFERR_VERB = b"RFERR"

_LOGGER = logging.getLogger(__name__)


class GeckoRFErrProtocolHandler(GeckoPacketProtocolHandler):
    """Handle RFERR."""

    @staticmethod
    def response(**kwargs: Any) -> GeckoRFErrProtocolHandler:
        """Generate a response."""
        return GeckoRFErrProtocolHandler(content=RFERR_VERB, **kwargs)

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)
        self._error_count: int = 0
        self._last_error_at: datetime | None = None

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this."""
        return received_bytes.startswith(RFERR_VERB)

    def handle(self, _received_bytes: bytes, _sender: tuple) -> None:
        """Handle RFERR."""
        self._error_count += 1
        self._last_error_at = datetime.now(tz=UTC)
        _LOGGER.debug(
            "RF error #%d, intouch2 EN module cannot communicate with spa (CO) module",
            self.total_error_count,
        )

    @property
    def total_error_count(self) -> int:
        """Return total number of RFErr messages that this handler has processed."""
        return self._error_count

    @property
    def last_error_at(self) -> datetime | None:
        """Return the last time an RFErr occurred, or None if never."""
        return self._last_error_at
