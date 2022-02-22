""" Gecko handler for unhanded verbs """

import asyncio
from distutils.log import Log
import logging
from ..udp_socket import GeckoUdpProtocolHandler
from ...const import GeckoConstants


_LOGGER = logging.getLogger(__name__)


class GeckoUnhandledProtocolHandler(GeckoUdpProtocolHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def consume(self, socket, queue):
        while True:
            if queue.head is not None:
                # First time we see this, we mark the queue
                queue.mark()
                # Allow the rest of the tasks to operate
                await asyncio.sleep(0)
                # If we get here then no one processed the datagram
                # so we can remove it and moan about it
                if queue.is_marked:
                    data, sender = queue.head
                    queue.pop()
                    _LOGGER.debug("No handler for %s from %s found", data, sender)
            await asyncio.sleep(0)
