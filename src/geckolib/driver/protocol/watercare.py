"""Gecko GETWC/WCGET/SETWC/WCSET/REQWC/WCREQ/ADDWC/MDFWC/DELWC handlers."""

from __future__ import annotations

import logging
import struct
from dataclasses import dataclass
from enum import IntEnum
from typing import TYPE_CHECKING, Any

from geckolib.config import GeckoConfig
from geckolib.const import GeckoConstants

from .packet import GeckoPacketProtocolHandler

if TYPE_CHECKING:
    from geckolib.driver.async_udp_protocol import GeckoAsyncUdpProtocol

GETWC_VERB = b"GETWC"  # Get watercare mode
WCGET_VERB = b"WCGET"  # Get watercare mode response
SETWC_VERB = b"SETWC"  # Set watercare mode
WCSET_VERB = b"WCSET"  # Set watercare mode response
REQWC_VERB = b"REQWC"  # Get watercare schedule list
WCREQ_VERB = b"WCREQ"  # Get watercare schedule list response
WCERR_VERB = b"WCERR"  # Watercare error
ADDWC_VERB = b"ADDWC"  # Add a watercare schedule
WCADD_VERB = b"WCADD"  # Add a watercare schedule response
MDFWC_VERB = b"MDFWC"  # Modify a watercare schedule
WCMDF_VERB = b"WCMDF"  # Modify a watercare schedule response
DELWC_VERB = b"DELWC"  # Delete a watercare schedule
WCDEL_VERB = b"WCDEL"  # Delete a watercare schedule response


GET_WATERCARE_FORMAT = ">B"
SET_WATERCARE_FORMAT = ">BB"

# A schedule record is (mode, type, number, start day, stop day, start hour,
# start minute, stop hour, stop minute), one byte each.
SCHEDULE_FORMAT = ">9B"
SCHEDULE_RECORD_SIZE = struct.calcsize(SCHEDULE_FORMAT)
# Deleting only needs to identify the schedule: (mode, type, number)
SCHEDULE_KEY_FORMAT = ">3B"

_LOGGER = logging.getLogger(__name__)


class GeckoWatercareScheduleType(IntEnum):
    """The kind of watercare schedule."""

    EMPTY = 0
    ECONOMY = 1
    FILTRATION = 2


class GeckoScheduleDay(IntEnum):
    """
    Day values used in schedules.

    The spa only stores a start and stop day in the range SUNDAY to SATURDAY.
    WEEKDAY, WEEKEND and EVERYDAY are conveniences that `day_range` expands.
    """

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    WEEKDAY = 7
    WEEKEND = 8
    EVERYDAY = 9

    @staticmethod
    def day_range(day: int) -> tuple[int, int]:
        """Get the (start, stop) day values the spa stores for a day selection."""
        if day == GeckoScheduleDay.EVERYDAY:
            return (GeckoScheduleDay.SUNDAY, GeckoScheduleDay.SATURDAY)
        if day == GeckoScheduleDay.WEEKDAY:
            return (GeckoScheduleDay.MONDAY, GeckoScheduleDay.FRIDAY)
        if day == GeckoScheduleDay.WEEKEND:
            return (GeckoScheduleDay.SATURDAY, GeckoScheduleDay.SUNDAY)
        return (GeckoScheduleDay(day), GeckoScheduleDay(day))


