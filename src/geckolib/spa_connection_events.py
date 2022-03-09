"""Connection events issued during spa discovery/connection"""
from __future__ import annotations

from enum import Enum
from typing import Callable, Any, Coroutine


class GeckoSpaConnectionEvent(Enum):
    """Events triggered during locating and connection status of spas"""

    # Locating spas -----------------------------------------------------
    LOCATING_STARTED = 100
    """Locating spas on the network has started"""

    LOCATING_DISCOVERED_SPA = 150
    """A spa was located, spa_descriptor= contains the details """

    LOCATING_FINISHED = 199
    """Locating spas on the network has finished"""

    # Connecting to spas ------------------------------------------------
    CONNECTION_STARTED = 200
    """Connecting to a spa on the network has started"""

    CONNECTION_FINISHED = 299
    """Connecting to a spa on the network has finished"""

    # Error states that SpaMan can retry without ------------------------
    # intervention

    # Terminal states that require subclasses to ------------------------
    # let go of the facade and all automation objects and reconnect

    CallBack = Callable[..., Coroutine[Any, Any, None]]
    """Typedef for event callbacks, located here so we can be DRY"""
