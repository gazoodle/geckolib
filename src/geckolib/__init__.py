"""Library to communicate with Gecko Alliance products via the in.touch2 module."""

import logging

from ._version import VERSION
from .async_locator import GeckoAsyncLocator
from .async_spa import GeckoAsyncSpa
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_spa_manager import GeckoAsyncSpaMan
from .async_taskman import GeckoAsyncTaskMan
from .async_tasks import AsyncTasks
from .automation import (
    GeckoAsyncFacade,
    GeckoAutomationBase,
    GeckoAutomationFacadeBase,
    GeckoBinarySensor,
    GeckoBlower,
    GeckoBubbleGenerator,
    GeckoButton,
    GeckoErrorSensor,
    GeckoHeatPump,
    GeckoInGrid,
    GeckoInMix,
    GeckoInMixSynchro,
    GeckoInMixZone,
    GeckoKeypad,
    GeckoLight,
    GeckoNumber,
    GeckoPump,
    GeckoReminders,
    GeckoSensor,
    GeckoSwitch,
    GeckoWaterCare,
    GeckoWaterfall,
    GeckoWaterHeater,
    GeckoWaterHeaterAbstract,
    MrSteam,
)
from .config import GeckoConfig
from .const import GeckoConstants
from .driver import (
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoConfigFileProtocolHandler,
    GeckoEnumStructAccessor,
    GeckoGetChannelProtocolHandler,
    GeckoGetWatercareModeProtocolHandler,
    GeckoGetWatercareScheduleListProtocolHandler,
    GeckoHelloProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoSetWatercareModeProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoStructAccessor,
    GeckoUdpProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareScheduleManager,
    GeckoWordStructAccessor,
    Observable,
)
from .spa_events import GeckoSpaEvent
from .spa_state import GeckoSpaState
from .utils import CUI, GeckoShell, GeckoSimulator, GeckoSnapshot

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = VERSION

__all__ = [
    "CUI",
    "VERSION",
    "AsyncTasks",
    "GeckoAsyncFacade",
    "GeckoAsyncLocator",
    "GeckoAsyncPartialStatusBlockProtocolHandler",
    "GeckoAsyncSpa",
    "GeckoAsyncSpaDescriptor",
    "GeckoAsyncSpaMan",
    "GeckoAsyncStructure",
    "GeckoAsyncTaskMan",
    "GeckoAutomationBase",
    "GeckoAutomationFacadeBase",
    "GeckoBinarySensor",
    "GeckoBlower",
    "GeckoBoolStructAccessor",
    "GeckoBubbleGenerator",
    "GeckoButton",
    "GeckoByteStructAccessor",
    "GeckoConfig",
    "GeckoConfigFileProtocolHandler",
    "GeckoConstants",
    "GeckoEnumStructAccessor",
    "GeckoErrorSensor",
    "GeckoGetChannelProtocolHandler",
    "GeckoGetWatercareModeProtocolHandler",
    "GeckoGetWatercareScheduleListProtocolHandler",
    "GeckoHeatPump",
    "GeckoHelloProtocolHandler",
    "GeckoInGrid",
    "GeckoInMix",
    "GeckoInMixSynchro",
    "GeckoInMixZone",
    "GeckoKeypad",
    "GeckoLight",
    "GeckoNumber",
    "GeckoPackCommandProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPingProtocolHandler",
    "GeckoPump",
    "GeckoReminderType",
    "GeckoReminders",
    "GeckoRemindersProtocolHandler",
    "GeckoSensor",
    "GeckoSetWatercareModeProtocolHandler",
    "GeckoShell",
    "GeckoSimulator",
    "GeckoSnapshot",
    "GeckoSpaEvent",
    "GeckoSpaState",
    "GeckoStatusBlockProtocolHandler",
    "GeckoStructAccessor",
    "GeckoSwitch",
    "GeckoUdpProtocolHandler",
    "GeckoUpdateFirmwareProtocolHandler",
    "GeckoVersionProtocolHandler",
    "GeckoWaterCare",
    "GeckoWaterHeater",
    "GeckoWaterHeaterAbstract",
    "GeckoWatercareScheduleManager",
    "GeckoWaterfall",
    "GeckoWordStructAccessor",
    "MrSteam",
    "Observable",
]
