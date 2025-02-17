"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoWatercareProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoWatercareHandler(unittest.TestCase):
    """Watercare handler tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoWatercareProtocolHandler.request(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>GETWC\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoWatercareProtocolHandler.get_response(3, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>WCGET\x03</DATAS></PACKT>",
        )

    def test_send_construct_schedule(self) -> None:
        handler = GeckoWatercareProtocolHandler.giveschedule(parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>WCREQ\x00\x00\x00\x01\x00\x00\x06\x00\x00\x00\x00\x02\x01\x00"
            b"\x01\x05"
            b"\x06\x00\x12\x00\x03\x01\x00\x00\x06\x06\x00\x12\x00\x04\x01\x00"
            b"\x01\x05\x00\x00\x00\x00</DATAS></PACKT>",
        )

    def test_send_construct_set(self) -> None:
        handler = GeckoWatercareProtocolHandler.set(1, 2, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SETWC\x01\x02</DATAS></PACKT>",
        )
        self.assertEqual(handler._timeout_in_seconds, 4)

    def test_recv_can_handle(self) -> None:
        handler = GeckoWatercareProtocolHandler()
        self.assertTrue(handler.can_handle(b"GETWC", PARMS))
        self.assertTrue(handler.can_handle(b"WCGET", PARMS))
        self.assertTrue(handler.can_handle(b"REQWC", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoWatercareProtocolHandler()
        handler.handle(b"GETWC\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)
        self.assertFalse(handler.schedule)

    def test_recv_handle_response(self) -> None:
        handler = GeckoWatercareProtocolHandler()
        handler.handle(b"WCGET\x03", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertFalse(handler.schedule)
        self.assertEqual(handler.mode, 3)

    def test_recv_handle_request_schedule(self) -> None:
        handler = GeckoWatercareProtocolHandler()
        handler.handle(b"REQWC\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertTrue(handler.schedule)


if __name__ == "__main__":
    unittest.main()
