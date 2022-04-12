""" Gecko GETWC/WCGET/SETWC/WCSET/REQWC/WCREQ handlers """

import logging
import struct

from typing import Optional

from ...config import GeckoConfig
from .packet import GeckoPacketProtocolHandler

GETWC_VERB = b"GETWC"
WCGET_VERB = b"WCGET"
SETWC_VERB = b"SETWC"
WCSET_VERB = b"WCSET"
REQWC_VERB = b"REQWC"
WCREQ_VERB = b"WCREQ"
WCERR_VERB = b"WCERR"


GET_WATERCARE_FORMAT = ">B"
SET_WATERCARE_FORMAT = ">BB"

_LOGGER = logging.getLogger(__name__)


class GeckoWatercareProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoWatercareProtocolHandler(
            content=b"".join([GETWC_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def set(seq, mode, **kwargs):
        return GeckoWatercareProtocolHandler(
            content=b"".join(
                [SETWC_VERB, struct.pack(SET_WATERCARE_FORMAT, seq, mode)]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            **kwargs,
        )

    @staticmethod
    def response(mode, **kwargs):
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
    def giveschedule(**kwargs):
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

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.mode: Optional[int] = None
        self.schedule = False

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return (
            received_bytes.startswith(GETWC_VERB)
            or received_bytes.startswith(WCGET_VERB)
            or received_bytes.startswith(REQWC_VERB)
            or received_bytes.startswith(WCSET_VERB)
        )

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        remainder = received_bytes[5:]
        if received_bytes.startswith(GETWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            self.schedule = False
            return  # Stay in the handler list
        if received_bytes.startswith(REQWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            self.schedule = True
            return  # Stay in the handler list
        if received_bytes.startswith(WCGET_VERB):
            self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0]
            self.schedule = False
        # Otherwise must be WCSET
        self._should_remove_handler = True


class GeckoWatercareErrorHandler(GeckoPacketProtocolHandler):
    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(WCERR_VERB)

    def handle(self, received_bytes: bytes, sender: tuple):
        pass
