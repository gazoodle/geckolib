""" GeckoComms - Implement base communication class """

import socket
import re
import logging
import threading

from ..const import GeckoConstants

logger = logging.getLogger(__name__)


class GeckoComms:
    """ Communicate with a Gecko in.touch2 module """

    def __init__(self, ipaddress=None, conns=None):
        self._socket = None
        self._ipaddress = ipaddress
        self._port = GeckoConstants.INTOUCH2_PORT
        self._conns = ""
        if conns is not None:
            self._conns = conns
        self._sequence_number = 0

        self._exit_event = None
        self._receive_thread = None

        self._handlers = []

    def __enter__(self):
        self._socket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
        )
        self._socket.settimeout(1)
        return self

    def __exit__(self, *args):
        if self._receive_thread:
            self._exit_event.set()
            self._receive_thread.join()
        if self._socket:
            self._socket.close()
            self._socket = None

    def start(self):
        """ Start the use of this comms object if not used in a `with` statement """
        self.__enter__()

    def complete(self):
        """ Complete the use of this comms object if not used in a `with` statement """
        self.__exit__()

    def set_broadcast(self):
        """ Convert the socket to a broadcast one """
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def start_receiving(self):
        """ Start the receiving thread, dispatching responses to the handlers """
        self._exit_event = threading.Event()
        self._receive_thread = threading.Thread(
            target=self._receive_thread_func, daemon=True
        )
        self._receive_thread.start()

    def send_message(self, message, destination=None):
        """ Send the message to the destination address and port """
        if destination is None:
            destination = self._ipaddress
        logger.debug(
            "Send message %s to %s",
            message.encode(GeckoConstants.MESSAGE_ENCODING),
            (destination, self._port),
        )
        self._socket.sendto(
            message.encode(GeckoConstants.MESSAGE_ENCODING), (destination, self._port)
        )

    def receive_answer(self):
        """ Receive an answer from the other end """
        data, remote = self._socket.recvfrom(GeckoConstants.MAX_PACKET_SIZE)
        logger.debug("Receive answer %s from %s", data, remote)
        return (data, remote)

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
        if parms is not None:
            cmd += parms
        return self.assemble_packet(cmd)

    @classmethod
    def extract_data_using_regex(cls, message, data):
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

    def add_handler(self, handler):
        """ Add a handler to the handler list """
        self._handlers.append(handler)

    def remove_handler(self, handler):
        """ Remove a handler from the handler list """
        self._handlers.remove(handler)

    def _clean_handlers(self):
        handlers_to_remove = [
            handler for handler in self._handlers if handler.check_timeout(self)
        ]
        self._handlers = [
            handler for handler in self._handlers if handler not in handlers_to_remove
        ]

    @property
    def isalive(self):
        """ Check to see if the exit event has been set """
        return not self._exit_event.is_set()

    def wait(self, timeout):
        """ Wait for a timeout """
        self._exit_event.wait(timeout)

    def _receive_thread_func(self):
        logger.info("Receive thread started")
        while self.isalive:
            try:
                self._handle_response(
                    self.extract_data_using_regex(
                        GeckoConstants.MESSAGE_PART_DATAS, self.receive_answer()[0]
                    )
                )
            except socket.timeout:
                continue
            except Exception:  # pylint: disable=broad-except
                logger.exception("Exception in receive thread func, aborting")
                self._exit_event.set()
            self._clean_handlers()
        logger.info("Receive thread finished")

    def _handle_response(self, response):
        # Iterate over the handlers to see if any are interested in this response ...
        for handler in self._handlers:
            if handler.handle_response_if_matched(self, response):
                return
        # We sometimes get extraneous PACKS response when another client has issued
        # the SPACK command ... don't fret about it!
        # if response.startswith(GeckoConstants.REQUEST_AND_RESPONSE_PACK_COMMAND[1]):
        #    return
        logger.warning("Unhandled response %s (%d)", response, len(response))
