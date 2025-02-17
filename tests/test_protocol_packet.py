"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoPacketProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoPacketHandler(unittest.TestCase):
    """Packet handler tests."""

    def setUp(self) -> None:
        """Set up the class."""
        self.handler = GeckoPacketProtocolHandler(content=b"CONTENT", parms=PARMS)

    def test_recv_can_handle(self) -> None:
        self.assertTrue(self.handler.can_handle(b"<PACKT></PACKT>", ()))
        self.assertFalse(self.handler.can_handle(b"<PACKT></PACKT", ()))
        self.assertFalse(self.handler.can_handle(b"<PACKT></PACKT> ", ()))
        self.assertFalse(self.handler.can_handle(b"<SOMETHING>", ()))

    def test_recv_extract_ok(self) -> None:
        self.assertFalse(
            self.handler.handle(
                b"<PACKT><SRCCN>SRCID</SRCCN><DESCN>DESTID</DESCN>"
                b"<DATAS>DATA</DATAS></PACKT>",
                (1, 2),
            )
        )
        assert self.handler.parms is not None
        self.assertTupleEqual(self.handler.parms, PARMS)
        self.assertEqual(self.handler.packet_content, b"DATA")

    def test_send_construct(self) -> None:
        self.assertEqual(
            self.handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>CONTENT</DATAS></PACKT>",
        )
        assert self.handler.parms is not None
        self.assertEqual(self.handler.parms[0], 1)
        self.assertEqual(self.handler.parms[1], 2)


if __name__ == "__main__":
    unittest.main()
