#!/usr/bin/python3
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

#   HISTORY
#   =======
#
#   0.1.x       Oct 2020        -   Proof of concept code
#   0.2.x       Oct 2020        -   Initial development
#   0.3.x       Oct 2020        -   Created GitHub repo and readied for initial experimental release
#
#   Using Semantic versioning https://semver.org/

import logging
import os.path
import re
import socket
import struct
import sys
import threading
import time
import traceback
import xml.etree.ElementTree as ET

import urllib3

# Module logger, uses the library name (at this time it was geckolib) and it is silent unless required ...
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

###################################################################################################
class gecko_constants:
    '''
        gecko_constants is a literal class so that we can program in a mostly DRY fashion,
        for example a filename or url would be present as would values that could be changed
        and might be difficult to discover inline, but some constants that form part of a functions
        documented behaviour might not be here, e.g. 'rw' as a parameter to open()
    '''
    version_major = 0
    version_minor = 3
    version_patch = 7

    include_dummy_spa = False
    intouch2_port = 10022
    max_packet_size = 8192
    discovery_timeout_in_seconds = 4
    discovery_retry_count_to_find_any_spa = 3
    ping_timeout_in_seconds = 4

    broadcast_address = '255.255.255.255'
    message_encoding = 'utf-8'
    format_client_identifier = 'IOS{0}'

    spa_pack_struct_file = "SpaPackStruct.xml"
    spa_pack_struct_url = "http://intouch.geckoal.com/gecko/prod/SpaPackStruct.xml"
    # XPaths and attributes for SpaPackStruct
    spa_pack_revision_xpath = "./SpaPackStruct/FileRevision"
    spa_pack_revision_attrib = 'Number'
    spa_pack_plateform_xpath = './Plateform'
    spa_pack_name_attrib = 'Name'
    spa_pack_config_xpath = "./ConfigStructures/ConfigStructure[@LibRev='{0}']"
    spa_pack_log_xpath = "./LogStructures/LogStructure[@LibRev='{0}']"
    spa_pack_struct_pos_attrib = 'Pos'
    spa_pack_struct_type_attrib = 'Type'
    spa_pack_struct_bitpos_attrib = 'BitPos'
    spa_pack_struct_items_attrib = 'Items'
    spa_pack_struct_word_type = 'Word'
    spa_pack_struct_time_type = 'Time'
    spa_pack_struct_maxitems_attrib = 'MaxItems'
    spa_pack_struct_bool_type = 'Bool'
    spa_pack_struct_enum_type = 'Enum'
    spa_pack_struct_pos_elements_xpath = './/*[@Pos]'
    spa_pack_struct_word_type_elements_xpath = './/*[@Type="Word"]'
    spa_pack_struct_begin_attrib = 'Begin'
    spa_pack_struct_end_attrib = 'End'
    spa_pack_struct_read_write_attrib = 'RW'
    # Accessor keys for SpaPackStruct
    key_pack_type = 'PackType'
    key_pack_config_id = 'PackConfID'
    key_pack_config_rev = 'PackConfRev'
    key_pack_config_rel = 'PackConfRel'
    key_config_number = 'ConfigNumber'
    key_temp_units = 'TempUnits'
    key_rh_water_temp = 'RhWaterTemp'
    key_setpoint_g = 'SetpointG'
    key_real_setpoint_g = 'RealSetPointG'
    key_displayed_temp_g = 'DisplayedTempG'
    key_user_demand_light = 'UdLi'
    key_pump_1 = "P1"
    key_pump_2 = "P2"
    key_pump_3 = "P3"
    key_pump_4 = "P4"
    key_pump_5 = "P5"
    key_blower = "BL"

    exception_message_no_spa_pack = "Cannot find spa pack for {0}"
    exception_message_not_writable = "Cannot set value for {0}. This status array item doesn't allow writing"

    # Message pseudo xml parts
    message_hello = '<HELLO>{0}</HELLO>'
    message_part_packet = '<PACKT>{0}</PACKT>'
    message_part_datas = '<DATAS>{0}</DATAS>'
    message_part_src_connection_name = '<SRCCN>{0}</SRCCN>'
    message_part_dest_connection_name = '<DESCN>{0}</DESCN>'

    # Command & response pseudo xml content
    request_and_response_ping = ('APING', b'APING')
    request_and_response_get_version = ('AVERS', b'SVERS')
    request_and_response_get_channel = ('CURCH', b'CHCUR')
    request_and_response_get_config = ('SFILE', b'FILES')
    request_and_response_get_status = ('STATU', b'STATV')
    request_and_response_partial_status = ('STATQ', b'STATP')
    request_and_response_pack_command = ('SPACK', b'PACKS')

    # Pack commands
    pack_command_key_press = 57
    pack_command_set_value = 70

    # Gecko keypad constants
    keypad_pump_1 = 1
    keypad_pump_2 = 2
    keypad_pump_3 = 3
    keypad_pump_4 = 4
    keypad_pump_5 = 5
    keypad_blower = 6
    keypad_light = 16
    keypad_up = 21
    keypad_down = 22

    # Pack outputs
    pack_outputs_xpaths = [ './HCOutputConfig/*[@Type="Enum"]', 
        './LCOutputConfig/*[@Type="Enum"]', 
        './LVOutputConfig/*[@Type="Enum"]' ]
    spa_pack_device_xpath = "./DeviceStatus/*"
    spa_pack_user_demands = "./UserDemands/*"

    device_class_pump = "PUMP"
    device_class_blower = "BLOWER"
    device_class_light = "LIGHT"

    # Spa devices and accessories, dictionary of tuples
    #   ID: Description, keypad, structure key, class
    devices = {
        "P1": ("Pump 1", keypad_pump_1, key_pump_1, device_class_pump),
        "P2": ("Pump 2", keypad_pump_2, key_pump_2, device_class_pump),
        "P3": ("Pump 3", keypad_pump_3, key_pump_3, device_class_pump),
        "P4": ("Pump 4", keypad_pump_4, key_pump_4, device_class_pump),
        "P5": ("Pump 5", keypad_pump_5, key_pump_5, device_class_pump),
        "BL": ("Blower", keypad_blower, key_blower, device_class_blower),
        "LI": ("Lights", keypad_light, key_user_demand_light, device_class_light)
    }

    # Buttons, list of tuples
    #   ID, Description, KeyPad ID
    buttons = [
        ("P1", "Pump 1 Button", keypad_pump_1),
        ("P2", "Pump 2 Button", keypad_pump_2),
        ("P3", "Pump 3 Button", keypad_pump_3),
        ("P4", "Pump 4 Button", keypad_pump_4),
        ("P5", "Pump 5 Button", keypad_pump_5),
        ("BLOWER", "Blower Button", keypad_blower),
        ("LIGHT", "Lights Button", keypad_light),
        ("UP", "Up Button", keypad_up),
        ("DOWN", "Down Button", keypad_down)

    ]

    regex_dot_star = '(.*)'

