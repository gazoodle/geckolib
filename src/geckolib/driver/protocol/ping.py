""" Gecko APING handlers """

import logging
import struct

from .packet import GeckoPacketProtocolHandler

PING_VERB = b"APING"

_LOGGER = logging.getLogger(__name__)


class GeckoPingProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(**kwargs):
        return GeckoPingProtocolHandler(content=PING_VERB, **kwargs)

    @staticmethod
    def response(**kwargs):
        return GeckoPingProtocolHandler(
            content=b"".join([PING_VERB, b"\x00"]), **kwargs
        )

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(PING_VERB)

    def handle(self, socket, received_bytes: bytes, sender: tuple):
        remainder = received_bytes[5:]
        if len(remainder) > 0:
            self._sequence = struct.unpack(">B", remainder)[0]
