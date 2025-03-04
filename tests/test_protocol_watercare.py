"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoGetWatercareModeProtocolHandler,
    GeckoGetWatercareScheduleListProtocolHandler,
    GeckoSetWatercareModeProtocolHandler,
    GeckoWatercareScheduleManager,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoGetWatercareModeHandler(unittest.TestCase):
    """Get Watercare handler tests."""

    def test_send_construct_get(self) -> None:
        handler = GeckoGetWatercareModeProtocolHandler.get(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>GETWC\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoGetWatercareModeProtocolHandler.get_response(3, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>WCGET\x03</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoGetWatercareModeProtocolHandler()
        self.assertTrue(handler.can_handle(b"GETWC", PARMS))
        self.assertTrue(handler.can_handle(b"WCGET", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoGetWatercareModeProtocolHandler()
        handler.handle(b"GETWC\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoGetWatercareModeProtocolHandler()
        handler.handle(b"WCGET\x03", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(handler.mode, 3)


class TestGeckoSetWatercareModeHandler(unittest.TestCase):
    """Set watercare mode handler tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoSetWatercareModeProtocolHandler.set(1, 2, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SETWC\x01\x02</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoSetWatercareModeProtocolHandler.set_response(2, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>WCSET\x02</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoSetWatercareModeProtocolHandler()
        self.assertTrue(handler.can_handle(b"SETWC", PARMS))
        self.assertTrue(handler.can_handle(b"WCSET", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoSetWatercareModeProtocolHandler()
        handler.handle(b"SETWC\x01\x02", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)
        self.assertEqual(handler.mode, 2)

    def test_recv_handle_response(self) -> None:
        handler = GeckoSetWatercareModeProtocolHandler()
        handler.handle(b"WCSET\x02", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(handler.mode, 2)


class TestGeckoGetWatercareScheduleListHandler(unittest.TestCase):
    """Get Watercare schedule list tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler.get(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>REQWC\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler.get_response(
            GeckoWatercareScheduleManager(), parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>WCREQ\x00\x00\x00\x01\x00\x00\x06\x00\x00\x00\x00\x02\x01\x00"
            b"\x01\x05"
            b"\x06\x00\x12\x00\x03\x01\x00\x00\x06\x06\x00\x12\x00\x04\x01\x00"
            b"\x01\x05\x00\x00\x00\x00</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        self.assertTrue(handler.can_handle(b"REQWC", PARMS))
        self.assertTrue(handler.can_handle(b"WCREQ", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(b"REQWC\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(b"WCREQ\x02", PARMS)
        self.assertTrue(handler.should_remove_handler)


if __name__ == "__main__":
    unittest.main()
