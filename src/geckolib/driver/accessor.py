""" Structure accessor """

import struct
import logging

from ..const import GeckoConstants
from .observable import Observable

logger = logging.getLogger(__name__)


class GeckoStructAccessor(Observable):
    """Class to access the spa data structure according to the declaration
    in SpaPackStruct.xml"""

    def __init__(self, struct_, element):
        super().__init__()
        self.element = element
        self.tag = element.tag
        self.struct = struct_
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

    def _get_raw_value(self, status_block=None):
        """Get a value from the pack structure using the initialized declaration
        or using the optionally supplied status_block (used by change notification)"""
        if status_block is None:
            status_block = self.struct.status_block
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
        return data

    def _get_value(self, status_block=None):
        data = self._get_raw_value(status_block)
        if self.type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            data = data == 1
            logger.debug("Bool accessor %s adjusted data = %s", self.tag, data)
        elif self.type == GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            try:
                data = self.items[data]
                logger.debug("Enum accessor %s adjusted data = %s", self.tag, data)
            except IndexError:
                logger.exception(
                    "Enum accessor %s out-of-range for %s", self.tag, self.items
                )
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
            self.format, self.struct.status_block[self.pos : self.pos + self.length]
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

        # We can't handle this here, we must delegate via the structure
        self.struct.set_value(self.pos, self.length, newvalue)

    @property
    def value(self):
        """ Get a value from the pack structure using the initialized declaration """
        return self._get_value()

    @property
    def raw_value(self):
        """Get a raw integer value from the pack structure using the initialized
        declaration"""
        return self._get_raw_value()

    @value.setter
    def value(self, newvalue):
        """ Set a value in the pack structure using the initialized declaration """
        self._set_value(newvalue)

    def __repr__(self):
        return f"{self.tag!r}: {self.value!r}"
