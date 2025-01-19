"""Library to communicate with Gecko Alliance products via the in.touch2 module"""

import logging

from ._version import VERSION
from .async_locator import GeckoAsyncLocator
from .async_spa import GeckoAsyncSpa
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_spa_manager import GeckoAsyncSpaMan
from .async_tasks import AsyncTasks
from .automation import (
    GeckoAsyncFacade,
    GeckoAutomationBase,
    GeckoAutomationFacadeBase,
    GeckoBinarySensor,
    GeckoBlower,
    GeckoButton,
    GeckoErrorSensor,
    GeckoFacade,
    GeckoKeypad,
    GeckoLight,
    GeckoPump,
    GeckoReminders,
    GeckoSensor,
    GeckoSwitch,
    GeckoWaterCare,
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
    GeckoPartialStatusBlockProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoStatusBlockProtocolHandler,
    GeckoStructAccessor,
    GeckoStructure,
    GeckoUdpProtocolHandler,
    GeckoUdpSocket,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareProtocolHandler,
    GeckoWordStructAccessor,
    Observable,
)
from .locator import GeckoLocator
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
    "GeckoAutomationBase",
    "GeckoAutomationFacadeBase",
    "GeckoBinarySensor",
    "GeckoBlower",
    "GeckoBoolStructAccessor",
    "GeckoButton",
    "GeckoByteStructAccessor",
    "GeckoConfig",
    "GeckoConfigFileProtocolHandler",
    "GeckoConstants",
    "GeckoEnumStructAccessor",
    "GeckoErrorSensor",
    "GeckoFacade",
    "GeckoFacade",
    "GeckoGetChannelProtocolHandler",
    "GeckoHelloProtocolHandler",
    "GeckoKeypad",
    "GeckoLight",
    "GeckoLocator",
    "GeckoPackCommandProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPartialStatusBlockProtocolHandler",
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
    "GeckoStructure",
    "GeckoSwitch",
    "GeckoUdpProtocolHandler",
    "GeckoUdpSocket",
    "GeckoUpdateFirmwareProtocolHandler",
    "GeckoVersionProtocolHandler",
    "GeckoWaterCare",
    "GeckoWaterHeater",
    "GeckoWatercareProtocolHandler",
    "GeckoWordStructAccessor",
    "Observable",
]
