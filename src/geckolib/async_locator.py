"""Gecko Async Locator class."""

import asyncio
import logging
import socket
import time

from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_taskman import GeckoAsyncTaskMan
from .config import GeckoConfig, config_sleep
from .const import GeckoConstants
from .driver import (
    GeckoAsyncUdpProtocol,
    GeckoHelloProtocolHandler,
    Observable,
)
from .spa_events import GeckoSpaEvent

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncLocator(Observable):
    """GeckoAsyncLocator class locates in.touch2 devices on your local LAN."""

    def __init__(
        self,
        taskman: GeckoAsyncTaskMan,
        event_handler: GeckoSpaEvent.CallBack,
        **kwargs: str | None,
    ) -> None:
        """Init the async locator."""
        super().__init__()
        # Get the arguments
        self._task_man: GeckoAsyncTaskMan = taskman
        self._event_handler: GeckoSpaEvent.CallBack = event_handler
        self._spa_address: str | None = kwargs.get("spa_address")
        if self._spa_address == "":
            self._spa_address = None
        self._spa_identifier: str | None = kwargs.get("spa_identifier")
        if self._spa_identifier == "":
            self._spa_identifier = None

        self._spas: list[GeckoAsyncSpaDescriptor] | None = None
        self._spa_identifiers: list[bytes] = []

        self._has_found_spa: bool = False
        self._started: float | None = None
        self._transport: asyncio.BaseTransport | None = None
        self._protocol: GeckoAsyncUdpProtocol | None = None

    async def _async_on_discovered(
        self, handler: GeckoHelloProtocolHandler, sender: tuple
    ) -> None:
        if handler.spa_identifier in self._spa_identifiers:
            return

        _LOGGER.debug("Discovered spa %s", handler.spa_identifier)
        if (
            self._spa_identifier is not None
            and self._spa_identifier
            != handler.spa_identifier.decode(GeckoConstants.MESSAGE_ENCODING)
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

        assert self._spas is not None  # noqa: S101
        self._spas.append(descriptor)
        await self._event_handler(
            GeckoSpaEvent.LOCATING_DISCOVERED_SPA, spa_descriptor=descriptor
        )

        if self._spa_address is not None or self._spa_identifier is not None:
            _LOGGER.debug(
                "Spa address or identifier was specified, so spa must have been found"
            )
            self._has_found_spa = True

    @property
    def age(self) -> float:
        """Get the ago of this locator."""
        if self._started is None:
            return 0
        return time.monotonic() - self._started

    @property
    def spas(self) -> list[GeckoAsyncSpaDescriptor] | None:
        """Get the list of spas."""
        return self._spas

    @property
    def has_had_enough_time(self) -> bool:
        """Return if we have had enough time to discover the spas."""
        return self.age > GeckoConfig.DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS

    @property
    def is_running(self) -> bool:
        """Return the running state."""
        if self._started is None:
            return False
        return self._protocol is not None

    async def _broadcast_loop(self, hello_handler: GeckoHelloProtocolHandler) -> None:
        """Send a discovery message every second."""
        try:
            while True:
                if self._protocol is not None:
                    self._protocol.queue_send(
                        hello_handler,
                        GeckoHelloProtocolHandler.broadcast_address(
                            static_ip=self._spa_address
                        ),
                    )
                await config_sleep(
                    GeckoConstants.ASYNC_LOCATOR_BROADCAST_SLEEP,
                    "Async locator broadcast loop",
                )
        except asyncio.CancelledError:
            _LOGGER.debug("Broadcast loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("Broadcast loop caught exception")
            raise

    async def discover(self) -> None:
        """Discover spas on the local lan."""
        loop = asyncio.get_running_loop()
        on_con_lost = asyncio.Event()
        self._transport, _protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(self._task_man, on_con_lost, None),
            family=socket.AF_INET,
            allow_broadcast=True,
        )
        try:
            assert isinstance(_protocol, GeckoAsyncUdpProtocol)  # noqa: S101
            self._protocol = _protocol
            assert self._transport is not None  # noqa: S101
            self._spas = []

            hello_handler = GeckoHelloProtocolHandler.broadcast(
                async_on_handled=self._async_on_discovered
            )
            self._task_man.add_task(
                hello_handler.consume(self._protocol), "Hello handler", "LOC"
            )
            self._task_man.add_task(
                self._broadcast_loop(hello_handler), "Broadcast loop", "LOC"
            )

            self._started = time.monotonic()
            self._on_change(self)

            while self.age < GeckoConfig.DISCOVERY_TIMEOUT_IN_SECONDS:
                if self.has_had_enough_time and len(self._spas) > 0:
                    _LOGGER.info("Found %d spas ... %s", len(self._spas), self._spas)
                    break
                if self._has_found_spa:
                    break
                await config_sleep(
                    GeckoConstants.ASYNC_LOCATOR_BROADCAST_SLEEP,
                    "Async locator discovery loop",
                )

        finally:
            _LOGGER.debug("Discovery complete, close transport")
            self._task_man.cancel_key_tasks("LOC")
            self._transport.close()
            self._transport = None
            self._protocol = None
            self._on_change(self)
