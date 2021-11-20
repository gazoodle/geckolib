""" Gecko REQRM/RMREQ handlers """

import logging
import struct

from .packet import GeckoPacketProtocolHandler

REQRM_VERB = b"REQRM"
RMREQ_VERB = b"RMREQ"

RESPONSE_FORMAT = ">BBB"

_LOGGER = logging.getLogger(__name__)


desc = ["Invalid", "RinseFilter", "CleanFilter", "ChangeWater",
        "CheckSpa", "ChangeOzonator", "ChangeVisionCartridge"]


class GeckoRemindersProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoRemindersProtocolHandler(
            content=b"".join([REQRM_VERB, struct.pack(">B", seq)]), **kwargs
        )

    @staticmethod
    def response(**kwargs):
        return GeckoRemindersProtocolHandler(
            content=b"".join(
                [
                    RMREQ_VERB,
                    b"\x01\x01\x00\x01\x02\x1f\x00\x01\x03\x29"
                    b"\x00\x01\x04\xa9\x02\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00"
                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reminders = []

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(REQRM_VERB) or received_bytes.startswith(
            RMREQ_VERB
        )

    def handle(self, socket, received_bytes: bytes, sender: tuple):
        reminder = received_bytes[5:]
        if received_bytes.startswith(REQRM_VERB):
            self._sequence = struct.unpack(">B", reminder[0:1])[0]
            return  # Stay in the handler list

        # Otherwise must be RMREQ
        rest = reminder
        while (len(rest) > 0):
            (t, days, push, rest) = struct.unpack(
                '<BhB{}s'.format(len(rest)-4), rest)
            _LOGGER.debug(f"T:{t}, Days:{days}, Push:{push}, Rest:{rest}")
            if (t > 0):
                _LOGGER.debug(f"{desc[t]} {days} days")
            self.reminders.append(tuple((desc[t], days)))

        self._should_remove_handler = True