###################################################################################################
class gecko_response:
    '''
        gecko_response: base class for handling the UDP conversation with the intouch module
    '''

    def __init__(self, request_and_response, handler=None, timeout=5, timeout_handler=None):
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
        if self.timeout == 0:
            return False
        if time.monotonic() - self.init_time > self.timeout:
            self.retry_count += 1
            logger.warning("Handler for %s timed out, retry %d" % ( self.request_and_response[0], self.retry_count ))
            if self.retry_count < 5:
                self.init_time = time.monotonic()
                self.send_request(spa)
                return False
            logger.warning("Handler for %s timed out, aborted" % ( self.request_and_response[0] ))
            if not self.timeout_handler is None:
                self.timeout_handler()
            return True
        return False

    def handle_response_if_matched(self, spa, response):
        if response.startswith(self.request_and_response[1]):
            if self.handler(spa, response):
                spa.remove_handler(self)
            return True
        return False

    def send_request(self, spa):
        spa.send_message(spa.build_command(self.request_and_response[0], self.has_sequence, self.parms))

    def unpack(self, format, length, response ):
        cmd_len = 0
        if response.startswith(self.request_and_response[1]):
            cmd_len = len(self.request_and_response[1])
        return struct.unpack(format, response[cmd_len:cmd_len+length]) + (response[cmd_len+length:],)

    def default_handler(self, spa, response):
        return True

