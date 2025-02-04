"""GeckoPack - A class to manage the pack for 'InK600-64K'."""  # noqa: N999

from . import GeckoAsyncStructure


class GeckoPack:
    """A GeckoPack class for a specific spa."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the GeckoPack class."""
        self.struct = struct_

    @property
    def name(self) -> str:
        """Get the plateform name."""
        return "InK600-64K"

    @property
    def plateform_type(self) -> int:
        """Get the plateform type."""
        return 7

    @property
    def plateform_segment(self) -> str:
        """Get the plateform segment."""
        return "aK600UpperControl"

    @property
    def revision(self) -> str:
        """Get the SpaPackStruct revision."""
        return "39.0"
