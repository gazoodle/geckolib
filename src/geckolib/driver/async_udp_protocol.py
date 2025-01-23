"""GeckoAsyncUdpProtocol - Gecko Async UDP protocol implementation."""

import asyncio
import logging
from operator import contains
from typing import Callable, Optional, TypeVar

from ..async_taskman import GeckoAsyncTaskMan
from ..config import GeckoConfig, config_sleep
from .async_peekablequeue import AsyncPeekableQueue
from .udp_protocol_handler import GeckoUdpProtocolHandler

_LOGGER = logging.getLogger(__name__)


class DbgLock(asyncio.Lock):
    """Class to debug locking semantics."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()

    async def __aenter__(self) -> None:
        """Async with."""
        t = asyncio.current_task()
        _LOGGER.debug("LOCK: About to acquire for task `%s`", t.get_name())
        _LOGGER.debug(self)
        await super().__aenter__()
        _LOGGER.debug("LOCK: acquired for task `%s`", t.get_name())
        return None

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
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
        self, taskman: GeckoAsyncTaskMan, on_connection_lost: asyncio.Event, destination
    ) -> None:
        """Initialize the protocol class."""
        self.transport = None
        self._on_connection_lost: asyncio.Event = on_connection_lost
        self._destination = destination

        self._sequence_counter_protocol = 0
        self._sequence_counter_command = 191
        self._queue = AsyncPeekableQueue()
        self._taskman = taskman
        # self._lock = DbgLock()  # asyncio.Lock()
        self._lock = asyncio.Lock()

    @property
    def Lock(self):
        return self._lock

    def connection_made(self, transport) -> None:
        _LOGGER.debug("GeckoAsyncUdpProtocol: connection made to %s", transport)
        self.transport = transport
        self._on_connection_lost.clear()

    def connection_lost(self, exc) -> None:
        _LOGGER.debug(
            "GeckoAsyncUdpProtocol: connection lost from %s (%s)", self.transport, exc
        )
        if self.transport is not None:
            self.transport.close()
            self.transport = None
        self._on_connection_lost.set()

    def error_received(self, exc) -> None:
        _LOGGER.exception("GeckoAsyncUdpProtocol: Exception received %s", exc)
        # TODO: What do we want to do with this?

    @property
    def isopen(self) -> bool:
        """Check to see if the transport is connected."""
        return self.transport is not None

    def disconnect(self) -> None:
        self.connection_lost(None)

    @property
    def queue(self) -> AsyncPeekableQueue:
        return self._queue

    def queue_send(
        self, protocol_handler: GeckoUdpProtocolHandler, destination=None
    ) -> None:
        """Queue a message to be sent async later."""
        if not self.isopen:
            _LOGGER.warning("Cannot queue message as transport is closed")
            return
        assert self.transport is not None
        if destination is None:
            destination = self._destination
        protocol_handler.last_destination = destination

        send_bytes = protocol_handler.send_bytes
        _LOGGER.debug("Sending %s to %s", send_bytes, destination)
        # transport.sendto is a non-blocking call.
        self.transport.sendto(send_bytes, destination)

    def get_and_increment_sequence_counter(self, command: bool) -> int:
        if command:
            if self._sequence_counter_command == 255:
                self._sequence_counter_command = 191
            self._sequence_counter_command += 1
            return self._sequence_counter_command
        else:
            if self._sequence_counter_protocol == 191:
                self._sequence_counter_protocol = 0
            self._sequence_counter_protocol += 1
            return self._sequence_counter_protocol

    def datagram_received(self, data, addr) -> None:
        _LOGGER.debug("Datagram received: %s from %s", data, addr)
        self.queue.push((data, addr))

    T = TypeVar("T", bound="GeckoUdpProtocolHandler")

    async def get(
        self,
        create_func: Callable[[], T],
        destination: tuple | None = None,
        retry_count: int = GeckoConfig.PROTOCOL_RETRY_COUNT,
    ) -> T | None:
        """Get the response to the request."""
        # _LOGGER.debug("Async get started")
        try:
            async with self.Lock:
                while retry_count > 0:
                    # Create the request
                    request = create_func()

                    # Queue it for delivery
                    self.queue_send(request, destination)

                    # Wait for a response up to a certain amount of time
                    await request.wait_for_response(self)
                    if not request.has_timedout:
                        # If handled, then return the handler which ought
                        # to contain the information as requested
                        return request

                    # Loop for retry
                    retry_count -= 1

                    # Pause between retries
                    await config_sleep(
                        GeckoConfig.PAUSE_BETWEEN_RETRIES_IN_SECONDS,
                        "Async UDP protocol retry",
                    )
            return None
        finally:
            pass
            # _LOGGER.debug(
            #    "Async get for `%s` finished.", asyncio.current_task().get_name()
            # )
