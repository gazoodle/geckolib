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


_LOGGER = logging.getLogger(__name__)

class GeckoAsyncLocator:
    """
    GeckoAsyncLocator class locates in.touch2 devices on your local LAN
    """
    def __init__(self, **kwargs):
        self.spas = []
        self.spa_identifiers = []
        self._static_ip = kwargs.get("static_ip", None)
        if self._static_ip == "":
            self._static_ip = None
        self._has_found_spa = False
        self._started = None

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
            self._has_found_spa = True
      
    @property
    def age(self):
        return time.monotonic() - self._started

    @property
    def has_had_enough_time(self):
        return self.age > GeckoConstants.DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS

    async def discover(self, loop):
        self._started = time.monotonic()
        on_con_lost = loop.create_future()
        transport, protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(on_con_lost),
            family=socket.AF_INET, allow_broadcast=True)

        hello_task = asyncio.create_task(protocol.add_receive_handler(
            GeckoHelloProtocolHandler.broadcast(on_handled=self._on_discovered)
        ))

        while self.age < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
            protocol.queue_send(
                GeckoHelloProtocolHandler.broadcast(),
                GeckoHelloProtocolHandler.broadcast_address(
                    static_ip=self._static_ip
                ),
            )

            if self.has_had_enough_time:
                if len(self.spas) > 0:
                    _LOGGER.info("Found %d spas ... %s", len(self.spas), self.spas)
                    break
            if self._has_found_spa:
                break
            await asyncio.sleep(1)

        transport.close()
        await hello_task
