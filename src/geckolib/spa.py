""" GeckoSpa class """

import logging
import threading
import time
import importlib

from .const import GeckoConstants
from .config import GeckoConfig
from .driver import (
    GeckoUdpSocket,
    GeckoHelloProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoPartialStatusBlockProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoRFErrProtocolHandler,
    # Rest
    GeckoStructure,
)

logger = logging.getLogger(__name__)


class GeckoSpa(GeckoUdpSocket):
    """
    GeckoSpa class manages an instance of a spa, and is the main point of contact for
    control and monitoring. Uses the declarations found in pack/* to build
    an object that exposes the properties and capabilities of your spa. This class
    should only be used via a Facade which hides the implementation details"""

    def __init__(self, descriptor):
        super().__init__()

        self.descriptor = descriptor
        self.on_connected = None
        self.is_in_error = False

        self.add_receive_handler(GeckoPacketProtocolHandler(socket=self))
        self.add_receive_handler(
            GeckoPartialStatusBlockProtocolHandler(
                self, on_handled=self._on_partial_status_update
            )
        )
        self._last_ping = time.monotonic()
        self._ping_thread = threading.Thread(target=self._ping_thread_func, daemon=True)

        # Default values for properties
        self.channel = 0
        self.signal = 0

        self.intouch_version_en = ""
        self.intouch_version_co = ""

        self.config_version = 0
        self.log_version = 0
        self.pack_type = None
        self._is_connected = False
        self._connection_started = None
        self.pack = None
        self.version = None
        self.config_number = None
        self.struct = GeckoStructure(self._on_set_value)

        self.new_pack_class = None
        self.new_log_class = None
        self.new_config_class = None

    def complete(self):
        """Complete the use of this spa class"""
        super().close()
        self._ping_thread.join()

    @property
    def accessors(self):
        return self.struct.accessors

    def _on_partial_status_update(self, handler, sender):
        for change in handler.changes:
            self.struct.replace_status_block_segment(change[0], change[1])
        else:
            handler.changes.clear()

    def _on_set_value(self, pos, length, newvalue):
        # We issue a pack command to acheive this ...
        self.add_receive_handler(GeckoPackCommandProtocolHandler())
        self.queue_send(
            GeckoPackCommandProtocolHandler.set_value(
                self.get_and_increment_sequence_counter(False),
                self.pack_type,
                self.config_version,
                self.log_version,
                pos,
                length,
                newvalue,
                parms=self.sendparms,
            ),
            self.sendparms,
        )

    def _on_config_received(self, handler, sender):

        # Stash the config and log structure declarations
        self.config_version = handler.config_version
        self.log_version = handler.log_version

        plateform_key = handler.plateform_key.lower()
        pack_module_name = f"geckolib.driver.packs.{plateform_key}"
        try:
            GeckoPack = importlib.import_module(pack_module_name).GeckoPack
            self.new_pack_class = GeckoPack(self.struct)
            self.pack_type = self.new_pack_class.type
        except ModuleNotFoundError:
            self.is_in_error = True
            raise Exception(
                GeckoConstants.EXCEPTION_MESSAGE_NO_SPA_PACK.format(
                    handler.plateform_key
                )
            )

        config_module_name = (
            f"geckolib.driver.packs.{plateform_key}-cfg-{self.config_version}"
        )
        try:
            GeckoConfigStruct = importlib.import_module(
                config_module_name
            ).GeckoConfigStruct
            self.new_config_class = GeckoConfigStruct(self.struct)
        except ModuleNotFoundError:
            self.is_in_error = True
            raise Exception(
                f"Cannot find GeckoConfigStruct module for {handler.plateform_key} v{self.config_version}"
            )

        log_module_name = (
            f"geckolib.driver.packs.{plateform_key}-log-{self.log_version}"
        )
        try:
            GeckoLogStruct = importlib.import_module(log_module_name).GeckoLogStruct
            self.new_log_class = GeckoLogStruct(self.struct)
        except ModuleNotFoundError:
            self.is_in_error = True
            raise Exception(
                f"Cannot find GeckoLogStruct module for {handler.plateform_key} v{self.log_version}"
            )

        logger.debug(
            "Got spa configuration Type %s - CFG %s/LOG %s, now ask for initial "
            "status block",
            self.pack_type,
            self.config_version,
            self.log_version,
        )

        self.struct.retry_request(
            self,
            GeckoStatusBlockProtocolHandler.full_request(
                self.get_and_increment_sequence_counter(False), parms=sender
            ),
            sender,
        )

    def _on_channel_received(self, handler, sender):
        self.channel = handler.channel
        self.signal = handler.signal_strength
        logger.debug("Got channel %s/%s, now get config", self.channel, self.signal)
        config_file_handler = GeckoConfigFileProtocolHandler.request(
            self.get_and_increment_sequence_counter(False),
            parms=sender,
            on_handled=self._on_config_received,
        )
        self.add_receive_handler(config_file_handler)
        self.queue_send(config_file_handler, sender)

    def _on_version_received(self, handler, sender):
        self.intouch_version_en = "{0} v{1}.{2}".format(
            handler.en_build, handler.en_major, handler.en_minor
        )
        self.intouch_version_co = "{0} v{1}.{2}".format(
            handler.co_build, handler.co_major, handler.co_minor
        )
        logger.debug(
            "Got software version %s/%s, now get channel",
            self.intouch_version_en,
            self.intouch_version_co,
        )
        get_channel_handler = GeckoGetChannelProtocolHandler.request(
            self.get_and_increment_sequence_counter(False),
            parms=sender,
            on_handled=self._on_channel_received,
        )
        self.add_receive_handler(get_channel_handler)
        self.queue_send(
            get_channel_handler,
            sender,
        )

    @property
    def revision(self):
        """Get the revision of the spa pack structure used to generate the pack modules"""
        return self.new_pack_class.revision

    @property
    def sendparms(self):
        return (
            self.descriptor.destination[0],
            self.descriptor.destination[1],
            self.descriptor.identifier,
            self.descriptor.client_identifier,
        )

    def _on_ping_response(self, handler, sender):
        self._last_ping = time.monotonic()

    def start_connect(self):
        """Connect to the in.touch2 module"""
        self._connection_started = time.monotonic()
        # Identify self to the intouch module
        self.open()
        self.queue_send(
            GeckoHelloProtocolHandler.client(self.descriptor.client_identifier),
            self.descriptor.destination,
        )
        self._ping_handler = GeckoPingProtocolHandler.request(
            parms=self.sendparms, on_handled=self._on_ping_response
        )
        self.add_receive_handler(self._ping_handler)
        self._ping_thread.start()
        # Get the intouch version
        logger.info("Starting spa connection handshake...")
        self.add_receive_handler(GeckoRFErrProtocolHandler())
        version_handler = GeckoVersionProtocolHandler.request(
            self.get_and_increment_sequence_counter(False),
            parms=self.sendparms,
            on_handled=self._on_version_received,
        )
        self.add_receive_handler(version_handler)
        self.queue_send(version_handler, self.sendparms)
        return self

    def _loop_func(self):
        if self._is_connected:
            return
        if self.isopen:
            if self.struct.had_at_least_one_block:
                self._final_connect()

    def _final_connect(self):
        logger.debug("Connected, build accessors")
        if self.new_config_class is None or self.new_log_class is None:
            self.is_in_error = True
            raise AttributeError("Config or Log class is None")
        self.struct.build_accessors(self.new_config_class, self.new_log_class)

        self.pack = self.accessors[GeckoConstants.KEY_PACK_TYPE].value
        self.version = "{0} v{1}.{2}".format(
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_ID].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REV].value,
            self.accessors[GeckoConstants.KEY_PACK_CONFIG_REL].value,
        )
        self.config_number = self.accessors[GeckoConstants.KEY_CONFIG_NUMBER].value
        self._is_connected = True
        if self.on_connected is not None:
            self.on_connected(self)
        logger.info("Spa is now connected")

    def _ping_thread_func(self):
        """Ping thread function"""
        logger.info("Ping thread started, %r", self.isopen)
        while self.isopen:
            self.queue_send(self._ping_handler, self.sendparms)
            self.refresh()
            self.wait(GeckoConfig.PING_FREQUENCY_IN_SECONDS)
            if (
                time.monotonic() - self._last_ping
                > GeckoConfig.PING_DEVICE_NOT_RESPONDING_TIMEOUT_IN_SECONDS
            ):
                logger.warning(
                    # TODO
                    "TODO: Spa is not responding to pings, need to reconnect..."
                )
        logger.info("Ping thread finished")

    def get_buttons(self):
        """Get a list of buttons that can be pressed"""
        return [button[0] for button in GeckoConstants.BUTTONS]

    @property
    def is_connected(self):
        if self._is_connected:
            return True
        if (
            time.monotonic() - self._connection_started
            > GeckoConstants.CONNECTION_TIMEOUT_IN_SECONDS
        ):
            self.is_in_error = True
            raise RuntimeError("Spa took too long to connect ...")
        return False

    def refresh(self):
        """Refresh the live spa data block"""
        if not self.is_connected:
            logger.debug("Can't refresh as we're not connected yet")
            return
        self.struct.retry_request(
            self,
            GeckoStatusBlockProtocolHandler.request(
                self.get_and_increment_sequence_counter(False),
                self.new_log_class.begin,
                self.new_log_class.end,
                parms=self.sendparms,
            ),
            self.sendparms,
        )

    def press(self, keypad):
        """Simulate a button press"""
        self.add_receive_handler(GeckoPackCommandProtocolHandler())
        self.queue_send(
            GeckoPackCommandProtocolHandler.keypress(
                self.get_and_increment_sequence_counter(True),
                self.pack_type,
                keypad,
                parms=self.sendparms,
            ),
            self.sendparms,
        )
