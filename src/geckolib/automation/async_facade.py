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
from ..async_tasks import AsyncTasks

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncFacade(Observable, AsyncTasks):
    """Async facade"""

    def __init__(self, client_uuid, **kwargs):
        """The Facade is an automation friendly class that manages the interaction between
        a client program and the low-level protocol of a Gecko Alliance spa equipped with
        an in.touch2 module. Ideally there should be no need to import anything other than
        this class, constructed in an appropriate fashion.

        First time:
            ```async with GeckoAsyncFacade(CLIENT_UUID) as facade:```

            ```facade.spas``` contains a list of spas found on the local network, or None

        Subnet usage:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_address="1.2.3.4") as facade:```

            ```facade.spas``` contains either one spa found at the above address pr None

        Connection to known spa:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_identifier="SPA01:02:03:04:05:06") as facade:```

            Will discover this spa on the network and then instigate connection to it,
            ```facade``` has various methods and properties suitable for automation,
            including status

        Connection to known spa at specific address:
            ```async with GeckoAsyncFacade(CLIENT_UUID, spa_identifier="SPA01:02:03:04:05:06", spa_address="1.2.3.4") as facade:```

            Will connect to this spa on the network at the specified addres.
            ```facade``` has various methods and properties suitable for automation,
            including status
        """
        Observable.__init__(self)
        AsyncTasks.__init__(self)
        self.client_id = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)

        self._spa_address = kwargs.get("spa_address", None)
        if self._spa_address == "":
            self._spa_address = None
        self._spa_identifier = kwargs.get("spa_identifier", None)
        if self._spa_identifier == "":
            self._spa_identifier = None

        self._sensors = []
        self._binary_sensors = []
        self._water_heater = None
        self._water_care = None
        self._pumps = None
        self._keypad = None
        self._ecomode = None
        self._facade_ready = False

        self._spa = None
        self._locator = None

    async def __aenter__(self):
        self.add_task(self._facade_pump(), "Facade pump")
        return self

    async def __aexit__(self, *exc_info):
        await AsyncTasks.__aexit__(self, exc_info)

    async def _facade_pump(self):
        _LOGGER.debug("Facade pump started %s", self)
        while True:
            # We need to run a discover whenever the spa identifier hasn't been supplied
            if self._spa_identifier is None and self._locator is None:
                self._locator = GeckoAsyncLocator(self, spa_address=self._spa_address)
                self._locator.watch(self._on_change)
                await self._locator.discover()

            # Keep everything running
            await asyncio.sleep(0)

    async def ready(self):
        while self._locator is None and self._spa is None:
            await asyncio.sleep(0)

        if self._locator is not None:
            while self._locator.is_running:
                await asyncio.sleep(0)

    @property
    def locator(self) -> GeckoAsyncLocator:
        return self._locator

    async def connect_to(self, spa_descriptor):
        """Connect to the specified spa on the network, using the
        descriptor provided"""
        self._spa = GeckoAsyncSpa(self.client_id, spa_descriptor)
        await self._spa.connect()
        self._water_heater = GeckoWaterHeater(self)

    # async def gather(self):
    #    if self._spa is not None:
    #        await self._spa.gather()

    def disconnect(self):
        _LOGGER.debug("Disconnect facade")
        if self._spa is not None:
            self._spa.disconnect()
            self._spa = None

    @property
    def water_heater(self):
        """Get the water heater handler"""
        return self._water_heater

    @property
    def pumps(self):
        """Get the pumps list"""
        return self._pumps

    @property
    def status_line(self) -> str:
        """Get a human readable status line showing the current state of the facade"""
        if self._spa is not None:
            return "Has spa object"
        if self._locator is not None:
            return self._locator.status_line
        return "Initializing"
