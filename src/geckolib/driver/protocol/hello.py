"""Gecko <HELLO> handlers."""

from __future__ import annotations

import logging
import time
from typing import Any

from geckolib.const import GeckoConstants
from geckolib.driver.udp_protocol_handler import GeckoUdpProtocolHandler

HELLO_OPEN = b"<HELLO>"
HELLO_CLOSE = b"</HELLO>"

_LOGGER = logging.getLogger(__name__)


class GeckoHelloProtocolHandler(GeckoUdpProtocolHandler):
    """Gecko <HELLO> handler."""

    def __init__(self, content: bytes, **kwargs: Any) -> None:
        """Initialize the class."""
        super().__init__(**kwargs)
        self._send_bytes = b"".join([HELLO_OPEN, content, HELLO_CLOSE])
        self.was_broadcast_discovery: bool = False
        self._client_identifier: bytes | None = None
        self._spa_identifier: bytes | None = None
        self._spa_name: str | None = None
        self.last_response: float = time.monotonic()

    @staticmethod
    def broadcast_address(static_ip: str | None) -> tuple:
        """Generate a broadcast address."""
        if static_ip is not None:
            return (static_ip, GeckoConstants.INTOUCH2_PORT)
        return (GeckoConstants.BROADCAST_ADDRESS, GeckoConstants.INTOUCH2_PORT)

    @staticmethod
    def broadcast(**kwargs: object) -> GeckoHelloProtocolHandler:
        """Generate a broadcast class."""
        return GeckoHelloProtocolHandler(b"1", **kwargs)

    @staticmethod
    def client(client_identifier: bytes, **kwargs: object) -> GeckoHelloProtocolHandler:
        """Generate a client class."""
        return GeckoHelloProtocolHandler(client_identifier, **kwargs)

    @staticmethod
    def response(
        spa_identifier: bytes, spa_name: str, **kwargs: object
    ) -> GeckoHelloProtocolHandler:
        """Generate a server response class."""
        return GeckoHelloProtocolHandler(
            b"".join(
                [spa_identifier, b"|", spa_name.encode(GeckoConstants.MESSAGE_ENCODING)]
            ),
            **kwargs,
        )

    @property
    def client_identifier(self) -> bytes:
        """Get the client identifier or raise exception if not set."""
        assert self._client_identifier is not None  # noqa: S101
        return self._client_identifier

    @property
    def spa_identifier(self) -> bytes:
        """Get the spa identifier or raise exception if not set."""
        assert self._spa_identifier is not None  # noqa: S101
        return self._spa_identifier

    @property
    def spa_name(self) -> str:
        """Get the spa name or raise exception if not set."""
        assert self._spa_name is not None  # noqa: S101
        return self._spa_name

    def can_handle(self, received_bytes: bytes, _sender: tuple) -> bool:
        """Determine if we can handle the packet bytes."""
        return received_bytes.startswith(HELLO_OPEN) and received_bytes.endswith(
            HELLO_CLOSE
        )

    def handle(self, received_bytes: bytes, _sender: tuple) -> None:
        """Handle the packet bytes."""
        content = received_bytes[7:-8]
        self.was_broadcast_discovery = False
        self._client_identifier = self._spa_identifier = self._spa_name = None

        if content == b"1":
            self.was_broadcast_discovery = True

        elif content.startswith((b"IOS", b"AND")):
            self._client_identifier = content

        elif not content.find(b"|"):
            self._spa_identifier = content
            self._spa_name = "Unnamed SPA"

        else:
            self._spa_identifier, spa_name = content.split(b"|")
            self._spa_name = spa_name.decode(GeckoConstants.MESSAGE_ENCODING)

    def __repr__(self) -> str:
        """Get string representation of the class."""
        return (
            f"{super().__repr__()} (was_broadcast={self.was_broadcast_discovery},"
            f" client_id={self._client_identifier!r}, spa_id={self._spa_identifier!r},"
            f" spa_name={self._spa_name} )"
        )
