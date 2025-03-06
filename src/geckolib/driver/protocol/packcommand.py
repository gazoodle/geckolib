"""Gecko SPACK/PACKS handlers."""

from __future__ import annotations

import logging
import struct
from typing import Any

from geckolib.config import GeckoConfig
from geckolib.driver.accessor import GeckoStructAccessor

from .packet import GeckoPacketProtocolHandler

SPACK_VERB = b"SPACK"
PACKS_VERB = b"PACKS"
PACK_COMMAND_KEY_PRESS = 57
PACK_COMMAND_SET_VALUE = 70

_LOGGER = logging.getLogger(__name__)


class GeckoPackCommandProtocolHandler(GeckoPacketProtocolHandler):
    """Pack Command handler."""

    @staticmethod
    def set_value(  # noqa: PLR0913
        seq: int,
        pack_type: int,
        config_version: int,
        log_version: int,
        pos: int,
        length: int,
        data: Any,
        **kwargs: Any,
    ) -> GeckoPackCommandProtocolHandler:
        """Generate a SetValue command."""
        return GeckoPackCommandProtocolHandler(
            content=b"".join(
                [
                    SPACK_VERB,
                    struct.pack(
                        ">BBBBBBH",
                        seq,
                        pack_type,
                        5 + length,
                        PACK_COMMAND_SET_VALUE,
                        config_version,
                        log_version,
                        pos,
                    ),
                    GeckoStructAccessor.pack_data(length, data),
                ]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS * 3,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def keypress(
        seq: int, pack_type: int, key: int, **kwargs: Any
    ) -> GeckoPackCommandProtocolHandler:
        """Generate a KeyPress command."""
        return GeckoPackCommandProtocolHandler(
            content=b"".join(
                [
                    SPACK_VERB,
                    struct.pack(
                        ">BBBBB", seq, pack_type, 2, PACK_COMMAND_KEY_PRESS, key
                    ),
                ]
            ),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS * 3,
            on_retry_failed=GeckoPacketProtocolHandler.default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(**kwargs: Any) -> GeckoPackCommandProtocolHandler:
        """Generate a response."""
        return GeckoPackCommandProtocolHandler(content=PACKS_VERB, **kwargs)

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)
        self.pack_type = None
        self.is_key_press = False
        self.keycode = None
        self.is_set_value = False
        self.position = None
        self.length = None
        self.new_data = None

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we handle this verb."""
        return received_bytes.startswith((SPACK_VERB, PACKS_VERB))

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the verb."""
        remainder = received_bytes[5:]
        if received_bytes.startswith(PACKS_VERB):
            self._should_remove_handler = True
            return
        # Otherwise must be SPACK, so work out what is going on ...
        self._sequence, self.pack_type, self.length, command = struct.unpack(
            ">BBBB", remainder[0:4]
        )
        if command == PACK_COMMAND_KEY_PRESS:
            if self.length == 2:  # noqa: PLR2004
                self.is_key_press = True
                self.is_set_value = False
                self.keycode = struct.unpack(">B", remainder[4:])[0]
            else:
                _LOGGER.warning("SPACK key press command incorrect length")
        elif command == PACK_COMMAND_SET_VALUE:
            self.is_set_value = True
            self.is_key_press = False
            self.length -= 5
            config_version, log_version, self.position = struct.unpack(
                ">BBH", remainder[4:8]
            )
            self.new_data = remainder[8:]
        else:
            _LOGGER.warning("Unhandled SPACK command %d", command)
