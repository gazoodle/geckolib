"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoGetChannelProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoGetChannelHandler(unittest.TestCase):
    """Channel handler tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoGetChannelProtocolHandler.request(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>CURCH\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoGetChannelProtocolHandler.response(10, 33, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>CHCUR\x0a\x21</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoGetChannelProtocolHandler()
        self.assertTrue(handler.can_handle(b"CURCH", PARMS))
        self.assertTrue(handler.can_handle(b"CHCUR", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoGetChannelProtocolHandler()
        handler.handle(b"CURCH\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoGetChannelProtocolHandler()
        handler.handle(b"CHCUR\x0a\x21", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(handler.channel, 10)
        self.assertEqual(handler.signal_strength, 33)


if __name__ == "__main__":
    unittest.main()
