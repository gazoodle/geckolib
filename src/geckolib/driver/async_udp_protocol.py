""" GeckoAsyncUdpProtocol - Gecko Async UDP protocol implementation """

import socket
import asyncio
import logging
import time
from .udp_protocol_handler import GeckoUdpProtocolHandler

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncUdpProtocol(asyncio.DatagramProtocol):
    """Gecko in.touch2 uses UDP to communicate. This class is an async
    UDP protocol handler for asyncio. It dispatches to classes derived
    from GeckoUdpProtocolHandler. Since it doesn't need to be thread safe
    it's a good deal more simple that its predecessor
    """

    _PORT = 10022
    _SOCKET_TIMEOUT = 0.05
    _MAX_PACKET_SIZE = 8192
    _SENDING_THROTTLE_RATE_PER_SECOND = 50

    def __init__(self, on_connection_lost=None):
        self.transport = None
        self._on_connection_lost = on_connection_lost

        self._receive_handlers = []
        self._busy_count = 0
        self._sequence_counter = 0
        self._last_send_time = time.monotonic()

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
    def isbusy(self):
        """Check to see if the socket is busy"""
        if self._send_handlers:
            return True
        if self._receive_handlers:
            return True
        return self._busy_count > 0

    async def add_receive_handler(self, protocol_handler: GeckoUdpProtocolHandler):
        """Add a receive handler to the list of available handlers"""
        self._receive_handlers.append(protocol_handler)
        while self.transport is not None:


            await asyncio.sleep(0)

        # Remove it now it's no longer needed
        self._receive_handlers.remove(protocol_handler)
        _LOGGER.debug("add_received_handler for %s stopped", protocol_handler)

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
        for handler in self._receive_handlers:
            if handler.can_handle(data, addr):
                try:
                    handler.handle(self, data, addr)
                    handler.handled(self, addr)
                except Exception:
                    _LOGGER.exception("Unhandled exception in receive_handler func")
                finally:
                    self._cleanup_handlers()
                    return

        _LOGGER.debug("Couldn't find new handler for %s", data)

    def _cleanup_handlers(self):
        remove_handlers = []

        # Build list of handlers that need to be removed
        remove_handlers = [
            handler
            for handler in self._receive_handlers
            if handler.should_remove_handler
        ]

        if remove_handlers:
            _LOGGER.debug("Removed timedout handlers %s", remove_handlers)

            # Remove them from the collection
            self._receive_handlers = [
                handler
                for handler in self._receive_handlers
                if handler not in remove_handlers
            ]

            if remove_handlers:
                _LOGGER.debug("Remaining handlers %s", self._receive_handlers)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} on {self.transport!r}\n"
            f"  receive_handlers={self._receive_handlers!r},\n"
            f"  isopen: {self.isopen}"
            f" isbusy: {self.isbusy}"
        )
