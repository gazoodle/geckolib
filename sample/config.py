"""Configuration class for complete async example"""

import configparser
import logging

# Configuration file constants
CONFIG_FILE = "sample.ini"
CK_DEFAULT = "DEFAULT"
CK_SPA_ID = "SPA_ID"
CK_SPA_ADDR = "SPA_ADDR"

_LOGGER = logging.getLogger(__name__)


class Config:
    """Hold the configuration for the complete async example app"""

    def __init__(self):
        _LOGGER.debug("Read config from %s", CONFIG_FILE)
        self._config = configparser.ConfigParser()
        self._config.read(CONFIG_FILE)

        # self._config[CK_DEFAULT][CK_SPA_ID] = "SPA80:1f:12:5c:d3:c0"
        # self._config[CK_DEFAULT][CK_SPA_ADDR] = "10.0.208.216"
        # self.save()

    def save(self) -> None:
        with open(CONFIG_FILE, "w") as configfile:
            self._config.write(configfile)

    @property
    def spa_id(self) -> str:
        if CK_SPA_ID in self._config[CK_DEFAULT]:
            return self._config[CK_DEFAULT][CK_SPA_ID]
        return None

    @property
    def spa_address(self) -> str:
        if CK_SPA_ADDR in self._config[CK_DEFAULT]:
            return self._config[CK_DEFAULT][CK_SPA_ADDR]
        return None
