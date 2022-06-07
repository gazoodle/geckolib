""" GeckoAsyncUdpProtocol - Gecko Async UDP protocol implementation """

import asyncio
import logging

from ..config import GeckoConfig, config_sleep
from .udp_protocol_handler import GeckoUdpProtocolHandler
from .async_peekablequeue import AsyncPeekableQueue
from typing import Optional, Callable, TypeVar

_LOGGER = logging.getLogger(__name__)


class DbgLock(asyncio.Lock):
    def __init__(self):
        super().__init__()

    async def __aenter__(self) -> None:
        t = asyncio.current_task()
        _LOGGER.debug("About to acquire lock for task %s", t.get_name())
        await super().__aenter__()
        _LOGGER.debug("Lock acquired for task %s", t.get_name())
        return None

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        t = asyncio.current_task()
        _LOGGER.debug("Release lock for task %s", t.get_name())
        return await super().__aexit__(exc_type, exc, tb)


class GeckoAsyncUdpProtocol(asyncio.DatagramProtocol):
    """Gecko in.touch2 uses UDP to communicate. This class is an async
    UDP protocol handler for asyncio. It dispatches to classes derived
    from GeckoUdpProtocolHandler. Since it doesn't need to be thread safe
    it's a good deal more simple that its predecessor
    """

    def __init__(self, on_connection_lost, destination) -> None:
        self.transport = None
        self._on_connection_lost = on_connection_lost
        self._destination = destination

        self._sequence_counter_protocol = 0
        self._sequence_counter_command = 191
        self._queue = AsyncPeekableQueue()
        self._lock = DbgLock()  # asyncio.Lock()

    @property
    def Lock(self):
        return self._lock

    def connection_made(self, transport) -> None:
        _LOGGER.debug("GeckoAsyncUdpProtocol: connection made to %s", transport)
        self.transport = transport

    def connection_lost(self, exc) -> None:
        _LOGGER.debug(
            "GeckoAsyncUdpProtocol: connection lost from %s (%s)", self.transport, exc
        )
        self.transport = None
        if self._on_connection_lost is not None:
            self._on_connection_lost.set_result(True)

    def error_received(self, exc) -> None:
        _LOGGER.exception("GeckoAsyncUdpProtocol: Exception received %s", exc)
        # TODO: What do we want to do with this?

    @property
    def isopen(self) -> bool:
        """Check to see if the transport is connected"""
        return self.transport is not None

    def disconnect(self) -> None:
        self.connection_lost(None)

    @property
    def queue(self) -> AsyncPeekableQueue:
        return self._queue

    def queue_send(
        self, protocol_handler: GeckoUdpProtocolHandler, destination=None
    ) -> None:
        """Queue a message to be sent async later"""
        if not self.isopen:
            _LOGGER.warning("Cannot queue message as transport is closed")
            return
        assert self.transport is not None
        if destination is None:
            destination = self._destination
        protocol_handler.last_destination = destination

        send_bytes = protocol_handler.send_bytes
        _LOGGER.debug("Sending %s to %s", send_bytes, destination)
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
        _LOGGER.debug("Received %s from %s", data, addr)
        self.queue.put_nowait((data, addr))

    T = TypeVar("T", bound="GeckoUdpProtocolHandler")

    async def get(
        self,
        create_func: Callable[[], T],
        destination: Optional[tuple] = None,
        retry_count: int = GeckoConfig.PROTOCOL_RETRY_COUNT,
    ) -> Optional[T]:

        _LOGGER.debug("Async get started")
        async with self.Lock:

            while retry_count > 0:

                # Create the request
                request = create_func()
                # Queue it for delivery
                self.queue_send(request, destination)

                # Wait for a response up to a certain amount of time
                if await request.wait_for_response(self):
                    # If handled, then return the handler which ought
                    # to contain the information as requested
                    return request

                # Loop for retry
                retry_count -= 1

                # Pause between retries
                await config_sleep(GeckoConfig.PAUSE_BETWEEN_RETRIES_IN_SECONDS)

            return None

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} on {self.transport!r}\n"
            f" isopen: {self.isopen}"
        )