@dataclass(frozen=True)
class GeckoWatercareSchedule:
    """
    A single watercare schedule.

    `number` is the position of the schedule within its watercare mode. The
    spa numbers Economy schedules first, then Filtration schedules.
    """

    mode: int
    schedule_type: GeckoWatercareScheduleType
    number: int
    start_day: int
    stop_day: int
    start_hour: int
    start_minute: int
    stop_hour: int
    stop_minute: int

    def __post_init__(self) -> None:
        """Validate the values so we never send garbage to the spa."""
        if not 0 <= self.start_hour < 24 or not 0 <= self.stop_hour < 24:  # noqa: PLR2004
            msg = f"Hour must be 0-23 in {self}"
            raise ValueError(msg)
        if not 0 <= self.start_minute < 60 or not 0 <= self.stop_minute < 60:  # noqa: PLR2004
            msg = f"Minute must be 0-59 in {self}"
            raise ValueError(msg)
        if not (
            GeckoScheduleDay.SUNDAY <= self.start_day <= GeckoScheduleDay.SATURDAY
            and GeckoScheduleDay.SUNDAY <= self.stop_day <= GeckoScheduleDay.SATURDAY
        ):
            msg = f"Start and stop day must be SUNDAY to SATURDAY in {self}"
            raise ValueError(msg)
        if not 0 <= self.number <= 255:  # noqa: PLR2004
            msg = f"Schedule number must fit in a byte in {self}"
            raise ValueError(msg)

    @property
    def key(self) -> tuple[int, int, int]:
        """Identify this schedule: (mode, type, number)."""
        return (self.mode, int(self.schedule_type), self.number)

    @property
    def start_time(self) -> str:
        """Get the start time as HH:MM."""
        return f"{self.start_hour:02d}:{self.start_minute:02d}"

    @property
    def stop_time(self) -> str:
        """Get the stop time as HH:MM."""
        return f"{self.stop_hour:02d}:{self.stop_minute:02d}"

    def pack(self) -> bytes:
        """Pack into the 9 byte wire record."""
        return struct.pack(
            SCHEDULE_FORMAT,
            self.mode,
            int(self.schedule_type),
            self.number,
            self.start_day,
            self.stop_day,
            self.start_hour,
            self.start_minute,
            self.stop_hour,
            self.stop_minute,
        )

    @staticmethod
    def unpack(data: bytes) -> GeckoWatercareSchedule:
        """Unpack from the 9 byte wire record."""
        (mode, kind, number, start_day, stop_day, sh, sm, eh, em) = struct.unpack(
            SCHEDULE_FORMAT, data
        )
        return GeckoWatercareSchedule(
            mode,
            GeckoWatercareScheduleType(kind),
            number,
            start_day,
            stop_day,
            sh,
            sm,
            eh,
            em,
        )


class GeckoWatercareScheduleManager:
    """Holds a set of watercare schedules, as reported by the spa."""

    def __init__(self, schedules: list[GeckoWatercareSchedule] | None = None) -> None:
        """Initialize the schedule manager."""
        self.schedules: list[GeckoWatercareSchedule] = list(schedules or [])

    def for_mode(self, mode: int) -> list[GeckoWatercareSchedule]:
        """Get the schedules for a watercare mode, in spa order."""
        return sorted(
            (s for s in self.schedules if s.mode == mode), key=lambda s: s.number
        )

    def next_number(self, mode: int, schedule_type: GeckoWatercareScheduleType) -> int:
        """
        Get the number a new schedule of this type would be given.

        Economy schedules come first, then filtration, so a new economy schedule
        is numbered after the existing economy ones, and a new filtration
        schedule after everything.
        """
        existing = self.for_mode(mode)
        if schedule_type == GeckoWatercareScheduleType.ECONOMY:
            return sum(1 for s in existing if s.schedule_type == schedule_type)
        return len(existing)

    def __len__(self) -> int:
        """Get the number of schedules."""
        return len(self.schedules)