###################################################################################################
class gecko_ping(gecko_response):

    def __init__(self):
        super().__init__(gecko_constants.request_and_response_ping, self.ping_handler, gecko_constants.ping_timeout_in_seconds)
        self.has_sequence = False

    def ping_handler(self, spa, response):
        logger.debug("Ping response received")
        return True

###################################################################################################
class gecko_partial_status(gecko_response):
    
    def __init__(self):
        super().__init__(gecko_constants.request_and_response_partial_status, self.partial_status_handler, 0)
        
    def partial_status_handler(self, spa, response):
        self.send_request(spa)
        change_count, response = self.unpack(">B", 1, response)
        #TODO: Must be a better way to do this with list comprehensions!
        for i in range(change_count):
            pos, b1, b2, response = self.unpack(">HBB", 4, response)
            ba = bytearray()
            ba.append(b1)
            ba.append(b2)
            spa.replace_status_block_segment( pos, ba )

        # Never complete so it will remain in the handler collection
        return False

###################################################################################################
class gecko_get_software_version(gecko_response):

    def __init__(self):
        super().__init__(gecko_constants.request_and_response_get_version, self.version_handler )

    def version_handler(self, spa, response):
        EN_build, EN_major, EN_minor, CO_build, CO_major, CO_minor, response = self.unpack(">HBBHBB", 8, response)
        spa.intouch_version_EN = "{0} v{1}.{2}".format(EN_build, EN_major, EN_minor)
        spa.intouch_version_CO = "{0} v{1}.{2}".format(CO_build, CO_major, CO_minor)
        logger.debug("Got software version %s/%s, now get channel" % (spa.intouch_version_EN, spa.intouch_version_CO ))
        spa.send_request(gecko_get_channel())
        return True

###################################################################################################
class gecko_get_channel(gecko_response):

    def __init__(self):
        super().__init__(gecko_constants.request_and_response_get_channel, self.channel_handler )

    def channel_handler(self, spa, response):
        spa.channel, spa.signal, response = self.unpack('>BB', 2, response)
        logger.debug("Got channel %s/%s, get config" % (spa.channel, spa.signal))
        spa.send_request(gecko_get_config())
        return True

###################################################################################################
class gecko_pack_command(gecko_response):

    def __init__(self, packtype, values):
        super().__init__(gecko_constants.request_and_response_pack_command)
        self.parms = "".join(chr(item) for item in [packtype, len(values)] + values)
        logger.debug("Pack cmd %s" % self.parms.encode(gecko_constants.message_encoding))

###################################################################################################
class gecko_get_config(gecko_response):

    def __init__(self):
        super().__init__(gecko_constants.request_and_response_get_config, self.config_handler )

    def config_handler(self, spa, response):
        # Treat the files as if they were indices into the SpaPackStruct.xml file
        config = response[6:].decode(gecko_constants.message_encoding).replace('.xml', '').split(',')
        # Split the string around the underscore
        gecko_pack_config = config[0].split('_')
        gecko_pack_log = config[1].split('_')

        # XML is case-sensitive, but the platform from the config isn't formed the same, so we manually
        # search the Plateform nodes to find the one we're interested in
        for plateform in spa.manager.spa_pack_struct.findall(gecko_constants.spa_pack_plateform_xpath):
            if plateform.attrib[gecko_constants.spa_pack_name_attrib].lower() == gecko_pack_config[0].lower():
                spa.gecko_pack_xml = plateform

        # We can't carry on without information on how the STATV data block is formed ...
        if spa.gecko_pack_xml is None:
            raise Exception(gecko_constants.exception_message_no_spa_pack.format(gecko_pack_config[0]))

        # Stash the config and log structure declarations
        spa.config_version = int(gecko_pack_config[1][1:])
        spa.config_xml = spa.gecko_pack_xml.find(gecko_constants.spa_pack_config_xpath.format(spa.config_version))
        spa.log_version = int(gecko_pack_log[1][1:])
        spa.log_xml = spa.gecko_pack_xml.find(gecko_constants.spa_pack_log_xpath.format(spa.log_version))
        spa.pack_type = int(spa.gecko_pack_xml.attrib[gecko_constants.spa_pack_struct_type_attrib])

        logger.debug("Got spa configuration Type %s - CFG %s/LOG %s, now ask for initial status block" % ( spa.pack_type, spa.config_version, spa.log_version ))

        # Grab a big chunk first time around
        spa.send_request(gecko_get_status(0, 1024))
        return True

