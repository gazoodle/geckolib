"""GeckoAsyncUdpProtocol - Gecko Async UDP protocol implementation."""

import asyncio
import logging
from collections.abc import Callable
from types import TracebackType
from typing import Any, TypeVar

from geckolib.async_taskman import GeckoAsyncTaskMan
from geckolib.config import GeckoConfig

from .async_peekablequeue import AsyncPeekableQueue
from .udp_protocol_handler import GeckoUdpProtocolHandler

_LOGGER = logging.getLogger(__name__)


class DbgLock(asyncio.Lock):
    """Class to debug locking semantics."""

    def __init__(self) -> None:
        """Initialize the class."""
        super().__init__()

    async def __aenter__(self) -> None:
        """Async with."""
        t = asyncio.current_task()
        _LOGGER.debug("LOCK: About to acquire for task `%s`", t.get_name())
        _LOGGER.debug(self)
        await super().__aenter__()
        _LOGGER.debug("LOCK: acquired for task `%s`", t.get_name())

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        """Async with."""
        t = asyncio.current_task()
        _LOGGER.debug("LOCK: About to release for task %s", t.get_name())
        await super().__aexit__(exc_type, exc, tb)
        _LOGGER.debug("LOCK: Released for task `%s`", t.get_name())
        _LOGGER.debug(self)


class GeckoAsyncUdpProtocol(asyncio.DatagramProtocol):
    """
    Gecko in.touch2 uses UDP to communicate.

    This class is an async UDP protocol handler for asyncio. It dispatches
    to classes derived from GeckoUdpProtocolHandler. Since it doesn't need
    to be thread safe it's a good deal more simple that its predecessor.
    """

    def __init__(
        self,
        taskman: GeckoAsyncTaskMan,
        on_connection_lost: asyncio.Event,
        destination: tuple[str, str],
    ) -> None:
        """Initialize the protocol class."""
        self.transport = None
        self._on_connection_lost: asyncio.Event = on_connection_lost
        self._destination = destination

        self._sequence_counter_protocol = 0
        self._sequence_counter_command = 191
        self._queue = AsyncPeekableQueue()
        self._taskman = taskman
        self._lock = asyncio.Lock()
        _LOGGER.debug("AsyncUdpProtocol started.")

    @property
    def lock(self) -> asyncio.Lock:
        """Get the lock object."""
        return self._lock

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        """Made connection."""
        _LOGGER.debug("GeckoAsyncUdpProtocol: connection made to %s.", transport)
        self.transport: asyncio.BaseTransport | None = transport
        self._on_connection_lost.clear()

    def connection_lost(self, exc: BaseException | None) -> None:
        """Lost connection."""
        _LOGGER.debug(
            "GeckoAsyncUdpProtocol: connection lost from %s (%s)", self.transport, exc
        )
        if self.transport is not None:
            self.transport.close()
            self.transport = None
        self._on_connection_lost.set()

    def error_received(self, exc: BaseException) -> None:
        """Error received."""
        _LOGGER.exception("GeckoAsyncUdpProtocol: Exception received %s", exc)

    @property
    def isopen(self) -> bool:
        """Check to see if the transport is connected."""
        return self.transport is not None

    def disconnect(self) -> None:
        """Disconnect the protocol from the socket."""
        if self.queue:
            _LOGGER.warning(
                "UDP protocol datagram queue not empty during disconnection",
            )
            while self.queue:
                item = self.queue.pop()
                _LOGGER.debug("Unprocessed[%s]", item)
        self.connection_lost(None)

    @property
    def queue(self) -> AsyncPeekableQueue:
        """Get the datagram queue."""
        return self._queue

    def queue_send(
        self,
        protocol_handler: GeckoUdpProtocolHandler,
        destination: tuple | None = None,
    ) -> None:
        """Queue a message to be sent async later."""
        if not self.isopen:
            _LOGGER.warning("Cannot queue message as transport is closed")
            return
        assert self.transport is not None  # noqa: S101
        if destination is None:
            destination = self._destination
        protocol_handler.last_destination = destination

        send_bytes = protocol_handler.send_bytes
        destination = (destination[0], destination[1])
        _LOGGER.debug("Sending %s to %s", send_bytes, destination)
        # transport.sendto is a non-blocking call.
        self.transport.sendto(send_bytes, destination)

    def get_and_increment_sequence_counter(self, *, command: bool = False) -> int:
        """Get (and increment) the sequence counter."""
        if command:
            if self._sequence_counter_command == 255:  # noqa: PLR2004
                self._sequence_counter_command = 191
            self._sequence_counter_command += 1
            return self._sequence_counter_command
        if self._sequence_counter_protocol == 191:  # noqa: PLR2004
            self._sequence_counter_protocol = 0
        self._sequence_counter_protocol += 1
        return self._sequence_counter_protocol

    def datagram_received(self, data: Any, addr: tuple) -> None:
        """Handle datagrame."""
        _LOGGER.debug("Datagram received: %s from %s", data, addr)
        if b"SPACK" in data or b"STATQ" in data:
            _LOGGER.debug("Put on command queue")
            self.queue.push_command((data, addr))
        else:
            self.queue.push((data, addr))

    T = TypeVar("T", bound="GeckoUdpProtocolHandler")

    async def get(
        self,
        create_func: Callable[[], T],
        destination: tuple | None = None,
        packet_timeout: int = GeckoConfig.PAUSE_BETWEEN_RETRIES_IN_SECONDS,
    ) -> T | None:
        """Get the response to the request."""
        async with self.lock:
            # Create the request
            request = create_func()

            try:
                async with asyncio.timeout(request.timeout_in_seconds):
                    while True:
                        # Queue it for delivery
                        self.queue_send(request, destination)

                        # Wait for a response up to a certain amount of time
                        if not await request.wait_for_response(self, packet_timeout):
                            # If handled, then return the handler which ought
                            # to contain the information as requested
                            return request

                        # Create a clean new request
                        request = create_func()

            except TimeoutError:
                _LOGGER.debug(
                    "TIMEOUT: Handler %s threw TimeoutError (%fs)",
                    request,
                    request.timeout_in_seconds,
                )
