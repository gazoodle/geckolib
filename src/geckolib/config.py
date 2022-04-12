"""Configuration management for geckolib"""

import asyncio
from dataclasses import dataclass
import logging
from typing import Optional

_LOGGER = logging.getLogger(__name__)


@dataclass
class _GeckoConfig:
    DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS = 1
    """Mininum time in seconds to wait for initial spa discovery even
    if one spa has responded"""

    DISCOVERY_TIMEOUT_IN_SECONDS = 1
    """Maximum time in seconds to wait for full discovery if no spas
    have responded"""

    TASK_TIDY_FREQUENCY_IN_SECONDS = 1
    """Time in seconds between task tidyup checks"""

    PING_FREQUENCY_IN_SECONDS = 1
    """Frequency in seconds to ping the spa to ensure it is still available"""

    PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS = 1
    """Time after which a spa is deemed to be not responding to pings"""

    FACADE_UPDATE_FREQUENCY_IN_SECONDS = 1
    """Frequency in seconds to update facade data"""

    SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS = 1
    """Frequency in seconds to request all LOG data from spa"""

    PROTOCOL_TIMEOUT_IN_SECONDS = 1
    """Default timeout for most protocol commands"""

    PROTOCOL_RETRY_COUNT = 1
    """Default retry count for protocol commands"""

    PAUSE_BETWEEN_RETRIES_IN_SECONDS = 1
    """Default pause between retry operations"""


CONFIG_MEMBERS = [
    attr
    for attr in dir(_GeckoConfig)
    if not callable(getattr(_GeckoConfig, attr)) and not attr.startswith("__")
]


@dataclass
class _GeckoActiveConfig(_GeckoConfig):
    """Gecko active configuration"""

    DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS = 4
    DISCOVERY_TIMEOUT_IN_SECONDS = 10
    TASK_TIDY_FREQUENCY_IN_SECONDS = 5
    PING_FREQUENCY_IN_SECONDS = 2
    PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS = 10
    FACADE_UPDATE_FREQUENCY_IN_SECONDS = 30
    SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS = 30
    PROTOCOL_TIMEOUT_IN_SECONDS = 4
    PROTOCOL_RETRY_COUNT = 10
    PAUSE_BETWEEN_RETRIES_IN_SECONDS = 2


@dataclass
class _GeckoIdleConfig(_GeckoConfig):
    """Gecko idle configuration"""

    DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS = 4
    DISCOVERY_TIMEOUT_IN_SECONDS = 10
    TASK_TIDY_FREQUENCY_IN_SECONDS = 60
    PING_FREQUENCY_IN_SECONDS = 60
    PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS = 120
    FACADE_UPDATE_FREQUENCY_IN_SECONDS = 120
    SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS = 120
    PROTOCOL_TIMEOUT_IN_SECONDS = 4
    PROTOCOL_RETRY_COUNT = 10
    PAUSE_BETWEEN_RETRIES_IN_SECONDS = 2


# Root config
GeckoConfig: _GeckoConfig = _GeckoIdleConfig()
ConfigChange: Optional[asyncio.Future] = None


def set_config_mode(active: bool) -> None:
    """Set config mode to active (true) or idle (false)."""
    _LOGGER.debug("set_config_mode: %s", active)
    new_config = _GeckoActiveConfig() if active else _GeckoIdleConfig()
    for member in CONFIG_MEMBERS:
        setattr(GeckoConfig, member, getattr(new_config, member))
    assert ConfigChange is not None
    if not ConfigChange.done():
        ConfigChange.set_result(True)


async def config_sleep(delay: float) -> None:
    global ConfigChange
    if ConfigChange is None or ConfigChange.done():
        ConfigChange = asyncio.get_running_loop().create_future()
    await asyncio.wait([ConfigChange], timeout=delay)
