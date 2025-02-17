"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoHelloProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoHelloHandler(unittest.TestCase):
    """Test the GeckoHelloProtocol classes."""

    def setUp(self) -> None:
        """Set up the class."""
        self.handler = GeckoHelloProtocolHandler(b"")

    def test_send_broadcast_construct(self) -> None:
        handler = GeckoHelloProtocolHandler.broadcast()
        self.assertEqual(handler.send_bytes, b"<HELLO>1</HELLO>")

    def test_send_client_construct(self) -> None:
        handler = GeckoHelloProtocolHandler.client(b"CLIENT")
        self.assertEqual(handler.send_bytes, b"<HELLO>CLIENT</HELLO>")

    def test_send_response_construct(self) -> None:
        handler = GeckoHelloProtocolHandler.response(b"SPA", "Name")
        self.assertEqual(handler.send_bytes, b"<HELLO>SPA|Name</HELLO>")

    def test_recv_can_handle(self) -> None:
        self.assertTrue(self.handler.can_handle(b"<HELLO></HELLO>", ()))
        self.assertFalse(self.handler.can_handle(b"<HELLO></HELLO", ()))
        self.assertFalse(self.handler.can_handle(b"<HELLO></HELLO> ", ()))
        self.assertFalse(self.handler.can_handle(b"<GOODBYE>", ()))

    def test_recv_broadcast(self) -> None:
        self.assertFalse(self.handler.handle(b"<HELLO>1</HELLO>", ()))
        self.assertTrue(self.handler.was_broadcast_discovery)
        self.assertIsNone(self.handler._client_identifier)
        self.assertIsNone(self.handler._spa_identifier)
        self.assertIsNone(self.handler._spa_name)

    def test_recv_client_ios(self) -> None:
        self.assertFalse(self.handler.handle(b"<HELLO>IOSCLIENT</HELLO>", ()))
        self.assertFalse(self.handler.was_broadcast_discovery)
        self.assertEqual(self.handler.client_identifier, b"IOSCLIENT")
        self.assertIsNone(self.handler._spa_identifier)
        self.assertIsNone(self.handler._spa_name)

    def test_recv_client_android(self) -> None:
        self.assertFalse(self.handler.handle(b"<HELLO>ANDCLIENT</HELLO>", ()))
        self.assertFalse(self.handler.was_broadcast_discovery)
        self.assertEqual(self.handler.client_identifier, b"ANDCLIENT")
        self.assertIsNone(self.handler._spa_identifier)
        self.assertIsNone(self.handler._spa_name)

    @unittest.expectedFailure
    def test_recv_client_unknown(self) -> None:
        self.handler.handle(b"<HELLO>UNKCLIENT</HELLO>", ())

    def test_recv_response(self) -> None:
        self.assertFalse(self.handler.handle(b"<HELLO>SPA|Name</HELLO>", ()))
        self.assertFalse(self.handler.was_broadcast_discovery)
        self.assertIsNone(self.handler._client_identifier)
        self.assertEqual(self.handler.spa_identifier, b"SPA")
        self.assertEqual(self.handler.spa_name, "Name")

    def test_recv_can_handle_multiple(self) -> None:
        self.test_recv_response()
        self.test_recv_client_android()
        self.test_recv_broadcast()


if __name__ == "__main__":
    unittest.main()
