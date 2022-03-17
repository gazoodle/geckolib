"""Configuration management for geckolib"""


class _GeckoConfigManager:
    """Configuration manangement class"""

    @property
    def DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS(self):
        """Mininum time in seconds to wait for initial spa discovery even
        if one spa has responded"""
        return 4

    @property
    def DISCOVERY_TIMEOUT_IN_SECONDS(self):
        """Maximum time in seconds to wait for full discovery if no spas
        have responded"""
        return 10

    @property
    def TASK_TIDY_FREQUENCY_IN_SECONDS(self):
        """Time in seconds between task tidyup checks"""
        return 5

    @property
    def PING_FREQUENCY_IN_SECONDS(self):
        """Frequency in seconds to ping the spa to ensure it is still available"""
        return 10

    @property
    def PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS(self):
        """Time after which a spa is deemed to be not responding to pings"""
        return 10

    @property
    def FACADE_UPDATE_FREQUENCY_IN_SECONDS(self):
        """Frequency in seconds to update facade data"""
        return 30

    @property
    def SPA_PACK_REFRESH_FREQUENCY_IN_SECONDS(self):
        """Frequency in seconds to request all LOG data from spa"""
        return 30


# Root config
GeckoConfig = _GeckoConfigManager()
