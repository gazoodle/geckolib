#!/usr/bin/python3
"""
    Library to communicate with Gecko Alliance products via the in.touch2 module
"""

#
#   Copyright (C) 2020, Gazoodle (https://github.com/gazoodle)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   Using Semantic versioning https://semver.org/

import logging
import os.path
import re
import socket
import struct
import threading
import time
import xml.etree.ElementTree as ET

import urllib3

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

###################################################################################################
class GeckoConstants:
    """
    GeckoConstants is a literal class so that we can program in a mostly DRY fashion,
    for example a filename or url would be present as would values that could be changed
    and might be difficult to discover inline, but some constants that form part of a functions
    documented behaviour might not be here, e.g. 'rw' as a parameter to open()
    """

    VERSION_MAJOR = 0
    VERSION_MINOR = 3
    VERSION_PATCH = 8

    INCLUDE_DUMMY_SPA = False
    INTOUCH2_PORT = 10022
    MAX_PACKET_SIZE = 8192
    DISCOVERY_TIMEOUT_IN_SECONDS = 4
    DISCOVERY_RETRY_COUNT_TO_FIND_ANY_SPA = 3
    PING_TIMEOUT_IN_SECONDS = 4
    PING_FREQUENCY_IN_SECONDS = 15

    BROADCAST_ADDRESS = "255.255.255.255"
    MESSAGE_ENCODING = "utf-8"
    FORMAT_CLIENT_IDENTIFIER = "IOS{0}"

    SPA_PACK_STRUCT_FILE = "SpaPackStruct.xml"
    SPA_PACK_STRUCT_URL = "http://intouch.geckoal.com/gecko/prod/SpaPackStruct.xml"
    # XPaths and attributes for SpaPackStruct
    SPA_PACK_REVISION_XPATH = "./SpaPackStruct/FileRevision"
    SPA_PACK_REVISION_ATTRIB = "Number"
    SPA_PACK_PLATEFORM_XPATH = "./Plateform"
    SPA_PACK_NAME_ATTRIB = "Name"
    SPA_PACK_CONFIG_XPATH = "./ConfigStructures/ConfigStructure[@LibRev='{0}']"
    SPA_PACK_LOG_XPATH = "./LogStructures/LogStructure[@LibRev='{0}']"
    SPA_PACK_STRUCT_POS_ATTRIB = "Pos"
    SPA_PACK_STRUCT_TYPE_ATTRIB = "Type"
    SPA_PACK_STRUCT_BITPOS_ATTRIB = "BitPos"
    SPA_PACK_STRUCT_ITEMS_ATTRIB = "Items"
    SPA_PACK_STRUCT_SIZE_ATTRIB = "Size"
    SPA_PACK_STRUCT_WORD_TYPE = "Word"
    SPA_PACK_STRUCT_TIME_TYPE = "Time"
    SPA_PACK_STRUCT_MAXITEMS_ATTRIB = "MaxItems"
    SPA_PACK_STRUCT_BOOL_TYPE = "Bool"
    SPA_PACK_STRUCT_ENUM_TYPE = "Enum"
    SPA_PACK_STRUCT_POS_ELEMENTS_XPATH = ".//*[@Pos]"
    SPA_PACK_STRUCT_WORD_TYPE_ELEMENTS_XPATH = './/*[@Type="Word"]'
    SPA_PACK_STRUCT_BEGIN_ATTRIB = "Begin"
    SPA_PACK_STRUCT_END_ATTRIB = "End"
    SPA_PACK_STRUCT_READ_WRITE_ATTRIB = "RW"
    # Accessor keys for SpaPackStruct
    KEY_PACK_TYPE = "PackType"
    KEY_PACK_CONFIG_ID = "PackConfID"
    KEY_PACK_CONFIG_REV = "PackConfRev"
    KEY_PACK_CONFIG_REL = "PackConfRel"
    KEY_CONFIG_NUMBER = "ConfigNumber"
    KEY_TEMP_UNITS = "TempUnits"
    KEY_RH_WATER_TEMP = "RhWaterTemp"
    KEY_SETPOINT_G = "SetpointG"
    KEY_REAL_SETPOINT_G = "RealSetPointG"
    KEY_DISPLAYED_TEMP_G = "DisplayedTempG"
    KEY_USER_DEMAND_LIGHT = "UdLi"
    KEY_PUMP_1 = "P1"
    KEY_PUMP_2 = "P2"
    KEY_PUMP_3 = "P3"
    KEY_PUMP_4 = "P4"
    KEY_PUMP_5 = "P5"
    key_blower = "BL"

    EXCEPTION_MESSAGE_NO_SPA_PACK = "Cannot find spa pack for {0}"
    EXCEPTION_MESSAGE_NOT_WRITABLE = (
        "Cannot set value for {0}. This status array item doesn't allow writing"
    )

    # Message pseudo xml parts
    MESSAGE_HELLO = "<HELLO>{0}</HELLO>"
    MESSAGE_PART_PACKET = "<PACKT>{0}</PACKT>"
    MESSAGE_PART_DATAS = "<DATAS>{0}</DATAS>"
    MESSAGE_PART_CONNECTION_NAMES = "<SRCCN>{0}</SRCCN><DESCN>{1}</DESCN>"

    # Command & response pseudo xml content
    REQUEST_AND_RESPONSE_PING = ("APING", b"APING")
    REQUEST_AND_RESPONSE_GET_VERSION = ("AVERS", b"SVERS")
    REQUEST_AND_RESPONSE_GET_CHANNEL = ("CURCH", b"CHCUR")
    REQUEST_AND_RESPONSE_GET_CONFIG = ("SFILE", b"FILES")
    REQUEST_AND_RESPONSE_GET_STATUS = ("STATU", b"STATV")
    REQUEST_AND_RESPONSE_PARTIAL_STATUS = ("STATQ", b"STATP")
    REQUEST_AND_RESPONSE_PACK_COMMAND = ("SPACK", b"PACKS")

    # Pack commands
    PACK_COMMAND_KEY_PRESS = 57
    PACK_COMMAND_SET_VALUE = 70

    # Gecko keypad constants
    KEYPAD_PUMP_1 = 1
    KEYPAD_PUMP_2 = 2
    KEYPAD_PUMP_3 = 3
    KEYPAD_PUMP_4 = 4
    KEYPAD_PUMP_5 = 5
    KEYPAD_BLOWER = 6
    KEYPAD_LIGHT = 16
    KEYPAD_UP = 21
    KEYPAD_DOWN = 22

    # Pack outputs
    PACK_OUTPUTS_XPATHS = [
        './HCOutputConfig/*[@Type="Enum"]',
        './LCOutputConfig/*[@Type="Enum"]',
        './LVOutputConfig/*[@Type="Enum"]',
    ]
    SPA_PACK_DEVICE_XPATH = "./DeviceStatus/*"
    SPA_PACK_USER_DEMANDS = "./UserDemands/*"

    DEVICE_CLASS_PUMP = "PUMP"
    DEVICE_CLASS_BLOWER = "BLOWER"
    DEVICE_CLASS_LIGHT = "LIGHT"

    # Spa devices and accessories, dictionary of tuples
    #   ID: Description, keypad, structure key, class
    DEVICES = {
        "P1": ("Pump 1", KEYPAD_PUMP_1, KEY_PUMP_1, DEVICE_CLASS_PUMP),
        "P2": ("Pump 2", KEYPAD_PUMP_2, KEY_PUMP_2, DEVICE_CLASS_PUMP),
        "P3": ("Pump 3", KEYPAD_PUMP_3, KEY_PUMP_3, DEVICE_CLASS_PUMP),
        "P4": ("Pump 4", KEYPAD_PUMP_4, KEY_PUMP_4, DEVICE_CLASS_PUMP),
        "P5": ("Pump 5", KEYPAD_PUMP_5, KEY_PUMP_5, DEVICE_CLASS_PUMP),
        "BL": ("Blower", KEYPAD_BLOWER, key_blower, DEVICE_CLASS_BLOWER),
        "LI": ("Lights", KEYPAD_LIGHT, KEY_USER_DEMAND_LIGHT, DEVICE_CLASS_LIGHT),
    }

    # Buttons, list of tuples
    #   ID, Description, KeyPad ID
    BUTTONS = [
        ("P1", "Pump 1 Button", KEYPAD_PUMP_1),
        ("P2", "Pump 2 Button", KEYPAD_PUMP_2),
        ("P3", "Pump 3 Button", KEYPAD_PUMP_3),
        ("P4", "Pump 4 Button", KEYPAD_PUMP_4),
        ("P5", "Pump 5 Button", KEYPAD_PUMP_5),
        ("BLOWER", "Blower Button", KEYPAD_BLOWER),
        ("LIGHT", "Lights Button", KEYPAD_LIGHT),
        ("UP", "Up Button", KEYPAD_UP),
        ("DOWN", "Down Button", KEYPAD_DOWN),
    ]

    REGEX_DOT_STAR = "(.*)"


