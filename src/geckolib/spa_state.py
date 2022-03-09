"""Spa state"""
from __future__ import annotations

from enum import Enum


class GeckoSpaState(Enum):
    """Spa, locator or spa manager state"""

    IDLE = 1
    """Idle state is when the spa manager is first initialized"""

    LOCATING_SPAS = 2
    """State when the spa manager is locating spas on the network"""

    CONNECTING = 3
    """State when the spa is going through connection protocol"""

    SPA_READY = 4
    """State when the spa is ready to have a facade built"""

    CONNECTED = 10
    """State when the spa manager is connected to a spa successfully"""

    ERROR_SPA_NOT_FOUND = 50
    """State when the spa cannot be found on the the network"""
    ERROR_NEEDS_ATTENTION = 51
    """State when the user needs to attend"""
