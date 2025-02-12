"""GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v1'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoWordStructAccessor,
)


class GeckoLogStruct:
    """Log Struct Class."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the log struct class."""
        self.struct = struct_

    @property
    def version(self) -> int:
        """Get the log struct class version."""
        return 1

    @property
    def begin(self) -> int:
        """Get the offset start."""
        return 256

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 280

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def all_device_keys(self) -> list[str]:
        """Get all device keys."""
        return []

    @property
    def user_demand_keys(self) -> list[str]:
        """Get all user demand keys."""
        return []

    @property
    def error_keys(self) -> list[str]:
        """Get all error keys."""
        return [
            "H2O2Err",
            "KeyStuckErr",
            "PowerFailErr",
            "Prr1Err",
            "Prr2Err",
            "SlaveH2O2Err",
        ]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Mode": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/Mode",
                257,
                0,
                ["OFF", "ON"],
                None,
                2,
                "ALL",
            ),
            "Pause": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Controls/Pause", 257, 1, "ALL"
            ),
            "Diagnostic": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Controls/Diagnostic", 257, 2, "ALL"
            ),
            "ChromaState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/ChromaState",
                257,
                3,
                ["OFF", "ON"],
                None,
                2,
                "ALL",
            ),
            "SelectedProg": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/SelectedProg",
                261,
                None,
                ["User", "Prog1", "Prog2"],
                None,
                None,
                "ALL",
            ),
            "UserSetpoint": GeckoByteStructAccessor(
                self.struct, "LogStructure/Controls/UserSetpoint", 262, "ALL"
            ),
            "UserRuntime": GeckoWordStructAccessor(
                self.struct, "LogStructure/Controls/UserRuntime", 263, "ALL"
            ),
            "UserAroma": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/UserAroma",
                265,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "Hours": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/Hours", 256, None
            ),
            "ExternalProbe": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/ExternalProbe", 258, 0, None
            ),
            "WaterDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/WaterDetected", 2658, 1, None
            ),
            "NoKeypad": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/NoKeypad", 258, 2, None
            ),
            "NoRegulation": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/NoRegulation", 258, 3, None
            ),
            "ExpressCycle": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/ExpressCycle", 258, 5, None
            ),
            "SlaveMode": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/SlaveMode",
                259,
                1,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "SlaveHeaterState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/SlaveHeaterState",
                259,
                3,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "PowerFailErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/PowerFailErr", 260, 0, None
            ),
            "Prr2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Prr2Err", 260, 1, None
            ),
            "Prr1Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Prr1Err", 260, 2, None
            ),
            "H2O2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/H2O2Err", 260, 3, None
            ),
            "SlaveH2O2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/SlaveH2O2Err", 260, 4, None
            ),
            "KeyStuckErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/KeyStuckErr", 260, 5, None
            ),
            "Jumper9": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper9", 266, 0, None
            ),
            "Jumper2": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper2", 266, 1, None
            ),
            "Jumper3": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper3", 266, 2, None
            ),
            "Jumper4": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper4", 266, 3, None
            ),
            "Jumper5": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper5", 266, 4, None
            ),
            "Jumper6": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper6", 266, 5, None
            ),
            "Jumper7": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper7", 266, 6, None
            ),
            "Jumper8": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper8", 266, 7, None
            ),
            "MaxRuntime": GeckoWordStructAccessor(
                self.struct, "LogStructure/Status/MaxRuntime", 267, None
            ),
            "PackBootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootID", 269, None
            ),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRev", 271, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRel", 272, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackType",
                273,
                None,
                [
                    "Unknown",
                    "inXE",
                    "MasIBC",
                    "MIA",
                    "DJS4",
                    "inClear",
                    "inXM",
                    "K600",
                    "inTerface",
                    "inTouch",
                    "inYT",
                    "Color_Keypad",
                    "inYJ",
                    "MrSteam",
                ],
                None,
                None,
                None,
            ),
            "PackMemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackMemRange",
                274,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackCoreID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreID", 275, None
            ),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRev", 277, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRel", 278, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfigLib", 279, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackStatusLib", 280, None
            ),
        }
