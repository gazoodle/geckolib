"""Configuration class for complete async example."""

import configparser
import logging
from pathlib import Path

# Configuration file constants
CONFIG_FILE = "cui.ini"
CK_DEFAULT = "DEFAULT"
CK_SPA_ID = "SPA_ID"
CK_SPA_ADDR = "SPA_ADDR"
CK_SPA_NAME = "SPA_NAME"

_LOGGER = logging.getLogger(__name__)


class Config:
    """Hold the configuration for the complete async example app."""

    def __init__(self) -> None:
        """Initialize the config class."""
        _LOGGER.debug("Read config from %s", CONFIG_FILE)
        self._config = configparser.ConfigParser()
        self._config.read(CONFIG_FILE)

    def save(self) -> None:
        """Save the config file."""
        with Path(CONFIG_FILE).open("w") as configfile:
            self._config.write(configfile)

    @property
    def spa_id(self) -> str | None:
        """Get the spa id."""
        return self._config[CK_DEFAULT].get(CK_SPA_ID, None)

    def set_spa_id(self, spa_id: str | None) -> None:
        """Set the spa id."""
        if spa_id is None:
            self._config.remove_option(CK_DEFAULT, CK_SPA_ID)
        else:
            self._config[CK_DEFAULT][CK_SPA_ID] = spa_id

    @property
    def spa_address(self) -> str | None:
        """Get the spa address."""
        return self._config[CK_DEFAULT].get(CK_SPA_ADDR, None)

    def set_spa_address(self, spa_address: str | None) -> None:
        """Set the spa address."""
        if spa_address is None:
            self._config.remove_option(CK_DEFAULT, CK_SPA_ADDR)
        else:
            self._config[CK_DEFAULT][CK_SPA_ADDR] = spa_address

    @property
    def spa_name(self) -> str | None:
        """Get the spa name."""
        return self._config[CK_DEFAULT].get(CK_SPA_NAME, None)

    def set_spa_name(self, spa_name: str | None) -> None:
        """Set the spa name."""
        if spa_name is None:
            self._config.remove_option(CK_DEFAULT, CK_SPA_NAME)
        else:
            self._config[CK_DEFAULT][CK_SPA_NAME] = spa_name
