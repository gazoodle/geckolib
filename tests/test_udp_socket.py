""" Unit tests for the UDP socket classes """

import logging
import unittest
import unittest.mock
import time
import socket


from context import (
    GeckoUdpProtocolHandler,
    GeckoUdpSocket,
)


class MockSocket:
    """A class that looks like a socket, but doesn't really
    send or receive anything - used in the tests"""

    def __init__(self):
        self.data_for_recvfrom = None
        self.last_data_sent = None

    def close(self):
        pass

    def settimeout(self, timeout):
        pass

    def recvfrom(self, max_size):
        if self.data_for_recvfrom is None:
            raise socket.timeout
        data = self.data_for_recvfrom
        self.data_for_recvfrom = None
        return (data, ("Mock", "Port"))

    def sendto(self, data, dest):
        self.last_data_sent = data


class TestUdpProtocolHandler(unittest.TestCase):
    def setUp(self):
        self.base_handler = GeckoUdpProtocolHandler()

    def test_constructor(self):
        self.assertIsNotNone(self.base_handler)

    @unittest.expectedFailure
    def test_default_bytes_not_implemented(self):
        self.assertEqual(self.base_handler.send_bytes, None)

    def test_loop(self):
        self.base_handler.loop(None)

    def test_not_timedout(self):
        self.assertFalse(self.base_handler.has_timedout)

    def test_timedout(self):
        handler = GeckoUdpProtocolHandler(timeout=0.005)
        self.assertFalse(handler.has_timedout)
        self.assertFalse(handler.should_remove_handler)
        time.sleep(0.005)
        self.assertTrue(handler.has_timedout)
        self.assertFalse(handler.should_remove_handler)
        handler.loop(None)
        self.assertTrue(handler.should_remove_handler)

    def test_should_remove_handler(self):
        self.assertFalse(self.base_handler.should_remove_handler)


class TestGeckoUdpSocket(unittest.TestCase):
    """ Test the GeckoUdpSocket class """

    def setUp(self):
        class UdpSocketHelper(GeckoUdpSocket):
            def __init__(self):
                self.mock_socket = MockSocket()
                super().__init__(self.mock_socket)

            def wait(self):
                while self.isbusy:
                    pass

        self.socket = UdpSocketHelper()
        self.socket.open()

    def tearDown(self):
        self.socket.close()

    def test_construct(self):
        socket = GeckoUdpSocket()
        self.assertFalse(socket.isopen)
        self.assertTrue(self.socket.isopen)

    def test_send(self):
        class Send(GeckoUdpProtocolHandler):
            @property
            def send_bytes(self):
                return b"REQUEST"

        self.socket.queue_send(Send(), (1, 2))
        self.assertTrue(self.socket.isbusy)
        self.socket.wait()
        self.assertEqual(self.socket.mock_socket.last_data_sent, b"REQUEST")

    def test_receive(self):
        class Receive(GeckoUdpProtocolHandler):
            def __init__(self):
                super().__init__()
                self.received = None

            def can_handle(self, received_bytes: bytes, sender: tuple):
                return True

            def handle(self, socket, received_bytes: bytes, sender: tuple):
                self.received = received_bytes
                self._should_remove_handler = True

        self.socket.mock_socket.data_for_recvfrom = None
        handler = Receive()
        self.assertIsNone(handler.received)
        try:
            self.socket.add_receive_handler(handler)
            self.socket.mock_socket.data_for_recvfrom = "ONCE"
            while handler.received is None:
                pass
        finally:
            self.socket.wait()
            self.assertEqual(handler.received, "ONCE")

    def test_new_receive_retry(self):
        class Retry(GeckoUdpProtocolHandler):
            def __init__(self):
                super().__init__(timeout=0.01, retry_count=5)
                self.retry_occurred = 0

            @property
            def send_bytes(self):
                return b"REQUEST"

            def can_handle(self, received_bytes: bytes, sender: tuple):
                return True

            def handle(self, socket, received_bytes: bytes, sender: tuple):
                self.should_remove_handler = True

            def _reset_timeout(self):
                super()._reset_timeout()
                self.retry_occurred += 1

        self.socket.mock_socket.data_for_recvfrom = None
        retry_handler = Retry()
        retry_handler.last_destination = (1, 2)
        now = time.monotonic()

        try:
            self.socket.add_receive_handler(retry_handler)
            while retry_handler.retry_occurred < 5 and (time.monotonic() - now) < 5:
                pass
            while len(self.socket._receive_handlers) > 0:
                pass
        finally:
            self.socket.wait()
            self.assertListEqual(self.socket._receive_handlers, [])
            self.assertEqual(retry_handler.retry_occurred, 5)


if __name__ == "__main__":
    if True:  # Change to True to enable logging
        stream_logger = logging.StreamHandler()
        stream_logger.setLevel(logging.DEBUG)
        stream_logger.setFormatter(logging.Formatter("LOG> %(levelname)s %(message)s"))
        logging.getLogger().addHandler(stream_logger)
    unittest.main()
