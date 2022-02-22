""" Async Facade to hide implementation details """

import logging
import asyncio

from .blower import GeckoBlower
from ..const import GeckoConstants
from .heater import GeckoWaterHeater
from .keypad import GeckoKeypad
from .light import GeckoLight
from .pump import GeckoPump
from .switches import GeckoSwitch
from .sensors import GeckoSensor, GeckoBinarySensor
from .watercare import GeckoWaterCare
from ..driver import Observable
from ..async_locator import GeckoAsyncLocator
from ..async_spa import GeckoAsyncSpa

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncFacade(Observable):
    def __init__(self, client_uuid):
        super().__init__()
        self.client_id = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)
        self._sensors = []
        self._binary_sensors = []
        self._water_heater = None
        self._water_care = None
        self._pumps = None
        self._keypad = None
        self._ecomode = None
        self._facade_ready = False

        self._spa = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc_info):
        await self.gather()

    async def connect_to(self, spa_descriptor):
        """Connect to the specified spa on the network, using the
        descriptor provided"""
        self._spa = GeckoAsyncSpa(self.client_id, spa_descriptor)
        await self._spa.connect()
        self._water_heater = GeckoWaterHeater(self)

    async def gather(self):
        if self._spa is not None:
            await self._spa.gather()

    def disconnect(self):
        _LOGGER.debug("Disconnect facade")
        self._spa.disconnect()
        self._spa = None

    @property
    def water_heater(self):
        """ Get the water heater handler """
        return self._water_heater

    @property
    def pumps(self):
        """ Get the pumps list """
        return self._pumps

 