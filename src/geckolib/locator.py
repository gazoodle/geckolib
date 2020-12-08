""" Gecko Locator class """

import logging
import time

from .driver import (
    GeckoUdpSocket,
    GeckoHelloProtocolHandler,
)
from .const import GeckoConstants
from .spa import GeckoSpaDescriptor

logger = logging.getLogger(__name__)


class GeckoLocator:
    """
    GeckoLocator class locates in.touch2 devices on your local LAN
    """

    def __init__(self, client_uuid):
        self.client_identifier = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)
        self.spas = []

    def __enter__(self):
        self._discover()
        return self

    def __exit__(self, *args):
        pass

    def _discover(self):
        with GeckoUdpSocket() as socket:
            logger.info("Discovery process started")
            socket.enable_broadcast()

            self.spas = []

            hello_protocol_handler = GeckoHelloProtocolHandler.broadcast(
                on_handled=lambda handler, socket, sender: self.spas.append(
                    GeckoSpaDescriptor(
                        self.client_identifier,
                        handler.spa_identifier,
                        handler.spa_name,
                        sender,
                    )
                )
            )
            socket.add_receive_handler(hello_protocol_handler)
            socket.queue_send(
                hello_protocol_handler,
                GeckoHelloProtocolHandler.broadcast_address(),
            )
            # Give it a second to settle down
            time.sleep(1)
            now = time.monotonic()
            # Wait for a while to see what we've got
            while time.monotonic() - now < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
                if len(self.spas) > 0:
                    logger.info(
                        "Found %d spas ... %s",
                        len(self.spas),
                        [(spa.name, spa.identifier) for spa in self.spas],
                    )
                    return

    def get_spa_from_identifier(self, identifier):
        """ Locate a spa based on its identifier """
        return next(spa for spa in self.spas if spa.identifier == identifier)

    def get_spa_from_name(self, name):
        """ Locate a spa based on its name """
        return next(spa for spa in self.spas if spa.name == name)