class GeckoGetWatercareModeProtocolHandler(GeckoPacketProtocolHandler):
    """Get watercare mode protocol handler class."""

    @staticmethod
    def get(seq: int, **kwargs: Any) -> GeckoGetWatercareModeProtocolHandler:
        """Generate a request."""
        return GeckoGetWatercareModeProtocolHandler(
            content=b"".join([GETWC_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def get_response(mode: int, **kwargs: Any) -> GeckoGetWatercareModeProtocolHandler:
        """Generate a watercare mode request response."""
        return GeckoGetWatercareModeProtocolHandler(
            content=b"".join(
                [
                    WCGET_VERB,
                    struct.pack(
                        GET_WATERCARE_FORMAT,
                        mode,
                    ),
                ]
            ),
            **kwargs,
        )

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((GETWC_VERB, WCGET_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        self.mode = None
        if received_bytes.startswith(GETWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list
        # Otherwise must be WCSET
        self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0] % len(
            GeckoConstants.WATERCARE_MODE
        )
        self._should_remove_handler = True


class GeckoSetWatercareModeProtocolHandler(GeckoPacketProtocolHandler):
    """Set watercare mode protocol handler class."""

    @staticmethod
    def set(seq: int, mode: int, **kwargs: Any) -> GeckoSetWatercareModeProtocolHandler:
        """Generatge a watercare set command."""
        return GeckoSetWatercareModeProtocolHandler(
            content=b"".join(
                [SETWC_VERB, struct.pack(SET_WATERCARE_FORMAT, seq, mode)]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            **kwargs,
        )

    @staticmethod
    def set_response(mode: int, **kwargs: Any) -> GeckoSetWatercareModeProtocolHandler:
        """Generate a watercare set mode response."""
        return GeckoSetWatercareModeProtocolHandler(
            content=b"".join([WCSET_VERB, struct.pack(GET_WATERCARE_FORMAT, mode)]),
            **kwargs,
        )

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((SETWC_VERB, WCSET_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        self.mode = None
        if received_bytes.startswith(SETWC_VERB):
            self._sequence, self.mode = struct.unpack(SET_WATERCARE_FORMAT, remainder)
            self.mode %= len(GeckoConstants.WATERCARE_MODE)
            return  # Stay in the handler list
        # Otherwise must be WCSET
        self.mode = struct.unpack(GET_WATERCARE_FORMAT, remainder)[0]
        self._should_remove_handler = True


class GeckoGetWatercareScheduleListProtocolHandler(GeckoPacketProtocolHandler):
    """
    Get list of watercare schedules.

    The spa may split the list over several WCREQ packets. Each starts with two
    bytes: the index of this packet, and the index of the next packet (0 if
    this was the last). The handler collects all the fragments, and only
    finishes when the last has arrived.
    """

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the schedule list handler."""
        super().__init__(**kwargs)
        self.schedules: list[GeckoWatercareSchedule] = []
        self._expected_index = 0
        self._is_complete = False

    @property
    def is_complete(self) -> bool:
        """Have all the fragments of the response been received."""
        return self._is_complete

    @staticmethod
    def get(seq: int, **kwargs: Any) -> GeckoGetWatercareScheduleListProtocolHandler:
        """Generate a request."""
        return GeckoGetWatercareScheduleListProtocolHandler(
            content=b"".join([REQWC_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def get_response(
        schedule: GeckoWatercareScheduleManager | None = None, **kwargs: Any
    ) -> GeckoGetWatercareScheduleListProtocolHandler:
        """Generate the response (as a single fragment)."""
        if schedule is not None and len(schedule) > 0:
            records = b"".join(s.pack() for s in schedule.schedules)
        else:
            records = b"".join(
                [
                    b"\x00\x01\x00\x00\x06\x00\x00\x00\x00",
                    b"\x02\x01\x00\x01\x05\x06\x00\x12\x00"
                    b"\x03\x01\x00\x00\x06\x06\x00\x12\x00"
                    b"\x04\x01\x00\x01\x05\x00\x00\x00\x00",
                ]
            )
        return GeckoGetWatercareScheduleListProtocolHandler.get_response_fragment(
            0, 0, records, **kwargs
        )

    @staticmethod
    def get_response_fragment(
        index: int, next_index: int, records: bytes, **kwargs: Any
    ) -> GeckoGetWatercareScheduleListProtocolHandler:
        """Generate one fragment of the response."""
        return GeckoGetWatercareScheduleListProtocolHandler(
            content=b"".join(
                [WCREQ_VERB, struct.pack(">BB", index, next_index), records]
            ),
            **kwargs,
        )

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((REQWC_VERB, WCREQ_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(REQWC_VERB):
            self._sequence = struct.unpack(">B", remainder)[0]
            return  # Stay in the handler list

        # Otherwise must be WCREQ
        if len(remainder) < 2:  # noqa: PLR2004
            _LOGGER.warning("Ignoring truncated watercare schedule packet")
            return
        index, next_index = remainder[0], remainder[1]
        if index == 0:
            # A (re)start of the list
            self.schedules = []
        elif index != self._expected_index:
            _LOGGER.warning(
                "Watercare schedule packet %d received, expected %d, ignored",
                index,
                self._expected_index,
            )
            return

        body = remainder[2:]
        usable = len(body) - len(body) % SCHEDULE_RECORD_SIZE
        for offset in range(0, usable, SCHEDULE_RECORD_SIZE):
            record = body[offset : offset + SCHEDULE_RECORD_SIZE]
            try:
                self.schedules.append(GeckoWatercareSchedule.unpack(record))
            except ValueError:
                _LOGGER.warning("Ignoring invalid watercare schedule %r", record)

        self._expected_index = next_index
        if next_index == 0:
            self._is_complete = True
            self._should_remove_handler = True

    async def wait_for_response(
        self,
        protocol: GeckoAsyncUdpProtocol,
        packet_timeout: int = GeckoConfig.PAUSE_BETWEEN_RETRIES_IN_SECONDS,
    ) -> bool:
        """Wait for every fragment of the response, not just the first."""
        while not self._is_complete:
            if await super().wait_for_response(protocol, packet_timeout):
                return True  # Timed out, the caller will retry from the start
        return False


class _GeckoWatercareScheduleChangeProtocolHandler(GeckoPacketProtocolHandler):
    """Base for the add/modify/delete schedule handlers."""

    REQUEST_VERB: bytes
    RESPONSE_VERB: bytes
    HAS_FULL_RECORD = True

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the handler."""
        super().__init__(**kwargs)
        self.schedule: GeckoWatercareSchedule | None = None
        self.key: tuple[int, int, int] | None = None

    @classmethod
    def _request_content(cls, seq: int, schedule: GeckoWatercareSchedule) -> bytes:
        payload = (
            schedule.pack()
            if cls.HAS_FULL_RECORD
            else struct.pack(SCHEDULE_KEY_FORMAT, *schedule.key)
        )
        return b"".join([cls.REQUEST_VERB, struct.pack(">B", seq), payload])

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle the verb."""
        return received_bytes.startswith((self.REQUEST_VERB, self.RESPONSE_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        if received_bytes.startswith(self.REQUEST_VERB):
            remainder = received_bytes[5:]
            self._sequence = remainder[0]
            if self.HAS_FULL_RECORD:
                self.schedule = GeckoWatercareSchedule.unpack(remainder[1:])
                self.key = self.schedule.key
            else:
                self.key = struct.unpack(SCHEDULE_KEY_FORMAT, remainder[1:])
            return  # Stay in the handler list
        # Otherwise it is the acknowledgement
        self._should_remove_handler = True


class GeckoAddWatercareScheduleProtocolHandler(
    _GeckoWatercareScheduleChangeProtocolHandler
):
    """Add a watercare schedule."""

    REQUEST_VERB = ADDWC_VERB
    RESPONSE_VERB = WCADD_VERB

    @classmethod
    def add(
        cls, seq: int, schedule: GeckoWatercareSchedule, **kwargs: Any
    ) -> GeckoAddWatercareScheduleProtocolHandler:
        """Generate an add command."""
        return cls(
            content=cls._request_content(seq, schedule),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @classmethod
    def add_response(cls, **kwargs: Any) -> GeckoAddWatercareScheduleProtocolHandler:
        """Generate an add response."""
        return cls(content=WCADD_VERB, **kwargs)


class GeckoModifyWatercareScheduleProtocolHandler(
    _GeckoWatercareScheduleChangeProtocolHandler
):
    """Modify a watercare schedule, identified by its mode, type and number."""

    REQUEST_VERB = MDFWC_VERB
    RESPONSE_VERB = WCMDF_VERB

    @classmethod
    def modify(
        cls, seq: int, schedule: GeckoWatercareSchedule, **kwargs: Any
    ) -> GeckoModifyWatercareScheduleProtocolHandler:
        """Generate a modify command."""
        return cls(
            content=cls._request_content(seq, schedule),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @classmethod
    def modify_response(
        cls, **kwargs: Any
    ) -> GeckoModifyWatercareScheduleProtocolHandler:
        """Generate a modify response."""
        return cls(content=WCMDF_VERB, **kwargs)


class GeckoDeleteWatercareScheduleProtocolHandler(
    _GeckoWatercareScheduleChangeProtocolHandler
):
    """Delete a watercare schedule, identified by its mode, type and number."""

    REQUEST_VERB = DELWC_VERB
    RESPONSE_VERB = WCDEL_VERB
    HAS_FULL_RECORD = False

    @classmethod
    def delete(
        cls, seq: int, schedule: GeckoWatercareSchedule, **kwargs: Any
    ) -> GeckoDeleteWatercareScheduleProtocolHandler:
        """Generate a delete command."""
        return cls(
            content=cls._request_content(seq, schedule),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @classmethod
    def delete_response(
        cls, **kwargs: Any
    ) -> GeckoDeleteWatercareScheduleProtocolHandler:
        """Generate a delete response."""
        return cls(content=WCDEL_VERB, **kwargs)


class GeckoWatercareErrorHandler(GeckoPacketProtocolHandler):
    """Watercare error handler."""

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith(WCERR_VERB)

    def handle(self, _received_bytes: bytes, _sender: tuple) -> None:
        """Handle this."""
