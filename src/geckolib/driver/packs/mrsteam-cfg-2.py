"""GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v2'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoTempStructAccessor,
    GeckoWordStructAccessor,
)


class GeckoConfigStruct:
    """Config Struct Class."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the config struct class."""
        self.struct = struct_

    @property
    def version(self) -> int:
        """Get the config struct class version."""
        return 2

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Prog1SetpointG": GeckoTempStructAccessor(
                self.struct, "Prog1SetpointG", 0, "ALL"
            ),
            "Prog1Runtime": GeckoWordStructAccessor(
                self.struct, "Prog1Runtime", 2, "ALL"
            ),
            "Prog1Aroma": GeckoEnumStructAccessor(
                self.struct, "Prog1Aroma", 4, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "Prog2SetpointG": GeckoTempStructAccessor(
                self.struct, "Prog2SetpointG", 5, "ALL"
            ),
            "Prog2Runtime": GeckoWordStructAccessor(
                self.struct, "Prog2Runtime", 7, "ALL"
            ),
            "Prog2Aroma": GeckoEnumStructAccessor(
                self.struct, "Prog2Aroma", 9, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 10, None, ["F", "C"], None, None, "ALL"
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "MinSetpointG", 11, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "MaxSetpointG", 13, "ALL"
            ),
        }