###################################################################################################
class GeckoResponse:
    """
    GeckoResponse: base class for handling the UDP conversation with the intouch module
    """

    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.

    def __init__(
        self, request_and_response, handler=None, timeout=5, timeout_handler=None
    ):
        self.request_and_response = request_and_response
        self.handler = handler
        if self.handler is None:
            self.handler = self.default_handler
        self.timeout = timeout
        self.timeout_handler = timeout_handler
        self.init_time = time.monotonic()
        self.has_sequence = True
        self.parms = None
        self.retry_count = 0

    def check_timeout(self, spa):
        """ Decide if this device response has timed-out, and if so, optionally retry """
        if self.timeout == 0:
            return False
        if time.monotonic() - self.init_time > self.timeout:
            self.retry_count += 1
            logger.warning(
                "Handler for %s timed out, retry %d",
                self.request_and_response[0],
                self.retry_count,
            )
            if self.retry_count < 5:
                self.init_time = time.monotonic()
                self.send_request(spa)
                return False
            logger.warning(
                "Handler for %s timed out, aborted", self.request_and_response[0]
            )
            if not self.timeout_handler is None:
                self.timeout_handler()
            return True
        return False

    def handle_response_if_matched(self, spa, response):
        """ Handle the response, and if it matches, call the handler """
        if response.startswith(self.request_and_response[1]):
            if self.handler(spa, response):
                spa.remove_handler(self)
            return True
        return False

    def send_request(self, spa):
        """ Send a request to the spa """
        spa.send_message(
            spa.build_command(
                self.request_and_response[0], self.has_sequence, self.parms
            )
        )

    def unpack(self, fmt, length, response):
        """ Unpack the response using the format, dealing with the keywords """
        cmd_len = 0
        if response.startswith(self.request_and_response[1]):
            cmd_len = len(self.request_and_response[1])
        return struct.unpack(fmt, response[cmd_len : cmd_len + length]) + (
            response[cmd_len + length :],
        )

    def default_handler(self, spa, response):
        """ Default handler does nothing """
        del self, spa, response  # Unused
        return True


