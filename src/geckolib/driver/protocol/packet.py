""" Gecko <PACKT> handlers """

import logging
import re

from ..udp_socket import GeckoUdpProtocolHandler

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._parms = kwargs.get("parms")
        self._content = kwargs.get("content", None)
        if self._content is not None:
            if not isinstance(self._content, bytes):
                raise TypeError(self._content, "Content must be of type `bytes`")
        self._packet_content = None
        self._sequence = None

    @property
    def send_bytes(self):
        return b"".join(
            [
                PACKET_OPEN,
                SRCCN_OPEN,
                self._parms[3],
                SRCCN_CLOSE,
                DESCN_OPEN,
                self._parms[2],
                DESCN_CLOSE,
                DATAS_OPEN,
                self._content,
                DATAS_CLOSE,
                PACKET_CLOSE,
            ]
        )

    @property
    def parms(self):
        return self._parms

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        # If the received bytes start with <PACKET>, we can help
        return received_bytes.startswith(PACKET_OPEN) and received_bytes.endswith(
            PACKET_CLOSE
        )

    def _extract_packet_parts(self, content):
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

    def handle(self, socket, received_bytes: bytes, sender: tuple):
        (
            src_identifier,
            dest_identifier,
            self._packet_content,
        ) = self._extract_packet_parts(received_bytes[7:-8])
        self._parms = (sender[0], sender[1], src_identifier, dest_identifier)
        if socket is not None:
            socket.dispatch_recevied_data(self._packet_content, self._parms)

    @property
    def packet_content(self):
        return self._packet_content

    def __repr__(self):
        return (
            f"{super().__repr__()}(parms={self.parms!r},"
            f" content={self.packet_content!r})"
        )
