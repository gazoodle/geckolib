"""GeckoAsyncSpa connection state"""
from __future__ import annotations

from enum import Enum


class GeckoSpaConnectionState(Enum):

    # Initialization phase
    INITIALIZATION = 1
    DISCONNECTED = 2
    PING_STARTED = 3
    GOT_FIRMWARE_VERSION = 4
    GOT_CHANNEL = 5
    GOT_CONFIG_FILES = 6
    INITIAL_DATA_REQUEST = 7

    # Normal running
    CONNECTED = 50

    # Error states that can be retried
    PROTOCOL_RETRY_EXCEEDED = 100

    # Error states that need a reconnection
    NO_PING_RESPONSE = 200
    PING_RESTORED = 201

    # Error states needing manual intervention
    CANNOT_FIND_SPA_PACK = 300
    CANNOT_FIND_CONFIG_VERSION = 301
    CANNOT_FIND_LOG_VERSION = 302
    TOO_MANY_RF_ERRORS = 303

    # Internal error that ought to have been handled
    CATASTROPHIC_CODE_FAILURE = 400

    def to_string(state: GeckoSpaConnectionState) -> str:
        """Convert these states to a human readable form"""
        if state == GeckoSpaConnectionState.INITIALIZATION:
            return "Initializing"
        elif state == GeckoSpaConnectionState.DISCONNECTED:
            return "Disconnected"
        elif state == GeckoSpaConnectionState.PING_STARTED:
            return "Ping started"
        elif state == GeckoSpaConnectionState.GOT_FIRMWARE_VERSION:
            return "Got in.touch2 firmware version"
        elif state == GeckoSpaConnectionState.GOT_CHANNEL:
            return "Got RF channel"
        elif state == GeckoSpaConnectionState.GOT_CONFIG_FILES:
            return "Got config files"
        elif state == GeckoSpaConnectionState.INITIAL_DATA_REQUEST:
            return "Requested initial data"

        elif state == GeckoSpaConnectionState.CONNECTED:
            return "Connected"

        elif state == GeckoSpaConnectionState.PROTOCOL_RETRY_EXCEEDED:
            return "Protocol retry failure"

        elif state == GeckoSpaConnectionState.NO_PING_RESPONSE:
            return "Spa not responding to pings"
        elif state == GeckoSpaConnectionState.PING_RESTORED:
            return "Spa responding to pings again"

        elif state == GeckoSpaConnectionState.CANNOT_FIND_SPA_PACK:
            return "Cannot find spa pack"
        elif state == GeckoSpaConnectionState.CANNOT_FIND_CONFIG_VERSION:
            return "Cannot find config version"
        elif state == GeckoSpaConnectionState.CANNOT_FIND_LOG_VERSION:
            return "Cannot find log version"
        elif state == GeckoSpaConnectionState.TOO_MANY_RF_ERRORS:
            return "Too many RF errors"

        elif state == GeckoSpaConnectionState.CATASTROPHIC_CODE_FAILURE:
            return "Code failure. Please report issue"

        else:
            return "Uknown spa connection state"