###################################################################################################
class GeckoPing(GeckoResponse):
    """ Handle the ping command """

    def __init__(self):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_PING,
            self.ping_handler,
            GeckoConstants.PING_TIMEOUT_IN_SECONDS,
        )
        self.has_sequence = False

    def ping_handler(self, spa, response):
        """ Handle the ping response from the other end """
        logger.debug("Ping response received")
        del spa, response  # unused
        return True


###################################################################################################
class GeckoPartialStatus(GeckoResponse):
    """ Handle partial status responses to stitch the block back together """

    def __init__(self):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_PARTIAL_STATUS,
            self.partial_status_handler,
            0,
        )

    def partial_status_handler(self, spa, response):
        """ Handle the partial status response from the other end """
        self.send_request(spa)
        change_count, response = self.unpack(">B", 1, response)
        for _ in range(change_count):
            pos, byte_1, byte_2, response = self.unpack(">HBB", 4, response)
            arry = bytearray()
            arry.append(byte_1)
            arry.append(byte_2)
            spa.replace_status_block_segment(pos, arry)

        # Never complete so it will remain in the handler collection
        return False


###################################################################################################
class GeckoGetSoftwareVersion(GeckoResponse):
    """ Process the Get the software version command """

    def __init__(self):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_GET_VERSION, self.version_handler
        )

    def version_handler(self, spa, response):
        """ Handle the software version response """
        (
            en_build,
            en_major,
            en_minor,
            co_build,
            co_major,
            co_minor,
            response,
        ) = self.unpack(">HBBHBB", 8, response)
        spa.intouch_version_en = "{0} v{1}.{2}".format(en_build, en_major, en_minor)
        spa.intouch_version_co = "{0} v{1}.{2}".format(co_build, co_major, co_minor)
        logger.debug(
            "Got software version %s/%s, now get channel",
            spa.intouch_version_en,
            spa.intouch_version_co,
        )
        spa.send_request(GeckoGetChannel())
        return True


