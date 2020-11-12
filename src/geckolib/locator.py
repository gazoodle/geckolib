""" Gecko Locator class """

import logging
import socket
import time

from .driver import GeckoComms
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
        )
        self.spas = []

    def __enter__(self):
        self._discover()
        return self

    def __exit__(self, *args):
        pass

    def complete(self):
        """ Finish using the manager class """
        print("Manager finish")
        for spa in self.spas:
            spa.complete()

    def _discover(self):
        with GeckoComms() as comms:
            logger.info("Discovery process started")
            comms.set_broadcast()
            self.spas = []
            retry_count = 0
            while retry_count < GeckoConstants.DISCOVERY_RETRY_COUNT_TO_FIND_ANY_SPA:
                # Broadcast the discovery message to every client on the local LAN
                comms.send_message(
                    GeckoConstants.MESSAGE_HELLO.format(1), GeckoConstants.BROADCAST_ADDRESS
                )
                # Wait to ensure we've heard from all the modules that responded within
                # the discovery period
                now = time.monotonic()
                while time.monotonic() - now < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
                    try:
                        self.spas.append(GeckoSpaDescriptor(self.client_identifier, comms.receive_answer()))
                    except socket.timeout:
                        break
                if len(self.spas) > 0:
                    # Dummy spa to test multiple spas in client programs ... will not actually respond!
                    if GeckoConstants.INCLUDE_DUMMY_SPA:
                        self.spas.append(
                            GeckoSpaDescriptor(
                                self.client_identifier,
                                (
                                    b"<HELLO>SPA90:1f:12:5c:d3:c0|Dummy Spa</HELLO>",
                                    ("127.0.0.1", 10022),
                                ),
                            )
                        )
                    logger.info(
                        "Found %d spas ... %s",
                        len(self.spas),
                        [(spa.name, spa.identifier) for spa in self.spas],
                    )
                    return
                retry_count += 1
                logger.info(
                    "Didn't find any spas within %d seconds, retry # %d",
                    GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS,
                    retry_count,
                )
            logger.warning(
                "No spas found, check that you are on the same LAN as your in.touch2 device"
            )

    def get_spa_from_identifier(self, identifier):
        """ Locate a spa based on its identifier """
        return next(spa for spa in self.spas if spa.identifier == identifier)

    def get_spa_from_name(self, name):
        """ Locate a spa based on its name """
        return next(spa for spa in self.spas if spa.name == name)
