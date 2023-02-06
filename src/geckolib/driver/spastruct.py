""" Spa Structure block """

import logging

from .protocol import GeckoStatusBlockProtocolHandler
from .udp_socket import GeckoUdpSocket

logger = logging.getLogger(__name__)


class GeckoStructure:
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
        """Replace a segment of the status block"""
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
        self, handler: GeckoStatusBlockProtocolHandler, sender
    ):
        if not self._next_expected == handler.sequence:
            logger.debug(
                "Out-of-sequence status block segment %d - ignored", handler.sequence
            )
            if handler.next == 0:
                logger.debug("Retry status block request")
                self._next_expected = 0
                self._status_block_segments = []
                if not handler.retry(self._socket):
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
        # Error keys
        self.error_keys = log_class.error_keys

    def retry_request(
        self,
        socket_: GeckoUdpSocket,
        request: GeckoStatusBlockProtocolHandler,
        sender: tuple,
    ):
        self._socket = socket_
        request._on_handled = self._on_status_block_received
        self._status_block_offset = request.start
        socket_.add_receive_handler(request)
        self._next_expected = 0
        self._status_block_segments = []
        socket_.queue_send(request, sender)

    def set_value(self, pos, length, newvalue):
        # Delegate this
        self._on_set_value(pos, length, newvalue)
