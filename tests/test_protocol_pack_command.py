"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoPackCommandProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoPackCommandHandlers(unittest.TestCase):
    """Pack Command tests."""

    def test_send_construct_key_press(self) -> None:
        handler = GeckoPackCommandProtocolHandler.keypress(1, 6, 1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SPACK\x01\x06\x02\x39\x01</DATAS></PACKT>",
        )

    def test_send_construct_set_value(self) -> None:
        handler = GeckoPackCommandProtocolHandler.set_value(
            1, 6, 9, 9, 15, 2, 702, parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SPACK\x01\x06\x07\x46\x09\x09\x00\x0f\x02\xbe</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoPackCommandProtocolHandler.response(parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>PACKS</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoPackCommandProtocolHandler()
        self.assertTrue(handler.can_handle(b"SPACK", PARMS))
        self.assertTrue(handler.can_handle(b"PACKS", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_key_press(self) -> None:
        handler = GeckoPackCommandProtocolHandler()
        handler.handle(b"SPACK\x01\x06\x02\x39\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)
        self.assertTrue(handler.is_key_press)
        self.assertEqual(handler.keycode, 1)
        self.assertFalse(handler.is_set_value)

    def test_recv_handle_set_value(self) -> None:
        handler = GeckoPackCommandProtocolHandler()
        handler.handle(b"SPACK\x01\x06\x07\x46\x09\x09\x00\x0f\x02\xbe", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)
        self.assertFalse(handler.is_key_press)
        self.assertTrue(handler.is_set_value)
        self.assertEqual(handler.position, 15)
        self.assertEqual(handler.new_data, b"\x02\xbe")

    def test_recv_handle_response(self) -> None:
        handler = GeckoPackCommandProtocolHandler()
        handler.handle(b"PACKS", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertFalse(handler.is_key_press)
        self.assertFalse(handler.is_set_value)


if __name__ == "__main__":
    unittest.main()
