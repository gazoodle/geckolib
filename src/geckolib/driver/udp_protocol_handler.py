"""GeckoUdpProtocolHandler base class"""

from __future__ import annotations
import logging
import time
import asyncio
from typing import TYPE_CHECKING

from geckolib.const import GeckoConstants

if TYPE_CHECKING:
    from .async_udp_protocol import GeckoAsyncUdpProtocol


from abc import ABC, abstractmethod

_LOGGER = logging.getLogger(__name__)


class GeckoUdpProtocolHandler(ABC):
    """
    Protocol handlers manage both sides of a specific conversation part with
    a remote end.

    The protocol is either initiated by a client or by a server, but either
    way a query should always met with a response from the remote end

    Both sides may instantiate listening handlers which will deal with
    unsolicited requests from remote clients and will respond so that the
    remote end knows the request was received and they may also send a query
    to the remote end, expecting a response to confirm receipt.

    A message sent will either make it to the destination, or it won't. Since
    this protocol is built on UDP, we have to cook our own timeout/retry
    mechanism to ensure delivery ... oddly this is precisely what TCP already
    does, no idea why this wasn't considered but hey-ho, this is all a bit of
    fun anyway!

    The base protocol handler will manage the lifetime of the handlers within
    the socket, and mechanisms are in place to allow retries to be handled
    with failure exit points available to allow clients to make class decisions
    or instance decisions, either by overridden methods, or by instance handlers

    """

    def __init__(self, **kwargs) -> None:
        # Send functionality
        self._send_bytes = kwargs.get("send_bytes", None)
        self.last_destination = None

        # Receive functionality
        self._on_handled = kwargs.get("on_handled", None)
        self._async_on_handled = kwargs.get("async_on_handled", None)

        # Lifetime functionality
        self._start_time = time.monotonic()
        self._timeout_in_seconds = kwargs.get("timeout", 0)
        self._retry_count = kwargs.get("retry_count", 0)
        self._on_retry_failed = kwargs.get("on_retry_failed", None)
        self._should_remove_handler = False

    ##########################################################################
    #
    #                         SEND FUNCTIONALITY
    #
    ##########################################################################
    @property
    def send_bytes(self) -> bytes:
        """The bytes to send to the remote end. Either uses the class instance
        data _send_bytes or can be overridden in a base class"""
        if self._send_bytes is None:
            raise NotImplementedError
        return self._send_bytes

    ##########################################################################
    #
    #                        RECEIVE FUNCTIONALITY
    #
    ##########################################################################

    @abstractmethod
    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        """Check if you can handle these bytes. If you return True, then your
        handle method will get called and no other handlers will be given a
        chance to process this data. If you return False then the search for a
        suitable handler will continue"""
        return False

    @abstractmethod
    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        """Handle this data. This will only be called if you returned True
        from the `can_handle` function. If you wish to remove this handler
        from the system, then you should set the `should_remove_handler`
        member."""

    def handled(self, sender: tuple) -> None:
        """Base class implementation for when the data has been handled"""
        self._reset_timeout()
        assert self._async_on_handled is None
        if self._on_handled is not None:
            self._on_handled(self, sender)

    ##########################################################################
    #
    #                           ASYNC FUNCTIONALITY
    #
    ##########################################################################

    async def async_handle(self, received_bytes: bytes, sender: tuple) -> None:
        """Handle this data. This will only be called if you returned True
        from the `can_handle` function. If you wish to remove this handler
        from the system, then you should set the `should_remove_handler`
        member."""
        self.handle(received_bytes, sender)

    async def async_handled(self, sender: tuple) -> None:
        """Base class implementation for when the data has been handled"""
        self._reset_timeout()
        assert self._on_handled is None
        if self._async_on_handled is not None:
            await self._async_on_handled(self, sender)

    async def wait_for_response(self, protocol: GeckoAsyncUdpProtocol) -> bool:
        """Wait for a response that this command can handle, return True if handled,
        False if timed-out.

        This function doesn't respect the _on_handled functionality since its
        use is for inline async stuff"""
        assert self._timeout_in_seconds > 0
        while True:
            if protocol.queue.head is not None:
                data, sender = protocol.queue.head
                if self.can_handle(data, sender):
                    protocol.queue.pop()
                    await self.async_handle(data, sender)
                    self._reset_timeout()
                    return True

            if self.has_timedout:
                _LOGGER.debug("Handler %s timed out", self)
                return False

            await asyncio.sleep(GeckoConstants.ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD)

    async def consume(self, protocol: GeckoAsyncUdpProtocol) -> None:
        """Async coroutine to handle datagram."""

        assert self._timeout_in_seconds == 0
        while True:
            if protocol.queue.head is not None:
                data, sender = protocol.queue.head
                if self.can_handle(data, sender):
                    protocol.queue.pop()
                    await self.async_handle(data, sender)
                    await self.async_handled(sender)

            await asyncio.sleep(GeckoConstants.ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD)

            if self.should_remove_handler:
                _LOGGER.debug("%s will be removed, consume loop terminating", self)
                break

    ##########################################################################
    #
    #                         LIFETIME MANAGEMENT
    #
    ##########################################################################
    @property
    def age(self) -> float:
        return time.monotonic() - self._start_time

    @property
    def has_timedout(self) -> bool:
        return (
            self.age > self._timeout_in_seconds
            if self._timeout_in_seconds > 0
            else False
        )

    @property
    def should_remove_handler(self) -> bool:
        return self._should_remove_handler

    def _reset_timeout(self) -> None:
        self._start_time = time.monotonic()

    def retry(self, socket) -> bool:
        if self._retry_count == 0:
            return False
        self._retry_count -= 1
        _LOGGER.debug("Handler retry count %d", self._retry_count)
        self._reset_timeout()
        if socket is not None:
            # Queue another send
            socket.queue_send(self, self.last_destination)
        return True

    def loop(self, socket) -> None:
        """Executed each time around the socket loop"""
        if not self.has_timedout:
            return
        _LOGGER.debug(f"Handler {self.__class__.__name__} has timed out")
        if self.retry(socket):
            return
        if self._on_retry_failed is not None:
            self._on_retry_failed(self, socket)

    @staticmethod
    def _default_retry_failed_handler(handler, socket) -> None:
        _LOGGER.debug("Default retry failed handler for %r being used", handler)
        handler._should_remove_handler = True

    # Pythonic methods
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(send_bytes={self._send_bytes!r},"
            f" age={self.age}, has_timedout={self.has_timedout},"
            f" should_remove_handler={self.should_remove_handler},"
            f" timeout={self._timeout_in_seconds}s,"
            f" retry_count={self._retry_count}"
            f")"
        )
