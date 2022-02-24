""" GeckoAsyncSpa class """

import logging
import asyncio
import importlib
import socket
import time
from enum import Enum


from .const import GeckoConstants
from .driver import (
    GeckoUdpSocket,
    GeckoAsyncUdpProtocol,
    GeckoHelloProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoPartialStatusBlockProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoRFErrProtocolHandler,
    GeckoUnhandledProtocolHandler,
    # Rest
    GeckoAsyncStructure,
    Observable,
)

_LOGGER = logging.getLogger(__name__)


class GeckoSpaConnectionState(Enum):
    DISCONNECTED = (1,)

    CONNECTED = 10


class GeckoAsyncSpa(Observable):
    """GeckoAsyncSpa class manages an instance of a spa, and is the main point of contact for
    control and monitoring. Uses the declarations found in pack/* to build
    an object that exposes the properties and capabilities of your spa. This class
    should only be used via a Facade which hides the implementation details"""

    def __init__(self, client_id, spa_descriptor, taskman):
        super().__init__()

        self.client_id = client_id
        self.descriptor = spa_descriptor
        self._taskman = taskman

        self._con_lost = None
        self._transport = None
        self._protocol = None
        self._connection_state = GeckoSpaConnectionState.DISCONNECTED

        self.struct = GeckoAsyncStructure(self._on_set_value)

    @property
    def sendparms(self):
        return (
            self.descriptor.destination[0],
            self.descriptor.destination[1],
            self.descriptor.identifier,
            self.client_id,
        )

    @property
    def connection_state(self):
        return self._connection_state

    async def connect(self):

        loop = asyncio.get_running_loop()
        self._con_lost = loop.create_future()

        self._transport, self._protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(self._con_lost), family=socket.AF_INET
        )

        self._taskman.add_task(
            GeckoUnhandledProtocolHandler().consume(None, self._protocol.queue),
            "Unhandled packet",
        )
        self._taskman.add_task(
            GeckoPacketProtocolHandler().consume(self._protocol, self._protocol.queue),
            "Packet handler",
        )

        # packet_task = asyncio.create_task(self._protocol.add_receive_handler(GeckoPacketProtocolHandler()))
        # partial_status_task = asyncio.create_task(self._protocol.add_receive_handler(
        #    GeckoPartialStatusBlockProtocolHandler(
        #      on_handled=self._on_partial_status_update
        #   )
        # ))

        # ping_task = asyncio.create_task(self.ping_loop())
        self._taskman.add_task(self.ping_loop(), "Ping loop")

        await asyncio.sleep(3)
        _LOGGER.debug("Connected!")

        # while self.connection_state != GeckoSpaConnectionState.CONNECTED:
        #    await asyncio.sleep(0)

        # return [packet_task, ping_task]

    def disconnect(self):
        self._protocol.disconnect()
        self._protocol = None
        self._transport = None

    @property
    def isopen(self):
        if self._protocol is None:
            return False
        return self._protocol.isopen

    def _on_ping_response(self, _handler, _socket, _sender):
        self._last_ping = time.monotonic()

    async def ping_loop(self):
        _LOGGER.info("Ping loop started")

        self._last_ping = time.monotonic()
        ping_handler = GeckoPingProtocolHandler.request(
            parms=self.sendparms, on_handled=self._on_ping_response
        )

        self._taskman.add_task(
            ping_handler.consume(None, self._protocol.queue), "Ping handler"
        )

        while self.isopen:
            self._protocol.queue_send(ping_handler, self.sendparms)
            await asyncio.wait(
                [self._con_lost], timeout=GeckoConstants.PING_FREQUENCY_IN_SECONDS
            )

            if (
                time.monotonic() - self._last_ping
                > GeckoConstants.PING_DEVICE_NOT_RESPONDING_TIMEOUT
            ):
                _LOGGER.warning(
                    # TODO
                    "TODO: Spa is not responding to pings, need to reconnect..."
                )

        _LOGGER.info("Ping loop finished")

    def _on_partial_status_update(self, handler, socket, sender):
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])
        else:
            handler.changes.clear()

    async def _on_set_value(self, pos, length, newvalue):
        # We issue a pack command to acheive this ...
        pack_command_task = asyncio.asyncio.create_task(
            self._protocol.add_receive_handler(GeckoPackCommandProtocolHandler())
        )
        self._protocol.queue_send(
            GeckoPackCommandProtocolHandler.set_value(
                self.get_and_increment_sequence_counter(),
                self.pack_type,
                self.config_version,
                self.log_version,
                pos,
                length,
                newvalue,
                parms=self.sendparms,
            ),
            self.sendparms,
        )
        await pack_command_task
