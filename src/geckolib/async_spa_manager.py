"""Class to manage the clienting of a Gecko in.touch2 enabled device """
from __future__ import annotations

from abc import ABC, abstractmethod

from .automation import GeckoAsyncFacade
from .async_locator import GeckoAsyncLocator
from .async_spa import GeckoAsyncSpa
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_tasks import AsyncTasks
from .const import GeckoConstants
from .spa_connection_events import GeckoSpaConnectionEvent

import logging
from typing import Optional, List

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncSpaMan(ABC, AsyncTasks):
    """GeckoAsyncSpaMan class manages the lifetime of an GeckoAsyncSpa and supporting
    classes

    This class is deliberately an abstract because you must provide your own
    implementation to manage the essential events that are required during operation

    The preferred pattern is to derive a class from SpaMan and then use it in
    an async with

        ```async with MySpaMan(client_uuid) as SpaMan:
            :
            :
        ```

    """

    def __init__(self, client_uuid: str) -> None:
        """Initialize a SpaMan class"""
        AsyncTasks.__init__(self)
        self._client_id = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        ).encode(GeckoConstants.MESSAGE_ENCODING)

        self._facade: Optional[GeckoAsyncFacade] = None
        self._spa: Optional[GeckoAsyncSpa] = None

    ########################################################################
    #
    #   Usage helpers
    #

    async def __aenter__(self) -> GeckoAsyncSpaMan:
        await AsyncTasks.__aenter__(self)
        return self

    async def __aexit__(self, *exc_info) -> None:
        await AsyncTasks.__aexit__(self, exc_info)

    ########################################################################
    #
    #   Public methods
    #

    async def async_locate_spas(
        self, spa_address=None
    ) -> Optional[List[GeckoAsyncSpaDescriptor]]:
        """Locate spas on this network

        This API will return a list of GeckoAsyncSpaDescriptor that were
        found on the network. If there are none found, then the return will be
        None. Events will be issued as the locating process proceeds


        """
        spa_descriptors: Optional[List[GeckoAsyncSpaDescriptor]] = None

        try:
            await self.handle_event(GeckoSpaConnectionEvent.LOCATING_STARTED)
            locator = GeckoAsyncLocator(
                self, self.handle_event, spa_address=spa_address
            )
            await locator.discover()
            spa_descriptors = locator.spas

        finally:
            await self.handle_event(
                GeckoSpaConnectionEvent.LOCATING_FINISHED,
                spa_descriptors=spa_descriptors,
            )

        return spa_descriptors

    async def connect_to_spa(self, spa_descriptor) -> Optional[GeckoAsyncFacade]:
        assert self._facade is None

        try:
            await self.handle_event(GeckoSpaConnectionEvent.CONNECTION_STARTED)
            self._spa = GeckoAsyncSpa(self._client_id, spa_descriptor, self)
            await self._spa.connect()
            self._facade = GeckoAsyncFacade(self._spa, self)

        finally:
            await self.handle_event(GeckoSpaConnectionEvent.CONNECTION_FINISHED)

        # return facade
        return self._facade

    @property
    def facade(self) -> Optional[GeckoAsyncFacade]:
        return self._facade

    ########################################################################
    #
    #   Abstract methods
    #
    @abstractmethod
    async def handle_event(self, event: GeckoSpaConnectionEvent, **kwargs) -> None:
        pass

    ########################################################################
    #
    #   Private methods
    #
