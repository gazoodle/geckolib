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
REQWC_VERB = b"REQWC"  # Get watercare schedule list
WCREQ_VERB = b"WCREQ"  # Get watercare schedule list response
WCERR_VERB = b"WCERR"  # Watercare error


GET_WATERCARE_FORMAT = ">B"
SET_WATERCARE_FORMAT = ">BB"

_LOGGER = logging.getLogger(__name__)


class GeckoWatercareScheduleManager:
    """Watercare schedule manager."""


class GeckoGetWatercareModeProtocolHandler(GeckoPacketProtocolHandler):
    """Get watercare mode protocol handler class."""

    @staticmethod
    def get(seq: int, **kwargs: Any) -> GeckoGetWatercareModeProtocolHandler:
        """Generate a request."""
        return GeckoGetWatercareModeProtocolHandler(
            content=b"".join([GETWC_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def get_response(mode: int, **kwargs: Any) -> GeckoGetWatercareModeProtocolHandler:
        """Generate a watercare mode request response."""
        return GeckoGetWatercareModeProtocolHandler(
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

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((GETWC_VERB, WCGET_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        self.mode = None
        if received_bytes.startswith(GETWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list
        # Otherwise must be WCSET
        self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0] % len(
            GeckoConstants.WATERCARE_MODE
        )
        self._should_remove_handler = True


class GeckoSetWatercareModeProtocolHandler(GeckoPacketProtocolHandler):
    """Set watercare mode protocol handler class."""

    @staticmethod
    def set(seq: int, mode: int, **kwargs: Any) -> GeckoSetWatercareModeProtocolHandler:
        """Generatge a watercare set command."""
        return GeckoSetWatercareModeProtocolHandler(
            content=b"".join(
                [SETWC_VERB, struct.pack(SET_WATERCARE_FORMAT, seq, mode)]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            **kwargs,
        )

    @staticmethod
    def set_response(mode: int, **kwargs: Any) -> GeckoSetWatercareModeProtocolHandler:
        """Generate a watercare set mode response."""
        return GeckoSetWatercareModeProtocolHandler(
            content=b"".join([WCSET_VERB, struct.pack(GET_WATERCARE_FORMAT, mode)]),
            **kwargs,
        )

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((SETWC_VERB, WCSET_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        self.mode = None
        if received_bytes.startswith(SETWC_VERB):
            self._sequence, self.mode = struct.unpack(SET_WATERCARE_FORMAT, remainder)
            self.mode %= len(GeckoConstants.WATERCARE_MODE)
            return  # Stay in the handler list
        # Otherwise must be WCSET
        self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0]
        self._should_remove_handler = True


class GeckoGetWatercareScheduleListProtocolHandler(GeckoPacketProtocolHandler):
    """Get list of watercare schdeules."""

    @staticmethod
    def get(seq: int, **kwargs: Any) -> GeckoGetWatercareScheduleListProtocolHandler:
        """Generate a request."""
        return GeckoGetWatercareScheduleListProtocolHandler(
            content=b"".join([REQWC_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def get_response(
        _schedule: GeckoWatercareScheduleManager, **kwargs: Any
    ) -> GeckoGetWatercareScheduleListProtocolHandler:
        """Generate the response."""
        return GeckoGetWatercareScheduleListProtocolHandler(
            content=b"".join(
                [
                    WCREQ_VERB,
                    b"\x00\x00",
                    b"\x00\x01\x00\x00\x06\x00\x00\x00\x00",
                    b"\x02\x01\x00\x01\x05\x06\x00\x12\x00"
                    b"\x03\x01\x00\x00\x06\x06\x00\x12\x00"
                    b"\x04\x01\x00\x01\x05\x00\x00\x00\x00",
                ]
            ),
            **kwargs,
        )

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((REQWC_VERB, WCREQ_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(REQWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list
        # Otherwise must be WCREQ
        self._should_remove_handler = True


class GeckoWatercareErrorHandler(GeckoPacketProtocolHandler):
    """Watercare error handler."""

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith(WCERR_VERB)

    def handle(self, _received_bytes: bytes, _sender: tuple) -> None:
        """Handle this."""
