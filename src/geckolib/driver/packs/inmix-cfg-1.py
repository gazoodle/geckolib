"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InMix v1'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
)


class GeckoConfigStruct:
    """Config Struct Class."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the config struct class."""
        self.struct = struct_

    @property
    def version(self) -> int:
        """Get the config struct class version."""
        return 1

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Zone1Led": GeckoEnumStructAccessor(
                self.struct, "Zone1Led", 592, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone1Type": GeckoEnumStructAccessor(
                self.struct, "Zone1Type", 592, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone1Supply": GeckoEnumStructAccessor(
                self.struct, "Zone1Supply", 592, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone2Led": GeckoEnumStructAccessor(
                self.struct, "Zone2Led", 593, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone2Type": GeckoEnumStructAccessor(
                self.struct, "Zone2Type", 593, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone2Supply": GeckoEnumStructAccessor(
                self.struct, "Zone2Supply", 593, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone3Led": GeckoEnumStructAccessor(
                self.struct, "Zone3Led", 594, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone3Type": GeckoEnumStructAccessor(
                self.struct, "Zone3Type", 594, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone3Supply": GeckoEnumStructAccessor(
                self.struct, "Zone3Supply", 594, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone4Led": GeckoEnumStructAccessor(
                self.struct, "Zone4Led", 595, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone4Type": GeckoEnumStructAccessor(
                self.struct, "Zone4Type", 595, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone4Supply": GeckoEnumStructAccessor(
                self.struct, "Zone4Supply", 595, 2, ["12V", "5V"], None, 2, None
            ),
        }
