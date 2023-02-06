""" Library to communicate with Gecko Alliance products via the in.touch2 module """

import logging

from .async_tasks import AsyncTasks
from .const import GeckoConstants
from .config import GeckoConfig
from .automation import (
    GeckoAutomationBase,
    GeckoAutomationFacadeBase,
    GeckoBlower,
    GeckoButton,
    GeckoFacade,
    GeckoAsyncFacade,
    GeckoWaterHeater,
    GeckoKeypad,
    GeckoLight,
    GeckoPump,
    GeckoSensor,
    GeckoBinarySensor,
    GeckoErrorSensor,
    GeckoSwitch,
    GeckoWaterCare,
    GeckoReminders,
)
from .async_locator import GeckoAsyncLocator
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_spa_manager import GeckoAsyncSpaMan
from .async_spa import GeckoAsyncSpa
from .spa_events import GeckoSpaEvent
from .spa_state import GeckoSpaState
from .locator import GeckoLocator
from .driver import (
    GeckoUdpProtocolHandler,
    GeckoUdpSocket,
    GeckoHelloProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoPartialStatusBlockProtocolHandler,
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoWatercareProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoPackCommandProtocolHandler,
    #
    GeckoStructure,
    GeckoAsyncStructure,
    GeckoStructAccessor,
    GeckoByteStructAccessor,
    GeckoWordStructAccessor,
    GeckoBoolStructAccessor,
    GeckoEnumStructAccessor,
    Observable,
)
from ._version import VERSION
from .utils import GeckoShell, GeckoSimulator, GeckoSnapshot

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = VERSION

__all__ = [
    "AsyncTasks",
    # From automation
    "GeckoAutomationBase",
    "GeckoAutomationFacadeBase",
    "GeckoBlower",
    "GeckoButton",
    "GeckoFacade",
    "GeckoAsyncFacade",
    "GeckoWaterHeater",
    "GeckoKeypad",
    "GeckoLight",
    "GeckoPump",
    "GeckoSensor",
    "GeckoBinarySensor",
    "GeckoErrorSensor",
    "GeckoSwitch",
    "GeckoWaterCare",
    "GeckoReminders",
    # From constants
    "GeckoConstants",
    # From config
    "GeckoConfig",
    # From facade
    "GeckoFacade",
    # From locator
    "GeckoLocator",
    "GeckoAsyncLocator",
    "GeckoAsyncSpaDescriptor",
    # From _version
    "VERSION",
    # From utils
    "GeckoShell",
    "GeckoSimulator",
    "GeckoSnapshot",
    # From driver
    "Observable",
    "GeckoHelloProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPingProtocolHandler",
    "GeckoVersionProtocolHandler",
    "GeckoGetChannelProtocolHandler",
    "GeckoConfigFileProtocolHandler",
    "GeckoStatusBlockProtocolHandler",
    "GeckoPartialStatusBlockProtocolHandler",
    "GeckoAsyncPartialStatusBlockProtocolHandler",
    "GeckoWatercareProtocolHandler",
    "GeckoUpdateFirmwareProtocolHandler",
    "GeckoRemindersProtocolHandler",
    "GeckoReminderType",
    "GeckoPackCommandProtocolHandler",
    #
    "GeckoStructure",
    "GeckoAsyncStructure",
    "GeckoStructAccessor",
    "GeckoByteStructAccessor",
    "GeckoWordStructAccessor",
    "GeckoBoolStructAccessor",
    "GeckoEnumStructAccessor",
    "GeckoUdpProtocolHandler",
    "GeckoUdpSocket",
    #
    "GeckoAsyncSpaMan",
    "GeckoSpaEvent",
    "GeckoSpaState",
    "GeckoAsyncSpa",
]
