""" GeckoSimulator class """

import logging
import os
import glob
import random
import importlib
import struct
from ..const import GeckoConstants

from .shared_command import GeckoCmd
from ..driver import (
    GeckoHelloProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoPartialStatusBlockProtocolHandler,
    GeckoWatercareProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoRFErrProtocolHandler,
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
        self._do_rferr = False
        self._send_structure_change = False
        self._clients = []
        random.seed()

        super().__init__(first_commands)

        self.intro = (
            "Welcome to the Gecko simulator. Type help or ? to list commands.\n"
        )
        self.prompt = "(GeckoSim) "
        try:
            import readline

            readline.set_completer_delims(" \r\n")
        except ImportError:
            pass

    def __exit__(self, *args):
        self._socket.close()
        self._socket = None

    def do_about(self, _arg):
        """Display information about this client program and support library : about"""
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

    def do_rferr(self, args):
        """Set the simulator to response with RFERR if the parameter is True"""
        self._do_rferr = args.lower() == "true"
        print(f"RFERR mode set to {self._do_rferr}")

    def do_get(self, arg):
        """Get the value of the specified spa pack structure element : get <Element>"""
        try:
            print("{0} = {1}".format(arg, self.structure.accessors[arg].value))
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception getting '%s'", arg)

    def do_set(self, arg):
        """Set the value of the specified spa pack structure
        element : set <Element>=<value>"""
        self._send_structure_change = True
        try:
            key, val = arg.split("=")
            self.structure.accessors[key].value = val
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Exception handling 'set %s'", arg)
        finally:
            self._send_structure_change = False

    def do_accessors(self, _arg):
        """Display the data from the accessors : accessors"""
        print("Accessors")
        print("=========")
        print("")
        for key in self.structure.accessors:
            print("   {0}: {1}".format(key, self.structure.accessors[key].value))
        print("")

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

    def do_name(self, args):
        """Set the name of the spa : name <spaname>."""
        self._hello_handler = GeckoHelloProtocolHandler.response(
            b"SPA01:02:03:04:05:06", args, on_handled=self._on_hello
        )

    def complete_load(self, text, line, start_idx, end_idx):
        return self._complete_path(text)

    def set_snapshot(self, snapshot):
        self.snapshot = snapshot
        self.structure.replace_status_block_segment(0, self.snapshot.bytes)

        try:
            # Attempt to get config and log classes
            plateform_key = self.snapshot.packtype.lower()

            pack_module_name = f"geckolib.driver.packs.{plateform_key}"
            try:
                GeckoPack = importlib.import_module(pack_module_name).GeckoPack
                self.pack_class = GeckoPack(self.structure)
                self.pack_type = self.pack_class.type
            except ModuleNotFoundError:
                raise Exception(
                    GeckoConstants.EXCEPTION_MESSAGE_NO_SPA_PACK.format(
                        self.snapshot.packtype
                    )
                )

            config_module_name = f"geckolib.driver.packs.{plateform_key}-cfg-{self.snapshot.config_version}"
            try:
                GeckoConfigStruct = importlib.import_module(
                    config_module_name
                ).GeckoConfigStruct
                self.config_class = GeckoConfigStruct(self.structure)
            except ModuleNotFoundError:
                raise Exception(
                    f"Cannot find GeckoConfigStruct module for {self.snapshot.packtype} v{self.snapshot.config_version}"
                )

            log_module_name = (
                f"geckolib.driver.packs.{plateform_key}-log-{self.snapshot.log_version}"
            )
            try:
                GeckoLogStruct = importlib.import_module(log_module_name).GeckoLogStruct
                self.log_class = GeckoLogStruct(self.structure)
            except ModuleNotFoundError:
                raise Exception(
                    f"Cannot find GeckoLogStruct module for {self.snapshot.packtype} v{self.snapshot.log_version}"
                )

            self.structure.build_accessors(self.config_class, self.log_class)
            for accessor in self.structure.accessors.values():
                accessor.set_read_write("ALL")

        except:  # noqa
            _LOGGER.exception("Exception during snapshot load")

    def _should_ignore(self, handler, sender, respect_rferr=True):
        if respect_rferr and self._do_rferr:
            self._socket.queue_send(
                GeckoRFErrProtocolHandler.response(parms=sender),
                sender,
            )
            # Always ignore responses because we've already replied with RFERR
            return True

        should_ignore = random.random() > self._reliability
        if should_ignore:
            print(f"Unreliable simulator ignoring request for {handler} from {sender}")
        return should_ignore

    def _install_standard_handlers(self):
        """All simulators needs to have some basic functionality such
        as discovery, error handling et al"""
        self.do_name("Udp Test Spa")
        self._socket.add_receive_handler(self._hello_handler)
        self._socket.add_receive_handler(
            GeckoPacketProtocolHandler(socket=self._socket)
        )
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

    def _on_hello(self, handler: GeckoHelloProtocolHandler, sender):
        if handler.was_broadcast_discovery:
            if self._should_ignore(handler, sender, False):
                return
            self._socket.queue_send(self._hello_handler, sender)
        elif handler.client_identifier is not None:
            # We're not fussy, we'll chat to anyone!
            pass

    def _on_ping(self, handler: GeckoPingProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoPingProtocolHandler.response(parms=sender),
            sender,
        )
        if sender not in self._clients:
            self._clients.append(sender)

    def _on_version(self, handler: GeckoVersionProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoVersionProtocolHandler.response(
                self.snapshot.intouch_EN,
                self.snapshot.intouch_CO,
                parms=sender,
            ),
            sender,
        )

    def _on_get_channel(self, handler: GeckoGetChannelProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoGetChannelProtocolHandler.response(10, 33, parms=sender),
            sender,
        )

    def _on_config_file(self, handler: GeckoConfigFileProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoConfigFileProtocolHandler.response(
                self.snapshot.packtype,
                self.snapshot.config_version,
                self.snapshot.log_version,
                parms=sender,
            ),
            sender,
        )

    def _on_watercare(self, handler: GeckoWatercareProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        if handler.schedule:
            self._socket.queue_send(
                GeckoWatercareProtocolHandler.giveschedule(parms=sender), sender
            )
        else:
            self._socket.queue_send(
                GeckoWatercareProtocolHandler.response(1, parms=sender), sender
            )

    def _on_update_firmware(self, handler: GeckoUpdateFirmwareProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoUpdateFirmwareProtocolHandler.response(parms=sender), sender
        )

    def _on_status_block(self, handler: GeckoStatusBlockProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
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
            if self._should_ignore(handler, sender, False):
                continue
            self._socket.queue_send(
                GeckoStatusBlockProtocolHandler.response(
                    idx,
                    next,
                    self.structure.status_block[start : start + length],
                    parms=sender,
                ),
                sender,
            )

    def _on_get_reminders(self, handler: GeckoRemindersProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoRemindersProtocolHandler.response(
                [
                    (GeckoReminderType.RINSE_FILTER, -13),
                    (GeckoReminderType.CLEAN_FILTER, 0),
                    (GeckoReminderType.CHANGE_WATER, 47),
                    (GeckoReminderType.CHECK_SPA, 687),
                    (GeckoReminderType.INVALID, -13),
                    (GeckoReminderType.INVALID, -13),
                    (GeckoReminderType.INVALID, 0),
                    (GeckoReminderType.INVALID, 0),
                    (GeckoReminderType.INVALID, 0),
                    (GeckoReminderType.INVALID, 0),
                ],
                parms=sender,
            ),
            sender,
        )

    def _on_pack_command(self, handler: GeckoPackCommandProtocolHandler, sender):
        if self._should_ignore(handler, sender):
            return
        self._socket.queue_send(
            GeckoPackCommandProtocolHandler.response(parms=sender), sender
        )
        if handler.is_key_press:
            print(f"Pressed a key ({handler.keycode})")
        elif handler.is_set_value:
            print(f"Set a value ({handler.position} = {handler.new_data})")

    def _on_set_value(self, pos, length, newvalue):
        print(f"Simulator: Set value @{pos} len {length} to {newvalue}")
        change = None
        if length == 1:
            change = (pos, struct.pack(">B", newvalue))
        elif length == 2:
            change = (pos, struct.pack(">H", newvalue))
        else:
            print("**** UNHANDLED SET SIZE ****")
            return

        self.structure.replace_status_block_segment(change[0], change[1])

        if self._send_structure_change:
            for client in self._clients:
                self._socket.queue_send(
                    GeckoPartialStatusBlockProtocolHandler.report_changes(
                        self._socket, [change], parms=client
                    ),
                    client,
                )
