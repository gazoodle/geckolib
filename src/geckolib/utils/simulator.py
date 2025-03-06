"""GeckoSimulator class."""

# ruff: noqa: T201

import asyncio
import logging
import random
import socket
import time
from pathlib import Path
from typing import Any, Self

from geckolib import VERSION
from geckolib.async_taskman import GeckoAsyncTaskMan
from geckolib.config import config_sleep, release_config_change_waiters
from geckolib.const import GeckoConstants
from geckolib.driver import (
    GeckoAsyncPartialStatusBlockProtocolHandler,
    GeckoAsyncStructure,
    GeckoAsyncUdpProtocol,
    GeckoConfigFileProtocolHandler,
    GeckoGetChannelProtocolHandler,
    GeckoGetWatercareModeProtocolHandler,
    GeckoHelloProtocolHandler,
    GeckoPackCommandProtocolHandler,
    GeckoPacketProtocolHandler,
    GeckoPingProtocolHandler,
    GeckoRemindersProtocolHandler,
    GeckoReminderType,
    GeckoRFErrProtocolHandler,
    GeckoSetWatercareModeProtocolHandler,
    GeckoStatusBlockProtocolHandler,
    GeckoStructAccessor,
    GeckoUdpProtocolHandler,
    GeckoUnhandledProtocolHandler,
    GeckoUpdateFirmwareProtocolHandler,
    GeckoVersionProtocolHandler,
    GeckoWatercareScheduleManager,
)
from geckolib.driver.protocol.watercare import (
    GeckoGetWatercareScheduleListProtocolHandler,
)

