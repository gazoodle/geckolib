""" Gecko GETWC/WCGET/SETWC/WCSET/REQWC/WCREQ handlers """

import logging
import struct

from .packet import GeckoPacketProtocolHandler

GETWC_VERB = b"GETWC"
WCGET_VERB = b"WCGET"
SETWC_VERB = b"SETWC"
WCSET_VERB = b"WCSET"
REQWC_VERB = b"REQWC"
WCREQ_VERB = b"WCREQ"


GET_WATERCARE_FORMAT = ">B"
SET_WATERCARE_FORMAT = ">BB"

_LOGGER = logging.getLogger(__name__)


class GeckoWatercareProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoWatercareProtocolHandler(
            content=b"".join([GETWC_VERB, struct.pack(">B", seq)]),
            timeout=2,
            retry_count=10,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def set(seq, mode, **kwargs):
        return GeckoWatercareProtocolHandler(
            content=b"".join(
                [SETWC_VERB, struct.pack(SET_WATERCARE_FORMAT, seq, mode)]
            ),
            timeout=4,
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
    def schedule(**kwargs):
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = None
        self.schedule = False

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return (
            received_bytes.startswith(GETWC_VERB)
            or received_bytes.startswith(WCGET_VERB)
            or received_bytes.startswith(REQWC_VERB)
        )

    def handle(self, socket, received_bytes: bytes, sender: tuple) -> bool:
        remainder = received_bytes[5:]
        if received_bytes.startswith(GETWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list
        if received_bytes.startswith(REQWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            self.schedule = True
            return  # Stay in the handler list
        # Otherwise must be WCGET
        self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0]
        self._should_remove_handler = True
