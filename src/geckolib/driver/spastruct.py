""" Spa Structure block """

import logging

from ..const import GeckoConstants
from .protocol import GeckoStatusBlockProtocolHandler
from .udp_socket import GeckoUdpSocket
from .accessor import GeckoStructAccessor
from .decorators import GeckoTemperatureDecorator

logger = logging.getLogger(__name__)


class GeckoStructure:
    """Class to host/manage the raw data block for a spa structure"""

    def __init__(self, on_set_value):
        self._status_block = b"\x00" * 1024
        self.accessors = {}
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
            logger.warning(
                "Out-of-sequence status block segment %d - ignored", handler.sequence
            )
            if handler.next == 0:
                logger.warning("Retry status block request")
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
                logger.info("Status block segments complete, update and remove handler")
                self.replace_status_block_segment(
                    self._status_block_offset, b"".join(self._status_block_segments)
                )
                self.had_at_least_one_block = True
                handler._should_remove_handler = True

    def build_accessors(self, xmllist):
        self.accessors = {
            element.tag: GeckoStructAccessor(self, element)
            for xml in xmllist
            for element in xml.findall(
                GeckoConstants.SPA_PACK_STRUCT_POS_ELEMENTS_XPATH
            )
        }
        # Fix temperature accessors ...
        temp_keys = {
            element.tag
            for xml in xmllist
            for element in xml.findall(
                GeckoConstants.SPA_PACK_STRUCT_WORD_TYPE_ELEMENTS_XPATH
            )
            if "temp" in element.tag.lower() or "setpoint" in element.tag.lower()
        }
        logger.debug("Temperature keys to decorate %s", temp_keys)
        for key in temp_keys:
            self.accessors[key] = GeckoTemperatureDecorator(self, self.accessors[key])

    def retry_request(
        self,
        socket_: GeckoUdpSocket,
        request: GeckoStatusBlockProtocolHandler,
        sender: tuple,
    ):
        request._on_handled = self._on_status_block_received
        self._status_block_offset = request.start
        socket_.add_receive_handler(request)
        self._next_expected = 0
        self._status_block_segments = []
        socket_.queue_send(request, sender)

    def set_value(self, pos, length, newvalue):
        # Delegate this
        self._on_set_value(pos, length, newvalue)
