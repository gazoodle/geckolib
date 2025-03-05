"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

import pytest
from context import (
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoUdpProtocolHandler,
)

from geckolib.driver.async_udp_protocol import GeckoAsyncUdpProtocol

PARMS = (1, 2, b"SRCID", b"DESTID")


class MockProtocol(GeckoAsyncUdpProtocol):
    """Mock protocol class."""

    def __init__(self) -> None:
        """Initialiale the mock protocol class."""
        self.sendbytes = None

    def queue_send(
        self,
        protocol_handler: GeckoUdpProtocolHandler,
        _destination: tuple | None = None,
    ) -> None:
        self.sendbytes = protocol_handler.send_bytes

    def get_and_increment_sequence_counter(self, *, command: bool = False) -> int:
        if command:
            return 192
        return 1


class TestGeckoStatusBlockHandler(unittest.TestCase):
    """Status block tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoStatusBlockProtocolHandler.request(1, 0, 637, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>STATU\x01\x00\x00\x02\x7d</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoStatusBlockProtocolHandler.response(
            3, 4, b"\x01\x02\x03\x04", parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>STATV\x03\x04\x04\x01\x02\x03\x04</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoStatusBlockProtocolHandler()
        self.assertTrue(handler.can_handle(b"STATU", PARMS))
        self.assertTrue(handler.can_handle(b"STATV", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_partial_can_handle(self) -> None:
        protocol = MockProtocol()
        handler = GeckoAsyncPartialStatusBlockProtocolHandler(protocol)
        self.assertTrue(handler.can_handle(b"STATP", PARMS))
        self.assertTrue(handler.can_handle(b"STATQ", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))
        self.assertIsNone(protocol.sendbytes)

    def test_recv_handle_request(self) -> None:
        handler = GeckoStatusBlockProtocolHandler()
        handler.handle(b"STATU\x01\x00\x00\x02\x7d", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler.sequence, 1)
        self.assertEqual(handler.start, 0)
        self.assertEqual(handler.length, 637)

    def test_recv_handle_response(self) -> None:
        handler = GeckoStatusBlockProtocolHandler()
        handler.handle(b"STATV\x03\x04\x04\x01\x02\x03\x04", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler.sequence, 3)
        self.assertEqual(handler.next, 4)
        self.assertEqual(handler.length, 4)
        self.assertEqual(handler.data, b"\x01\x02\x03\x04")

    def test_recv_handle_response_final(self) -> None:
        handler = GeckoStatusBlockProtocolHandler()
        handler.handle(b"STATV\x03\x00\x04\x01\x02\x03\x04", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler.sequence, 3)
        self.assertEqual(handler.next, 0)
        self.assertEqual(handler.length, 4)
        self.assertEqual(handler.data, b"\x01\x02\x03\x04")

    def test_send_partial(self) -> None:
        protocol = MockProtocol()
        handler = GeckoAsyncPartialStatusBlockProtocolHandler.report_changes(
            protocol, [(365, b"\x03\x84"), (366, b"\x84\x0c")], parms=PARMS
        )
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATP\x02\x01\x6d\x03\x84\x01\x6e\x84\x0c</DATAS></PACKT>",
        )

    def test_send_partial_three(self) -> None:
        protocol = MockProtocol()
        handler = GeckoAsyncPartialStatusBlockProtocolHandler.report_changes(
            protocol,
            [(365, b"\x03\x84"), (366, b"\x84\x0c"), (367, b"\x01\x02")],
            parms=PARMS,
        )
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATP\x03\x01\x6d\x03\x84\x01\x6e\x84\x0c\x01\x6f\x01\x02</DATAS></PACKT>",
        )

    @unittest.expectedFailure
    def test_send_partial_not_two_bytes(self) -> None:
        protocol = MockProtocol()
        handler = GeckoAsyncPartialStatusBlockProtocolHandler.report_changes(
            protocol,
            [(367, b"\x01")],
            parms=PARMS,
        )
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATP\x03\x01\x6d\x03\x84\x01\x6e\x84\x0c\x01\x6f\x01\x02</DATAS></PACKT>",
        )


class TestGeckoAsyncStatusBlockHandler:
    """Status block tests."""

    @pytest.mark.asyncio
    async def test_recv_handle_partial(self) -> None:
        protocol = MockProtocol()
        handler = GeckoAsyncPartialStatusBlockProtocolHandler(protocol)
        await handler.async_handle(b"STATV\x02\x01\x6d\x03\x84\x01\x6e\x84\x0c", PARMS)
        assert not handler.should_remove_handler
        assert handler.changes == [(365, b"\x03\x84"), (366, b"\x84\x0c")]
        assert (
            protocol.sendbytes
            == b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATQ\xc0</DATAS></PACKT>"
        )

    @pytest.mark.asyncio
    async def test_change_unpack_more(self) -> None:
        protocol = MockProtocol()
        handler = GeckoAsyncPartialStatusBlockProtocolHandler(protocol)
        await handler.async_handle(
            b"STATV\x05\x00\x01\x02\x02\x00\x02\x04\x04\x00\x03\x06\x06\x00\x04\x08\x08\x00\x05\x0a\x0a",
            PARMS,
        )
        assert handler.changes == [
            (1, b"\x02\x02"),
            (2, b"\x04\x04"),
            (3, b"\x06\x06"),
            (4, b"\x08\x08"),
            (5, b"\x0a\x0a"),
        ]
        assert (
            protocol.sendbytes
            == b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATQ\xc0</DATAS></PACKT>"
        )


if __name__ == "__main__":
    unittest.main()
