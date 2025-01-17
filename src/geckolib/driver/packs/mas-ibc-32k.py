"""GeckoPack - A class to manage the pack for 'MAS-IBC-32K'."""  # noqa: N999

from . import GeckoStructureTypeBase


class GeckoPack:
    """A GeckoPack class for a specific spa."""

    def __init__(self, struct_: GeckoStructureTypeBase) -> None:
        """Initialize the GeckoPack class."""
        self.struct = struct_

    @property
    def name(self) -> str:
        """Get the plateform name."""
        return "MAS-IBC-32K"

    @property
    def type(self) -> int:
        """Get the plateform type."""
        return 2

    @property
    def revision(self) -> str:
        """Get the SpaPackStruct revision."""
        return "39.0"
