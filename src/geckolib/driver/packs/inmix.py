"""GeckoPack - A class to manage the pack for 'InMix'."""

from . import GeckoAsyncStructure


class GeckoPack:
    """A GeckoPack class for a specific spa."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the GeckoPack class."""
        self.struct = struct_

    @property
    def name(self) -> str:
        """Get the plateform name."""
        return "InMix"

    @property
    def plateform_type(self) -> int:
        """Get the plateform type."""
        return 14

    @property
    def revision(self) -> str:
        """Get the SpaPackStruct revision."""
        return "39.0"
