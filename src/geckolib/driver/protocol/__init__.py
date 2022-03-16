""" Gecko driver communication handlers """

from .configfile import GeckoConfigFileProtocolHandler
from .firmware import GeckoUpdateFirmwareProtocolHandler
from .getchannel import GeckoGetChannelProtocolHandler
from .hello import GeckoHelloProtocolHandler
from .packcommand import GeckoPackCommandProtocolHandler
from .packet import GeckoPacketProtocolHandler
from .ping import GeckoPingProtocolHandler
from .reminders import GeckoRemindersProtocolHandler, GeckoReminderType
from .rferr import GeckoRFErrProtocolHandler
from .statusblock import (
    GeckoStatusBlockProtocolHandler,
    GeckoPartialStatusBlockProtocolHandler,
    GeckoAsyncPartialStatusBlockProtocolHandler,
)
from .unhandled import GeckoUnhandledProtocolHandler
from .version import GeckoVersionProtocolHandler
from .watercare import GeckoWatercareProtocolHandler, GeckoWatercareErrorHandler

__all__ = [
    # From hello
    "GeckoHelloProtocolHandler",
    # From packet
    "GeckoPacketProtocolHandler",
    # From ping
    "GeckoPingProtocolHandler",
    # From version
    "GeckoVersionProtocolHandler",
    # From getchannel
    "GeckoGetChannelProtocolHandler",
    # From configfile
    "GeckoConfigFileProtocolHandler",
    # From statusblock
    "GeckoStatusBlockProtocolHandler",
    "GeckoPartialStatusBlockProtocolHandler",
    "GeckoAsyncPartialStatusBlockProtocolHandler",
    # From watercare
    "GeckoWatercareProtocolHandler",
    "GeckoWatercareErrorHandler",
    # From firmware
    "GeckoUpdateFirmwareProtocolHandler",
    # From reminders
    "GeckoReminderType",
    "GeckoRemindersProtocolHandler",
    # From rferr
    "GeckoRFErrProtocolHandler",
    # From packcommand
    "GeckoPackCommandProtocolHandler",
    # From unhandled
    "GeckoUnhandledProtocolHandler",
]
