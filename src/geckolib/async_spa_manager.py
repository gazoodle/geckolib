"""Class to manage the clienting of a Gecko in.touch2 enabled device """
from __future__ import annotations

from abc import ABC, abstractmethod

from .automation import GeckoAsyncFacade
from .async_locator import GeckoAsyncLocator
from .async_spa import GeckoAsyncSpa
from .async_spa_descriptor import GeckoAsyncSpaDescriptor
from .async_tasks import AsyncTasks
from .const import GeckoConstants
from .spa_events import GeckoSpaEvent
from .spa_state import GeckoSpaState

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
        self._spa_state = GeckoSpaState.IDLE

    ########################################################################
    #
    #   Usage helpers
    #

    async def __aenter__(self) -> GeckoAsyncSpaMan:
        await AsyncTasks.__aenter__(self)
        await self._handle_event(GeckoSpaEvent.SPA_MAN_ENTER)
        return self

    async def __aexit__(self, *exc_info) -> None:
        await self._handle_event(GeckoSpaEvent.SPA_MAN_EXIT, exc_info=exc_info)
        await AsyncTasks.__aexit__(self, exc_info)

    ########################################################################
    #
    #   Public methods
    #

    async def async_locate_spas(
        self, spa_address: Optional[str] = None, spa_identifier: Optional[str] = None
    ) -> Optional[List[GeckoAsyncSpaDescriptor]]:
        """Locate spas on this network

        This API will return a list of GeckoAsyncSpaDescriptor that were
        found on the network. If there are none found, then the return will be
        None. Events will be issued as the locating process proceeds


        """
        spa_descriptors: Optional[List[GeckoAsyncSpaDescriptor]] = None

        try:
            await self._handle_event(GeckoSpaEvent.LOCATING_STARTED)
            locator = GeckoAsyncLocator(
                self, self._handle_event, spa_address=spa_address
            )
            await locator.discover()
            spa_descriptors = locator.spas
            del locator

        finally:
            await self._handle_event(
                GeckoSpaEvent.LOCATING_FINISHED,
                spa_descriptors=spa_descriptors,
            )

        return spa_descriptors

    async def async_connect_to_spa(self, spa_descriptor) -> Optional[GeckoAsyncFacade]:
        """Connect to spa.

        This API will connect to the specified spa using the supplied descriptor"""
        assert self._facade is None

        try:
            await self._handle_event(GeckoSpaEvent.CONNECTION_STARTED)
            self._spa = GeckoAsyncSpa(
                self._client_id, spa_descriptor, self, self._handle_event
            )
            await self._spa.connect()
            # Check state now
            if self._spa_state == GeckoSpaState.SPA_READY:
                self._facade = GeckoAsyncFacade(self._spa, self)

        finally:
            await self._handle_event(
                GeckoSpaEvent.CONNECTION_FINISHED, facade=self._facade
            )

        # return facade
        return self._facade

    async def async_connect(
        self, spa_identifier: str, spa_address: Optional[str] = None
    ) -> Optional[GeckoAsyncFacade]:
        """Connect to spa.

        This API will connect to the specified spa by doing a search with the
        supplied information. This is probably the API most commonly used by
        automation systems to avoid storing too much information in configuration"""

        spa_descriptors = await self.async_locate_spas(
            spa_address=spa_address, spa_identifier=spa_identifier
        )

        if spa_descriptors is None:
            await self._handle_event(
                GeckoSpaEvent.SPA_NOT_FOUND,
                spa_address=spa_address,
                spa_identifier=spa_identifier,
            )
            return None

        return await self.async_connect_to_spa(spa_descriptors[0])

    ########################################################################
    #
    #   Properties
    #

    @property
    def facade(self) -> Optional[GeckoAsyncFacade]:
        return self._facade

    @property
    def spa_state(self) -> GeckoSpaState:
        return self._spa_state

    @property
    def status_line(self) -> str:
        return self._status_line

    def __str__(self) -> str:
        return f"{self.status_line}"

    ########################################################################
    #
    #   Abstract methods
    #
    @abstractmethod
    async def handle_event(self, event: GeckoSpaEvent, **kwargs) -> None:
        pass

    ########################################################################
    #
    #   Private methods
    #

    async def _handle_event(self, event: GeckoSpaEvent, **kwargs) -> None:
        # Do any pre-processing of the event, such as setting the state or
        # updating the status line
        if event == GeckoSpaEvent.LOCATING_STARTED:
            self._spa_state = GeckoSpaState.LOCATING_SPAS

        elif event == GeckoSpaEvent.LOCATING_FINISHED:
            self._spa_state = GeckoSpaState.IDLE

        elif event == GeckoSpaEvent.SPA_NOT_FOUND:
            self._spa_state = GeckoSpaState.ERROR_SPA_NOT_FOUND

        elif event == GeckoSpaEvent.CONNECTION_STARTED:
            self._spa_state = GeckoSpaState.CONNECTING

        elif event == GeckoSpaEvent.CONNECTION_SPA_COMPLETE:
            self._spa_state = GeckoSpaState.SPA_READY

        elif event == GeckoSpaEvent.CONNECTION_FINISHED:
            if self._facade is not None:
                self._spa_state = GeckoSpaState.CONNECTED

        elif event in (
            GeckoSpaEvent.CONNECTION_PROTOCOL_RETRY_COUNT_EXCEEDED,
            GeckoSpaEvent.ERROR_PROTOCOL_RETRY_COUNT_EXCEEDED,
            GeckoSpaEvent.ERROR_TOO_MANY_RF_ERRORS,
        ):
            self._spa_state = GeckoSpaState.ERROR_NEEDS_ATTENTION

        # TODO: Better please
        self._status_line = f"State: {self._spa_state}, last event {event}"

        # Call the abstract method to allow derived classes to do useful work
        # such as disconnecting handlers when the spa needs to reconnect
        # after protocol failure
        await self.handle_event(event, **kwargs)

        # Any post-processing goes here
