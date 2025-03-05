"""Gecko <PACKT> handlers."""

import logging
import re
from typing import Any

from geckolib.driver.udp_protocol_handler import GeckoUdpProtocolHandler

PACKET_OPEN = b"<PACKT>"
PACKET_CLOSE = b"</PACKT>"
SRCCN_OPEN = b"<SRCCN>"
SRCCN_CLOSE = b"</SRCCN>"
DESCN_OPEN = b"<DESCN>"
DESCN_CLOSE = b"</DESCN>"
DATAS_OPEN = b"<DATAS>"
DATAS_CLOSE = b"</DATAS>"

_LOGGER = logging.getLogger(__name__)


class GeckoPacketProtocolHandler(GeckoUdpProtocolHandler):
    """Handle the PACKT structure."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)
        self._parms: tuple = kwargs.get("parms")
        self._content: bytes = kwargs.get("content")
        self._on_get_parms = kwargs.get("on_get_parms")
        if self._content is not None and not isinstance(self._content, bytes):
            raise TypeError(self._content, "Content must be of type `bytes`")
        self._packet_content = None
        self._sequence = None

    @property
    def send_bytes(self) -> bytes:
        """Generate the bytes to send."""
        parms = self.parms
        return b"".join(
            [
                PACKET_OPEN,
                SRCCN_OPEN,
                parms[3],
                SRCCN_CLOSE,
                DESCN_OPEN,
                parms[2],
                DESCN_CLOSE,
                DATAS_OPEN,
                self._content,
                DATAS_CLOSE,
                PACKET_CLOSE,
            ]
        )

    @property
    def parms(self) -> tuple:
        """Delegate parms."""
        if self._on_get_parms is None:
            return self._parms
        return self._on_get_parms(self)

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Can we unwrap this packet."""
        # If the received bytes start with <PACKET>, we can help
        return received_bytes.startswith(PACKET_OPEN) and received_bytes.endswith(
            PACKET_CLOSE
        )

    def _extract_packet_parts(self, content: bytes) -> tuple:
        match = re.search(
            b"".join(
                [
                    SRCCN_OPEN,
                    b"(.*)",
                    SRCCN_CLOSE,
                    DESCN_OPEN,
                    b"(.*)",
                    DESCN_CLOSE,
                    DATAS_OPEN,
                    b"(.*)",
                    DATAS_CLOSE,
                ]
            ),
            content,
            re.DOTALL,
        )
        if match:
            return match.groups()
        return (None, None, None)

    def handle(self, received_bytes: bytes, sender: tuple) -> None:
        """Unwrap the packet and dispatch."""
        (
            src_identifier,
            dest_identifier,
            self._packet_content,
        ) = self._extract_packet_parts(received_bytes[7:-8])
        self._parms = (sender[0], sender[1], src_identifier, dest_identifier)

    @property
    def packet_content(self) -> bytes | None:
        """Get packet content."""
        return self._packet_content

    def __repr__(self) -> str:
        """Get string representation."""
        return (
            f"{super().__repr__()}(parms={self.parms!r},"
            f" content={self.packet_content!r})"
        )
