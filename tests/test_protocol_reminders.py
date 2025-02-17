"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


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
        handler = GeckoRemindersProtocolHandler.req_response(
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

    def test_send_construct_set(self) -> None:
        handler = GeckoRemindersProtocolHandler.set(
            1,
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
            b"<DATAS>SETRM\x01"
            b"\x01\xf3\xff\x01"
            b"\x02\x01\x01\x01"
            b"\x03\x02\x00\x01"
            b"\x04\x00\x02\x01"
            b"\x05\x00\x00\x01"
            b"\x06\x80\x00\x01"
            b"\x00\x01\x00\x01"
            b"</DATAS></PACKT>",
        )

    def test_send_construct_set_ack(self) -> None:
        handler = GeckoRemindersProtocolHandler.set_ack(parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>RMSET</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        self.assertTrue(handler.can_handle(b"REQRM", PARMS))
        self.assertTrue(handler.can_handle(b"RMREQ", PARMS))
        self.assertTrue(handler.can_handle(b"SETRM", PARMS))
        self.assertTrue(handler.can_handle(b"RMSET", PARMS))
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

    def test_recv_handle_set_reminder(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(
            b"SETRM\x16\x01\x1e\x00\x01\x02\x00\x00\x01\x03/\x00\x01\x04\xaf\x02\x01\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00",
            PARMS,
        )
        self.assertListEqual(
            handler.reminders,
            [
                (GeckoReminderType.RINSE_FILTER, 30),
                (GeckoReminderType.CLEAN_FILTER, 0),
                (GeckoReminderType.CHANGE_WATER, 47),
                (GeckoReminderType.CHECK_SPA, 687),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
            ],
        )

    def test_recv_handle_set_reminder_reset_all(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(
            b"SETRMA\x01\x1e\x00\x01\x02<\x00\x01\x03Z\x00\x01\x04\xda\x02\x01\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00",
            PARMS,
        )
        self.assertListEqual(
            handler.reminders,
            [
                (GeckoReminderType.RINSE_FILTER, 30),
                (GeckoReminderType.CLEAN_FILTER, 60),
                (GeckoReminderType.CHANGE_WATER, 90),
                (GeckoReminderType.CHECK_SPA, 730),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
                (GeckoReminderType.INVALID, 30),
            ],
        )

    def test_recv_handle_set_reminder_reset_sim(self) -> None:
        handler = GeckoRemindersProtocolHandler()
        handler.handle(
            b"SETRM\t\x01\xf3\xff\x01\x02\x00\x00\x01\x03\x00\x00\x01\x04\xaf\x02\x01\x00\xf3\xff\x01\x00\xf3\xff\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01",
            PARMS,
        )
        self.assertListEqual(
            handler.reminders,
            [
                (GeckoReminderType.RINSE_FILTER, -13),
                (GeckoReminderType.CLEAN_FILTER, 0),
                (GeckoReminderType.CHANGE_WATER, 0),
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
