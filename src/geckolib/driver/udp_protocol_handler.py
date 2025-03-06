"""GeckoUdpProtocolHandler base class."""

from __future__ import annotations

import asyncio
import logging
import time
from typing import TYPE_CHECKING, Any

from geckolib.config import GeckoConfig, config_sleep

if TYPE_CHECKING:
    from .async_udp_protocol import GeckoAsyncUdpProtocol


from abc import ABC, abstractmethod

_LOGGER = logging.getLogger(__name__)


class GeckoUdpProtocolHandler(ABC):
    """
    Protocol handlers class.

    Manage both sides of a specific conversation part with
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
    or instance decisions, either by overridden methods, or by instance handlers.
    """

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the protocol handler class."""
        # Send functionality
        self._send_bytes = kwargs.get("send_bytes")
        self.last_destination = None

        # Receive functionality
        self._async_on_handled = kwargs.get("async_on_handled")

        # Lifetime functionality
        self._start_time = time.monotonic()
        self._timeout_in_seconds: float = kwargs.get("timeout", 0)
        self._on_retry_failed = kwargs.get("on_retry_failed")
        self._should_remove_handler = False

    ##########################################################################
    #
    #                         SEND FUNCTIONALITY
    #
    ##########################################################################
    @property
    def send_bytes(self) -> bytes:
        """
        The bytes to send to the remote end.

        Either uses the class instancedata _send_bytes or can be overridden
        in a base class.
        """
        if self._send_bytes is None:
            raise NotImplementedError
        return self._send_bytes

    @property
    def timeout_in_seconds(self) -> float:
        """The timeout in seconds."""
        return self._timeout_in_seconds

    ##########################################################################
    #
    #                        RECEIVE FUNCTIONALITY
    #
    ##########################################################################

    @abstractmethod
    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        """
        Check if you can handle these bytes.

        If you return True, then your handle method will get called and no
        more handlers will be given a chance to process this data. If you
        return False then the search for a suitable handler will continue
        """
        return False

    @abstractmethod
    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        """
        Handle this data.

        This will only be called if you returned True from the `can_handle`
        function. If you wish to remove this handler from the system, then
        you should set the `should_remove_handler member.
        """

    ##########################################################################
    #
    #                           ASYNC FUNCTIONALITY
    #
    ##########################################################################

    async def async_handle(self, received_bytes: bytes, sender: tuple) -> None:
        """
        Handle this data.

        This will only be called if you returned True from the `can_handle`
        function. If you wish to remove this handler from the system, then you
        should set the `should_remove_handler` member.
        """
        self.handle(received_bytes, sender)

    async def async_handled(self, sender: tuple) -> None:
        """Handle the data in the base class. Derivatives must call this."""
        self._reset_timeout()
        if self._async_on_handled is not None:
            await self._async_on_handled(self, sender)

    async def wait_for_response(
        self,
        protocol: GeckoAsyncUdpProtocol,
        packet_timeout: int = GeckoConfig.PAUSE_BETWEEN_RETRIES_IN_SECONDS,
    ) -> bool:
        """
        Wait for a response that this command can handle.

        This function doesn't respect the _async_on_handled functionality since its
        use is for inline async stuff.
        """
        assert self.timeout_in_seconds > 0  # noqa: S101
        _LOGGER.debug("Wait for response for %s", self)
        try:
            while True:
                try:
                    await config_sleep(None, "Async UDP handler - wait for response")

                    async with asyncio.timeout(packet_timeout):
                        await protocol.queue.wait()

                    peeked_data = protocol.queue.peek()
                    if peeked_data is None:
                        continue

                    data, sender = peeked_data
                    if self.can_handle(data, sender):
                        protocol.queue.pop()
                        await self.async_handle(data, sender)
                        self._reset_timeout()
                        return False

                except TimeoutError:
                    _LOGGER.debug(
                        "TIMEOUT: Packet timeout for %s threw TimeoutError (%fs)",
                        self,
                        packet_timeout,
                    )
                    return True

        except Exception:
            _LOGGER.exception("wait_for_response loop for %r caught exception", self)
            return True
        finally:
            _LOGGER.debug("wait_for_response loop for %r terminated", self)

    def _can_handle(
        self, _protocol: GeckoAsyncUdpProtocol, received_bytes: bytes, sender: tuple
    ) -> bool:
        """Provide for derived classes to overide."""
        return self.can_handle(received_bytes, sender)

    async def consume(self, protocol: GeckoAsyncUdpProtocol) -> None:
        """Async coroutine to handle datagram."""
        try:
            assert self.timeout_in_seconds == 0  # noqa: S101
            while True:
                await config_sleep(None, f"Async UDP handler - consume for {self}")
                await protocol.queue.wait()

                peeked_data = protocol.queue.peek()
                if peeked_data is None:
                    continue

                data, sender = peeked_data
                if self._can_handle(protocol, data, sender):
                    protocol.queue.pop()
                    await self.async_handle(data, sender)
                    await self.async_handled(sender)

                if self.should_remove_handler:
                    _LOGGER.debug("%s will be removed, consume loop terminating", self)
                    break

        except asyncio.CancelledError:
            _LOGGER.debug("Consume loop for %r cancelled", self)
            raise
        except Exception:
            _LOGGER.exception("Consume loop for %r caught exception", self)
            raise
        finally:
            _LOGGER.debug("Consume loop for %r terminated", self)

    ##########################################################################
    #
    #                         LIFETIME MANAGEMENT
    #
    ##########################################################################
    @property
    def age(self) -> float:
        """Get the age of this handler."""
        return time.monotonic() - self._start_time

    @property
    def should_remove_handler(self) -> bool:
        """Get the should remove handler property."""
        return self._should_remove_handler

    def _reset_timeout(self) -> None:
        self._start_time = time.monotonic()

    @staticmethod
    def default_retry_failed_handler(
        handler: GeckoUdpProtocolHandler, _protocol: GeckoAsyncUdpProtocol
    ) -> None:
        """Handle retry failure."""
        _LOGGER.debug("Default retry failed handler for %r being used", handler)
        handler._should_remove_handler = True

    # Pythonic methods
    def __repr__(self) -> str:
        """Get string representation of this class."""
        return (
            f"{self.__class__.__name__}(send_bytes={self._send_bytes!r},"
            f" age={self.age},"
            f" should_remove_handler={self.should_remove_handler},"
            f" timeout={self.timeout_in_seconds}s"
            f")"
        )
