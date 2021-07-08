""" Gecko <HELLO> handlers """

import logging
from ..udp_socket import GeckoUdpProtocolHandler
from ...const import GeckoConstants

HELLO_OPEN = b"<HELLO>"
HELLO_CLOSE = b"</HELLO>"

_LOGGER = logging.getLogger(__name__)


class GeckoHelloProtocolHandler(GeckoUdpProtocolHandler):
    def __init__(self, content: bytes, **kwargs):
        super().__init__(**kwargs)
        self._send_bytes = b"".join([HELLO_OPEN, content, HELLO_CLOSE])
        self.was_broadcast_discovery = False
        self.client_identifier = None
        self.spa_identifier = None
        self.spa_name = None

    @staticmethod
    def broadcast_address(static_ip):
        if static_ip is not None:
            return (static_ip, GeckoConstants.INTOUCH2_PORT)
        return (GeckoConstants.BROADCAST_ADDRESS, GeckoConstants.INTOUCH2_PORT)

    @staticmethod
    def broadcast(**kwargs):
        return GeckoHelloProtocolHandler(b"1", **kwargs)

    @staticmethod
    def client(client_identifier: bytes, **kwargs):
        return GeckoHelloProtocolHandler(client_identifier, **kwargs)

    @staticmethod
    def response(spa_identifier: bytes, spa_name: str, **kwargs):
        return GeckoHelloProtocolHandler(
            b"".join(
                [spa_identifier, b"|", spa_name.encode(GeckoConstants.MESSAGE_ENCODING)]
            ),
            **kwargs,
        )

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(HELLO_OPEN) and received_bytes.endswith(
            HELLO_CLOSE
        )

    def handle(self, socket, received_bytes: bytes, sender: tuple):
        content = received_bytes[7:-8]
        self.was_broadcast_discovery = False
        self.client_identifier = self.spa_identifier = self.spa_name = None
        if content == b"1":
            self.was_broadcast_discovery = True
        elif content.startswith(b"IOS") or content.startswith(b"AND"):
            self.client_identifier = content
        else:
            self.spa_identifier, spa_name = content.split(b"|")
            self.spa_name = spa_name.decode(GeckoConstants.MESSAGE_ENCODING)

    def __repr__(self):
        return (
            f"{super().__repr__()} (was_broadcast={self.was_broadcast_discovery},"
            f" client_id={self.client_identifier}, spa_id={self.spa_identifier},"
            f" spa_name={self.spa_name} )"
        )
