"""Configuration class for complete async example"""

import configparser
import logging

# Configuration file constants
CONFIG_FILE = "sample.ini"
CK_DEFAULT = "DEFAULT"
CK_SPA_ID = "SPA_ID"
CK_SPA_ADDR = "SPA_ADDR"
CK_SPA_NAME = "SPA_NAME"

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
    def spa_id(self) -> str | None:
        return self._config[CK_DEFAULT].get(CK_SPA_ID, None)

    def set_spa_id(self, spa_id) -> None:
        if spa_id is None:
            self._config.remove_option(CK_DEFAULT, CK_SPA_ID)
        else:
            self._config[CK_DEFAULT][CK_SPA_ID] = spa_id

    @property
    def spa_address(self) -> str | None:
        return self._config[CK_DEFAULT].get(CK_SPA_ADDR, None)

    def set_spa_address(self, spa_address) -> None:
        if spa_address is None:
            self._config.remove_option(CK_DEFAULT, CK_SPA_ADDR)
        else:
            self._config[CK_DEFAULT][CK_SPA_ADDR] = spa_address

    @property
    def spa_name(self) -> str | None:
        return self._config[CK_DEFAULT].get(CK_SPA_NAME, None)

    def set_spa_name(self, spa_name) -> None:
        if spa_name is None:
            self._config.remove_option(CK_DEFAULT, CK_SPA_NAME)
        else:
            self._config[CK_DEFAULT][CK_SPA_NAME] = spa_name
