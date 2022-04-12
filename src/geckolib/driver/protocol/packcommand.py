""" Gecko SPACK/PACKS handlers """

import logging
import struct

from ...config import GeckoConfig
from .packet import GeckoPacketProtocolHandler

SPACK_VERB = b"SPACK"
PACKS_VERB = b"PACKS"
PACK_COMMAND_KEY_PRESS = 57
PACK_COMMAND_SET_VALUE = 70

_LOGGER = logging.getLogger(__name__)


class GeckoPackCommandProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def set_value(
        seq, pack_type, config_version, log_version, pos, len, data, **kwargs
    ):
        if len == 1:
            data = struct.pack(">B", data)
        elif len == 2:
            data = struct.pack(">H", data)
        else:
            raise OverflowError(len)

        return GeckoPackCommandProtocolHandler(
            content=b"".join(
                [
                    SPACK_VERB,
                    struct.pack(
                        ">BBBBBBH",
                        seq,
                        pack_type,
                        5 + len,
                        PACK_COMMAND_SET_VALUE,
                        config_version,
                        log_version,
                        pos,
                    ),
                    data,
                ]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def keypress(seq, pack_type, key, **kwargs):
        return GeckoPackCommandProtocolHandler(
            content=b"".join(
                [
                    SPACK_VERB,
                    struct.pack(
                        ">BBBBB", seq, pack_type, 2, PACK_COMMAND_KEY_PRESS, key
                    ),
                ]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(**kwargs):
        return GeckoPackCommandProtocolHandler(content=PACKS_VERB, **kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack_type = None
        self.is_key_press = False
        self.keycode = None
        self.is_set_value = False
        self.position = None
        self.new_data = None

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(SPACK_VERB) or received_bytes.startswith(
            PACKS_VERB
        )

    def handle(self, received_bytes: bytes, sender: tuple):
        remainder = received_bytes[5:]
        if received_bytes.startswith(PACKS_VERB):
            self._should_remove_handler = True
            return
        # Otherwise must be SPACK, so work out what is going on ...
        self._sequence, self.pack_type, length, command = struct.unpack(
            ">BBBB", remainder[0:4]
        )
        if command == PACK_COMMAND_KEY_PRESS:
            if length == 2:
                self.is_key_press = True
                self.is_set_value = False
                self.keycode = struct.unpack(">B", remainder[4:])[0]
            else:
                _LOGGER.warning("SPACK key press command incorrect length")
        elif command == PACK_COMMAND_SET_VALUE:
            self.is_set_value = True
            self.is_key_press = False
            config_version, log_version, self.position = struct.unpack(
                ">BBH", remainder[4:8]
            )
            self.new_data = remainder[8:]
        else:
            _LOGGER.warning("Unhandled SPACK command %d", command)
