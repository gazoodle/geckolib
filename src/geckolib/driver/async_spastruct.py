"""Async Spa Structure block."""

from __future__ import annotations

import asyncio
import datetime
import importlib
import logging
from functools import partial
from typing import TYPE_CHECKING, Any

from geckolib._version import VERSION
from geckolib.config import GeckoConfig
from geckolib.const import GeckoConstants
from geckolib.driver.accessor import (
    GeckoByteStructAccessor,
)

INMIX_PACKTYPE = 14

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import ModuleType

    from geckolib.driver.async_udp_protocol import GeckoAsyncUdpProtocol

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncStructure:
    """Class to host/manage the raw data block for a spa structure."""

    def __init__(self, on_async_set_value: Callable) -> None:
        """Initialize the async version."""
        self._on_async_set_value = on_async_set_value
        self.reset()

    def replace_status_block_segment(self, offset: int, segment: bytes) -> None:
        """Replace a segment of the status block."""
        previous_block = self._status_block
        segment_len = len(segment)
        self._status_block = (
            self._status_block[0:offset]
            + segment
            + self._status_block[offset + segment_len :]
        )
        # Notify changes to accessors
        for accessor in self.accessors.values():
            accessor.status_block_changed(offset, segment_len, previous_block)

    @property
    def status_block(self) -> bytes:
        """Get the status block."""
        return self._status_block

    def set_status_block(self, block: bytes) -> None:
        """Set the status block."""
        self._status_block = block

    def build_accessors(self) -> None:
        """Build the accessors."""
        self.accessors = dict(
            self.config_class.accessors,
            **self.log_class.accessors,
            **self.inmix_config_accessors,
            **self.inmix_log_accessors,
        )
        # Get all outputs
        self.all_outputs = [*self.config_class.output_keys, *self.log_class.output_keys]
        # Get collection of possible devices
        self.all_devices = self.log_class.all_device_keys
        # User devices are those that have a Ud in the tag name
        self.user_demands = self.log_class.user_demand_keys
        # Error keys
        self.error_keys = self.log_class.error_keys

    def reset(self) -> None:
        """Reset this status block to initialization state."""
        self.accessors = {}
        self.all_outputs = []
        self.all_devices = []
        self.user_demands = []
        self.connections = []
        self._status_block: bytes = b"\x00" * 1024

        self.plateform_key: str = ""
        self.pack_class = None
        self.pack_type: int = 0
        self.config_version: int = 0
        self.config_class = None
        self.log_version: int = 0
        self.log_class = None

        self.inmix_config_class = None
        self.inmix_config_accessors = {}
        self.inmix_log_class = None
        self.inmix_log_accessors = {}

    async def get(
        self,
        protocol: GeckoAsyncUdpProtocol,
        create_func: Callable,
        packet_timeout: int = GeckoConfig.PAUSE_BETWEEN_RETRIES_IN_SECONDS,
    ) -> bool:
        """Get response from a command."""
        _LOGGER.debug("Async get for struct")
        async with protocol.lock:
            # Create the request
            request = create_func()

            try:
                async with asyncio.timeout(request.timeout_in_seconds):
                    while True:
                        # Queue it for delivery
                        protocol.queue_send(request)

                        # Setup some controls for the multiple responses expected
                        next_expected = 0
                        segments = []

                        while True:
                            # Wait for a response up to a certain amount of time
                            if await request.wait_for_response(
                                protocol, packet_timeout
                            ):
                                _LOGGER.debug("timeout waiting for any block")
                                break

                            if next_expected == request.sequence:
                                segments.append(request.data)
                                next_expected = request.next

                                if request.next == 0:
                                    _LOGGER.debug(
                                        "Status block segments complete, update"
                                    )
                                    self.replace_status_block_segment(
                                        request.start,
                                        b"".join(segments),
                                    )
                                    return True
                            else:
                                _LOGGER.debug(
                                    "Out-of-sequence status block segment %d - ignored",
                                    request.sequence,
                                )

                                if request.next == 0:
                                    break

                        # Create a clean new request
                        request = create_func()

            except TimeoutError:
                _LOGGER.debug(
                    "TIMEOUT: Handler %s threw TimeoutError (%fs)",
                    request,
                    request.timeout_in_seconds,
                )

            return False

    async def async_set_value(self, pos: int, length: int, newvalue: Any) -> None:
        """Set the value of a block."""
        await self._on_async_set_value(pos, length, newvalue)

    async def _async_import_module(self, module_name: str) -> ModuleType:
        """Load a module asyncronously."""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None, partial(importlib.import_module, module_name)
        )

    def get_differences(self, other: GeckoAsyncStructure) -> list[str]:
        """Get the differences between this structure and the other."""
        results = []
        if len(self.accessors) != len(other.accessors):
            results.append(
                f"Accessor length difference. I have {len(self.accessors)},"
                f" the other has {len(other.accessors)}"
            )

        # List my unique accessors
        unique_to_me = [
            self.accessors[key] for key in self.accessors if key not in other.accessors
        ]
        results.extend([f"Only me: {acc}" for acc in unique_to_me])

        # List other unique accessors
        unique_to_other = [
            other.accessors[key] for key in other.accessors if key not in self.accessors
        ]
        results.extend([f"Only other: {acc}" for acc in unique_to_other])

        # List shared accessor differences
        key_differences = [
            key
            for key in self.accessors
            if key in other.accessors and self.accessors[key] != other.accessors[key]
        ]
        results.extend(
            [
                f"Diff: {self.accessors[key]} != {other.accessors[key]}"
                for key in key_differences
            ]
        )

        return results

    ############################################################################
    #
    #   DRY functionality

    async def load_pack_class(self, plateform_key: str) -> None:
        """Load the pack class for this structure."""
        self.plateform_key = plateform_key
        pack_module_name = f"geckolib.driver.packs.{plateform_key}"
        pack_class = (await self._async_import_module(pack_module_name)).GeckoPack
        self.pack_class = pack_class(self)
        self.pack_type = self.pack_class.plateform_type

    async def load_config_module(self, config_version: int) -> None:
        """Load the config pack class for this structure."""
        config_module_name = (
            f"geckolib.driver.packs.{self.plateform_key}-cfg-{config_version}"
        )
        config_class = (
            await self._async_import_module(config_module_name)
        ).GeckoConfigStruct
        self.config_version = config_version
        self.config_class = config_class(self)

    async def load_log_module(self, log_version: int) -> None:
        """Load the log pack class for this structure."""
        log_module_name = (
            f"geckolib.driver.packs.{self.plateform_key}-log-{log_version}"
        )
        log_class = (await self._async_import_module(log_module_name)).GeckoLogStruct
        self.log_version = log_version
        self.log_class = log_class(self)

    def get_snapshot_data(self) -> dict:
        """Get snapshot data that the structure can supply."""
        pack_id = GeckoConstants.KEY_PACK_CONFIG_ID
        if pack_id not in self.accessors:
            pack_id = GeckoConstants.KEY_PACK_CORE_ID
        rev_id = GeckoConstants.KEY_PACK_CONFIG_REV
        if rev_id not in self.accessors:
            rev_id = GeckoConstants.KEY_PACK_CORE_REV
        rel_id = GeckoConstants.KEY_PACK_CONFIG_REL
        if rel_id not in self.accessors:
            rel_id = GeckoConstants.KEY_PACK_CORE_REL

        return {
            "Library Version": VERSION,
            "SpaPackStruct.xml revision": self.pack_class.revision,
            "Spa pack": f"{self.accessors[GeckoConstants.KEY_PACK_TYPE].value}"
            f" {
                self.accessors[pack_id].value
                if pack_id in self.accessors
                else ' (NO PACK)'
            }"
            f" v{
                self.accessors[rev_id].value
                if rev_id in self.accessors
                else ' (NO REV)'
            }"
            f".{
                self.accessors[rel_id].value
                if rel_id in self.accessors
                else ' (NO REL)'
            }",
            "Low level configuration #": self.accessors[
                GeckoConstants.KEY_CONFIG_NUMBER
            ].value
            if GeckoConstants.KEY_CONFIG_NUMBER in self.accessors
            else "(NO CONFIG #)",
            "Log version": self.log_version,
            "Config version": self.config_version,
            "Pack type": self.pack_type,
            "Snapshot UTC Time": f"{datetime.datetime.now(tz=datetime.UTC)}",
            "Status Block": [hex(b) for b in self.status_block],
        }

    def build_connections(self) -> None:
        """Scan the spa pack outputs to generate a list of connections."""
        _LOGGER.debug("All outputs are %s", self.all_outputs)

        self.connections = [
            value
            for output in self.all_outputs
            if (value := self.accessors[output].value) not in ["NA", "Not_Set"]
        ]

        _LOGGER.debug("Connections are %s", self.connections)

    ############################################################################
    #
    #   Accessory support

    @property
    def is_mr_steam(self) -> bool:
        """Is this a MrSteam pack."""
        return self.plateform_key == "mrsteam"

    async def check_for_accessories(self) -> None:
        """After the initial pack has been loaded, check for accessories too."""
        inmix_packtype = GeckoByteStructAccessor(self, "inMix-PackType", 628, None)
        if inmix_packtype.value == INMIX_PACKTYPE:
            inmix_configlib = GeckoByteStructAccessor(
                self, "inMix-ConfigLib", 634, None
            )
            inmix_statuslib = GeckoByteStructAccessor(
                self, "inMix-StatusLib", 635, None
            )
            await self.load_inmix_config_module(inmix_configlib.value)
            await self.load_inmix_log_module(inmix_statuslib.value)

    async def load_inmix_config_module(self, config_version: int) -> None:
        """Load the config module for the inmix system."""
        config_module_name = f"geckolib.driver.packs.inmix-cfg-{config_version}"
        config_class = (
            await self._async_import_module(config_module_name)
        ).GeckoConfigStruct
        self.inmix_config_class = config_class(self)
        self.inmix_config_accessors = self.inmix_config_class.accessors

    async def load_inmix_log_module(self, log_version: int) -> None:
        """Load the config module for the inmix system."""
        log_module_name = f"geckolib.driver.packs.inmix-log-{log_version}"
        log_class = (await self._async_import_module(log_module_name)).GeckoLogStruct
        self.inmix_log_class = log_class(self)
        self.inmix_log_accessors = self.inmix_log_class.accessors
