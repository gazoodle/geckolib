""" GeckoUdpSocket - Gecko UDP socket implementation """

import socket
import logging
import threading
import time
from .udp_protocol_handler import GeckoUdpProtocolHandler

_LOGGER = logging.getLogger(__name__)


class GeckoUdpSocket:
    """Gecko in.touch2 uses UDP to communicate. This class is a wrapper around
    a socket and a thread and serviced by classes derived from GeckoUdpProtocolHandler
    """

    _PORT = 10022
    _SOCKET_TIMEOUT = 0.05
    _MAX_PACKET_SIZE = 8192
    _SENDING_THROTTLE_RATE_PER_SECOND = 50

    def __init__(self, socket=None):
        self._socket = socket
        self._exit_event = None
        self._thread = None
        self._lock = threading.Lock()
        self._send_handlers = []
        self._receive_handlers = []
        self._busy_count = 0
        self._sequence_counter_protocol = 0
        self._sequence_counter_command = 191
        self._last_send_time = time.monotonic()

    def __enter__(self):
        if self._socket is None:
            self._socket = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
            )
        self._socket.settimeout(self._SOCKET_TIMEOUT)
        self._exit_event = threading.Event()
        self._thread = threading.Thread(target=self._thread_func, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, *args):
        if self._exit_event:
            self._exit_event.set()
        if self._thread:
            self._thread.join()
            self._thread = None
        if self._socket:
            self._socket.close()
            self._socket = None

    class _BusyLock:
        def __init__(self, socket):
            self._socket = socket

        def __enter__(self):
            with self._socket._lock:
                self._socket._busy_count += 1

        def __exit__(self, *args):
            with self._socket._lock:
                self._socket._busy_count -= 1

    def open(self):
        """Start the use of this UDP socket object if not used
        in a `with` statement"""
        self.__enter__()

    def close(self):
        """Finish the use of this UDP socket object if not used
        in a `with` statement"""
        self.__exit__()

    @property
    def isopen(self):
        """Check to see if the socket is open"""
        if not self._exit_event:
            return False
        return not self._exit_event.is_set()

    @property
    def isbusy(self):
        """Check to see if the socket is busy"""
        if self._send_handlers:
            return True
        if self._receive_handlers:
            return True
        return self._busy_count > 0

    def wait(self, timeout):
        """Wait for a timeout, respecting the exit event"""
        self._exit_event.wait(timeout)

    def bind(self):
        """Bind this UDP socket to the local address and port"""
        self._socket.bind(("", self._PORT))

    def enable_broadcast(self):
        """Set this UDP socket to support broadcast"""
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def add_receive_handler(self, protocol_handler: GeckoUdpProtocolHandler):
        """Add a receive handler to the list of available handlers"""
        with self._lock:
            self._receive_handlers.append(protocol_handler)

    def remove_receive_handler(self, protocol_handler: GeckoUdpProtocolHandler):
        """Remove a receive handler from the list of available handlers"""
        with self._lock:
            self._receive_handlers.remove(protocol_handler)

    def queue_send(self, protocol_handler: GeckoUdpProtocolHandler, destination: tuple):
        """Queue a message to be sent by the worker thread"""
        with self._lock:
            self._send_handlers.append((protocol_handler, destination))

    def get_and_increment_sequence_counter(self, command: bool):
        with self._lock:
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

    def _process_send_requests(self):
        # Throttle the sending rate to prevent message loss
        if (time.monotonic() - self._last_send_time) < (
            1.0 / self._SENDING_THROTTLE_RATE_PER_SECOND
        ):
            return

        with GeckoUdpSocket._BusyLock(self):
            # Assume there are no send requests
            send_handler = None
            # Play safely with clients, and minimize the time spend locked
            with self._lock:
                if self._send_handlers:
                    send_handler = self._send_handlers.pop(0)
            # If there is a handler, then use it
            if send_handler:
                try:
                    send_bytes = send_handler[0].send_bytes
                    destination = send_handler[1]
                    if destination is None:
                        raise AssertionError(
                            f"Cannot have destination set to None for {send_handler}"
                        )
                    # For convenience, the entire destination sometimes gets passed in,
                    # this fixes it to be just the address and port
                    if len(destination) > 2:
                        destination = (destination[0], destination[1])
                    send_handler[0].last_destination = destination
                    _LOGGER.debug("Sending %s to %s", send_bytes, destination)
                    self._socket.sendto(send_bytes, destination)
                    self._last_send_time = time.monotonic()
                except Exception:
                    _LOGGER.exception("Exception during send processing")

    def dispatch_recevied_data(self, received_bytes: bytes, remote_end: tuple):
        """Dispatch bytes to the handlers, maybe someone is interested!"""
        with GeckoUdpSocket._BusyLock(self):
            _LOGGER.debug("Received %s from %s", received_bytes, remote_end)
            receive_handler = None
            with self._lock:
                for handler in self._receive_handlers:
                    if handler.can_handle(received_bytes, remote_end):
                        receive_handler = handler
                        break

            if receive_handler:
                try:
                    receive_handler.handle(received_bytes, remote_end)
                    receive_handler.handled(remote_end)
                except Exception:
                    _LOGGER.exception("Unhandled exception in receive_handler func")
            else:
                _LOGGER.debug("Couldn't find new handler for %s", received_bytes)

    def _process_received_data(self):
        with GeckoUdpSocket._BusyLock(self):
            try:
                received_bytes, remote_end = self._socket.recvfrom(
                    self._MAX_PACKET_SIZE
                )
                self.dispatch_recevied_data(received_bytes, remote_end)
            except socket.timeout:
                return
            except OSError as e:
                _LOGGER.debug("OS Exception %s during socket receive", e)
                return
            except Exception:
                _LOGGER.exception("Exception during receive processing")
                return
            finally:
                pass

    def _cleanup_handlers(self):
        with GeckoUdpSocket._BusyLock(self):
            remove_handlers = []

            with self._lock:
                # Build list of handlers that need to be removed
                remove_handlers = [
                    handler
                    for handler in self._receive_handlers
                    if handler.should_remove_handler
                ]

            if remove_handlers:
                _LOGGER.debug("Removed timedout handlers %s", remove_handlers)

            # Remove them from the collection
            with self._lock:
                self._receive_handlers = [
                    handler
                    for handler in self._receive_handlers
                    if handler not in remove_handlers
                ]

            if remove_handlers:
                _LOGGER.debug("Remaining handlers %s", self._receive_handlers)

    def _thread_func(self):
        while self.isopen:
            self._process_send_requests()
            self._process_received_data()
            # Do loop for timeout/retry
            for handler in self._receive_handlers:
                handler.loop(self)
            self._cleanup_handlers()
            self._loop_func()

        _LOGGER.info("GeckoUdpSocket thread finished")

    def _loop_func(self):
        # Opportunity for sub-class to get a thread loop
        pass

    def __repr__(self):
        return (
            f"{self.__class__.__name__} on {self._socket!r}\n"
            f"  receive_handlers={self._receive_handlers!r},\n"
            f"  send_handlers={self._send_handlers!r}\n"
            f"  isopen: {self.isopen}"
            f" isbusy: {self.isbusy}"
        )
