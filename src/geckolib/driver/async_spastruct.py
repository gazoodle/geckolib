"""Async Spa Structure block."""

import asyncio
from functools import partial
import importlib
import logging
from types import ModuleType
from typing import Any

from geckolib.const import GeckoConstants

_LOGGER = logging.getLogger(__name__)


class GeckoAsyncStructure:
    """Class to host/manage the raw data block for a spa structure."""

    def __init__(self, on_async_set_value) -> None:
        """Initialize the async version."""
        self._on_async_set_value = on_async_set_value
        self.accessors = {}
        self.reset()

    def replace_status_block_segment(self, offset, segment) -> None:
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
        self.accessors = dict(self.config_class.accessors, **self.log_class.accessors)
        # Get all outputs
        self.all_outputs = self.config_class.output_keys
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
        self._status_block: bytes = b"\x00" * 1024

    async def get(self, protocol, create_func, retry_count=10):
        _LOGGER.debug("Async get for struct")
        async with protocol.Lock:
            while retry_count > 0:
                # Create the request
                request = create_func()

                # Queue it for delivery
                protocol.queue_send(request)

                # Setup some controls for the multiple responses expected
                next_expected = 0
                segments = []

                while True:
                    # Wait for a response up to a certain amount of time
                    await request.wait_for_response(protocol)
                    if request.has_timedout:
                        _LOGGER.debug("timeout waiting for any block")
                        break

                    if next_expected == request.sequence:
                        segments.append(request.data)
                        next_expected = request.next

                        if request.next == 0:
                            _LOGGER.debug(
                                "Status block segments complete, update and complete"
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

                retry_count -= 1
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
        self.config_class = config_class(self)

    async def load_log_module(self, log_version: int) -> None:
        """Load the log pack class for this structure."""
        log_module_name = (
            f"geckolib.driver.packs.{self.plateform_key}-log-{log_version}"
        )
        log_class = (await self._async_import_module(log_module_name)).GeckoLogStruct
        self.log_class = log_class(self)
