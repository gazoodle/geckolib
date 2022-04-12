""" Gecko CURCH/CHCUR handlers """

import logging
import struct

from ...config import GeckoConfig
from .packet import GeckoPacketProtocolHandler

CURCH_VERB = b"CURCH"
CHCUR_VERB = b"CHCUR"
GETCHANNEL_FORMAT = ">BB"

_LOGGER = logging.getLogger(__name__)


class GeckoGetChannelProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoGetChannelProtocolHandler(
            content=b"".join([CURCH_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(channel, signal_strength, **kwargs):
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.channel = self.signal_strength = None

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(CURCH_VERB) or received_bytes.startswith(
            CHCUR_VERB
        )

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
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
