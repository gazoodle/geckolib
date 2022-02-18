""" Async Spa Structure block """

import logging
import asyncio

from .protocol import GeckoStatusBlockProtocolHandler
from .async_udp_protocol import GeckoAsyncUdpProtocol

logger = logging.getLogger(__name__)


class GeckoAsyncStructure:
    """Class to host/manage the raw data block for a spa structure"""

    def __init__(self, on_set_value):
        self._status_block = b"\x00" * 1024
        self.accessors = {}
        self.all_outputs = []
        self.all_devices = []
        self.user_demands = []
        self.had_at_least_one_block = False
        self._on_set_value = on_set_value

        # Install a set of handlers

    def replace_status_block_segment(self, offset, segment):
        """ Replace a segment of the status block """
        previous_block = self._status_block
        segment_len = len(segment)
        self._status_block = (
            self._status_block[0:offset]
            + segment
            + self._status_block[offset + segment_len :]
        )
        # Notify changes to accessors
        for accessor in self.accessors.values():
            accessor.status_block_changed(offset, segment_len, previous_block)

    @property
    def status_block(self):
        return self._status_block

    def set_status_block(self, block):
        self._status_block = block

    def _on_status_block_received(
        self, handler: GeckoStatusBlockProtocolHandler, socket, sender
    ):
        if not self._next_expected == handler.sequence:
            logger.debug(
                "Out-of-sequence status block segment %d - ignored", handler.sequence
            )
            if handler.next == 0:
                logger.debug("Retry status block request")
                self._next_expected = 0
                self._status_block_segments = []
                if not handler.retry(socket):
                    raise RuntimeError("Too many retries")
        else:
            self._status_block_segments.append(handler.data)
            self._next_expected = handler.next
            # When we get the last partial segment, we can assume the spa is
            # connected and we can report on status
            if handler.next == 0:
                logger.debug(
                    "Status block segments complete, update and remove handler"
                )
                self.replace_status_block_segment(
                    self._status_block_offset, b"".join(self._status_block_segments)
                )
                self.had_at_least_one_block = True
                handler._should_remove_handler = True

    def build_accessors(self, config_class, log_class):
        self.accessors = dict(config_class.accessors, **log_class.accessors)
        # Get all outputs
        self.all_outputs = config_class.output_keys
        # Get collection of possible devices
        self.all_devices = log_class.all_device_keys
        # User devices are those that have a Ud in the tag name
        self.user_demands = log_class.user_demand_keys

    async def retry_request(
        self,
        protocol_: GeckoAsyncUdpProtocol,
        request: GeckoStatusBlockProtocolHandler,
        sender: tuple,
    ):
        request._on_handled = self._on_status_block_received
        self._status_block_offset = request.start
        request_task = asyncio.create_task(protocol_.add_receive_handler(request))
        self._next_expected = 0
        self._status_block_segments = []
        protocol_.queue_send(request, sender)
        await request_task

    async def set_value(self, pos, length, newvalue):
        # Delegate this
        await self._on_set_value(pos, length, newvalue)
