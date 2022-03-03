""" Gecko RFERR handlers """

import logging
from datetime import datetime
from typing import Optional

from .packet import GeckoPacketProtocolHandler

RFERR_VERB = b"RFERR"

_LOGGER = logging.getLogger(__name__)


class GeckoRFErrProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def response(**kwargs):
        return GeckoRFErrProtocolHandler(content=RFERR_VERB, **kwargs)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._error_count: int = 0
        self._last_error_at: Optional[datetime] = None

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(RFERR_VERB)

    def handle(self, received_bytes: bytes, sender: tuple):
        self._error_count += 1
        self._last_error_at = datetime.now()
        _LOGGER.debug(
            "RF error #%d, intouch2 EN module cannot communicate with spa (CO) module",
            self.total_error_count,
        )

    @property
    def total_error_count(self) -> int:
        """Return total number of RFErr messages that this handler has processed"""
        return self._error_count

    @property
    def last_error_at(self) -> Optional[datetime]:
        """Return the last time an RFErr occurred, or None if never"""
        return self._last_error_at
