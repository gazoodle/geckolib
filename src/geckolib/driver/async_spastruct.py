""" Async Spa Structure block """

import logging


_LOGGER = logging.getLogger(__name__)


class GeckoAsyncStructure:
    """Class to host/manage the raw data block for a spa structure"""

    def __init__(self, on_set_value, on_async_set_value):
        self._on_set_value = on_set_value
        self._on_async_set_value = on_async_set_value
        self.accessors = {}
        self.reset()

    def replace_status_block_segment(self, offset, segment):
        """Replace a segment of the status block"""
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
    def status_block(self):
        return self._status_block

    def set_status_block(self, block):
        self._status_block = block

    def build_accessors(self, config_class, log_class):
        self.accessors = dict(config_class.accessors, **log_class.accessors)
        # Get all outputs
        self.all_outputs = config_class.output_keys
        # Get collection of possible devices
        self.all_devices = log_class.all_device_keys
        # User devices are those that have a Ud in the tag name
        self.user_demands = log_class.user_demand_keys
        # Error keys
        self.error_keys = log_class.error_keys

    def reset(self) -> None:
        """Reset this status block to initialization state"""
        self.accessors = {}
        self.all_outputs = []
        self.all_devices = []
        self.user_demands = []
        self._status_block = b"\x00" * 1024

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
                    if await request.wait_for_response(protocol):

                        if next_expected == request.sequence:

                            segments.append(request.data)
                            next_expected = request.next

                            if request.next == 0:

                                _LOGGER.debug(
                                    (
                                        "Status block segments complete, "
                                        "update and complete"
                                    )
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

                    else:

                        _LOGGER.debug("timeout waiting for any block")
                        break

                retry_count -= 1
            return False

    def set_value(self, pos, length, newvalue):
        # Delegate this
        self._on_set_value(pos, length, newvalue)

    async def async_set_value(self, pos, length, newvalue):
        # Delegate this
        await self._on_async_set_value(pos, length, newvalue)
