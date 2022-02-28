import logging
import time
import asyncio

_LOGGER = logging.getLogger(__name__)


class GeckoUdpProtocolHandler:
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

    def __init__(self, **kwargs):
        # Send functionality
        self._send_bytes = kwargs.get("send_bytes", None)
        self.last_destination = None

        # Receive functionality
        self._on_handled = kwargs.get("on_handled", None)

        # Lifetime functionality
        self._start_time = time.monotonic()
        self._timeout_in_seconds = kwargs.get("timeout", 0)
        self._retry_count = kwargs.get("retry_count", 0)
        self._on_retry_failed = kwargs.get("on_retry_failed", None)
        self._on_complete = kwargs.get("on_complete", None)
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

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        """Check if you can handle these bytes. If you return True, then your
        handle method will get called and no other handlers will be given a
        chance to process this data. If you return False then the search for a
        suitable handler will continue"""
        return False

    def handle(self, socket, received_bytes: bytes, sender: tuple):
        """Handle this data. This will only be called if you returned True
        from the `can_handle` function. If you wish to remove this handler
        from the system, then you should set the `should_remove_handler`
        member."""

    def handled(self, socket, sender: tuple):
        self._reset_timeout()
        if self._on_handled is not None:
            self._on_handled(self, socket, sender)

    async def consume(self, socket, queue):
        """Async coroutine to handle datagram. Uses the sync functions to
        manage this at present"""
        while True:
            if queue.head is not None:
                data, sender = queue.head
                if self.can_handle(data, sender):
                    queue.pop()
                    self.handle(socket, data, sender)
                    self.handled(socket, sender)
            await asyncio.sleep(0)

            # Here is where retry and so on are handled in async world...
            if self.should_remove_handler:
                _LOGGER.debug("%s needs to be stopped", self)
                if self._on_complete is not None:
                    self._on_complete(self, socket, queue)
                break

    ##########################################################################
    #
    #                         LIFETIME MANAGEMENT
    #
    ##########################################################################
    @property
    def age(self):
        return time.monotonic() - self._start_time

    @property
    def has_timedout(self):
        return (
            self.age > self._timeout_in_seconds
            if self._timeout_in_seconds > 0
            else False
        )

    @property
    def should_remove_handler(self):
        return self._should_remove_handler

    def _reset_timeout(self):
        self._start_time = time.monotonic()

    def retry(self, socket):
        if self._retry_count == 0:
            return False
        self._retry_count -= 1
        _LOGGER.debug("Handler retry count %d", self._retry_count)
        self._reset_timeout()
        if socket is not None:
            # Queue another send
            socket.queue_send(self, self.last_destination)
        return True

    def loop(self, socket):
        """Executed each time around the socket loop"""
        if not self.has_timedout:
            return
        _LOGGER.debug("Handler has timed out")
        if self.retry(socket):
            return
        if self._on_retry_failed is not None:
            self._on_retry_failed(self, socket)

    @staticmethod
    def _default_retry_failed_handler(handler, socket):
        _LOGGER.debug("Default retry failed handler for %r being used", handler)
        handler._should_remove_handler = True

    # Pythonic methods
    def __repr__(self):
        return (
            f"{self.__class__.__name__}(send_bytes={self._send_bytes!r},"
            f" age={self.age}, has_timedout={self.has_timedout},"
            f" should_remove_handler={self.should_remove_handler},"
            f" timeout={self._timeout_in_seconds}s,"
            f" retry_count={self._retry_count}"
            f")"
        )
