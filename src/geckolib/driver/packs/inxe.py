"""GeckoPack - A class to manage the pack for 'InXE'."""

from . import GeckoStructureTypeBase


class GeckoPack:
    """A GeckoPack class for a specific spa."""

    def __init__(self, struct_: GeckoStructureTypeBase) -> None:
        """Initialize the GeckoPack class."""
        self.struct = struct_

    @property
    def name(self) -> str:
        """Get the plateform name."""
        return "InXE"

    @property
    def plateform_type(self) -> int:
        """Get the plateform type."""
        return 1

    @property
    def revision(self) -> str:
        """Get the SpaPackStruct revision."""
        return "39.0"
