""" Manager class """

import logging
import os
import socket
import time
import xml.etree.ElementTree as ET

import urllib3

from .driver import GeckoComms
from .const import GeckoConstants
from .spa import GeckoSpa
from ._version import VERSION

logger = logging.getLogger(__name__)


class GeckoManager(GeckoComms):
    """
    GeckoManager class manages the local spa collection and hosts the discovery process
    """

    def __init__(self, client_uuid):
        super().__init__(self)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        if not os.path.exists(GeckoConstants.SPA_PACK_STRUCT_FILE):
            logger.info("SpaPackStruct.xml not found, downloading from the internet...")
            self.download()
        self.spa_pack_struct = ET.parse(GeckoConstants.SPA_PACK_STRUCT_FILE)
        self.spa_pack_struct_revision = self.spa_pack_struct.find(
            GeckoConstants.SPA_PACK_REVISION_XPATH
        ).attrib[GeckoConstants.SPA_PACK_REVISION_ATTRIB]
        self.client_identifier = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        )
        logger.info("SpaPackStruct v%s", self.spa_pack_struct_revision)
        logger.info("Client identifier %s", self.client_identifier)
        self.retry_count = 0
        self.spas = []

    def finish(self):
        """ Disconnect all the connected spas and release the background worker threads """
        for spa in self.spas:
            spa.disconnect()

    def download(self):
        """ Download SpaPackStruct.xml from it's permanent home """
        logger.info("Downloading SpaPackStruct.xml")
        http = urllib3.PoolManager()
        response = http.request(
            "GET", GeckoConstants.SPA_PACK_STRUCT_URL, preload_content=False
        )

        with open(GeckoConstants.SPA_PACK_STRUCT_FILE, "wb") as out:
            while True:
                data = response.read(4096)
                if not data:
                    break
                out.write(data)

        response.release_conn()
        logger.info("SpaPackStruct.xml downloaded")

    def discover(self):
        """Start the discovery process to locate any intouch2 capable
        Gecko modules on the local network."""
        logger.info("Discovery process started")
        self.spas = []
        while self.retry_count < GeckoConstants.DISCOVERY_RETRY_COUNT_TO_FIND_ANY_SPA:
            # Broadcast the discovery message to every client on the local LAN
            self.send_message(
                GeckoConstants.MESSAGE_HELLO.format(1), GeckoConstants.BROADCAST_ADDRESS
            )
            # Wait to ensure we've heard from all the modules that responded within
            # the discovery period
            now = time.monotonic()
            while time.monotonic() - now < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
                try:
                    self.spas.append(GeckoSpa(self, self.receive_answer()))
                except socket.timeout:
                    break
            if len(self.spas) > 0:
                # Dummy spa to test multiple spas in client programs ... will not actually respond!
                if GeckoConstants.INCLUDE_DUMMY_SPA:
                    self.spas.append(
                        GeckoSpa(
                            self,
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
            self.retry_count += 1
            logger.info(
                "Didn't find any spas within %d seconds, retry %d",
                GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS,
                self.retry_count,
            )
        logger.warning(
            "No spas found, check that you are on the same LAN as your in.touch2 device"
        )

    @property
    def version(self):
        """ Get the version of the library """
        return "v{0}".format(VERSION)
