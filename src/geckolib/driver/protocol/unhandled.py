""" Gecko handler for unhanded verbs """

import asyncio
import logging

from geckolib.const import GeckoConstants
from ..udp_socket import GeckoUdpProtocolHandler


_LOGGER = logging.getLogger(__name__)


class GeckoUnhandledProtocolHandler(GeckoUdpProtocolHandler):
    """Protocol handler to deal with unhandled or unsolicited messages"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def can_handle(self, _received_bytes: bytes, _sender: tuple) -> bool:
        return True

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        pass

    async def consume(self, protocol):
        while True:
            if protocol.queue.head is not None:
                # First time we see this, we mark the queue
                protocol.queue.mark()
                # Allow the rest of the tasks to operate
                await asyncio.sleep(GeckoConstants.ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD)
                # If we get here then no one processed the datagram
                # so we can remove it and moan about it
                if protocol.queue.is_marked:
                    data, sender = protocol.queue.head
                    protocol.queue.pop()
                    _LOGGER.debug(
                        "No handler for %s from %s found, message ignored", data, sender
                    )
            await asyncio.sleep(GeckoConstants.ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD)
