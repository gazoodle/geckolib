""" Gecko RFERR handlers """

import logging

from .packet import GeckoPacketProtocolHandler

RFERR_VERB = b"RFERR"

_LOGGER = logging.getLogger(__name__)


class GeckoRFErrProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def response(**kwargs):
        return GeckoRFErrProtocolHandler(content=RFERR_VERB, **kwargs)

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(RFERR_VERB)

    def handle(self, socket, received_bytes: bytes, sender: tuple):
        _LOGGER.info("RF error, intouch2 module cannot communicate with spa")
