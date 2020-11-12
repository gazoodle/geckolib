""" GeckoSpa class """

import logging
import threading

from .driver import GeckoComms
from .const import GeckoConstants
from .driver import (
    GeckoTemperatureDecorator,
    GeckoGetSoftwareVersion,
    GeckoGetStatus,
    GeckoPackCommand,
    GeckoPartialStatus,
    GeckoPing,
    GeckoSpaPack
)
from .driver import GeckoStructAccessor
from .automation import GeckoFacade

logger = logging.getLogger(__name__)

##################################################################################################
class GeckoSpaDescriptor:
    """ A descriptor class for spas that have been discovered on the network """

    def __init__(self, client_identifier, response):
        self.client_identifier = client_identifier
        data = GeckoComms.extract_data_using_regex(
            GeckoConstants.MESSAGE_HELLO, response[0]
        ).decode(GeckoConstants.MESSAGE_ENCODING)
        self.identifier, self.name = data.split("|")
        self.ipaddress, self.port = response[1]

    def get_facade(self):
        """ Get an automation facade to interact with the spa described by this class """
        return GeckoFacade(GeckoSpa(self).connect())

##################################################################################################
class GeckoSpa(GeckoComms, GeckoSpaPack):
    """
    GeckoSpa class manages an instance of a spa, and is the main point of contact for control
    and monitoring. Uses the declarations found in SpaPackStruct.xml to build an object that
    exposes the properties and capabilities of your spa. This class should only be used via
    a Facade which hides the implementation details
    """

    def __init__(self, descriptor):
        super().__init__(descriptor.ipaddress, GeckoConstants.MESSAGE_PART_CONNECTION_NAMES.format(
            descriptor.client_identifier, descriptor.identifier
        ))
        GeckoSpaPack.__init__(self)
        self.descriptor = descriptor
        self.start()
        self.add_handler(GeckoPartialStatus())
        self.start_receiving()

        self._ping_thread = threading.Thread(target=self._ping_thread_func,daemon=True)

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

    def complete(self):
        """ Complete the use of this spa class """
        super().complete()
        self._ping_thread.join()

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
        self.send_message(GeckoConstants.MESSAGE_HELLO.format(self.descriptor.client_identifier))
        self._ping_thread.start()
        # Get the intouch version
        logger.info("Starting spa connection handshake...")
        self.is_connected = False
        self.send_request(GeckoGetSoftwareVersion())
        # Wait for connection sequence to complete
        while not self.is_connected:
            if not self.isalive:
                return
        self._build_accessors()
        self.pack = self.accessors[GeckoConstants.KEY_PACK_TYPE].value
        self.version = "{0} v{1}.{2}".format(
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_ID].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REV].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REL].value,
        )
        self.config_number = self.accessors[GeckoConstants.KEY_CONFIG_NUMBER].value
        logger.info("Spa is connected")
        return self

    def _ping_thread_func(self):
        """ Ping thread function """
        logger.info("Ping thread started")
        while self.isalive:
            self.send_request(GeckoPing())
            self.wait(GeckoConstants.PING_FREQUENCY_IN_SECONDS)
        logger.info("Ping thread finished")

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
