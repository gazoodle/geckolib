""" Gecko Locator class """

import logging
import time
import threading

from .driver import (
    GeckoUdpSocket,
    GeckoHelloProtocolHandler,
)
from .const import GeckoConstants
from .config import GeckoConfig
from .spa_descriptor import GeckoSpaDescriptor


_LOGGER = logging.getLogger(__name__)


class GeckoLocator:
    """
    GeckoLocator class locates in.touch2 devices on your local LAN
    """

    def __init__(self, client_uuid, **kwargs):
        self.client_identifier = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)
        self.spas = []
        self.spa_identifiers = []
        self._retry_thread = threading.Thread(
            target=self._retry_thread_func, daemon=True
        )
        self._socket = None
        self._on_found = kwargs.get("on_found", None)
        self._spa_to_find = kwargs.get("spa_to_find", None)
        self._static_ip = kwargs.get("static_ip", None)
        if self._static_ip == "":
            self._static_ip = None
        self._has_found_spa = False
        self._started = None

    def __enter__(self):
        self.start_discovery(True)
        return self

    def __exit__(self, *args):
        if self._socket.isopen:
            self._socket.close()
        if self._retry_thread.is_alive:
            self._retry_thread.join()

    def complete(self):
        """Finish using this locator if not used in a with context"""
        self.__exit__()

    def _on_discovered(self, handler, sender):
        if handler.spa_identifier in self.spa_identifiers:
            return
        self.spa_identifiers.append(handler.spa_identifier)
        descriptor = GeckoSpaDescriptor(
            self.client_identifier,
            handler.spa_identifier,
            handler.spa_name,
            sender,
        )
        self.spas.append(descriptor)
        if self._on_found is not None:
            self._on_found(descriptor)
        if self._spa_to_find is not None:
            if descriptor.identifier_as_string == self._spa_to_find:
                self._has_found_spa = True
            if descriptor.identifier == self._spa_to_find:
                self._has_found_spa = True
        if self._static_ip is not None:
            self._has_found_spa = True

    @property
    def age(self):
        return time.monotonic() - self._started

    @property
    def has_had_enough_time(self):
        return self.age > GeckoConfig.DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS

    def wait(self, timeout):
        self._socket.wait(timeout)

    def start_discovery(self, should_wait=False):
        _LOGGER.info("Discovery process started")
        self._socket = GeckoUdpSocket()
        self._socket.open()
        self._socket.enable_broadcast()
        self._socket.add_receive_handler(
            GeckoHelloProtocolHandler.broadcast(on_handled=self._on_discovered)
        )
        self._started = time.monotonic()
        self._retry_thread.start()
        if should_wait:
            try:

                while self.age < GeckoConfig.DISCOVERY_TIMEOUT_IN_SECONDS:
                    if self.has_had_enough_time:
                        if len(self.spas) > 0:
                            _LOGGER.info(
                                "Found %d spas ... %s", len(self.spas), self.spas
                            )
                            return
                    if self._has_found_spa:
                        return
                    self._socket.wait(0.1)
            finally:
                self._socket.close()

    def _retry_thread_func(self):
        _LOGGER.debug("Locator retry thread started")
        while self._socket.isopen:
            # Only broadcast for the full discovery time
            if self.age < GeckoConfig.DISCOVERY_TIMEOUT_IN_SECONDS:
                self._socket.queue_send(
                    GeckoHelloProtocolHandler.broadcast(),
                    GeckoHelloProtocolHandler.broadcast_address(
                        static_ip=self._static_ip
                    ),
                )
            self._socket.wait(1)
        _LOGGER.debug("Locator retry thread stopped")

    def get_spa_from_identifier(self, identifier):
        """Locate a spa based on its identifier"""
        try:
            if isinstance(identifier, bytes):
                return next(spa for spa in self.spas if spa.identifier == identifier)
            return next(
                spa for spa in self.spas if spa.identifier_as_string == identifier
            )
        except StopIteration:
            _LOGGER.error(
                "Cannot find spa from identifier %s, using first one ...", identifier
            )
            return self.spas[0]

    def get_spa_from_name(self, name):
        """Locate a spa based on its name"""
        try:
            return next(spa for spa in self.spas if spa.name == name)
        except StopIteration:
            _LOGGER.error("Cannot find spa from name %s", name)
            return None

    @staticmethod
    def find_spa(client_uuid, spa_identifier, spa_address=None):
        with GeckoLocator(
            client_uuid, spa_to_find=spa_identifier, static_ip=spa_address
        ) as locator:
            return locator.get_spa_from_identifier(spa_identifier)

    @staticmethod
    def get_facade(client_uuid, spa_id, spa_address=None):
        return GeckoLocator.find_spa(client_uuid, spa_id, spa_address).get_facade(False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(age={self.age},has_had_enough_time="
            f"{self.has_had_enough_time},spas={self.spas})"
        )
