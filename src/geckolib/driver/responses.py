""" Requests and responses from in.touch2 module """

import struct
import time
import logging

from ..const import GeckoConstants

logger = logging.getLogger(__name__)

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
        self.aborted = False

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
            self.aborted = True
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
class GeckoGetActiveWatercare(GeckoResponse):
    """ Process the Get active watercare command """

    def __init__(self):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_GET_ACTIVE_WATERCARE,
            self.watercare_handler,
        )
        self.active_mode = None

    def watercare_handler(self, spa, response):
        """ Handle the get active watercare response """
        del spa
        self.active_mode = self.unpack(">B", 1, response)[0]
        logger.debug(
            "Got active watercare %d(%s)",
            self.active_mode,
            GeckoConstants.WATERCARE_MODE_STRING[self.active_mode],
        )
        return True


###################################################################################################
class GeckoSetActiveWatercare(GeckoResponse):
    """ Process the Set active watercare command """

    def __init__(self, new_mode):
        super().__init__(
            GeckoConstants.REQUEST_AND_RESPONSE_SET_ACTIVE_WATERCARE,
            self.watercare_handler,
        )
        self.parms = chr(new_mode)

    def watercare_handler(self, spa, response):
        """ Handle the set active watercare response """
        del self, spa, response
        return True


###################################################################################################
class GeckoPackCommand(GeckoResponse):
    """ Handle the pack command """

    def __init__(self, packtype, values):
        super().__init__(GeckoConstants.REQUEST_AND_RESPONSE_PACK_COMMAND)
        self.parms = "".join(chr(item) for item in [packtype, len(values)] + values)
        logger.debug(
            "Pack cmd %s(%d)",
            self.parms.encode(GeckoConstants.MESSAGE_ENCODING),
            len(self.parms),
        )


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
