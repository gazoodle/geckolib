"""GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v2'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoTempStructAccessor,
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
        return 2

    @property
    def begin(self) -> int:
        """Get the offset start."""
        return 256

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 301

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
            "FlashErr",
            "H2O2Err",
            "KeyStuckErr",
            "PowerFailErr",
            "Prr1Err",
            "Prr2Err",
            "Prr3Err",
            "Prr4Err",
            "SlaveH2O2Err",
        ]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "UserMode": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/UserMode",
                256,
                None,
                ["OFF", "ON", "DIAGNOSTIC"],
                None,
                None,
                "ALL",
            ),
            "UserPause": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Controls/UserPause", 257, 1, "ALL"
            ),
            "UserAroma": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/UserAroma",
                258,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "UserChroma": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/UserChroma",
                259,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "UserSetpointG": GeckoTempStructAccessor(
                self.struct, "LogStructure/Controls/UserSetpointG", 264, "ALL"
            ),
            "UserRuntime": GeckoWordStructAccessor(
                self.struct, "LogStructure/Controls/UserRuntime", 261, "ALL"
            ),
            "UserProg": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Controls/UserProg",
                263,
                None,
                ["User", "Prog1", "Prog2"],
                None,
                None,
                "ALL",
            ),
            "Hours": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/Hours", 268, None
            ),
            "ModeState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/ModeState",
                269,
                0,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "PauseState": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/PauseState", 269, 1, None
            ),
            "DiagnosticState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/DiagnosticState",
                269,
                2,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "ExternalProbe": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/ExternalProbe", 269, 3, None
            ),
            "WaterDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/WaterDetected", 269, 4, None
            ),
            "NoRegulation": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/NoRegulation", 269, 5, None
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/MasterSlave",
                269,
                6,
                ["SLAVE", "MASTER"],
                None,
                2,
                None,
            ),
            "KeypadProbe": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/KeypadProbe", 270, 0, None
            ),
            "ExpressCycle": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/ExpressCycle", 270, 1, None
            ),
            "SlaveOnState": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/SlaveOnState", 271, 1, None
            ),
            "SlaveHeaterState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/SlaveHeaterState",
                271,
                3,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "PowerFailErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/PowerFailErr", 272, 0, None
            ),
            "Prr2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Prr2Err", 272, 1, None
            ),
            "Prr1Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Prr1Err", 272, 2, None
            ),
            "H2O2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/H2O2Err", 272, 3, None
            ),
            "SlaveH2O2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/SlaveH2O2Err", 272, 4, None
            ),
            "KeyStuckErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/KeyStuckErr", 272, 5, None
            ),
            "FlashErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/FlashErr", 272, 6, None
            ),
            "Prr3Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Prr3Err", 272, 7, None
            ),
            "Prr4Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Prr4Err", 273, 0, None
            ),
            "Jumper9": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper9", 274, 0, None
            ),
            "Jumper2": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper2", 274, 1, None
            ),
            "Jumper3": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper3", 274, 2, None
            ),
            "Jumper4": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper4", 274, 3, None
            ),
            "Jumper5": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper5", 274, 4, None
            ),
            "Jumper6": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper6", 274, 5, None
            ),
            "Jumper7": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper7", 274, 6, None
            ),
            "Jumper8": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/Jumper8", 274, 7, None
            ),
            "MaxRuntime": GeckoWordStructAccessor(
                self.struct, "LogStructure/Status/MaxRuntime", 275, None
            ),
            "KeypadType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/KeypadType",
                277,
                None,
                ["NO_TSC", "SC_54", "TSC_53", "AUX_SW", "COLOR_SERIES"],
                None,
                None,
                None,
            ),
            "KeypadID": GeckoWordStructAccessor(
                self.struct, "LogStructure/Status/KeypadID", 298, None
            ),
            "KeypadRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/KeypadRev", 300, None
            ),
            "KeypadRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/KeypadRel", 301, None
            ),
            "RoomTempG": GeckoTempStructAccessor(
                self.struct, "LogStructure/Status/RoomTempG", 278, None
            ),
            "K1000TempG": GeckoTempStructAccessor(
                self.struct, "LogStructure/Status/K1000TempG", 296, "ALL"
            ),
            "RemainingRuntime": GeckoWordStructAccessor(
                self.struct, "LogStructure/Status/RemainingRuntime", 293, None
            ),
            "DrainValveOutput": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/DrainValveOutput", 295, 0, None
            ),
            "AromaOutput": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/AromaOutput", 295, 1, None
            ),
            "HeaterOutput": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/HeaterOutput", 295, 2, None
            ),
            "WaterValveOutput": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/WaterValveOutput", 295, 3, None
            ),
            "ChromaOutput": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Status/ChromaOutput", 295, 4, None
            ),
            "PackBootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootID", 281, None
            ),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRev", 283, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRel", 284, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackType",
                285,
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
                286,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackCoreID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreID", 287, None
            ),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRev", 289, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRel", 290, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfigLib", 291, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackStatusLib", 292, None
            ),
        }
