""" GeckoSimulator class """

import logging
import readline
import os
import glob
import random

from .shared_command import GeckoCmd
from ..driver import (
    GeckoHelloProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    # GeckoPartialStatusBlockProtocolHandler,
    GeckoWatercareProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoStructure,
    GeckoUdpSocket,
)
from .snapshot import GeckoSnapshot
from .. import VERSION

_LOGGER = logging.getLogger(__name__)


class GeckoSimulator(GeckoCmd):
    """GeckoSimulator is a server application to aid with investigating
    Gecko protocol"""

    _STATUS_BLOCK_SEGMENT_SIZE = 39

    def __init__(self, first_commands=None):

        self._socket = GeckoUdpSocket()
        self._install_standard_handlers()
        self.structure = GeckoStructure(self._on_set_value)
        self.snapshot = None
        self._reliability = 1.0
        random.seed()

        super().__init__(first_commands)

        self.intro = (
            "Welcome to the Gecko simulator. Type help or ? to list commands.\n"
        )
        self.prompt = "(GeckoSim) "
        readline.set_completer_delims(" \r\n")

    def __exit__(self, *args):
        self._socket.close()
        self._socket = None

    def do_about(self, arg):
        """Display information about this client program and support library : about"""
        del arg
        print("")
        print(
            "GeckoSimulator: A python program using GeckoLib library to simulate Gecko"
            " enabled devices with in.touch2 communication modules"
        )
        print("Library version v{0}".format(VERSION))

    def do_start(self, args):
        """Start the configured simulator : start"""
        if self._socket.isopen:
            print("Simulator is already started")
            return
        self._socket.open()
        self._socket.enable_broadcast()
        self._socket.bind()

    def _complete_path(self, path):
        if os.path.isdir(path):
            return glob.glob(os.path.join(path, "*"))
        return glob.glob(path + "*")

    def do_parse(self, args):
        """Parse logfiles to extract snapshots to the ./snapshot directory. Will
        overwrite identically named snapshot files if present : parse <logfile>"""
        for snapshot in GeckoSnapshot.parse_log_file(args):
            snapshot.save("snapshots")
            print(f"Saved snapshot snapshots/{snapshot.filename}")

    def do_reliability(self, args):
        """Set simulator reliability factor. Reliability is a measure of how likely
        the simulator will respond to an incoming message. Reliability of 1.0 (default)
        means the simulator will always respond, whereas 0.0 means it will never
        respond. This does not take into account messages that actually don't get
        recieved : reliability <factor> where <factor> is a float between 0.0 and
        1.0."""
        if args == "":
            print(f"Current reliability is {self._reliability}")
            return
        self._reliability = min(1.0, max(0.0, float(args)))

    def complete_parse(self, text, line, start_idx, end_idx):
        return self._complete_path(text)

    def do_load(self, args):
        """Load a snapshot : load <snapshot>"""
        snapshots = GeckoSnapshot.parse_log_file(args)
        if len(snapshots) == 1:
            self.set_snapshot(snapshots[0])
            return
        print(
            f"{args} contains {len(snapshots)} snapshots. Please use the"
            f" `parse` command to break it apart"
        )

    def complete_load(self, text, line, start_idx, end_idx):
        return self._complete_path(text)

    def set_snapshot(self, snapshot):
        self.snapshot = snapshot
        self.structure.replace_status_block_segment(0, self.snapshot.bytes)

    def _should_ignore(self, handler, sender):
        should_ignore = random.random() > self._reliability
        if should_ignore:
            print(f"Unreliable simulator ignoring request for {handler} from {sender}")
        return should_ignore

    def _install_standard_handlers(self):
        """All simulators needs to have some basic functionality such
        as discovery, error handling et al"""
        self._hello_handler = GeckoHelloProtocolHandler.response(
            b"SPA01:02:03:04:05:06", "Udp Test Spa", on_handled=self._on_hello
        )

        self._socket.add_receive_handler(self._hello_handler)
        self._socket.add_receive_handler(GeckoPacketProtocolHandler())
        self._socket.add_receive_handler(
            GeckoPingProtocolHandler(on_handled=self._on_ping)
        ),
        self._socket.add_receive_handler(
            GeckoVersionProtocolHandler(on_handled=self._on_version)
        )
        self._socket.add_receive_handler(
            GeckoGetChannelProtocolHandler(on_handled=self._on_get_channel)
        )
        self._socket.add_receive_handler(
            GeckoConfigFileProtocolHandler(on_handled=self._on_config_file)
        )
        self._socket.add_receive_handler(
            GeckoStatusBlockProtocolHandler(on_handled=self._on_status_block)
        )
        self._socket.add_receive_handler(
            GeckoWatercareProtocolHandler(on_handled=self._on_watercare)
        )
        self._socket.add_receive_handler(
            GeckoUpdateFirmwareProtocolHandler(on_handled=self._on_update_firmware)
        )
        self._socket.add_receive_handler(
            GeckoRemindersProtocolHandler(on_handled=self._on_get_reminders)
        )
        self._socket.add_receive_handler(
            GeckoPackCommandProtocolHandler(on_handled=self._on_pack_command)
        )

    def _on_hello(self, handler: GeckoHelloProtocolHandler, socket, sender):
        if handler.was_broadcast_discovery:
            if self._should_ignore(handler, sender):
                return
            socket.queue_send(self._hello_handler, sender)
        elif handler.client_identifier is not None:
            # We're not fussy, we'll chat to anyone!
            pass

    def _on_ping(self, handler: GeckoPingProtocolHandler, socket, sender):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(
            GeckoPingProtocolHandler.response(parms=sender),
            sender,
        )

    def _on_version(self, handler: GeckoVersionProtocolHandler, socket, sender):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(
            GeckoVersionProtocolHandler.response(
                self.snapshot.intouch_EN,
                self.snapshot.intouch_CO,
                parms=sender,
            ),
            sender,
        )

    def _on_get_channel(self, handler: GeckoGetChannelProtocolHandler, socket, sender):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(
            GeckoGetChannelProtocolHandler.response(10, 33, parms=sender),
            sender,
        )

    def _on_config_file(self, handler: GeckoConfigFileProtocolHandler, socket, sender):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(
            GeckoConfigFileProtocolHandler.response(
                self.snapshot.packtype,
                self.snapshot.config_version,
                self.snapshot.log_version,
                parms=sender,
            ),
            sender,
        )

    def _on_watercare(self, handler: GeckoWatercareProtocolHandler, socket, sender):
        if self._should_ignore(handler, sender):
            return
        if handler.schedule:
            socket.queue_send(
                GeckoWatercareProtocolHandler.schedule(parms=sender), sender
            )
        else:
            socket.queue_send(
                GeckoWatercareProtocolHandler.response(1, parms=sender), sender
            )

    def _on_update_firmware(
        self, handler: GeckoUpdateFirmwareProtocolHandler, socket, sender
    ):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(
            GeckoUpdateFirmwareProtocolHandler.response(parms=sender), sender
        )

    def _on_status_block(
        self, handler: GeckoStatusBlockProtocolHandler, socket, sender
    ):
        for idx, start in enumerate(
            range(
                handler.start,
                handler.start + handler.length,
                self._STATUS_BLOCK_SEGMENT_SIZE,
            )
        ):
            length = min(
                self._STATUS_BLOCK_SEGMENT_SIZE,
                len(self.structure.status_block) - start,
            )
            next = (idx + 1) % ((handler.length // self._STATUS_BLOCK_SEGMENT_SIZE) + 1)
            socket.queue_send(
                GeckoStatusBlockProtocolHandler.response(
                    idx,
                    next,
                    self.structure.status_block[start : start + length],
                    parms=sender,
                ),
                sender,
            )

    def _on_get_reminders(self, handler: GeckoRemindersProtocolHandler, socket, sender):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(GeckoRemindersProtocolHandler.response(parms=sender), sender)

    def _on_pack_command(
        self, handler: GeckoPackCommandProtocolHandler, socket, sender
    ):
        if self._should_ignore(handler, sender):
            return
        socket.queue_send(
            GeckoPackCommandProtocolHandler.response(parms=sender), sender
        )
        if handler.is_key_press:
            print(f"Pressed a key ({handler.keycode})")
        elif handler.is_set_value:
            print(f"Set a value ({handler.position} = {handler.new_data})")

    def _on_set_value(self, pos, length, newvalue):
        print(f"Simulator: Set value @{pos} for {length} to {newvalue}")
