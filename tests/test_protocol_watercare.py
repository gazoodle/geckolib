"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

import pytest
from context import (
    GeckoAddWatercareScheduleProtocolHandler,
    GeckoDeleteWatercareScheduleProtocolHandler,
    GeckoGetWatercareModeProtocolHandler,
    GeckoGetWatercareScheduleListProtocolHandler,
    GeckoModifyWatercareScheduleProtocolHandler,
    GeckoScheduleDay,
    GeckoSetWatercareModeProtocolHandler,
    GeckoWatercareSchedule,
    GeckoWatercareScheduleManager,
    GeckoWatercareScheduleType,
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
        handler.handle(b"WCREQ\x00\x00", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertTrue(handler.is_complete)
        self.assertEqual(handler.schedules, [])

    def test_recv_handle_truncated_response_is_ignored(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(b"WCREQ\x02", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertFalse(handler.is_complete)

    def test_recv_handle_single_fragment(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(
            b"WCREQ\x00\x00"
            b"\x01\x02\x00\x00\x06\x17\x1e\x02\x1e"
            b"\x01\x02\x01\x00\x06\x09\x00\x0c\x00",
            PARMS,
        )
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(
            handler.schedules,
            [
                GeckoWatercareSchedule(
                    1, GeckoWatercareScheduleType.FILTRATION, 0, 0, 6, 23, 30, 2, 30
                ),
                GeckoWatercareSchedule(
                    1, GeckoWatercareScheduleType.FILTRATION, 1, 0, 6, 9, 0, 12, 0
                ),
            ],
        )

    def test_recv_handle_multiple_fragments(self) -> None:
        # The first fragment as captured from a real spa. Its header says that
        # fragment 1 is to follow, so the handler must not finish yet.
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(
            b"WCREQ\x00\x01"
            b"\x00\x01\x00\x00\x06\x00\x00\x00\x00"
            b"\x00\x02\x01\x00\x06\x14\x00\x16\x00"
            b"\x01\x02\x00\x00\x06\x17\x1e\x02\x1e"
            b"\x01\x02\x01\x00\x06\x09\x00\x0c\x00",
            PARMS,
        )
        self.assertFalse(handler.should_remove_handler)
        self.assertFalse(handler.is_complete)
        self.assertEqual(len(handler.schedules), 4)

        handler.handle(b"WCREQ\x01\x00\x02\x02\x00\x00\x06\x14\x00\x16\x00", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertTrue(handler.is_complete)
        self.assertEqual(len(handler.schedules), 5)
        self.assertEqual(handler.schedules[0].schedule_type, 1)
        self.assertEqual(handler.schedules[0].start_time, "00:00")
        self.assertEqual(handler.schedules[1].start_time, "20:00")
        self.assertEqual(handler.schedules[1].stop_time, "22:00")
        self.assertEqual(handler.schedules[4].mode, 2)

    def test_recv_handle_out_of_order_fragment_is_ignored(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(b"WCREQ\x00\x01\x00\x01\x00\x00\x06\x00\x00\x00\x00", PARMS)
        handler.handle(b"WCREQ\x02\x00\x02\x02\x00\x00\x06\x14\x00\x16\x00", PARMS)
        self.assertFalse(handler.is_complete)
        self.assertEqual(len(handler.schedules), 1)

    def test_recv_handle_restart_discards_partial_list(self) -> None:
        handler = GeckoGetWatercareScheduleListProtocolHandler()
        handler.handle(b"WCREQ\x00\x01\x00\x01\x00\x00\x06\x00\x00\x00\x00", PARMS)
        handler.handle(b"WCREQ\x00\x00\x02\x02\x00\x00\x06\x14\x00\x16\x00", PARMS)
        self.assertTrue(handler.is_complete)
        self.assertEqual(len(handler.schedules), 1)
        self.assertEqual(handler.schedules[0].mode, 2)

    def test_response_round_trip(self) -> None:
        schedules = [
            GeckoWatercareSchedule(
                3, GeckoWatercareScheduleType.ECONOMY, 0, 1, 5, 6, 15, 18, 45
            )
        ]
        handler = GeckoGetWatercareScheduleListProtocolHandler.get_response(
            GeckoWatercareScheduleManager(schedules), parms=PARMS
        )
        parsed = GeckoGetWatercareScheduleListProtocolHandler()
        parsed.handle(handler.packet_content or handler._content, PARMS)
        self.assertEqual(parsed.schedules, schedules)


class TestGeckoWatercareSchedule(unittest.TestCase):
    """Schedule model tests."""

    def test_pack_unpack(self) -> None:
        schedule = GeckoWatercareSchedule(
            1, GeckoWatercareScheduleType.FILTRATION, 2, 0, 6, 9, 5, 12, 30
        )
        self.assertEqual(schedule.pack(), b"\x01\x02\x02\x00\x06\x09\x05\x0c\x1e")
        self.assertEqual(GeckoWatercareSchedule.unpack(schedule.pack()), schedule)

    def test_validation(self) -> None:
        kind = GeckoWatercareScheduleType.FILTRATION
        with pytest.raises(ValueError):  # noqa: PT011
            GeckoWatercareSchedule(1, kind, 0, 0, 6, 24, 0, 1, 0)
        with pytest.raises(ValueError):  # noqa: PT011
            GeckoWatercareSchedule(1, kind, 0, 0, 6, 1, 60, 1, 0)
        with pytest.raises(ValueError):  # noqa: PT011
            GeckoWatercareSchedule(1, kind, 0, 0, 7, 1, 0, 1, 0)
        with pytest.raises(ValueError):  # noqa: PT011
            GeckoWatercareSchedule(1, kind, 256, 0, 6, 1, 0, 1, 0)

    def test_day_range(self) -> None:
        self.assertEqual(GeckoScheduleDay.day_range(GeckoScheduleDay.EVERYDAY), (0, 6))
        self.assertEqual(GeckoScheduleDay.day_range(GeckoScheduleDay.WEEKDAY), (1, 5))
        self.assertEqual(GeckoScheduleDay.day_range(GeckoScheduleDay.WEEKEND), (6, 0))
        self.assertEqual(GeckoScheduleDay.day_range(GeckoScheduleDay.TUESDAY), (2, 2))


class TestGeckoWatercareScheduleManager(unittest.TestCase):
    """Schedule manager tests."""

    ECO = GeckoWatercareScheduleType.ECONOMY
    FILT = GeckoWatercareScheduleType.FILTRATION

    def make(
        self, mode: int, kind: GeckoWatercareScheduleType, number: int
    ) -> GeckoWatercareSchedule:
        return GeckoWatercareSchedule(mode, kind, number, 0, 6, 1, 0, 2, 0)

    def test_for_mode_is_ordered_and_filtered(self) -> None:
        manager = GeckoWatercareScheduleManager(
            [
                self.make(1, self.FILT, 1),
                self.make(2, self.FILT, 0),
                self.make(1, self.ECO, 0),
            ]
        )
        self.assertEqual([s.number for s in manager.for_mode(1)], [0, 1])
        self.assertEqual(len(manager.for_mode(2)), 1)
        self.assertEqual(manager.for_mode(4), [])

    def test_next_number(self) -> None:
        # Economy schedules are numbered before filtration schedules
        manager = GeckoWatercareScheduleManager(
            [self.make(0, self.ECO, 0), self.make(0, self.FILT, 1)]
        )
        self.assertEqual(manager.next_number(0, self.ECO), 1)
        self.assertEqual(manager.next_number(0, self.FILT), 2)
        self.assertEqual(manager.next_number(3, self.ECO), 0)
        self.assertEqual(manager.next_number(3, self.FILT), 0)


class TestGeckoWatercareScheduleChangeHandlers(unittest.TestCase):
    """Add, modify and delete schedule tests."""

    SCHEDULE = GeckoWatercareSchedule(
        1, GeckoWatercareScheduleType.FILTRATION, 2, 0, 6, 9, 5, 12, 30
    )

    def test_add_send_construct(self) -> None:
        handler = GeckoAddWatercareScheduleProtocolHandler.add(
            7, self.SCHEDULE, parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>ADDWC\x07\x01\x02\x02\x00\x06\x09\x05\x0c\x1e</DATAS></PACKT>",
        )

    def test_modify_send_construct(self) -> None:
        handler = GeckoModifyWatercareScheduleProtocolHandler.modify(
            7, self.SCHEDULE, parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>MDFWC\x07\x01\x02\x02\x00\x06\x09\x05\x0c\x1e</DATAS></PACKT>",
        )

    def test_delete_send_construct_only_identifies_the_schedule(self) -> None:
        handler = GeckoDeleteWatercareScheduleProtocolHandler.delete(
            7, self.SCHEDULE, parms=PARMS
        )
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>DELWC\x07\x01\x02\x02</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        for cls, req, ack in (
            (GeckoAddWatercareScheduleProtocolHandler, b"ADDWC", b"WCADD"),
            (GeckoModifyWatercareScheduleProtocolHandler, b"MDFWC", b"WCMDF"),
            (GeckoDeleteWatercareScheduleProtocolHandler, b"DELWC", b"WCDEL"),
        ):
            handler = cls()
            self.assertTrue(handler.can_handle(req, PARMS))
            self.assertTrue(handler.can_handle(ack, PARMS))
            self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request_and_ack(self) -> None:
        handler = GeckoAddWatercareScheduleProtocolHandler()
        handler.handle(b"ADDWC\x07\x01\x02\x02\x00\x06\x09\x05\x0c\x1e", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 7)
        self.assertEqual(handler.schedule, self.SCHEDULE)
        handler.handle(b"WCADD", PARMS)
        self.assertTrue(handler.should_remove_handler)

    def test_recv_handle_delete_request(self) -> None:
        handler = GeckoDeleteWatercareScheduleProtocolHandler()
        handler.handle(b"DELWC\x07\x01\x02\x02", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler.key, (1, 2, 2))
        handler.handle(b"WCDEL", PARMS)
        self.assertTrue(handler.should_remove_handler)


if __name__ == "__main__":
    unittest.main()