from .shared_command import GeckoCmd
from .simulator_action import GeckoSimulatorAction
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
        self.snapshot: GeckoSnapshot = GeckoSnapshot()
        self._reliability = 1.0
        self._tardiness = 0.0
        self._do_rferr = False
        self._do_thermodynamics = False
        self._send_structure_change = False
        self._clients = []
        random.seed()

        self._accessor_change_queue: asyncio.Queue = asyncio.Queue()

        self._structure_change_queue: asyncio.Queue = asyncio.Queue()
        self._can_report_structure_changes: asyncio.Event = asyncio.Event()
        self._can_report_structure_changes.set()

        self.intro = (
            "Welcome to the Gecko simulator. Type help or ? to list commands.\n"
        )
        self.prompt = "(GeckoSim) "
        try:
            import readline

            readline.set_completer_delims(" \r\n")
        except ImportError:
            pass

        self._action = GeckoSimulatorAction()
        for name in GeckoSimulatorAction.__annotations__:
            setattr(self._action, name, None)

        self._current_watercare_mode: int = GeckoConstants.WATERCARE_MODE[1]
        self._reminders: list[tuple[GeckoReminderType, int]] = [
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
        ]

        self._watercare_schedule_manager: GeckoWatercareScheduleManager = (
            GeckoWatercareScheduleManager()
        )

        self._hello_task: asyncio.Task | None = None

    async def __aenter__(self) -> Self:
        """Support async with."""
        await GeckoAsyncTaskMan.__aenter__(self)
        GeckoAsyncTaskMan.add_task(
            self, self._process_accesor_changes(), "Accessor Change Handler", "SIM"
        )
        GeckoAsyncTaskMan.add_task(
            self, self._notify_structure_changes(), "Notify Structure Changes", "SIM"
        )
        self.add_task(self._timer_loop(), "Timer", "SIM")
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
        await self._install_standard_handlers()
        self._send_structure_change = True

    async def do_stop(self, _args: str) -> None:
        """Stop the simulator : stop."""
        if self._protocol:
            self._protocol.disconnect()
            self._protocol = None
        if self._transport:
            self._transport.close()
            self._transport = None

    def do_parse(self, args: str) -> None:
        """
        Parse logfiles.

        Extract snapshots to the ./snapshot directory. Will
        overwrite identically named snapshot files if present.

        usage: parse <logfile>
        """
        for snapshot in GeckoSnapshot.parse_log_file(args):
            snapshot.save("snapshots")
            print(f"Saved snapshot snapshots/{snapshot.filename}")

    def do_reliability(self, args: str) -> None:
        """
        Set simulator reliability factor.

        Reliability is a measure of how likely
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

    def do_tardiness(self, args: str) -> None:
        """
        Set simulator tardiness factor.

        Tardomess is a measure of how rapidly the simulator will respond to an
        incoming message. Tardiness of 0.0 (default) means the simulator will
        respond immediately. Larger numbers are how long in seconds it could
        take to respond. This isn't an absolute delay, it will be somewhere in
        the range 0.0 to the tardiness value.

        Usage: tardiness [<factor>] where <factor> is a float. Missing the
               parameter will show the current value
        """
        if args == "":
            print(f"Current tardiness is {self._tardiness}")
            return
        self._tardiness = float(args)

    def do_rferr(self, args: str) -> None:
        """Set the simulator to response with RFERR if the parameter is True."""
        self._do_rferr = args.lower() == "true"
        print(f"RFERR mode set to {self._do_rferr}")

    def complete_parse(
        self, text: str, _line: str, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the parse command."""
        return self._complete_path(text)

    async def do_load(self, args: str) -> None:
        """
        Load a snapshot.

        Usage: load <snapshot>
        """
        snapshots = GeckoSnapshot.parse_log_file(args)
        if len(snapshots) == 1:
            await self.set_snapshot(snapshots[0])
            return
        print(
            f"{args} contains {len(snapshots)} snapshots. Please use the"
            f" `parse` command to break it apart"
        )

    def complete_load(
        self, text: str, _line: str, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the load command."""
        return self._complete_path(text)

    def do_save(self, args: str) -> None:
        """
        Save a snapshot.

        Usage: save <snapshot file>
        """
        path = Path(args)
        data = self.get_snapshot_data()
        with path.open("w") as f:
            f.write(f"{data}")

    def complete_save(
        self, text: str, _line: str, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the save command."""
        return self._complete_path(text)

    async def do_import(self, args: str) -> None:
        """Import a JSON snapshot."""
        snapshot = GeckoSnapshot.parse_json(args)
        await self.set_snapshot(snapshot)

    async def do_name(self, args: str) -> None:
        """Set the name of the spa : name <spaname>."""
        self._name = args
        if self._hello_task is not None:
            self._hello_task.cancel()
            self._hello_task = None
            release_config_change_waiters()
            await asyncio.sleep(1)

        assert self._protocol is not None  # noqa: S101
        # Hello handler
        self._hello_task = self.add_task(
            GeckoHelloProtocolHandler.response(
                SPA_IDENTIFIER,
                self._name,
                async_on_handled=self._async_on_hello,
            ).consume(self._protocol),
            "Hello handler",
            "SIM",
        )

    async def set_snapshot(self, snapshot: GeckoSnapshot) -> None:
        """Assign snapshot to this simulator."""
        compatible = self.snapshot.is_compatible(snapshot)
        if not compatible:
            print("The new snapshot structure is not compatible, so doing a full reset")
            print(self.prompt, end="", flush=True)
            if "PackType" in self.structure.accessors:
                await self.structure.accessors["PackType"].async_set_value(
                    self.structure.accessors["PackType"].value, always_send=True
                )

            self.structure.reset()

        self.snapshot = snapshot
        _LOGGER.debug(snapshot)

        await self._set_structure_from_snapshot(
            self.structure, self.snapshot, do_rebuild=not compatible
        )
        if not compatible:
            for accessor in self.structure.accessors.values():
                accessor.set_read_write("ALL")
                accessor.watch(self._on_accessor_changed)

    async def _set_structure_from_snapshot(
        self, struct: GeckoAsyncStructure, snapshot: GeckoSnapshot, *, do_rebuild: bool
    ) -> None:
        struct.replace_status_block_segment(0, snapshot.bytes)

        if do_rebuild:
            # Must rebuild stuff
            try:
                # Attempt to get config and log classes
                await struct.load_pack_class(snapshot.packtype.lower())
                await struct.load_config_module(snapshot.config_version)
                await struct.load_log_module(snapshot.log_version)
                await struct.check_for_accessories()
                struct.build_accessors()

            except ModuleNotFoundError:
                _LOGGER.exception("Module not found during snapshot load")
        struct.build_connections()

    async def do_diff(self, arg: str) -> None:
        """
        Perform a diff between spa data structures.

        You can either diff two separate files,
        or a single file and the current structure.

        usage: diff <file1> <file2>
        """
        file1 = arg
        file2 = ""
        rest = None
        if " " in arg:
            file1, file2, *rest = arg.split(" ")
        if not file1:
            print("Need at least one file.")

        struct = GeckoAsyncStructure(None)
        snapshot = GeckoSnapshot.parse_log_file(file1)[0]
        await self._set_structure_from_snapshot(struct, snapshot, do_rebuild=True)

        differences = self.structure.get_differences(struct)
        if differences:
            print("Differences are:")
            print("\n".join(differences))
        else:
            print("Identical snapshot")
        print(self.prompt, end="", flush=True)

    def complete_diff(
        self, text: str, _line: str, _start_idx: int, _end_idx: int
    ) -> list[str]:
        """Complete the do_diff command."""
        return self._complete_path(text)

    async def do_reset_to(self, arg: str) -> None:
        """
        Reset simulator to specific platform and version.

        usage: reset_to <platform> <config_version> <log_version>.
        """
        try:
            plateform, config, log = arg.split(" ")
            await self.set_snapshot(GeckoSnapshot.create(plateform, config, log))
        except IndexError:
            pass

    def do_thermodynamics(self, arg: str) -> None:
        """
        Run thermodynamics simulator.

        Turn the thermodynamics simulation control on or off
        usage: thermodynamics <ON|OFF>. Defaults to ON
        """
        if not arg:
            arg = "ON"
        self._do_thermodynamics = arg == "ON"

    async def _should_ignore(
        self,
        handler: GeckoUdpProtocolHandler,
        sender: tuple,
        *,
        respect_rferr: bool = True,
    ) -> bool:
        if respect_rferr and self._do_rferr:
            assert self._protocol is not None  # noqa: S101
            self._protocol.queue_send(
                GeckoRFErrProtocolHandler.response(parms=sender), sender
            )
            # Always ignore responses because we've already replied with RFERR
            return True

        tardiness = random.random() * self._tardiness  # noqa: S311 (Not interested in crypto strength!)
        if tardiness > 0.0:
            await asyncio.sleep(tardiness)

        should_ignore = random.random() > self._reliability  # noqa: S311 (Not interested in crypto strength!)
        if should_ignore:
            _LOGGER.debug(
                f"Unreliable simulator ignoring request for {handler} from {sender}"  # noqa: G004
            )
        return should_ignore

    async def _install_standard_handlers(self) -> None:
        """
        Install standard handlers.

        All simulators needs to have some basic functionality such
        as discovery, error handling et al
        """
        await self.do_name("Simulator")

        assert self._protocol is not None  # noqa: S101
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
        # Watercare if not MrSteam
        if not self.structure.is_mr_steam:
            self.add_task(
                GeckoGetWatercareModeProtocolHandler(
                    async_on_handled=self._async_on_get_watercare_mode
                ).consume(self._protocol),
                "GetWatercareMode",
                "SIM",
            )
            self.add_task(
                GeckoSetWatercareModeProtocolHandler(
                    async_on_handled=self._async_on_set_watercare_mode
                ).consume(self._protocol),
                "SetWatercareMode",
                "SIM",
            )
            self.add_task(
                GeckoGetWatercareScheduleListProtocolHandler(
                    async_on_handled=self._async_on_get_watercare_schedule
                ).consume(self._protocol),
                "GetWatercareSchedule",
                "SIM",
            )

            # Reminders
            self.add_task(
                GeckoRemindersProtocolHandler(
                    async_on_handled=self._async_on_reminders
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
        # Partial pack ack
        self.add_task(
            GeckoAsyncPartialStatusBlockProtocolHandler(self._protocol).consume(
                self._protocol
            ),
            "Partial pack ACK",
            "SIM",
        )

    async def _async_on_hello(
        self, handler: GeckoHelloProtocolHandler, sender: tuple
    ) -> None:
        if handler.was_broadcast_discovery:
            if await self._should_ignore(handler, sender, respect_rferr=False):
                return
            assert self._protocol is not None  # noqa: S101
            if (
                time.monotonic() - handler.last_response
                > GeckoConstants.SIMULATOR_MIN_TIME_BETWEEN_HELLO_BROADCAST_RESPONSES
            ):
                handler.last_response = time.monotonic()
                self._protocol.queue_send(handler, sender)
        elif handler.client_identifier is not None:
            # We're not fussy, we'll chat to anyone!
            pass

    async def _async_on_ping(
        self, handler: GeckoPingProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
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
        if await self._should_ignore(handler, sender):
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
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoGetChannelProtocolHandler.response(10, 33, parms=sender),
            sender,
        )

    async def _async_on_config_file(
        self, handler: GeckoConfigFileProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
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
        if await self._should_ignore(handler, sender):
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
            next_index = (idx + 1) % (
                (handler.length // self._STATUS_BLOCK_SEGMENT_SIZE) + 1
            )
            if await self._should_ignore(handler, sender, respect_rferr=False):
                continue
            assert self._protocol is not None  # noqa: S101
            self._protocol.queue_send(
                GeckoStatusBlockProtocolHandler.response(
                    idx,
                    next_index,
                    self.structure.status_block[start : start + length],
                    parms=sender,
                ),
                sender,
            )

    async def _async_on_get_watercare_mode(
        self, handler: GeckoGetWatercareModeProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoGetWatercareModeProtocolHandler.get_response(
                self._current_watercare_mode, parms=sender
            ),
            sender,
        )

    async def _async_on_set_watercare_mode(
        self, handler: GeckoSetWatercareModeProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        print(
            f"Set watercare mode to {GeckoConstants.WATERCARE_MODE_STRING[handler.mode]}"  # noqa: E501
        )
        self._current_watercare_mode = handler.mode
        self._protocol.queue_send(
            GeckoSetWatercareModeProtocolHandler.set_response(
                self._current_watercare_mode, parms=sender
            ),
            sender,
        )

    async def _async_on_get_watercare_schedule(
        self, handler: GeckoGetWatercareScheduleListProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoGetWatercareScheduleListProtocolHandler.get_response(
                self._watercare_schedule_manager, parms=sender
            ),
            sender,
        )

    async def _async_on_reminders(
        self, handler: GeckoRemindersProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        if handler.is_request:
            self._protocol.queue_send(
                GeckoRemindersProtocolHandler.req_response(
                    self._reminders,
                    parms=sender,
                ),
                sender,
            )
            return

        assert handler.reminders  # noqa: S101
        self._reminders = handler.reminders
        self._protocol.queue_send(
            GeckoRemindersProtocolHandler.set_ack(parms=sender), sender
        )

    async def _async_on_update_firmware(
        self, handler: GeckoUpdateFirmwareProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoUpdateFirmwareProtocolHandler.response(parms=sender), sender
        )

    async def _async_on_pack_command(
        self, handler: GeckoPackCommandProtocolHandler, sender: tuple
    ) -> None:
        if await self._should_ignore(handler, sender):
            return
        assert self._protocol is not None  # noqa: S101
        self._protocol.queue_send(
            GeckoPackCommandProtocolHandler.response(parms=sender), sender
        )
        if handler.is_key_press:
            await self._async_handle_pack_key_press(handler.keycode)
        elif handler.is_set_value:
            await self._async_handle_pack_set_value(
                handler.position, handler.length, handler.new_data
            )
        else:
            _LOGGER.error("Unhandled pack command")

    async def _async_handle_pack_key_press(self, keycode: int) -> None:
        """Handle a key press command."""
        _LOGGER.debug("Pack command press key %d", keycode)

        self._fill_action_state()

        # Iterate through all attributes in GeckoConstants
        for name, val in vars(GeckoConstants).items():
            # Check if the attribute is an integer, matches the given value,
            # and starts with 'KEYPAD_'
            if isinstance(val, int) and val == keycode and name.startswith("KEYPAD_"):
                # Now find a function in the action class
                func = getattr(self._action, f"on_{name}", None)
                if func is not None:
                    func()
                    await self._report_action_state()
                    return

        _LOGGER.warning("Simulator didn't handle key pad command for %d", keycode)

    async def _async_handle_pack_set_value(
        self, pos: int, _length: int, data: bytes
    ) -> None:
        """Handle set value."""
        _LOGGER.debug(
            "Replace status block segmemnt @ %d with %s (%d bytes)",
            pos,
            f"{data}",
            len(data),
        )
        self.structure.replace_status_block_segment(pos, data)
        if self._send_structure_change:
            await self._structure_change_queue.put(pos)

    async def _async_on_set_value(self, pos: int, length: int, newvalue: Any) -> None:
        """Call when the structure notifies a change."""
        change = (pos, GeckoStructAccessor.pack_data(length, newvalue))
        await self._async_handle_pack_set_value(change[0], length, change[1])

    async def _notify_structure_changes(self) -> None:
        try:
            while True:
                await self._can_report_structure_changes.wait()
                changes: list = []
                changes.append(await self._structure_change_queue.get())
                while self._structure_change_queue.qsize():
                    changes.append(self._structure_change_queue.get_nowait())
                # The change report system only handles two byte changes, so
                # we have to suck those from the actual status block.
                changes = [
                    (
                        change,
                        self.structure.status_block[change : change + 2],
                    )
                    for change in changes
                ]
                assert self._protocol is not None  # noqa: S101
                for client in self._clients:
                    self._protocol.queue_send(
                        GeckoAsyncPartialStatusBlockProtocolHandler.report_changes(
                            self._protocol, changes, parms=client
                        ),
                        client,
                    )

        except asyncio.CancelledError:
            _LOGGER.debug("Simulator notify structure change loop cancelled")
            raise

        except:
            _LOGGER.exception("Simulator notify structure change loop exception")
            raise

        finally:
            _LOGGER.debug("Simulator notify structure change loop finished")

    def _on_accessor_changed(
        self, accessor: GeckoStructAccessor, old_value: Any, new_value: Any
    ) -> None:
        print(f"accessor {accessor} changed from {old_value} to {new_value}")
        self._accessor_change_queue.put_nowait((accessor, old_value, new_value))
        if self._send_structure_change:
            self._structure_change_queue.put_nowait(accessor.pos)

    async def _process_accesor_changes(self) -> None:
        accessor: GeckoStructAccessor
        old_value: Any
        new_value: Any
        try:
            while True:
                accessor, old_value, new_value = await self._accessor_change_queue.get()

                self._fill_action_state()
                func = getattr(self._action, f"on_{accessor.tag}", None)
                if func is not None:
                    func()
                    await self._report_action_state()
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

    def _fill_action_state(self) -> None:
        for name in vars(self._action):
            if name in self.structure.accessors:
                setattr(self._action, name, self.structure.accessors[name].value)
            else:
                setattr(self._action, name, None)
        self._action.set_connections(self.structure.connections)

    async def _report_action_state(self) -> None:
        # Write all the properties back, only the changed
        # ones will be sent.
        self._can_report_structure_changes.clear()
        for name, val in vars(self._action).items():
            if name in self.structure.accessors and val is not None:
                await self.structure.accessors[name].async_set_value(val)
        self._can_report_structure_changes.set()

    def get_snapshot_data(self) -> dict:
        """Get snapshot data that the simulator can supply."""
        data = self.structure.get_snapshot_data()
        assert self.snapshot is not None  # noqa: S101
        data.update(
            {
                "intouch version EN": self.snapshot.intouch_EN_str,
                "intouch version CO": self.snapshot.intouch_CO_str,
            }
        )
        return data

    async def _timer_loop(self) -> None:
        elapsed_time = 0
        try:
            while True:
                await config_sleep(1, "Simulator Timer")
                elapsed_time += 1
                self._fill_action_state()
                self._action.every_second(elapsed_time)
                if elapsed_time % 10 == 0 and self._do_thermodynamics:
                    self._action.check_thermodynamics(elapsed_time)
                if elapsed_time % 60 == 0:
                    self._action.every_minute(int(elapsed_time / 60))
                if elapsed_time % 3600 == 0:
                    self._action.every_hour(int(elapsed_time / 3600))
                await self._report_action_state()

        except asyncio.CancelledError:
            _LOGGER.debug("Simulator timer loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("Simulator timer loop caught exception")
            raise