###################################################################################################
class GeckoGetChannel(GeckoResponse):
    """ Process the Get channel command """

    def __init__(self):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_GET_CHANNEL, self.channel_handler
        )

    def channel_handler(self, spa, response):
        """ Handle the get channel response """
        spa.channel, spa.signal, response = self.unpack(">BB", 2, response)
        logger.debug("Got channel %s/%s, get config", spa.channel, spa.signal)
        spa.send_request(GeckoGetConfig())
        return True


###################################################################################################
class GeckoPackCommand(GeckoResponse):
    """ Handle the pack command """

    def __init__(self, packtype, values):
        super().__init__(GeckoConstants.REQUEST_AND_RESPONSE_PACK_COMMAND)
        self.parms = "".join(chr(item) for item in [packtype, len(values)] + values)
        logger.debug("Pack cmd %s", self.parms.encode(GeckoConstants.MESSAGE_ENCODING))


###################################################################################################
class GeckoGetConfig(GeckoResponse):
    """ Handle the GetConfig command """

    def __init__(self):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_GET_CONFIG, self.config_handler
        )

    def config_handler(self, spa, response):
        """ Handle the get config response """
        # Treat the files as if they were indices into the SpaPackStruct.xml file
        config = (
            response[6:]
            .decode(GeckoConstants.MESSAGE_ENCODING)
            .replace(".xml", "")
            .split(",")
        )
        # Split the string around the underscore
        gecko_pack_config = config[0].split("_")
        gecko_pack_log = config[1].split("_")

        # XML is case-sensitive, but the platform from the config isn't formed the same,
        # so we manually search the Plateform nodes to find the one we're interested in
        for plateform in spa.manager.spa_pack_struct.findall(
            GeckoConstants.SPA_PACK_PLATEFORM_XPATH
        ):
            if (
                plateform.attrib[GeckoConstants.SPA_PACK_NAME_ATTRIB].lower()
                == gecko_pack_config[0].lower()
            ):
                spa.gecko_pack_xml = plateform

        # We can't carry on without information on how the STATV data block is formed ...
        if spa.gecko_pack_xml is None:
            raise Exception(
                GeckoConstants.EXCEPTION_MESSAGE_NO_SPA_PACK.format(
                    gecko_pack_config[0]
                )
            )

        # Stash the config and log structure declarations
        spa.config_version = int(gecko_pack_config[1][1:])
        spa.config_xml = spa.gecko_pack_xml.find(
            GeckoConstants.SPA_PACK_CONFIG_XPATH.format(spa.config_version)
        )
        spa.log_version = int(gecko_pack_log[1][1:])
        spa.log_xml = spa.gecko_pack_xml.find(
            GeckoConstants.SPA_PACK_LOG_XPATH.format(spa.log_version)
        )
        spa.pack_type = int(
            spa.gecko_pack_xml.attrib[GeckoConstants.SPA_PACK_STRUCT_TYPE_ATTRIB]
        )

        logger.debug(
            "Got spa configuration Type %s - CFG %s/LOG %s, now ask for initial status block",
            spa.pack_type,
            spa.config_version,
            spa.log_version,
        )

        # Grab a big chunk first time around
        spa.send_request(GeckoGetStatus(0, 1024))
        return True


