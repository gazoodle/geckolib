"""GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v1'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
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
        return 1

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Prog1Setpoint": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/All/Prog1Setpoint", 0, "ALL"
            ),
            "Prog1Runtime": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/All/Prog1Runtime", 1, "ALL"
            ),
            "Prog1Aroma": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/Prog1Aroma",
                3,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "Prog2Setpoint": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/All/Prog2Setpoint", 4, "ALL"
            ),
            "Prog2Runtime": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/All/Prog2Runtime", 5, "ALL"
            ),
            "Prog2Aroma": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/Prog2Aroma",
                7,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/TempUnits",
                8,
                None,
                ["F", "C"],
                None,
                None,
                "ALL",
            ),
        }
