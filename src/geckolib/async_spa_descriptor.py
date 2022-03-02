""" GeckoAsyncSpaDescriptor class """

import logging

from .const import GeckoConstants

logger = logging.getLogger(__name__)


class GeckoAsyncSpaDescriptor:
    """A descriptor class for spas that have been discovered on the network"""

    def __init__(
        self,
        spa_identifier: bytes,
        spa_name: str,
        sender: tuple,
    ) -> None:
        self.identifier = spa_identifier
        self.name = spa_name
        self.ipaddress, self.port = sender

    @property
    def identifier_as_string(self) -> str:
        """The spa identifier as a string. Useful for storing in configuration and
        then passing as spa_identifier to the facade"""
        return self.identifier.decode(GeckoConstants.MESSAGE_ENCODING)

    @property
    def destination(self) -> tuple:
        return (self.ipaddress, self.port)

    def __repr__(self) -> str:
        return f"{self.name}({self.identifier_as_string})"
