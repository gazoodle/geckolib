"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

import unittest
import unittest.mock

import pytest
from context import (
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoHelloProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoStatusBlockProtocolHandler,
    GeckoUdpProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareProtocolHandler,
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


class TestGeckoConfigFileHandler(unittest.TestCase):
    """Config file tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoConfigFileProtocolHandler.request(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SFILE\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoConfigFileProtocolHandler.response("inXM", 7, 8, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>FILES,inXM_C07.xml,inXM_S08.xml</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        self.assertTrue(handler.can_handle(b"SFILE", PARMS))
        self.assertTrue(handler.can_handle(b"FILES", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        handler.handle(b"SFILE\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        handler.handle(b"FILES,inXM_C09.xml,inXM_S09.xml", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(handler.plateform_key, "inXM")
        self.assertEqual(handler.config_version, 9)
        self.assertEqual(handler.log_version, 9)

    @unittest.expectedFailure
    def test_recv_handle_response_error(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        self.assertTrue(handler.handle(b"FILES,inXM_C09.xml,inYE_S09.xml", PARMS))


class MockProtocol:
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

    def get_and_increment_sequence_counter(self, command: bool) -> int:
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
        print(handler.send_bytes)
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
        print(handler.send_bytes)
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
            == b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATQ\x01</DATAS></PACKT>"
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
            == b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN><DATAS>STATQ\x01</DATAS></PACKT>"
        )


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
        handler = GeckoWatercareProtocolHandler.response(3, parms=PARMS)
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


class TestGeckoRemindersHandler(unittest.TestCase):
    """Reminders handler tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoRemindersProtocolHandler.request(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>REQRM\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoRemindersProtocolHandler.response(
            [
                (GeckoReminderType.RINSE_FILTER, -13),
                (GeckoReminderType.CLEAN_FILTER, 257),
                (GeckoReminderType.CHANGE_WATER, 2),
                (GeckoReminderType.CHECK_SPA, 512),
                (GeckoReminderType.CHANGE_OZONATOR, 0),
                (GeckoReminderType.CHANGE_VISION_CARTRIDGE, 128),
                (GeckoReminderType.INVALID, 1),
            ],
            parms=PARMS,
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>RMREQ"
            b"\x01\xf3\xff\x01"
            b"\x02\x01\x01\x01"
            b"\x03\x02\x00\x01"
            b"\x04\x00\x02\x01"
            b"\x05\x00\x00\x01"
            b"\x06\x80\x00\x01"
            b"\x00\x01\x00\x01"
            b"</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        self.assertTrue(handler.can_handle(b"REQRM", PARMS))
        self.assertTrue(handler.can_handle(b"RMREQ", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(b"REQRM\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(
            b"RMREQ"
            b"\x01\x01\x00\x01\x02\x1f\x00\x01\x03\x29"
            b"\x00\x01\x04\xa9\x02\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            PARMS,
        )
        self.assertListEqual(
            handler.reminders,
            [
                (GeckoReminderType.RINSE_FILTER, 1),
                (GeckoReminderType.CLEAN_FILTER, 31),
                (GeckoReminderType.CHANGE_WATER, 41),
                (GeckoReminderType.CHECK_SPA, 681),
                (GeckoReminderType.INVALID, 1),
                (GeckoReminderType.INVALID, 1),
                (GeckoReminderType.INVALID, 0),
                (GeckoReminderType.INVALID, 0),
                (GeckoReminderType.INVALID, 0),
                (GeckoReminderType.INVALID, 0),
            ],
        )

    def test_recv_handle_boundary_conditions_response(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(
            b"RMREQ"
            b"\x01\xf3\xff\x01"
            b"\x02\x01\x01\x01"
            b"\x03\x02\x00\x01"
            b"\x04\x00\x02\x01"
            b"\x05\x00\x00\x01"
            b"\x06\x80\x00\x01"
            b"\x07\x01\x01\x01"
            b"\x08\x01\x01\x01"
            b"\xff\x01\x01\x01"
            b"\x00\x01\x00\x01",
            PARMS,
        )
        self.assertListEqual(
            handler.reminders,
            [
                (GeckoReminderType.RINSE_FILTER, -13),
                (GeckoReminderType.CLEAN_FILTER, 257),
                (GeckoReminderType.CHANGE_WATER, 2),
                (GeckoReminderType.CHECK_SPA, 512),
                (GeckoReminderType.CHANGE_OZONATOR, 0),
                (GeckoReminderType.CHANGE_VISION_CARTRIDGE, 128),
                (GeckoReminderType.INVALID, 1),
            ],
        )

    def test_recv_handle_negative_number_response(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(
            b"RMREQ\x01\xf3\xff\x01\x02\x11\x00\x01\x03/\x00\x01\x04\xaf\x02\x01"
            b"\x00\xf3\xff\x00\x00\xf3\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00",
            PARMS,
        )
        self.assertListEqual(
            handler.reminders,
            [
                (GeckoReminderType.RINSE_FILTER, -13),
                (GeckoReminderType.CLEAN_FILTER, 17),
                (GeckoReminderType.CHANGE_WATER, 47),
                (GeckoReminderType.CHECK_SPA, 687),
                (GeckoReminderType.INVALID, -13),
                (GeckoReminderType.INVALID, -13),
                (GeckoReminderType.INVALID, 0),
                (GeckoReminderType.INVALID, 0),
                (GeckoReminderType.INVALID, 0),
                (GeckoReminderType.INVALID, 0),
            ],
        )


if __name__ == "__main__":
    unittest.main()
