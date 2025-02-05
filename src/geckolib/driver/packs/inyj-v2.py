"""GeckoPack - A class to manage the pack for 'InYJ-V2'."""  # noqa: N999

from . import GeckoAsyncStructure


class GeckoPack:
    """A GeckoPack class for a specific spa."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the GeckoPack class."""
        self.struct = struct_

    @property
    def name(self) -> str:
        """Get the plateform name."""
        return "InYJ-V2"

    @property
    def plateform_type(self) -> int:
        """Get the plateform type."""
        return 12

    @property
    def plateform_segment(self) -> str:
        """Get the plateform segment."""
        return "aMainControl"

    @property
    def revision(self) -> str:
        """Get the SpaPackStruct revision."""
        return "39.0"
