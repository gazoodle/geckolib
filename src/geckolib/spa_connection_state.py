"""GeckoAsyncSpa connection state"""
from enum import Enum


class GeckoSpaConnectionState(Enum):
    DISCONNECTED = 1
    PING_STARTED = 2
    GOT_FIRMWARE_VERSION = 3
    GOT_CHANNEL = 4
    GOT_CONFIG_FILES = 5

    CONNECTED = 10

    # Error states
    CANNOT_FIND_SPA_PACK = 99
    CANNOT_FIND_CONFIG_VERSION = 98
    CANNOT_FIND_LOG_VERSION = 97
    NO_PING_RESPONSE = 96
    PROTOCOL_RETRY_EXCEEDED = 95
