""" Gecko Async Locator class """

import logging
import time
import asyncio
import socket

from .async_tasks import AsyncTasks
from .driver import (
    GeckoHelloProtocolHandler,
    GeckoAsyncUdpProtocol,
)
from .const import GeckoConstants
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .driver import Observable
from typing import Optional, List

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncLocator(Observable):
    """
    GeckoAsyncLocator class locates in.touch2 devices on your local LAN
    """

    def __init__(self, taskman: AsyncTasks, **kwargs: Optional[str]) -> None:
        super().__init__()
        # Get the arguments
        self._task_man: AsyncTasks = taskman
        self._spa_address: Optional[str] = kwargs.get("spa_address", None)
        if self._spa_address == "":
            self._spa_address = None
        self._spa_identifier: Optional[str] = kwargs.get("spa_identifier", None)
        if self._spa_identifier == "":
            self._spa_identifier = None

        self.spas: Optional[List[GeckoAsyncSpaDescriptor]] = None
        self._spa_identifiers: List[bytes] = []

        self._has_found_spa: bool = False
        self._started: Optional[float] = None
        self._transport: Optional[asyncio.BaseTransport] = None
        self._protocol: Optional[GeckoAsyncUdpProtocol] = None

    def _on_discovered(
        self, handler: GeckoHelloProtocolHandler, _socket, sender: tuple
    ) -> None:
        if handler.spa_identifier in self._spa_identifiers:
            return

        _LOGGER.debug("Discovered spa %s", handler.spa_identifier)
        if self._spa_identifier is not None:
            if self._spa_identifier != handler.spa_identifier.decode(
                GeckoConstants.MESSAGE_ENCODING
            ):
                _LOGGER.debug("But we're not interested in that, so ignore it")
                return

        self._on_change(self)
        self._spa_identifiers.append(handler.spa_identifier)
        descriptor = GeckoAsyncSpaDescriptor(
            handler.spa_identifier,
            handler.spa_name,
            sender,
        )

        if self.spas is None:
            self.spas = []
        self.spas.append(descriptor)

        if self._spa_address is not None or self._spa_identifier is not None:
            _LOGGER.debug(
                "Spa address or identifier was specified, so spa must have been found"
            )
            self._has_found_spa = True

    @property
    def age(self) -> float:
        if self._started is None:
            return 0
        return time.monotonic() - self._started

    @property
    def has_had_enough_time(self) -> bool:
        return self.age > GeckoConstants.DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS

    @property
    def is_running(self) -> bool:
        if self._started is None:
            return True
        return self._protocol is not None

    async def discover(self) -> None:
        loop = asyncio.get_running_loop()
        on_con_lost = loop.create_future()
        self._transport, _protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(on_con_lost, None),
            family=socket.AF_INET,
            allow_broadcast=True,
        )
        assert isinstance(_protocol, GeckoAsyncUdpProtocol)
        self._protocol = _protocol
        assert self._transport is not None

        hello_handler = GeckoHelloProtocolHandler.broadcast(
            on_handled=self._on_discovered
        )
        self._task_man.add_task(hello_handler.consume(self._protocol), "Hello handler")

        self._started = time.monotonic()
        self._on_change(self)
        while self.age < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
            self._protocol.queue_send(
                hello_handler,
                GeckoHelloProtocolHandler.broadcast_address(
                    static_ip=self._spa_address
                ),
            )
            await asyncio.sleep(1)
            if self.has_had_enough_time:
                if self.spas is not None and len(self.spas) > 0:
                    _LOGGER.info("Found %d spas ... %s", len(self.spas), self.spas)
                    break
            if self._has_found_spa:
                break

        _LOGGER.debug("Discovery complete, close transport")
        self._transport.close()
        self._transport = None
        self._protocol = None
        self._on_change(self)

    @property
    def status_line(self) -> str:
        if self.is_running:
            return "Discovering spas"
        elif self.spas is None:
            return "No spas found on your network"
        else:
            return "Choose spa to connect to"
