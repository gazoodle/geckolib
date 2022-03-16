"""Spa state"""
from __future__ import annotations

from enum import Enum


class GeckoSpaState(Enum):
    """Spa, locator or spa manager state"""

    IDLE = 1
    """Idle state is when the spa manager is first initialized"""

    LOCATING_SPAS = 2
    """State when the spa manager is locating spas on the network"""

    LOCATED_SPAS = 3
    """State when the spa manager has finished locating spas"""

    CONNECTING = 4
    """State when the spa is going through connection protocol"""

    SPA_READY = 5
    """State when the spa is ready to have a facade built"""

    CONNECTED = 10
    """State when the spa manager is connected to a spa successfully"""

    ERROR_SPA_NOT_FOUND = 50
    """State when the spa cannot be found on the the network"""
    ERROR_NEEDS_ATTENTION = 51
    """State when the user needs to attend"""
    ERROR_PING_MISSED = 52
    """State when a ping was missed, can auto-connect on restore"""
    ERROR_RF_FAULT = 53
    """State when the EN module reports it can't talk to the CO module"""

    @staticmethod
    def to_string(state: GeckoSpaState) -> str:
        if state == GeckoSpaState.CONNECTED:
            return "Connected"
        elif state == GeckoSpaState.CONNECTING:
            return "Connecting..."
        elif state == GeckoSpaState.ERROR_RF_FAULT:
            return "Lost contact with spa (RFERR)"
        elif state == GeckoSpaState.ERROR_PING_MISSED:
            return "Lost contact with in.touch2 module"
        elif state == GeckoSpaState.ERROR_NEEDS_ATTENTION:
            return "Needs attention, check logs"
        elif state == GeckoSpaState.LOCATING_SPAS:
            return "Searching for spas..."
        elif state == GeckoSpaState.LOCATED_SPAS:
            return "Choose spa"
        elif state == GeckoSpaState.ERROR_SPA_NOT_FOUND:
            return "Cannot find spa, check logs"
        else:
            return f"{state}"
