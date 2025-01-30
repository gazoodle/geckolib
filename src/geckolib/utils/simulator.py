"""GeckoSimulator class."""

# ruff: noqa: T201

import asyncio
import glob
import importlib
import logging
import os
from pickle import NEWOBJ_EX
import random
import socket
import struct
from typing import Any, Self

from geckolib import VERSION
from geckolib.async_taskman import GeckoAsyncTaskMan
from geckolib.const import GeckoConstants
from geckolib.driver import (
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoConfigFileProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoHelloProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoRFErrProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareProtocolHandler,
)
from geckolib.driver.accessor import GeckoStructAccessor
from geckolib.driver.async_spastruct import GeckoAsyncStructure
from geckolib.driver.async_udp_protocol import GeckoAsyncUdpProtocol
from geckolib.driver.protocol.unhandled import GeckoUnhandledProtocolHandler

from .shared_command import GeckoCmd
from .snapshot import GeckoSnapshot

_LOGGER = logging.getLogger(__name__)


SPA_IDENTIFIER = b"SPA01:02:03:04:05:06"


class GeckoSimulator(GeckoCmd, GeckoAsyncTaskMan):
    """
    GeckoSimulator.

    This is a server application to aid with investigating
    the Gecko protocol.
    """

    _STATUS_BLOCK_SEGMENT_SIZE = 39

    def __init__(self) -> None:
        """Initialize the simulator class."""
        GeckoAsyncTaskMan.__init__(self)
        GeckoCmd.__init__(self, self)

        # Async properties
        self._con_lost = asyncio.Event()
        self._protocol: GeckoAsyncUdpProtocol | None = None
        self._transport: asyncio.BaseTransport | None = None
        self._name: str = "Sim"
        self.structure: GeckoAsyncStructure = GeckoAsyncStructure(
            self._async_on_set_value
        )
        self.snapshot = None
        self._reliability = 1.0
        self._do_rferr = False
        self._send_structure_change = False
        self._clients = []
        random.seed()

        self._accessor_change_queue: asyncio.Queue = asyncio.Queue()

        self.intro = (
            "Welcome to the Gecko simulator. Type help or ? to list commands.\n"
        )
        self.prompt = "(GeckoSim) "
        try:
            import readline

            readline.set_completer_delims(" \r\n")
        except ImportError:
            pass

    async def __aenter__(self) -> Self:
        await GeckoAsyncTaskMan.__aenter__(self)
        GeckoAsyncTaskMan.add_task(
            self, self._process_accesor_changes(), "Accessor Change Handler", "SIM"
        )
        return self

    async def __aexit__(self, *_args: object) -> None:
        """Support 'with' statements."""
        await self.do_stop("")

    def do_about(self, _arg: str) -> None:
        """Display information about this client program and support library : about."""
        print()
        print(
            "GeckoSimulator: A python program using GeckoLib library to simulate Gecko"
            " enabled devices with in.touch2 communication modules"
        )
        print(f"Library version v{VERSION}")

    async def do_start(self, _args: str) -> None:
        """Start the configured simulator : start."""
        loop = asyncio.get_running_loop()
        self._con_lost.clear()
        # Create a socket that can handle broadcast
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(("0.0.0.0", 10022))  # noqa: S104
        # Start the transport and protocol handler
        self._transport, self._protocol = await loop.create_datagram_endpoint(
            lambda: GeckoAsyncUdpProtocol(self, self._con_lost, None),
            sock=sock,
        )
        self._install_standard_handlers()
        self._send_structure_change = True

    async def do_stop(self, _args: str) -> None:
        """Stop the simulator : stop."""
        if self._protocol:
            self._protocol.disconnect()
            self._protocol = None
        if self._transport:
            self._transport.close()
            self._transport = None

    def _complete_path(self, path):
        if os.path.isdir(path):
            return glob.glob(os.path.join(path, "*"))
        return glob.glob(path + "*")

    def do_parse(self, args):
        """
        Parse logfiles to extract snapshots to the ./snapshot directory. Will
        overwrite identically named snapshot files if present : parse <logfile>
        """
        for snapshot in GeckoSnapshot.parse_log_file(args):
            snapshot.save("snapshots")
            print(f"Saved snapshot snapshots/{snapshot.filename}")

    def do_reliability(self, args):
        """
        Set simulator reliability factor. Reliability is a measure of how likely
        the simulator will respond to an incoming message. Reliability of 1.0 (default)
        means the simulator will always respond, whereas 0.0 means it will never
        respond. This does not take into account messages that actually don't get
        recieved : reliability <factor> where <factor> is a float between 0.0 and
        1.0.
        """
        if args == "":
            print(f"Current reliability is {self._reliability}")
            return
        self._reliability = min(1.0, max(0.0, float(args)))

    def do_rferr(self, args):
        """Set the simulator to response with RFERR if the parameter is True"""
        self._do_rferr = args.lower() == "true"
        print(f"RFERR mode set to {self._do_rferr}")

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

    def do_snapshot(self, args):
        """Set a snapshot state"""
        snapshot = GeckoSnapshot.parse_json(args)
        self.set_snapshot(snapshot)

    def do_name(self, args):
        """Set the name of the spa : name <spaname>."""
        self._name = args

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
                self.pack_type = self.pack_class.plateform_type
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

            # Watch some accessors
            self.structure.accessors["UdP1"].watch(self._on_accessor_changed)

        except:  # noqa
            _LOGGER.exception("Exception during snapshot load")

    def _should_ignore(self, handler, sender, respect_rferr=True) -> bool:
        if respect_rferr and self._do_rferr:
            self._protocol.queue_send(
                GeckoRFErrProtocolHandler.response(parms=sender), sender
            )
            # Always ignore responses because we've already replied with RFERR
            return True

        should_ignore = random.random() > self._reliability
        if should_ignore:
            print(f"Unreliable simulator ignoring request for {handler} from {sender}")
        return should_ignore

    def _install_standard_handlers(self) -> None:
        """
        Install standard handlers.

        All simulators needs to have some basic functionality such
        as discovery, error handling et al
        """
        self.do_name("Udp Test Spa")

        assert self._protocol is not None  # noqa: S101
        # Hello handler
        self.add_task(
            GeckoHelloProtocolHandler.response(
                SPA_IDENTIFIER,
                self._name,
                async_on_handled=self._async_on_hello,
            ).consume(self._protocol),
            "Hello handler",
            "SIM",
        )
        # Helper to unwrap PACK packets
        self.add_task(
            GeckoPacketProtocolHandler(async_on_handled=self._async_on_packet).consume(
                self._protocol
            ),
            "Packet handler",
            "SIM",
        )
        # Unhandled packets get thrown
        self.add_task(
            GeckoUnhandledProtocolHandler().consume(self._protocol),
            "Unhandled packet",
            "SIM",
        )
        # Ping response handler
        self.add_task(
            GeckoPingProtocolHandler(async_on_handled=self._async_on_ping).consume(
                self._protocol
            ),
            "Ping handler",
            "SIM",
        )
        # Version handler
        self.add_task(
            GeckoVersionProtocolHandler(
                async_on_handled=self._async_on_version
            ).consume(self._protocol),
            "Version handler",
            "SIM",
        )
        # Channel handler
        self.add_task(
            GeckoGetChannelProtocolHandler(
                async_on_handled=self._async_on_get_channel
            ).consume(self._protocol),
            "Get channel",
            "SIM",
        )
        # Config file
        self.add_task(
            GeckoConfigFileProtocolHandler(
                async_on_handled=self._async_on_config_file
            ).consume(self._protocol),
            "Config file",
            "SIM",
        )
        # Status block
        self.add_task(
            GeckoStatusBlockProtocolHandler(
                async_on_handled=self._async_on_status_block
            ).consume(self._protocol),
            "Status block",
            "SIM",
        )
        # Watercase
        self.add_task(
            GeckoWatercareProtocolHandler(
                async_on_handled=self._async_on_watercare
            ).consume(self._protocol),
            "Watercase",
            "SIM",
        )
        # Reminders
        self.add_task(
            GeckoRemindersProtocolHandler(
                async_on_handled=self._async_on_get_reminders
            ).consume(self._protocol),
            "Reminders",
            "SIM",
        )
        # Update firmware fake
        self.add_task(
            GeckoUpdateFirmwareProtocolHandler(
                async_on_handled=self._async_on_update_firmware
            ).consume(self._protocol),
            "Update Firmware",
            "SIM",
        )
        # Pack command
        self.add_task(
            GeckoPackCommandProtocolHandler(
                async_on_handled=self._async_on_pack_command
            ).consume(self._protocol),
            "Pack command",
            "SIM",
        )

    async def _async_on_hello(
        self, handler: GeckoHelloProtocolHandler, sender: tuple
    ) -> None:
        if handler.was_broadcast_discovery:
            if self._should_ignore(handler, sender, False):
                return
            assert self._protocol is not None  # noqa: S101
            self._protocol.queue_send(handler, sender)
        elif handler.client_identifier is not None:
            # We're not fussy, we'll chat to anyone!
            pass

    async def _async_on_ping(
        self, handler: GeckoPingProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoPingProtocolHandler.response(on_get_parms=lambda _handler: sender),
            sender,
        )
        if sender not in self._clients:
            self._clients.append(sender)

    async def _async_on_packet(
        self, handler: GeckoPacketProtocolHandler, _sender: tuple
    ) -> None:
        assert self._protocol is not None  # noqa: S101
        assert handler.parms is not None  # noqa: S101
        if handler.parms[3] != SPA_IDENTIFIER:
            _LOGGER.warning(
                "Dropping packet from %s because it didn't match %s",
                handler.parms,
                SPA_IDENTIFIER,
            )
        assert handler.packet_content is not None  # noqa: S101
        self._protocol.datagram_received(handler.packet_content, handler.parms)

    async def _async_on_version(
        self, handler: GeckoVersionProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        assert self.snapshot is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoVersionProtocolHandler.response(
                self.snapshot.intouch_EN,
                self.snapshot.intouch_CO,
                parms=sender,
            ),
            sender,
        )

    async def _async_on_get_channel(
        self, handler: GeckoGetChannelProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoGetChannelProtocolHandler.response(10, 33, parms=sender),
            sender,
        )

    async def _async_on_config_file(
        self, handler: GeckoConfigFileProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        assert self.snapshot is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoConfigFileProtocolHandler.response(
                self.snapshot.packtype,
                self.snapshot.config_version,
                self.snapshot.log_version,
                parms=sender,
            ),
            sender,
        )

    async def _async_on_status_block(
        self, handler: GeckoStatusBlockProtocolHandler, sender: tuple
    ) -> None:
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
            assert self._protocol is not None  # noqa: S101
            self._protocol.queue_send(
                GeckoStatusBlockProtocolHandler.response(
                    idx,
                    next,
                    self.structure.status_block[start : start + length],
                    parms=sender,
                ),
                sender,
            )

    async def _async_on_watercare(
        self, handler: GeckoWatercareProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        if handler.schedule:
            self._protocol.queue_send(
                GeckoWatercareProtocolHandler.giveschedule(parms=sender), sender
            )
        else:
            self._protocol.queue_send(
                GeckoWatercareProtocolHandler.response(1, parms=sender), sender
            )

    async def _async_on_get_reminders(
        self, handler: GeckoRemindersProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
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

    async def _async_on_update_firmware(
        self, handler: GeckoUpdateFirmwareProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        assert self._protocol is not None
        self._protocol.queue_send(
            GeckoUpdateFirmwareProtocolHandler.response(parms=sender), sender
        )

    async def _async_on_pack_command(
        self, handler: GeckoPackCommandProtocolHandler, sender: tuple
    ) -> None:
        if self._should_ignore(handler, sender):
            return
        if handler.is_key_press:
            await self._async_handle_key_press(handler.keycode)
        elif handler.is_set_value:
            await self.__async_handle_set_value(
                handler.position, handler.length, handler.new_data
            )
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoPackCommandProtocolHandler.response(parms=sender), sender
        )

    async def _async_handle_key_press(self, keycode: int) -> None:
        """Handle a key press command."""
        _LOGGER.debug("Pack command press key %d", keycode)

        if keycode == GeckoConstants.KEYPAD_PUMP_1:
            udp1 = self.structure.accessors["UdP1"]
            if udp1.value == "OFF":
                await udp1.async_set_value("HI")
            else:
                await udp1.async_set_value("OFF")

    async def __async_handle_set_value(
        self, pos: int, length: int, data: bytes
    ) -> None:
        """Handle set value."""
        _LOGGER.debug("Pack command set value %d=%s", pos, data)
        self.structure.replace_status_block_segment(pos, data)

    async def _async_on_set_value(self, pos, length, newvalue):
        _LOGGER.debug(f"Simulator: Async Set value @{pos} len {length} to {newvalue}")
        print(f"Simulator: Set value @{pos} len {length} to {newvalue}")
        change = (pos, GeckoPackCommandProtocolHandler.pack_data(length, newvalue))
        self.structure.replace_status_block_segment(change[0], change[1])
        assert self._protocol is not None

        if self._send_structure_change:
            for client in self._clients:
                self._protocol.queue_send(
                    GeckoAsyncPartialStatusBlockProtocolHandler.report_changes(
                        self._protocol, [change], parms=client
                    ),
                    client,
                )

    def _on_accessor_changed(
        self, accessor: GeckoStructAccessor, old_value: Any, new_value: Any
    ) -> None:
        self._accessor_change_queue.put_nowait((accessor, old_value, new_value))

    async def _process_accesor_changes(self) -> None:
        accessor: GeckoStructAccessor
        old_value: Any
        new_value: Any
        try:
            while True:
                accessor, old_value, new_value = await self._accessor_change_queue.get()

                if accessor.tag == "UdP1":
                    p1: GeckoStructAccessor = self.structure.accessors["P1"]
                    if new_value == "HI":
                        await p1.async_set_value("HIGH")
                    elif new_value == "LO":
                        await p1.async_set_value("LOW")
                    else:
                        await p1.async_set_value("OFF")

                else:
                    _LOGGER.debug(
                        "%s changed from %s to %s", accessor, old_value, new_value
                    )
                self._accessor_change_queue.task_done()

        except asyncio.CancelledError:
            _LOGGER.debug("Simulator accessort change loop cancelled")
            raise

        except:
            _LOGGER.exception("Simulator value update loop exception")
            raise

        finally:
            _LOGGER.debug("Simulator value update loop finished")

{
    GeckoConstants.KEY_PUMP_1: { if }
}