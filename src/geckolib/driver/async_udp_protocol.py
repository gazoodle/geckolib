""" GeckoAsyncUdpProtocol - Gecko Async UDP protocol implementation """

import socket
import asyncio
import logging
import time
from .udp_protocol_handler import GeckoUdpProtocolHandler
from .async_peekablequeue import AsyncPeekableQueue

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncUdpProtocol(asyncio.DatagramProtocol):
    """Gecko in.touch2 uses UDP to communicate. This class is an async
    UDP protocol handler for asyncio. It dispatches to classes derived
    from GeckoUdpProtocolHandler. Since it doesn't need to be thread safe
    it's a good deal more simple that its predecessor
    """

    def __init__(self, on_connection_lost=None):
        self.transport = None
        self._on_connection_lost = on_connection_lost

        self._busy_count = 0
        self._sequence_counter = 0
        self._last_send_time = time.monotonic()

        self._queue = AsyncPeekableQueue()

    def connection_made(self, transport):
        _LOGGER.debug("GeckoAsyncUdpProtocol: connection made to %s", transport)
        self.transport = transport

    def connection_lost(self, exc):
        _LOGGER.debug("GeckoAsyncUdpProtocol: connection lost from %s (%s)", self.transport, exc)
        self.transport = None
        if self._on_connection_lost is not None:
            self._on_connection_lost.set_result(True)

    def error_received(self, exc):
        _LOGGER.exception("GeckoAsyncUdpProtocol: Exception received %s", exc)
        # TODO: What do we want to do with this?


    @property
    def isopen(self):
        """Check to see if the transport is connected"""
        return self.transport is not None

    def disconnect(self):
        self.connection_lost(None)

    @property
    def queue(self):
        return self._queue

    @property
    def isbusy(self):
        """Check to see if the socket is busy"""
        if self._send_handlers:
            return True
        return self._busy_count > 0

    def queue_send(self, protocol_handler: GeckoUdpProtocolHandler, destination: tuple):
        """Queue a message to be sent async later"""
        if destination is None:
            raise AssertionError(
                f"Cannot have destination set to None for {protocol_handler}")
        # For convenience, the entire destination sometimes gets passed in,
        # this fixes it to be just the address and port
        if len(destination) > 2:
            destination = (destination[0], destination[1])
        protocol_handler.last_destination = destination

        send_bytes = protocol_handler.send_bytes
        _LOGGER.debug("Sending %s to %s", send_bytes, destination)
        self.transport.sendto(send_bytes, destination)
        self._last_send_time = time.monotonic()

    def get_and_increment_sequence_counter(self):
        with self._lock:
            self._sequence_counter += 1
            return self._sequence_counter % 256

    def datagram_received(self, data, addr):
        _LOGGER.debug("Received %s from %s", data, addr)
        self.queue.put_nowait((data, addr))

    def __repr__(self):
        return (
            f"{self.__class__.__name__} on {self.transport!r}\n"
            f" isopen: {self.isopen}"
            f" isbusy: {self.isbusy}"
        )
