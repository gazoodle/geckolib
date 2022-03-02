#!/usr/bin/python3
"""
    Diag tool for geckolib
"""

import sys
import logging
from context import (
    GeckoUdpSocket,
    GeckoHelloProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoPacketProtocolHandler,
)

STATIC_IP = None
SPA_ID = None
SPA_NAME = None
SPA_DESTINATION = None
CLIENT_IDENTIFIER_1 = "IOSE31808F4-0CAC-462B-ADE6-55EE716DAD6E"
PING_DONE = False

_LOGGER = logging.getLogger(__name__)


def _on_discovered(handler, socket, sender):
    _LOGGER.info(f"_on_discovered: {handler}, {socket}, {sender}")
    global SPA_ID, SPA_NAME, SPA_DESTINATION
    SPA_ID = handler.spa_identifier
    SPA_NAME = handler.spa_name
    SPA_DESTINATION = sender


def _on_ping(handler, socket, sender):
    _LOGGER.info(f"_on_ping: {handler}, {socket}, {sender}")
    global PING_DONE
    PING_DONE = True


def comms_diag(arg):
    _LOGGER.info("Start comms diag with %s", arg)
    if len(arg) == 1:
        global STATIC_IP
        STATIC_IP = arg[0]

    _LOGGER.info("Discovery process started, create socket")
    _socket = GeckoUdpSocket()
    _LOGGER.debug("UDP Socket created, open it")
    _socket.open()
    _LOGGER.debug("Socket opened, set broadcast")
    _socket.enable_broadcast()
    _LOGGER.debug("Broadcast enabled, add hello handler")
    _socket.add_receive_handler(
        GeckoHelloProtocolHandler.broadcast(on_handled=_on_discovered)
    )
    _LOGGER.debug("Hello handler added, queue a broadcast")

    for idx in range(3):
        _socket.queue_send(
            GeckoHelloProtocolHandler.broadcast(),
            GeckoHelloProtocolHandler.broadcast_address(static_ip=STATIC_IP),
        )
        _socket.wait(1)
        if SPA_ID is not None:
            break

    if SPA_ID is None:
        _LOGGER.error("Cannot find any spas on this network")
        return

    _LOGGER.info(
        f"Found spa : {SPA_NAME} ({SPA_ID}) at {SPA_DESTINATION}, try to start connection"
    )

    _socket.add_receive_handler(GeckoPacketProtocolHandler())

    client_id = CLIENT_IDENTIFIER_1.encode("Latin1")
    # Do 5 of these to make sure the in.touch2 module hears us
    for idx in range(5):
        _socket.queue_send(
            GeckoHelloProtocolHandler.client(client_id),
            SPA_DESTINATION,
        )

    # Install ping handler
    _LOGGER.debug("Connection started, install ping handler")
    sendparms = (SPA_DESTINATION[0], SPA_DESTINATION[1], SPA_ID, client_id)
    ping_handler = GeckoPingProtocolHandler.request(
        parms=sendparms, on_handled=_on_ping
    )
    _socket.add_receive_handler(ping_handler)

    # Send ping command
    _LOGGER.debug("Handler installed, send ping")
    _socket.queue_send(ping_handler, SPA_DESTINATION)

    _LOGGER.debug("Ping sent, wait for a minute")
    for idx in range(60):
        if PING_DONE:
            break
        _socket.wait(1)

    if PING_DONE:
        _LOGGER.info("SUCCESS: Ping received back")
    else:
        _LOGGER.error("Failed to get PING response")


if __name__ == "__main__":
    stream_logger = logging.StreamHandler()
    stream_logger.setLevel(logging.DEBUG)
    stream_logger.setFormatter(
        logging.Formatter("%(asctime)s> %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(stream_logger)
    logging.getLogger().setLevel(logging.DEBUG)
    comms_diag(sys.argv[1:])
    _LOGGER.info("*** DIAG COMPLETE ***")
