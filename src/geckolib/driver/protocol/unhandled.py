"""Gecko handler for unhanded verbs."""

import asyncio
import logging
from typing import Any

from geckolib.driver.udp_socket import GeckoUdpProtocolHandler

_LOGGER = logging.getLogger(__name__)


class GeckoUnhandledProtocolHandler(GeckoUdpProtocolHandler):
    """Protocol handler to deal with unhandled or unsolicited messages."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the default handler."""
        super().__init__(**kwargs)

    def can_handle(self, _received_bytes: bytes, _sender: tuple) -> bool:
        """You can't handle the truth ... wait! No actually you can."""
        return True

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        """Go on then, handle it."""

    async def consume(self, protocol: Any) -> None:
        """Consume the packet."""
        try:
            while True:
                await asyncio.sleep(0)
                await protocol.queue.wait()
                if protocol.queue.head is not None:
                    break
                if protocol.queue.is_marked:
                    data, sender = protocol.queue.head
                    protocol.queue.pop()
                    _LOGGER.debug(
                        "No handler for %s from %s found, message ignored",
                        data,
                        sender,
                    )
                else:
                    protocol.queue.mark()

        except asyncio.CancelledError:
            _LOGGER.debug("Unhandled handler loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("Unhandled handler consume function caught exception")
            raise
