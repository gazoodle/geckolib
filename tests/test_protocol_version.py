"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoVersionProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoVersionHandler(unittest.TestCase):
    """Version handler tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoVersionProtocolHandler.request(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>AVERS\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoVersionProtocolHandler.response(
            (1, 2, 3), (4, 5, 6), parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SVERS\x00\x01\x02\x03\x00\x04\x05\x06</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoVersionProtocolHandler()
        self.assertTrue(handler.can_handle(b"AVERS", PARMS))
        self.assertTrue(handler.can_handle(b"SVERS", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoVersionProtocolHandler()
        handler.handle(b"AVERS\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoVersionProtocolHandler()
        handler.handle(b"SVERS\x00\x01\x02\x03\x00\x04\x05\x06", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(handler.en_build, 1)
        self.assertEqual(handler.en_major, 2)
        self.assertEqual(handler.en_minor, 3)
        self.assertEqual(handler.co_build, 4)
        self.assertEqual(handler.co_major, 5)
        self.assertEqual(handler.co_minor, 6)


if __name__ == "__main__":
    unittest.main()
