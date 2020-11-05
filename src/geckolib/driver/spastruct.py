""" Structure accessor """

import struct
import logging

from ..const import GeckoConstants
from .responses import GeckoPackCommand

logger = logging.getLogger(__name__)


class GeckoStructAccessor:
    """ Class to access the spa data structure according to the declaration in SpaPackStruct.xml """

    def __init__(self, spa, element):
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

    @property
    def value(self):
        """ Get a value from the pack structure using the initialized declaration """
        data = struct.unpack(
            self.format, self.spa.status_block[self.pos : self.pos + self.length]
        )[0]
        logger.debug(
            "Accessor %s @ %s, %s raw data = %x", self.tag, self.pos, self.type, data
        )
        if not self.bitpos is None:
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

    @value.setter
    def value(self, newvalue):
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
            self.format, self.spa.status_block[self.pos : self.pos + self.length]
        )[0]
        if not self.bitpos is None:
            logger.debug(
                "Bitpos %s accessor %s adjusted from %s",
                (self.bitpos, self.bitmask),
                self.tag,
                newvalue,
            )
            newvalue = (existing & ~(self.bitmask << self.bitpos)) | (
                (newvalue & self.bitmask) << self.bitpos
            )

        if self.length == 1:
            newvalue = [int(newvalue)]
        elif self.length == 2:
            newvalue = [int(newvalue) // 256, int(newvalue) % 256]

        logger.debug(
            "Accessor %s @ %s, %s setting value to %s, existing value was %s. Length is %d",
            self.tag,
            self.pos,
            self.type,
            newvalue,
            existing,
            self.length,
        )

        # We issue a pack command to acheive this ...
        self.spa.send_request(
            GeckoPackCommand(
                self.spa.pack_type,
                [
                    GeckoConstants.PACK_COMMAND_SET_VALUE,
                    self.spa.config_version,
                    self.spa.log_version,
                    self.pos // 256,
                    self.pos % 256,
                ]
                + newvalue,
            )
        )
