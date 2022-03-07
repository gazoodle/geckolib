"""Class to manage the clienting of a Gecko in.touch2 enabled device """
from __future__ import annotations

from abc import ABC, abstractmethod
from .async_locator import GeckoAsyncLocator
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_tasks import AsyncTasks
from enum import Enum

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

        ```async with MySpaMan() as SpaMan:
            :
            :
        ```

    """

    class Event(Enum):
        """Event enumeration to let clients know what is going on"""

        # Locating spas
        LOCATING_STARTED = 100

        LOCATING_FINISHED = 110

        # Connecting to spas

        # Error states that SpaMan can retry without
        # intervention

        # Terminal states that require subclasses to
        # let go of the facade and all automation objects and reconnect

    def __init__(self) -> None:
        """Initialize a SpaMan class"""
        AsyncTasks.__init__(self)

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

    async def async_locate_spas(self) -> Optional[List[GeckoAsyncSpaDescriptor]]:
        """Locate spas on this network

        This API will return a list of GeckoAsyncSpaDescriptor that were
        found on the network. If there are none found, then the return will be
        None. Events will be issued as the locating process proceeds


        """
        spa_descriptors: Optional[List[GeckoAsyncSpaDescriptor]] = None

        try:
            await self.handle_event(GeckoAsyncSpaMan.Event.LOCATING_STARTED)
            locator = GeckoAsyncLocator(self)
            await locator.discover()
            spa_descriptors = locator.spas

        finally:
            await self.handle_event(
                GeckoAsyncSpaMan.Event.LOCATING_FINISHED,
                spa_descriptors=spa_descriptors,
            )

        return spa_descriptors

    def normal(self) -> None:
        pass

    ########################################################################
    #
    #   Abstract methods
    #
    @abstractmethod
    async def handle_event(self, event: Event, **kwargs) -> None:
        pass

    ########################################################################
    #
    #   Private methods
    #
