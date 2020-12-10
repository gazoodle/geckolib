""" Structure accessor """

import struct
import logging

from ..const import GeckoConstants
from .observable import Observable
from .protocol import (
    GeckoPackCommandProtocolHandler,
    GeckoStatusBlockProtocolHandler,
)
from .udp_socket import GeckoUdpSocket

logger = logging.getLogger(__name__)


class GeckoStructure:
    """Class to host/manage the raw data block for a spa structure"""

    def __init__(self, socket: GeckoUdpSocket):
        self._status_block = b"\x00" * 1024
        self._socket = socket
        self._accessors = {}
        self.had_at_least_one_block = False

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
        for accessor in self._accessors.values():
            accessor.status_block_changed(offset, segment_len, previous_block)

    @property
    def status_block(self):
        return self._status_block

    def set_status_block(self, block):
        self._status_block = block

    def _on_retry(self, socket, handler):
        print("Retry")
        if handler is not None:
            handler.reset_timeout()
        self._next_expected = 0
        self._status_block_segments = []

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

    def retry_request(self, request: GeckoStatusBlockProtocolHandler, sender: tuple):
        request._on_handled = self._on_status_block_received
        self._status_block_offset = request.start
        self._socket.add_receive_handler(request)
        self._next_expected = 0
        self._status_block_segments = []
        self._socket.queue_send(request, sender)


class GeckoStructAccessor(Observable):
    """Class to access the spa data structure according to the declaration
    in SpaPackStruct.xml"""

    def __init__(self, spa, element):
        super().__init__()
        self.element = element
        self.tag = element.tag
        self.spa = spa
        self.pos = int(element.attrib[GeckoConstants.SPA_PACK_STRUCT_POS_ATTRIB])
        self.type = element.attrib[GeckoConstants.SPA_PACK_STRUCT_TYPE_ATTRIB]
        self.bitpos = None

        if GeckoConstants.SPA_PACK_STRUCT_BITPOS_ATTRIB in element.attrib:
            self.bitpos = int(
                element.attrib[GeckoConstants.SPA_PACK_STRUCT_BITPOS_ATTRIB]
            )
            self.bitmask = 1
        if GeckoConstants.SPA_PACK_STRUCT_ITEMS_ATTRIB in element.attrib:
            self.items = element.attrib[
                GeckoConstants.SPA_PACK_STRUCT_ITEMS_ATTRIB
            ].split("|")

        self.length = 1
        self.format = ">B"

        if GeckoConstants.SPA_PACK_STRUCT_SIZE_ATTRIB in element.attrib:
            self.length = int(
                element.attrib[GeckoConstants.SPA_PACK_STRUCT_SIZE_ATTRIB]
            )
            if self.length == 2:
                self.format = ">H"

        if (
            self.type == GeckoConstants.SPA_PACK_STRUCT_WORD_TYPE
            or self.type == GeckoConstants.SPA_PACK_STRUCT_TIME_TYPE
        ):
            self.length = 2
            self.format = ">H"
        if GeckoConstants.SPA_PACK_STRUCT_MAXITEMS_ATTRIB in element.attrib:
            self.maxitems = int(
                element.attrib[GeckoConstants.SPA_PACK_STRUCT_MAXITEMS_ATTRIB]
            )
            if self.maxitems > 8:
                self.bitmask = 15
            elif self.maxitems > 4:
                self.bitmask = 7
            elif self.maxitems > 2:
                self.bitmask = 3
        self.read_write = None
        if GeckoConstants.SPA_PACK_STRUCT_READ_WRITE_ATTRIB in element.attrib:
            self.read_write = element.attrib[
                GeckoConstants.SPA_PACK_STRUCT_READ_WRITE_ATTRIB
            ]

    def status_block_changed(self, offset, len, previous):
        # Does the notified range intersect us, if not then we don't care!
        intersection_start = max(offset, self.pos)
        intersection_end = min(offset + len, self.pos + self.length)
        if intersection_end - intersection_start <= 0:
            return

        logger.debug(
            "Accessor %s @ %d-%d notified of change at %d-%d",
            self.tag,
            self.pos,
            self.pos + self.length,
            offset,
            offset + len,
        )

        old_value = self._get_value(previous)
        new_value = self.value

        # No reason to notify if there is no change
        if new_value == old_value:
            return

        logger.info(
            "Value for %s changed from %s to %s", self.tag, old_value, new_value
        )

        self._on_change(self, old_value, new_value)

    def _get_value(self, status_block=None):
        """Get a value from the pack structure using the initialized declaration
        or using the optionally supplied status_block (used by change notification)"""
        if status_block is None:
            status_block = self.spa.struct.status_block
        data = struct.unpack(
            self.format, status_block[self.pos : self.pos + self.length]
        )[0]
        logger.debug(
            "Accessor %s @ %s, %s raw data = %x", self.tag, self.pos, self.type, data
        )
        if self.bitpos is not None:
            data = (data >> self.bitpos) & self.bitmask
            logger.debug(
                "BitPos %s accessor %s adjusted data = %x",
                (self.bitpos, self.bitmask),
                self.tag,
                data,
            )
        if self.type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            data = data == 1
            logger.debug("Bool accessor %s adjusted data = %s", self.tag, data)
        elif self.type == GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            data = self.items[data]
            logger.debug("Enum accessor %s adjusted data = %s", self.tag, data)
        return data

    def _set_value(self, newvalue):
        """ Set a value in the pack structure using the initialized declaration """
        if self.read_write is None:
            raise Exception(
                GeckoConstants.EXCEPTION_MESSAGE_NOT_WRITABLE.format(self.tag)
            )

        if self.type == GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            logger.debug("Enum accessor %s adjusted from %s", self.tag, newvalue)
            newvalue = self.items.index(newvalue)

        # If it is a bitpos, then mask it with the existing value
        existing = struct.unpack(
            self.format, self.spa.struct.status_block[self.pos : self.pos + self.length]
        )[0]
        if self.bitpos is not None:
            logger.debug(
                "Bitpos %s accessor %s adjusted from %s",
                (self.bitpos, self.bitmask),
                self.tag,
                newvalue,
            )
            newvalue = (existing & ~(self.bitmask << self.bitpos)) | (
                (newvalue & self.bitmask) << self.bitpos
            )

        logger.debug(
            "Accessor %s @ %s, %s setting value to %s, existing value was %s. "
            "Length is %d",
            self.tag,
            self.pos,
            self.type,
            newvalue,
            existing,
            self.length,
        )

        # We issue a pack command to acheive this ...
        self.spa.add_receive_handler(GeckoPackCommandProtocolHandler())
        self.spa.queue_send(
            GeckoPackCommandProtocolHandler.set_value(
                self.spa.get_and_increment_sequence_counter(),
                self.spa.pack_type,
                self.spa.config_version,
                self.spa.log_version,
                self.pos,
                self.length,
                newvalue,
                parms=self.spa.sendparms,
            ),
            self.spa.sendparms,
        )

    @property
    def value(self):
        """ Get a value from the pack structure using the initialized declaration """
        return self._get_value()

    @value.setter
    def value(self, newvalue):
        """ Set a value in the pack structure using the initialized declaration """
        self._set_value(newvalue)

    def __repr__(self):
        return f"{self.tag!r}: {self.value!r}"