###################################################################################################
class gecko_get_status(gecko_response):

    def __init__(self, start, length):
        self.offset = start
        self.length = length
        self.next_expected = 0
        self.received = 0
        super().__init__(gecko_constants.request_and_response_get_status, self.status_handler, 20 )
        self.parms = "{0:c}{1:c}{2:c}{3:c}".format(start//256, start%256, length//256, length%256 )

    def status_handler(self, spa, response):
        seq, nxt, ln, response = self.unpack('>BBB', 3, response )
        logger.debug("Status block segment # %d (then #%d) length %d, was expecting %d" % (seq, nxt, ln, self.next_expected))
        if not self.next_expected == seq:
            logger.warning("Out-of-sequence status block segment - ignored")
            if nxt == 0:
                logger.warning("Retry status block request")
                spa.send_request(gecko_get_status(self.offset, self.length))
        else:
            spa.replace_status_block_segment(self.offset + self.received, response[0:ln])
            self.received += ln
            self.next_expected = nxt
            # When we get the last partial segment, we can assume the spa is connected and we can report on status
            if nxt==0:
                spa.is_connected = True
        return nxt==0

###################################################################################################
class gecko_comms:

    def __init__(self, manager):
        # Create a UDP socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.settimeout(1)
        self.ipaddress = None
        self.port = gecko_constants.intouch2_port
        self.identifier = None
        self.srccn = None
        self.descn = None
        self.manager = manager
        self.sequence_number = 1

    def __del__(self):
        self.socket.close()

    def send_message(self, message, destination = None):
        if destination is None:
            destination = self.ipaddress
        logger.debug("Send message %s to %s" % ( message.encode(gecko_constants.message_encoding), ( destination, self.port )))
        self.socket.sendto( message.encode(gecko_constants.message_encoding), (destination, self.port))

    def receive_answer(self):
        data, remote = self.socket.recvfrom(gecko_constants.max_packet_size)
        logger.debug("Receive answer %s from %s" % ( data, remote ) )
        return (data, remote)

    def extract_data_using_regex(self, message, data):
        match = re.search(bytes(message.format(gecko_constants.regex_dot_star), gecko_constants.message_encoding), data, re.DOTALL)
        return match.group(1)

    def assemble_packet(self, data):
        return gecko_constants.message_part_packet.format( 
            "{0}{1}{2}".format(
                self.srccn,
                self.descn,
                gecko_constants.message_part_datas.format(data)
            )
        )

    def build_command(self, cmd, has_sequence=True, parms=None):
        if has_sequence:
            self.sequence_number += 1
            cmd += chr(self.sequence_number)
        if not parms is None:
            cmd += parms
        return self.assemble_packet(cmd)

###################################################################################################
class gecko_struct_accessor:
    def __init__(self, spa, element):
        self.spa = spa
        self.tag = element.tag
        self.pos = int(element.attrib[gecko_constants.spa_pack_struct_pos_attrib])
        self.type = element.attrib[gecko_constants.spa_pack_struct_type_attrib]
        self.bitpos = None
        if gecko_constants.spa_pack_struct_bitpos_attrib in element.attrib:
            self.bitpos = int(element.attrib[gecko_constants.spa_pack_struct_bitpos_attrib])
            self.bitmask = 1
        if gecko_constants.spa_pack_struct_items_attrib in element.attrib:
            self.items = element.attrib[gecko_constants.spa_pack_struct_items_attrib].split('|')
        self.length = 1
        self.format = ">B"
        if self.type == gecko_constants.spa_pack_struct_word_type or self.type == gecko_constants.spa_pack_struct_time_type:
            self.length = 2
            self.format = ">H"
        if gecko_constants.spa_pack_struct_maxitems_attrib in element.attrib:
            self.maxitems = int(element.attrib[gecko_constants.spa_pack_struct_maxitems_attrib])
            if self.maxitems > 8:
                self.bitmask = 15
            elif self.maxitems > 4:
                self.bitmask = 7
            elif self.maxitems > 2:
                self.bitmask = 3
        self.read_write = None
        if gecko_constants.spa_pack_struct_read_write_attrib in element.attrib:
            self.read_write = element.attrib[gecko_constants.spa_pack_struct_read_write_attrib]

    @property
    def value(self):
        data = struct.unpack(self.format, self.spa.status_block[self.pos:self.pos+self.length])[0]
        logger.debug("Accessor %s @ %s, %s raw data = %x" % (self.tag, self.pos, self.type, data))
        if not self.bitpos is None:
            data = (data >> self.bitpos) & self.bitmask
            logger.debug("BitPos %s accessor %s adjusted data = %x" % ((self.bitpos, self.bitmask), self.tag, data))
        if self.type == gecko_constants.spa_pack_struct_bool_type:
            data = data == 1
            logger.debug("Bool accessor %s adjusted data = %s" % (self.tag, data))
        elif self.type == gecko_constants.spa_pack_struct_enum_type:
            data = self.items[data]
            logger.debug("Enum accessor %s adjusted data = %s" % (self.tag, data))
        return data

    @value.setter
    def value(self, newvalue):
        if self.read_write is None:
            raise Exception(gecko_constants.exception_message_not_writable.format(self.tag))

        if self.type == gecko_constants.spa_pack_struct_bool_type:
            logger.debug("Bool accessor %s adjusted from %s" % (self.tag, newvalue))
            newvalue = newvalue.lower() == "true"
        elif self.type == gecko_constants.spa_pack_struct_enum_type:
            logger.debug("Enum accessor %s adjusted from %s" % (self.tag, newvalue))
            newvalue = self.items.index(newvalue)

        # If it is a bitpos, then mask it with the existing value
        existing = struct.unpack(self.format, self.spa.status_block[self.pos:self.pos+self.length])[0]
        if not self.bitpos is None:
            logger.debug("Bitpos %s accessor %s adjusted from %s" % ((self.bitpos, self.bitmask), self.tag, newvalue))
            newvalue = (existing & ~(self.bitmask << self.bitpos)) | ((newvalue & self.bitmask) << self.bitpos)

        if self.length == 1:
            newvalue = [ int(newvalue) ]
        elif self.length == 2:
            newvalue = [ int(newvalue)//256, int(newvalue)%256 ]

        logger.debug("Accessor %s @ %s, %s setting value to %s, existing value was %s" % (self.tag, self.pos, self.type, newvalue, existing))

        # We issue a pack command to acheive this ...
        self.spa.send_request(gecko_pack_command(self.spa.pack_type, [gecko_constants.pack_command_set_value, self.spa.config_version, self.spa.log_version, self.pos//256, self.pos%256 ] + newvalue))


###################################################################################################
class gecko_temperature_decorator:

    def __init__(self, spa, accessor):
        self.spa = spa
        self.accessor = accessor

    @property
    def value(self):
        # Temp is in farenheight tenths, offset from freezing point
        temp = self.accessor.value
        units = self.spa.accessors[gecko_constants.key_temp_units].value
        if units == "C":
            temp = temp / 18.0
        else:
            temp = (temp + 320) / 10.0
        return temp
        #return "{0:.1f}°{1}".format(temp, units)

    @value.setter
    def value(self, temp):
        units = self.spa.accessors[gecko_constants.key_temp_units].value
        if units == "C":
            temp = float(temp) * 18.0
        else:
            temp = (float(temp) * 10.0) - 320
        self.accessor.value = int(temp)

###################################################################################################
class gecko_spa(gecko_comms):
    '''
        gecko_spa class manages an instance of a spa, and is the main point of contact for control 
        and monitoring. Uses the declarations found in SpaPackStruct.xml to build an object that
        exposes the properties and capabilities of your spa
    '''
    def __init__(self, manager, response):
        super().__init__(manager)
        data = self.extract_data_using_regex(gecko_constants.message_hello, response[0]).decode(gecko_constants.message_encoding)
        self.client_identifier = manager.client_identifier
        self.identifier, self.name = data.split('|')
        self.ipaddress, self.port = response[1]
        self.srccn = gecko_constants.message_part_src_connection_name.format(self.client_identifier)
        self.descn = gecko_constants.message_part_dest_connection_name.format(self.identifier)
        self.handlers = []
        self.add_handler( gecko_partial_status() )

        self.exit = threading.Event()
        self.receive_thread = threading.Thread(target=self.receive_thread_func)
        self.ping_thread = threading.Thread(target=self.ping_thread_func)
        self.receive_thread.start()

        # Default values for properties
        self.channel = 0
        self.signal = 0

        self.intouch_version_EN = ""
        self.intouch_version_CO = ""

        self.gecko_pack_xml = None
        self.config_version = 0
        self.config_xml = None
        self.log_version = 0
        self.log_xml = None
        self.pack_type = None

        # Inspection of the SpaPackStruct.xml shows that there are (currently) no configurations larger than this
        self.status_block = b'\x00' * 1024
        self.accessors = {}

    def __del__(self):
        super().__del__()
        self.receive_thread.join()
        self.ping_thread.join()

    def send_request(self, request):
        self.add_handler(request)
        request.send_request(self)

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)

    def replace_status_block_segment(self, offset, segment):
        segment_len = len(segment)
        prefix = self.status_block[0:offset]
        suffix = self.status_block[offset+segment_len:]
        self.status_block = prefix + segment + suffix

    def connect(self):
        # Identify self to the intouch module
        self.send_message(gecko_constants.message_hello.format(self.client_identifier))
        self.ping_thread.start()
        # Get the intouch version
        logger.info("Starting spa connection handshake...")
        self.is_connected = False
        self.send_request(gecko_get_software_version())
        # Wait for connection sequence to complete
        while not self.is_connected:
            pass
        self.build_accessors()
        self.pack = self.accessors[gecko_constants.key_pack_type].value
        self.version = "{0} v{1}.{2}".format(self.accessors[gecko_constants.key_pack_config_id].value, self.accessors[gecko_constants.key_pack_config_rev].value, self.accessors[gecko_constants.key_pack_config_rel].value)
        self.config_number = self.accessors[gecko_constants.key_config_number].value
        logger.info("Spa is connected")

    def disconnect(self):
        self.exit.set()

    def ping_thread_func(self):
        while not self.exit.is_set():
            self.send_request(gecko_ping())
            self.exit.wait(5)

    def clean_handlers(self):
        handlers_to_remove = [ handler for handler in self.handlers if handler.check_timeout(self) ]
        self.handlers = [handler for handler in self.handlers if handler not in handlers_to_remove]

    def receive_thread_func(self):
        while not self.exit.is_set():
            try:
                self.handle_response(self.extract_data_using_regex(gecko_constants.message_part_datas, self.receive_answer()[0]))
            except socket.timeout:
                pass
            except:
                (ex,ty,tb) = sys.exc_info()
                print("{0}: {1}".format(ex,ty))
                traceback.print_tb(tb)
            self.clean_handlers()

    def handle_response(self, response):
        # Iterate over the handlers to see if any are interested in this response ...
        for handler in self.handlers:
            if handler.handle_response_if_matched(self, response):
                return
        # We sometimes get extraneous PACKS response when another client has issued the SPACK command ... don't fret about it!
        if response.startswith(gecko_constants.request_and_response_pack_command[1]):
            return
        logger.warning("Unhandled response %s (%d)" % (response, len(response)))

    def build_accessors(self):
        self.accessors = { element.tag: gecko_struct_accessor(self, element) for xml in [ self.config_xml, self.log_xml ] for element in xml.findall(gecko_constants.spa_pack_struct_pos_elements_xpath) }
        # Fix temperature accessors ...
        temp_keys = { element.tag for xml in [ self.config_xml, self.log_xml ] for element in xml.findall( gecko_constants.spa_pack_struct_word_type_elements_xpath ) if "temp" in element.tag.lower() or "setpoint" in element.tag.lower() }
        logger.debug("Temperature keys to decorate %s" % temp_keys)
        for key in temp_keys:
            self.accessors[key] = gecko_temperature_decorator(self, self.accessors[key])

    def get_buttons(self):
        # TODO: Use config to determine this ...
        return [button[0] for button in gecko_constants.buttons]

    def refresh(self):
        self.send_request(gecko_get_status(int(self.log_xml.attrib[gecko_constants.spa_pack_struct_begin_attrib]), int(self.log_xml.attrib[gecko_constants.spa_pack_struct_end_attrib])))

    def press(self, keypad):
        self.send_request(gecko_pack_command(self.pack_type, [gecko_constants.pack_command_key_press, keypad]))

###################################################################################################
class gecko_manager(gecko_comms):
    '''
        gecko_manager class manages the local spa collection and hosts the discovery process
    '''

    def __init__(self, client_uuid):
        super().__init__(self)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        if not os.path.exists(gecko_constants.spa_pack_struct_file):
            logger.info("SpaPackStruct.xml not found, downloading from the internet...")
            self.download()
        self.spa_pack_struct = ET.parse(gecko_constants.spa_pack_struct_file)
        self.spa_pack_struct_revision = self.spa_pack_struct.find(gecko_constants.spa_pack_revision_xpath).attrib[gecko_constants.spa_pack_revision_attrib]
        self.client_identifier = gecko_constants.format_client_identifier.format(client_uuid)
        logger.info("SpaPackStruct v%s" % (self.spa_pack_struct_revision ))
        logger.info("Client identifier %s" % self.client_identifier )

    def finish(self):
        '''
            Disconnect all the connected spas and release the background worker threads
        '''
        for spa in self.spas:
            spa.disconnect()

    def download(self):
        '''
            Download SpaPackStruct.xml from it's permanent home
        '''
        logger.info("Downloading SpaPackStruct.xml")
        http = urllib3.PoolManager()
        response = http.request('GET', gecko_constants.spa_pack_struct_url, preload_content=False)

        with open(gecko_constants.spa_pack_struct_file, 'wb') as out:
            while True:
                data = response.read(4096)
                if not data:
                    break
                out.write(data)

        response.release_conn()
        logger.info("SpaPackStruct.xml downloaded")

    def discover(self):
        '''
            Start the discovery process to locate any intouch2 capable Gecko modules on the local network.
        '''
        logger.info("Discovery process started")
        self.retry_count = 0
        while self.retry_count < gecko_constants.discovery_retry_count_to_find_any_spa:
            # Broadcast the discovery message to every client on the local LAN 
            self.send_message(gecko_constants.message_hello.format(1), gecko_constants.broadcast_address)
            self.spas = []
            # Wait to ensure we've heard from all the modules that responded within the discovery period
            now = time.monotonic()
            while time.monotonic() - now < gecko_constants.discovery_timeout_in_seconds:
                try:
                    self.spas.append(gecko_spa(self, self.receive_answer()))
                except socket.timeout:
                    break
            if len(self.spas) > 0:
                # Dummy spa to test multiple spas in client programs ... will not actually respond!
                if gecko_constants.include_dummy_spa:
                    self.spas.append(gecko_spa(self, (b'<HELLO>SPA90:1f:12:5c:d3:c0|Dummy Spa</HELLO>', ('127.0.0.1', 10022))))
                logger.info("Found %d spas ... %s" % ( len(self.spas), [(spa.name, spa.identifier) for spa in self.spas] ))
                return
            self.retry_count += 1
            logger.info("Didn't find any spas within %d seconds, retry %d" % ( gecko_constants.discovery_timeout_in_seconds, self.retry_count ))
        logger.warning("No spas found, check that you are on the same LAN as your in.touch2 device")

    @property
    def version(self):
        return "v{0}.{1}.{2}".format(gecko_constants.version_major, gecko_constants.version_minor, gecko_constants.version_patch)

#TODO: DocTest here please ...
if __name__ == "__main__":
    manager = gecko_manager("8e82a3e9-fc08-4952-96aa-292863e27dac")
