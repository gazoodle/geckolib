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
    GeckoPump,
    GeckoReminders,
    GeckoSensor,
    GeckoSwitch,
    GeckoWaterCare,
    GeckoWaterfall,
    GeckoWaterHeater,
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
    GeckoHelloProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoStatusBlockProtocolHandler,
    GeckoStructAccessor,
    GeckoUdpProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareProtocolHandler,
    GeckoWordStructAccessor,
    Observable,
)
from .spa_events import GeckoSpaEvent
from .spa_state import GeckoSpaState
from .utils import GeckoShell, GeckoSimulator, GeckoSnapshot

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = VERSION

__all__ = [
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
    "GeckoHeatPump",
    "GeckoHelloProtocolHandler",
    "GeckoInGrid",
    "GeckoInMix",
    "GeckoInMixSynchro",
    "GeckoInMixZone",
    "GeckoKeypad",
    "GeckoLight",
    "GeckoPackCommandProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPingProtocolHandler",
    "GeckoPump",
    "GeckoReminderType",
    "GeckoReminders",
    "GeckoRemindersProtocolHandler",
    "GeckoSensor",
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
    "GeckoWatercareProtocolHandler",
    "GeckoWaterfall",
    "GeckoWordStructAccessor",
    "Observable",
]