###################################################################################################
class GeckoGetStatus(GeckoResponse):
    """ Handle the get status command """

    def __init__(self, start, length):
        self.offset = start
        self.length = length
        self.next_expected = 0
        self.received = 0
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_GET_STATUS, self.status_handler, 20
        )
        self.parms = "{0:c}{1:c}{2:c}{3:c}".format(
            start // 256, start % 256, length // 256, length % 256
        )

    def status_handler(self, spa, response):
        """ Handle the status response segment """
        seq, nxt, length, response = self.unpack(">BBB", 3, response)
        logger.debug(
            "Status block segment # %d (then #%d) length %d, was expecting %d",
            seq,
            nxt,
            length,
            self.next_expected,
        )
        if not self.next_expected == seq:
            logger.warning("Out-of-sequence status block segment - ignored")
            if nxt == 0:
                logger.warning("Retry status block request")
                spa.send_request(GeckoGetStatus(self.offset, self.length))
        else:
            spa.replace_status_block_segment(
                self.offset + self.received, response[0:length]
            )
            self.received += length
            self.next_expected = nxt
            # When we get the last partial segment, we can assume the spa is
            # connected and we can report on status
            if nxt == 0:
                spa.is_connected = True
        return nxt == 0


###################################################################################################
class GeckoComms:
    """ Base class for UDP packet sending and receiving """

    def __init__(self, mgr):
        # Create a UDP socket
        self.socket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
        )
        self.socket.settimeout(1)
        self.ipaddress = None
        self.port = GeckoConstants.INTOUCH2_PORT
        self.identifier = None
        self.manager = mgr
        self._conns = None
        self._sequence_number = 1

    def __del__(self):
        self.socket.close()

    def send_message(self, message, destination=None):
        """ Send the message to the destination address and port """
        if destination is None:
            destination = self.ipaddress
        logger.debug(
            "Send message %s to %s",
            message.encode(GeckoConstants.MESSAGE_ENCODING),
            (destination, self.port),
        )
        self.socket.sendto(
            message.encode(GeckoConstants.MESSAGE_ENCODING), (destination, self.port)
        )

    def receive_answer(self):
        """ Process a received answer from the other end """
        data, remote = self.socket.recvfrom(GeckoConstants.MAX_PACKET_SIZE)
        logger.debug("Receive answer %s from %s", data, remote)
        return (data, remote)

    def extract_data_using_regex(self, message, data):
        """ Extract the data from the XML message using a regex expression """
        match = re.search(
            bytes(
                message.format(GeckoConstants.REGEX_DOT_STAR),
                GeckoConstants.MESSAGE_ENCODING,
            ),
            data,
            re.DOTALL,
        )
        return match.group(1)

    def assemble_packet(self, data):
        """ Assemble an XML packet to send """
        return GeckoConstants.MESSAGE_PART_PACKET.format(
            "{0}{1}".format(self._conns, GeckoConstants.MESSAGE_PART_DATAS.format(data))
        )

    def build_command(self, cmd, has_sequence=True, parms=None):
        """ Build a command, optionally using a sequence number and parameters """
        if has_sequence:
            self._sequence_number += 1
            cmd += chr(self._sequence_number)
        if not parms is None:
            cmd += parms
        return self.assemble_packet(cmd)


