""" GeckoSpaDescriptor class """

import logging


from .const import GeckoConstants
from .automation import GeckoFacade
from .spa import GeckoSpa

logger = logging.getLogger(__name__)


class GeckoSpaDescriptor:
    """ A descriptor class for spas that have been discovered on the network """

    def __init__(
        self,
        client_identifier: bytes,
        spa_identifier: bytes,
        spa_name: str,
        sender: tuple,
    ):
        self.client_identifier = client_identifier
        self.identifier = spa_identifier
        self.name = spa_name
        self.ipaddress, self.port = sender

    def get_facade(self, wait_for_connection=True):
        """Get an automation facade to interact with the spa described
        by this class"""
        facade = GeckoFacade(GeckoSpa(self).start_connect())
        if wait_for_connection:
            while not facade.is_connected:
                facade.wait(0.1)
        return facade

    @property
    def identifier_as_string(self):
        return self.identifier.decode(GeckoConstants.MESSAGE_ENCODING)

    @property
    def destination(self):
        return (self.ipaddress, self.port)

    def __repr__(self):
        return f"{self.name}({self.identifier_as_string})"
