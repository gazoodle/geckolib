"""GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v3'."""  # noqa: N999

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
        return 3

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Prog1SetpointG": GeckoTempStructAccessor(
                self.struct, "ConfigStructure/All/Prog1SetpointG", 0, "ALL"
            ),
            "Prog1Runtime": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/All/Prog1Runtime", 2, "ALL"
            ),
            "Prog1Aroma": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/Prog1Aroma",
                4,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "Prog2SetpointG": GeckoTempStructAccessor(
                self.struct, "ConfigStructure/All/Prog2SetpointG", 5, "ALL"
            ),
            "Prog2Runtime": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/All/Prog2Runtime", 7, "ALL"
            ),
            "Prog2Aroma": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/Prog2Aroma",
                9,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/TempUnits",
                10,
                None,
                ["F", "C"],
                None,
                None,
                "ALL",
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "ConfigStructure/All/MinSetpointG", 11, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "ConfigStructure/All/MaxSetpointG", 13, "ALL"
            ),
            "ValveOut1Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/ValveOut1Type",
                15,
                None,
                ["NONE", "HEAD", "BODY", "WAND"],
                None,
                None,
                "ALL",
            ),
            "ValveOut2Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/ValveOut2Type",
                16,
                None,
                ["NONE", "HEAD", "BODY", "WAND"],
                None,
                None,
                "ALL",
            ),
            "ValveOut3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/ValveOut3Type",
                17,
                None,
                ["NONE", "HEAD", "BODY", "WAND"],
                None,
                None,
                "ALL",
            ),
        }
