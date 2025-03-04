"""Gecko driver communication handlers."""

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
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoStatusBlockProtocolHandler,
)
from .unhandled import GeckoUnhandledProtocolHandler
from .version import GeckoVersionProtocolHandler
from .watercare import (
    GeckoGetWatercareModeProtocolHandler,
    GeckoGetWatercareScheduleListProtocolHandler,
    GeckoSetWatercareModeProtocolHandler,
    GeckoWatercareErrorHandler,
    GeckoWatercareScheduleManager,
)

__all__ = [
    "GeckoAsyncPartialStatusBlockProtocolHandler",
    "GeckoConfigFileProtocolHandler",
    "GeckoGetChannelProtocolHandler",
    "GeckoGetWatercareModeProtocolHandler",
    "GeckoGetWatercareModeProtocolHandler",
    "GeckoGetWatercareScheduleListProtocolHandler",
    "GeckoHelloProtocolHandler",
    "GeckoPackCommandProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPingProtocolHandler",
    "GeckoRFErrProtocolHandler",
    "GeckoReminderType",
    "GeckoRemindersProtocolHandler",
    "GeckoSetWatercareModeProtocolHandler",
    "GeckoStatusBlockProtocolHandler",
    "GeckoUnhandledProtocolHandler",
    "GeckoUpdateFirmwareProtocolHandler",
    "GeckoVersionProtocolHandler",
    "GeckoWatercareErrorHandler",
    "GeckoWatercareScheduleManager",
]
