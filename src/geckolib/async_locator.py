""" Gecko Async Locator class """

import logging
import time
import asyncio
import socket

from .driver import (
    GeckoHelloProtocolHandler,
    GeckoAsyncUdpProtocol,
)
from .const import GeckoConstants
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_tasks import AsyncTasks


_LOGGER = logging.getLogger(__name__)


class GeckoAsyncLocator(AsyncTasks):
    """
    GeckoAsyncLocator class locates in.touch2 devices on your local LAN
    """
    def __init__(self, **kwargs):
        super().__init__()
        self.spas = []
        self.spa_identifiers = []
        self._static_ip = kwargs.get("static_ip", None)
        if self._static_ip == "":
            self._static_ip = None
        self._has_found_spa = False
        self._started = None

    async def __aenter__(self):
        await self.discover()
        return self

    def _on_discovered(self, handler, socket, sender):
        if handler.spa_identifier in self.spa_identifiers:
            return
        _LOGGER.debug("Discovered spa %s", handler.spa_identifier)
        self.spa_identifiers.append(handler.spa_identifier)
        descriptor = GeckoAsyncSpaDescriptor(
            handler.spa_identifier,
            handler.spa_name,
            sender,
        )
        self.spas.append(descriptor)
        if self._static_ip is not None:
            _LOGGER.debug("Static IP was specified, so spa has been found")
            self._has_found_spa = True

    @property
    def age(self):
        return time.monotonic() - self._started

    @property
    def has_had_enough_time(self):
        return self.age > GeckoConstants.DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS

    async def discover(self):
        self._started = time.monotonic()
        loop = asyncio.get_running_loop()
        on_con_lost = loop.create_future()
        transport, protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(on_con_lost),
            family=socket.AF_INET, allow_broadcast=True)

        hello_handler = GeckoHelloProtocolHandler.broadcast(on_handled=self._on_discovered)
        self.add_task(hello_handler.consume(None, protocol.queue))

        while self.age < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
            protocol.queue_send(
                hello_handler,
                GeckoHelloProtocolHandler.broadcast_address(
                    static_ip=self._static_ip
                ),
            )
            await asyncio.sleep(1)
            if self.has_had_enough_time:
                if len(self.spas) > 0:
                    _LOGGER.info("Found %d spas ... %s", len(self.spas), self.spas)
                    break
            if self._has_found_spa:
                break

        transport.close()
