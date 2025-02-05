"""Gecko handler for unhanded verbs."""

import logging
from typing import Any

from geckolib.driver.async_udp_protocol import GeckoAsyncUdpProtocol
from geckolib.driver.udp_protocol_handler import GeckoUdpProtocolHandler

_LOGGER = logging.getLogger(__name__)


class GeckoUnhandledProtocolHandler(GeckoUdpProtocolHandler):
    """Protocol handler to deal with unhandled or unsolicited messages."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the default handler."""
        super().__init__(**kwargs)

    def can_handle(self, _received_bytes: bytes, _sender: tuple) -> None:
        """Will never get called."""

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        """Go on then, handle it."""

    def _can_handle(
        self, protocol: GeckoAsyncUdpProtocol, _received_bytes: bytes, _sender: tuple
    ) -> bool:
        # If the protocol queue is marked, then we can handle it because no
        # one else can
        if protocol.queue.is_marked:
            _LOGGER.debug(
                "Packet %s from %s is unhandled and will be ignored",
                _received_bytes,
                _sender,
            )
            return True
        # Mark the queue and let others have a go
        protocol.queue.mark()
        return False
