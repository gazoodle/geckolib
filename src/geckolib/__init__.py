""" Library to communicate with Gecko Alliance products via the in.touch2 module """

import logging

from .const import GeckoConstants
from .automation import (
    GeckoAutomationBase,
    GeckoBlower,
    GeckoFacade,
    GeckoWaterHeater,
    GeckoKeypad,
    GeckoLight,
    GeckoPump,
    GeckoSensor,
    GeckoBinarySensor,
    GeckoSwitch,
    GeckoWaterCare,
)
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
    GeckoWatercareProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoPackCommandProtocolHandler,
    #
    GeckoSpaPack,
    GeckoStructure,
    GeckoStructAccessor,
    GeckoTemperatureDecorator,
    Observable,
)
from ._version import VERSION
from .utils import GeckoShell, GeckoSimulator, GeckoSnapshot

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = VERSION

__all__ = [
    # From automation
    "GeckoAutomationBase",
    "GeckoBlower",
    "GeckoFacade",
    "GeckoWaterHeater",
    "GeckoKeypad",
    "GeckoLight",
    "GeckoPump",
    "GeckoSensor",
    "GeckoBinarySensor",
    "GeckoSwitch",
    "GeckoWaterCare",
    # From constants
    "GeckoConstants",
    # From facade
    "GeckoFacade",
    # From locator
    "GeckoLocator",
    # From _version
    "VERSION",
    # From utils
    "GeckoShell",
    "GeckoSimulator",
    "GeckoSnapshot",
    # From driver
    "GeckoTemperatureDecorator",
    "Observable",
    "GeckoHelloProtocolHandler",
    "GeckoPacketProtocolHandler",
    "GeckoPingProtocolHandler",
    "GeckoVersionProtocolHandler",
    "GeckoGetChannelProtocolHandler",
    "GeckoConfigFileProtocolHandler",
    "GeckoStatusBlockProtocolHandler",
    "GeckoPartialStatusBlockProtocolHandler",
    "GeckoWatercareProtocolHandler",
    "GeckoUpdateFirmwareProtocolHandler",
    "GeckoRemindersProtocolHandler",
    "GeckoPackCommandProtocolHandler",
    #
    "GeckoSpaPack",
    "GeckoStructure",
    "GeckoStructAccessor",
    "GeckoUdpProtocolHandler",
    "GeckoUdpSocket",
]