###################################################################################################
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
            "Accessor %s @ %s, %s setting value to %s, existing value was %s",
            self.tag,
            self.pos,
            self.type,
            newvalue,
            existing,
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


###################################################################################################
class GeckoTemperatureDecorator:
    """Class to decorate a temperature accessor so that the farenheight tenths, offset
    from freezing are handled"""

    def __init__(self, spa, accessor):
        self.spa = spa
        self.accessor = accessor

    @property
    def value(self):
        """ Get the temperature """
        # Internally, temp is in farenheight tenths, offset from freezing point
        temp = self.accessor.value
        units = self.spa.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        if units == "C":
            temp = temp / 18.0
        else:
            temp = (temp + 320) / 10.0
        return temp

    @value.setter
    def value(self, temp):
        """ Set the temperature """
        units = self.spa.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        if units == "C":
            temp = float(temp) * 18.0
        else:
            temp = (float(temp) * 10.0) - 320
        self.accessor.value = int(temp)


###################################################################################################
class GeckoCommsClient(GeckoComms):
    """ GeckoCommsClient handles the receive thread lifetime and handler list """

    def __init__(self, mgr):
        super().__init__(mgr)
        self.handlers = []
        self.exit = threading.Event()
        self.receive_thread = threading.Thread(target=self.receive_thread_func)
        self.receive_thread.start()

    def __del__(self):
        super().__del__()
        self.receive_thread.join()

    def finished(self):
        """ Signal that we're finished with the communication """
        self.exit.set()

    def add_handler(self, handler):
        """ Add a handler to the handler list """
        self.handlers.append(handler)

    def remove_handler(self, handler):
        """ Remove a handler from the handler list """
        self.handlers.remove(handler)

    def clean_handlers(self):
        """ Cleanup handlers that have timed out """
        handlers_to_remove = [
            handler for handler in self.handlers if handler.check_timeout(self)
        ]
        self.handlers = [
            handler for handler in self.handlers if handler not in handlers_to_remove
        ]

    def receive_thread_func(self):
        """ Thread function for processing async received messages """
        while not self.exit.is_set():
            try:
                self._handle_response(
                    self.extract_data_using_regex(
                        GeckoConstants.MESSAGE_PART_DATAS, self.receive_answer()[0]
                    )
                )
            except socket.timeout:
                continue
            except Exception:  # pylint: disable=broad-except
                logger.exception("Exception in receive thread func")
            self.clean_handlers()

    def _handle_response(self, response):
        # Iterate over the handlers to see if any are interested in this response ...
        for handler in self.handlers:
            if handler.handle_response_if_matched(self, response):
                return
        # We sometimes get extraneous PACKS response when another client has issued
        # the SPACK command ... don't fret about it!
        if response.startswith(GeckoConstants.REQUEST_AND_RESPONSE_PACK_COMMAND[1]):
            return
        logger.warning("Unhandled response %s (%d)", response, len(response))


