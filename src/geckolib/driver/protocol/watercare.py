"""Gecko GETWC/WCGET/SETWC/WCSET/REQWC/WCREQ handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig
from geckolib.const import GeckoConstants

from .packet import GeckoPacketProtocolHandler

GETWC_VERB = b"GETWC"  # Get watercare mode
WCGET_VERB = b"WCGET"  # Get watercare mode response
SETWC_VERB = b"SETWC"  # Set watercare mode
WCSET_VERB = b"WCSET"  # Set watercare mode response
REQWC_VERB = b"REQWC"
WCREQ_VERB = b"WCREQ"
WCERR_VERB = b"WCERR"


GET_WATERCARE_FORMAT = ">B"
SET_WATERCARE_FORMAT = ">BB"

_LOGGER = logging.getLogger(__name__)


class GeckoWatercareProtocolHandler(GeckoPacketProtocolHandler):
    """Watercare protocol handler class."""

    @staticmethod
    def request(seq: int, **kwargs: Any) -> GeckoWatercareProtocolHandler:
        """Generate a request."""
        return GeckoWatercareProtocolHandler(
            content=b"".join([GETWC_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def set(seq: int, mode: int, **kwargs: Any) -> GeckoWatercareProtocolHandler:
        """Generatge a watercare set command."""
        return GeckoWatercareProtocolHandler(
            content=b"".join(
                [SETWC_VERB, struct.pack(SET_WATERCARE_FORMAT, seq, mode)]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            **kwargs,
        )

    @staticmethod
    def get_response(mode: int, **kwargs: Any) -> GeckoWatercareProtocolHandler:
        """Generate a watercare mode request response."""
        return GeckoWatercareProtocolHandler(
            content=b"".join(
                [
                    WCGET_VERB,
                    struct.pack(
                        GET_WATERCARE_FORMAT,
                        mode,
                    ),
                ]
            ),
            **kwargs,
        )

    @staticmethod
    def set_response(mode: int, **kwargs: Any) -> GeckoWatercareProtocolHandler:
        """Generate a watercare set mode response."""
        return GeckoWatercareProtocolHandler(
            content=b"".join(
                [
                    WCSET_VERB,
                    struct.pack(
                        GET_WATERCARE_FORMAT,
                        mode,
                    ),
                ]
            ),
            **kwargs,
        )

    @staticmethod
    def giveschedule(**kwargs: Any) -> GeckoWatercareProtocolHandler:
        """Generate a watercare schedule request response."""
        return GeckoWatercareProtocolHandler(
            content=b"".join(
                [
                    WCREQ_VERB,
                    b"\x00\x00\x00\x01\x00\x00\x06\x00\x00\x00\x00\x02\x01\x00\x01\x05"
                    b"\x06\x00\x12\x00\x03\x01\x00\x00\x06\x06\x00\x12\x00\x04\x01\x00"
                    b"\x01\x05\x00\x00\x00\x00",
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)
        self.mode: int | None = None
        self.schedule = False

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith(
            (GETWC_VERB, SETWC_VERB, WCGET_VERB, REQWC_VERB, WCSET_VERB)
        )

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        self.schedule = False
        self.mode = None
        if received_bytes.startswith(GETWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list
        if received_bytes.startswith(REQWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            self.schedule = True
            return  # Stay in the handler list
        if received_bytes.startswith(SETWC_VERB):
            self.mode = struct.unpack(SET_WATERCARE_FORMAT, remainder)[1] % len(
                GeckoConstants.WATERCARE_MODE
            )
            return  # Stay in the handler list
        if received_bytes.startswith(WCGET_VERB):
            self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0] % len(
                GeckoConstants.WATERCARE_MODE
            )
        if received_bytes.startswith(WCSET_VERB):
            self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0] % len(
                GeckoConstants.WATERCARE_MODE
            )

        # Otherwise must be WCSET
        self._should_remove_handler = True


class GeckoWatercareErrorHandler(GeckoPacketProtocolHandler):
    """Watercare error handler."""

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith(WCERR_VERB)

    def handle(self, _received_bytes: bytes, _sender: tuple) -> None:
        """Handle this."""
