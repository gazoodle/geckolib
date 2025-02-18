"""GeckoLib automation interface."""

from .async_facade import GeckoAsyncFacade
from .base import GeckoAutomationBase, GeckoAutomationFacadeBase
from .blower import GeckoBlower
from .bubblegen import GeckoBubbleGenerator
from .button import GeckoButton
from .heater import GeckoWaterHeater
from .heatpump import GeckoHeatPump
from .ingrid import GeckoInGrid
from .inmix import GeckoInMix, GeckoInMixSynchro, GeckoInMixZone
from .keypad import GeckoKeypad
from .keypad_backlight import GeckoKeypadBacklight
from .light import GeckoLight
from .pump import GeckoPump
from .reminders import GeckoReminders
from .sensors import GeckoBinarySensor, GeckoErrorSensor, GeckoSensor
from .switch import GeckoSwitch
from .watercare import GeckoWaterCare
from .waterfall import GeckoWaterfall

__all__ = [
    "GeckoAsyncFacade",
    "GeckoAutomationBase",
    "GeckoAutomationFacadeBase",
    "GeckoBinarySensor",
    "GeckoBlower",
    "GeckoBubbleGenerator",
    "GeckoButton",
    "GeckoErrorSensor",
    "GeckoHeatPump",
    "GeckoInGrid",
    "GeckoInMix",
    "GeckoInMixSynchro",
    "GeckoInMixZone",
    "GeckoKeypad",
    "GeckoKeypadBacklight",
    "GeckoLight",
    "GeckoPump",
    "GeckoReminders",
    "GeckoSensor",
    "GeckoSwitch",
    "GeckoWaterCare",
    "GeckoWaterHeater",
    "GeckoWaterfall",
]