###################################################################################################
class GeckoSpa(GeckoCommsClient):
    """
    GeckoSpa class manages an instance of a spa, and is the main point of contact for control
    and monitoring. Uses the declarations found in SpaPackStruct.xml to build an object that
    exposes the properties and capabilities of your spa
    """

    def __init__(self, mgr, response):
        super().__init__(mgr)
        data = self.extract_data_using_regex(
            GeckoConstants.MESSAGE_HELLO, response[0]
        ).decode(GeckoConstants.MESSAGE_ENCODING)
        self.client_identifier = mgr.client_identifier
        self.identifier, self.name = data.split("|")
        self.ipaddress, self.port = response[1]
        self._conns = GeckoConstants.MESSAGE_PART_CONNECTION_NAMES.format(
            self.client_identifier, self.identifier
        )
        self.add_handler(GeckoPartialStatus())

        self.ping_thread = threading.Thread(target=self.ping_thread_func)

        # Default values for properties
        self.channel = 0
        self.signal = 0

        self.intouch_version_en = ""
        self.intouch_version_co = ""

        self.gecko_pack_xml = None
        self.config_version = 0
        self.config_xml = None
        self.log_version = 0
        self.log_xml = None
        self.pack_type = None
        self.is_connected = False
        self.pack = None
        self.version = None
        self.config_number = None

        # Inspection of the SpaPackStruct.xml shows that there are (currently) no
        # configurations larger than this
        self.status_block = b"\x00" * 1024
        self.accessors = {}

    def __del__(self):
        super().__del__()
        self.ping_thread.join()

    def send_request(self, request):
        """ Send a request and hold the handler to wait for the response """
        self.add_handler(request)
        request.send_request(self)

    def replace_status_block_segment(self, offset, segment):
        """ Replace a segment of the status block """
        segment_len = len(segment)
        prefix = self.status_block[0:offset]
        suffix = self.status_block[offset + segment_len :]
        self.status_block = prefix + segment + suffix

    def connect(self):
        """ Connect to the in.touch2 module """
        # Identify self to the intouch module
        self.send_message(GeckoConstants.MESSAGE_HELLO.format(self.client_identifier))
        self.ping_thread.start()
        # Get the intouch version
        logger.info("Starting spa connection handshake...")
        self.is_connected = False
        self.send_request(GeckoGetSoftwareVersion())
        # Wait for connection sequence to complete
        while not self.is_connected:
            pass
        self._build_accessors()
        self.pack = self.accessors[GeckoConstants.KEY_PACK_TYPE].value
        self.version = "{0} v{1}.{2}".format(
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_ID].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REV].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REL].value,
        )
        self.config_number = self.accessors[GeckoConstants.KEY_CONFIG_NUMBER].value
        logger.info("Spa is connected")

    def disconnect(self):
        """ Disconnect from the in.touch2 module """
        self.finished()

    def ping_thread_func(self):
        """ Ping thread function """
        while not self.exit.is_set():
            self.send_request(GeckoPing())
            self.exit.wait(GeckoConstants.PING_FREQUENCY_IN_SECONDS)

    def _build_accessors(self):
        self.accessors = {
            element.tag: GeckoStructAccessor(self, element)
            for xml in [self.config_xml, self.log_xml]
            for element in xml.findall(
                GeckoConstants.SPA_PACK_STRUCT_POS_ELEMENTS_XPATH
            )
        }
        # Fix temperature accessors ...
        temp_keys = {
            element.tag
            for xml in [self.config_xml, self.log_xml]
            for element in xml.findall(
                GeckoConstants.SPA_PACK_STRUCT_WORD_TYPE_ELEMENTS_XPATH
            )
            if "temp" in element.tag.lower() or "setpoint" in element.tag.lower()
        }
        logger.debug("Temperature keys to decorate %s", temp_keys)
        for key in temp_keys:
            self.accessors[key] = GeckoTemperatureDecorator(self, self.accessors[key])

    def get_buttons(self):
        """ Get a list of buttons that can be pressed """
        return [button[0] for button in GeckoConstants.BUTTONS]

    def refresh(self):
        """ Refresh the live spa data block """
        self.send_request(
            GeckoGetStatus(
                int(self.log_xml.attrib[GeckoConstants.SPA_PACK_STRUCT_BEGIN_ATTRIB]),
                int(self.log_xml.attrib[GeckoConstants.SPA_PACK_STRUCT_END_ATTRIB]),
            )
        )

    def press(self, keypad):
        """ Simulate a button press """
        self.send_request(
            GeckoPackCommand(
                self.pack_type, [GeckoConstants.PACK_COMMAND_KEY_PRESS, keypad]
            )
        )


