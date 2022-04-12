""" Gecko UPDTS/SUPDT handlers """

import logging
import struct

from ...config import GeckoConfig
from .packet import GeckoPacketProtocolHandler

UPDTS_VERB = b"UPDTS"
SUPDT_VERB = b"SUPDT"

_LOGGER = logging.getLogger(__name__)


class GeckoUpdateFirmwareProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoUpdateFirmwareProtocolHandler(
            content=b"".join([UPDTS_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(**kwargs):
        return GeckoUpdateFirmwareProtocolHandler(
            content=b"".join(
                [
                    SUPDT_VERB,
                    b"\x00",
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(UPDTS_VERB) or received_bytes.startswith(
            SUPDT_VERB
        )

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        remainder = received_bytes[5:]
        if received_bytes.startswith(UPDTS_VERB):
            self._sequence = struct.unpack(">B", remainder[0:1])[0]
            return  # Stay in the handler list
        # Otherwise must be SUPDT
        self._should_remove_handler = True
