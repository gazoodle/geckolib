"""Gecko driver communication handlers."""

from .configfile import GeckoConfigFileProtocolHandler
from .firmware import GeckoUpdateFirmwareProtocolHandler
from .getchannel import (
    GeckoChangeChannelProtocolHandler,
    GeckoGetChannelProtocolHandler,
)
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
    GeckoAddWatercareScheduleProtocolHandler,
    GeckoDeleteWatercareScheduleProtocolHandler,
    GeckoGetWatercareModeProtocolHandler,
    GeckoGetWatercareScheduleListProtocolHandler,
    GeckoModifyWatercareScheduleProtocolHandler,
    GeckoScheduleDay,
    GeckoSetWatercareModeProtocolHandler,
    GeckoWatercareErrorHandler,
    GeckoWatercareSchedule,
    GeckoWatercareScheduleManager,
    GeckoWatercareScheduleType,
)

__all__ = [
    "GeckoAddWatercareScheduleProtocolHandler",
    "GeckoAsyncPartialStatusBlockProtocolHandler",
    "GeckoChangeChannelProtocolHandler",
    "GeckoConfigFileProtocolHandler",
    "GeckoDeleteWatercareScheduleProtocolHandler",
    "GeckoGetChannelProtocolHandler",
    "GeckoGetWatercareModeProtocolHandler",
    "GeckoGetWatercareModeProtocolHandler",
    "GeckoGetWatercareScheduleListProtocolHandler",
    "GeckoHelloProtocolHandler",
    "GeckoModifyWatercareScheduleProtocolHandler",
    "GeckoPackCommandProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPingProtocolHandler",
    "GeckoRFErrProtocolHandler",
    "GeckoReminderType",
    "GeckoRemindersProtocolHandler",
    "GeckoScheduleDay",
    "GeckoSetWatercareModeProtocolHandler",
    "GeckoStatusBlockProtocolHandler",
    "GeckoUnhandledProtocolHandler",
    "GeckoUpdateFirmwareProtocolHandler",
    "GeckoVersionProtocolHandler",
    "GeckoWatercareErrorHandler",
    "GeckoWatercareSchedule",
    "GeckoWatercareScheduleManager",
    "GeckoWatercareScheduleType",
]
