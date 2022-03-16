"""Connection events issued during spa discovery/connection"""
from __future__ import annotations

from enum import Enum
from typing import Callable, Any, Coroutine


class GeckoSpaEvent(Enum):
    """Events triggered during locating and connection status of spas"""

    # Spa manager -------------------------------------------------------
    SPA_MAN_ENTER = 1
    """Spa manager was initialized"""
    SPA_MAN_EXIT = 2
    """Spa manager was exited, exc_info= exception if present"""

    SPA_NOT_FOUND = 5
    """Specified spa was not found on the network, spa_address= and
    spa_identifier= have more information"""

    # Locating spas -----------------------------------------------------
    LOCATING_STARTED = 100
    """Locating spas on the network has started"""

    LOCATING_DISCOVERED_SPA = 150
    """A spa was located, spa_descriptor= contains the details """

    LOCATING_FINISHED = 199
    """Locating spas on the network has finished, spa_descriptors=
    contains a list (possibly empty) of the spas that were found"""

    # Connecting to spas ------------------------------------------------
    CONNECTION_STARTED = 200
    """Connecting to a spa on the network has started"""

    CONNECTION_GOT_FIRMWARE_VERSION = 201
    """Connection has in.touch2 firmware versions, **kwargs has details"""

    CONNECTION_GOT_CHANNEL = 202
    """Connection has channel and RF strength. **kwargs has details"""

    CONNECTION_GOT_CONFIG_FILES = 203
    """Connection has got config files and versions. **kwargs has details"""

    CONNECTION_INITIAL_DATA_BLOCK_REQUEST = 204
    """Connection has asked for initial data block"""

    CONNECTION_SPA_COMPLETE = 250
    """Connection has completed for this spa, the facade can be constructed"""

    CONNECTION_CANNOT_FIND_LOG_VERSION = 295
    """During connection, the log version of the spa pack count not be
    found. **kwargs has details"""

    CONNECTION_CANNOT_FIND_CONFIG_VERSION = 296
    """During connection, the config version of the spa pack count not be
    found. **kwargs has details"""

    CONNECTION_CANNOT_FIND_SPA_PACK = 297
    """During connection, the calculated spa pack could not be found.
    **kwargs has details"""

    CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED = 298
    """During connection, the retry count was exceeded for part of the
    protocol handshake"""

    CONNECTION_FINISHED = 299
    """Connecting to a spa on the network has finished, facade=
    has the connected facade or None if some error occurred"""

    # Running spa ------------------------------------------------------
    RUNNING_PING_RECEIVED = 300
    """Running spa received a ping response"""
    RUNNING_PING_MISSED = 301
    """Running spa missed a ping response"""
    RUNNING_PING_NO_RESPONSE = 302
    """Running spa not responding to pings """
    RUNNING_SPA_DISCONNECTED = 303
    """Running spa was disconnected"""
    RUNNING_SPA_WATER_CARE_ERROR = 304
    """A running spa will sometimes get an unprompted watercare error"""

    # Events targeted at clients, to determine when things can be shown
    # or hidden in the UI
    CLIENT_HAS_STATUS_SENSOR = 401
    """The spa manager has the status sensor"""
    CLIENT_HAS_RECONNECT_BUTTON = 402
    """The spa manager has the reconnect button"""
    CLIENT_HAS_PING_SENSOR = 403
    """The spa manager has the ping sensor"""

    CLIENT_FACADE_IS_READY = 420
    """The facade is ready for use."""
    CLIENT_FACADE_TEARDOWN = 421
    """Facade is being torn down."""

    # Error event that SpaMan can retry without ------------------------
    # intervention

    # Terminal states that require subclasses to ------------------------
    # let go of the facade and all automation objects and reconnect
    ERROR_TOO_MANY_RF_ERRORS = 500
    """The spa has had too many RF errors"""

    ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED = 501
    """Protocol retry count was exceeded during normal operations"""

    ERROR_RF_ERROR = 502
    """The in.touch EN module can't communicate with the CO module"""

    CallBack = Callable[..., Coroutine[Any, Any, None]]
    """Typedef for event callbacks, located here so we can be DRY"""
