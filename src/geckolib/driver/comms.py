""" GeckoComms - Implement base communication class """

import socket
import re
import logging
import threading

from ..const import GeckoConstants

logger = logging.getLogger(__name__)


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