###################################################################################################
class GeckoManager(GeckoComms):
    """
    GeckoManager class manages the local spa collection and hosts the discovery process
    """

    def __init__(self, client_uuid):
        super().__init__(self)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        if not os.path.exists(GeckoConstants.SPA_PACK_STRUCT_FILE):
            logger.info("SpaPackStruct.xml not found, downloading from the internet...")
            self.download()
        self.spa_pack_struct = ET.parse(GeckoConstants.SPA_PACK_STRUCT_FILE)
        self.spa_pack_struct_revision = self.spa_pack_struct.find(
            GeckoConstants.SPA_PACK_REVISION_XPATH
        ).attrib[GeckoConstants.SPA_PACK_REVISION_ATTRIB]
        self.client_identifier = GeckoConstants.FORMAT_CLIENT_IDENTIFIER.format(
            client_uuid
        )
        logger.info("SpaPackStruct v%s", self.spa_pack_struct_revision)
        logger.info("Client identifier %s", self.client_identifier)
        self.retry_count = 0
        self.spas = []

    def finish(self):
        """ Disconnect all the connected spas and release the background worker threads """
        for spa in self.spas:
            spa.disconnect()

    def download(self):
        """ Download SpaPackStruct.xml from it's permanent home """
        logger.info("Downloading SpaPackStruct.xml")
        http = urllib3.PoolManager()
        response = http.request(
            "GET", GeckoConstants.SPA_PACK_STRUCT_URL, preload_content=False
        )

        with open(GeckoConstants.SPA_PACK_STRUCT_FILE, "wb") as out:
            while True:
                data = response.read(4096)
                if not data:
                    break
                out.write(data)

        response.release_conn()
        logger.info("SpaPackStruct.xml downloaded")

    def discover(self):
        """Start the discovery process to locate any intouch2 capable
        Gecko modules on the local network."""
        logger.info("Discovery process started")
        self.spas = []
        while self.retry_count < GeckoConstants.DISCOVERY_RETRY_COUNT_TO_FIND_ANY_SPA:
            # Broadcast the discovery message to every client on the local LAN
            self.send_message(
                GeckoConstants.MESSAGE_HELLO.format(1), GeckoConstants.BROADCAST_ADDRESS
            )
            # Wait to ensure we've heard from all the modules that responded within
            # the discovery period
            now = time.monotonic()
            while time.monotonic() - now < GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS:
                try:
                    self.spas.append(GeckoSpa(self, self.receive_answer()))
                except socket.timeout:
                    break
            if len(self.spas) > 0:
                # Dummy spa to test multiple spas in client programs ... will not actually respond!
                if GeckoConstants.INCLUDE_DUMMY_SPA:
                    self.spas.append(
                        GeckoSpa(
                            self,
                            (
                                b"<HELLO>SPA90:1f:12:5c:d3:c0|Dummy Spa</HELLO>",
                                ("127.0.0.1", 10022),
                            ),
                        )
                    )
                logger.info(
                    "Found %d spas ... %s",
                    len(self.spas),
                    [(spa.name, spa.identifier) for spa in self.spas],
                )
                return
            self.retry_count += 1
            logger.info(
                "Didn't find any spas within %d seconds, retry %d",
                GeckoConstants.DISCOVERY_TIMEOUT_IN_SECONDS,
                self.retry_count,
            )
        logger.warning(
            "No spas found, check that you are on the same LAN as your in.touch2 device"
        )

    @property
    def version(self):
        """ Get the version of the library """
        return "v{0}.{1}.{2}".format(
            GeckoConstants.VERSION_MAJOR,
            GeckoConstants.VERSION_MINOR,
            GeckoConstants.VERSION_PATCH,
        )


if __name__ == "__main__":
    manager = GeckoManager("8e82a3e9-fc08-4952-96aa-292863e27dac")
