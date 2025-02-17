"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoPingProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoPingHandler(unittest.TestCase):
    """Ping handler tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoPingProtocolHandler.request(parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>APING</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoPingProtocolHandler.response(parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>APING\x00</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoPingProtocolHandler.request(parms=PARMS)
        self.assertTrue(handler.can_handle(b"APING", PARMS))
        self.assertIsNone(handler._sequence)

    def test_recv_handle(self) -> None:
        handler = GeckoPingProtocolHandler.request(parms=PARMS)
        handler.handle(b"APING\x00", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 0)


if __name__ == "__main__":
    unittest.main()
