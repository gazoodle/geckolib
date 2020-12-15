""" Gecko AVERS/SVERS handlers """

import logging
import struct

from .packet import GeckoPacketProtocolHandler

AVERS_VERB = b"AVERS"
SVERS_VERB = b"SVERS"
VERSION_FORMAT = ">HBBHBB"

_LOGGER = logging.getLogger(__name__)


class GeckoVersionProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoVersionProtocolHandler(
            content=b"".join([AVERS_VERB, struct.pack(">B", seq)]),
            timeout=2,
            retry_count=10,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(intouch_EN: tuple, intouch_CO: tuple, **kwargs):
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.en_build = self.en_major = self.en_minor = None
        self.co_build = self.co_major = self.co_minor = None

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(AVERS_VERB) or received_bytes.startswith(
            SVERS_VERB
        )

    def handle(self, socket, received_bytes: bytes, sender: tuple):
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
