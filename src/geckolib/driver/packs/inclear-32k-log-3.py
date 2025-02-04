"""GeckoLogStruct - A class to manage the LogStruct for 'inClear-32K v3'."""  # noqa: N999

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
        return 3

    @property
    def begin(self) -> int:
        """Get the offset start."""
        return 544

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 589

    @property
    def all_device_keys(self) -> list[str]:
        """Get all device keys."""
        return ["LI"]

    @property
    def user_demand_keys(self) -> list[str]:
        """Get all user demand keys."""
        return []

    @property
    def error_keys(self) -> list[str]:
        """Get all error keys."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Hours": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/Hours", 544, None
            ),
            "FlowState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/FlowState",
                545,
                0,
                ["NO_FLOW", "FLOW"],
                None,
                2,
                None,
            ),
            "CellPolarity": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/CellPolarity",
                545,
                1,
                ["OUT1", "OUT2"],
                None,
                2,
                None,
            ),
            "PowerUp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/PowerUp", 545, 2, None
            ),
            "ResistivityCheck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/ResistivityCheck", 545, 3, None
            ),
            "MaintenanceQtyByte0": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/MaintenanceQtyByte0", 546, None
            ),
            "MaintenanceQtyByte1": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/MaintenanceQtyByte1", 547, None
            ),
            "MaintenanceQtyByte2": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/MaintenanceQtyByte2", 548, None
            ),
            "MaintenanceQtyByte3": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/MaintenanceQtyByte3", 549, None
            ),
            "BoostQtyByte0": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/BoostQtyByte0", 550, None
            ),
            "BoostQtyByte1": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/BoostQtyByte1", 551, None
            ),
            "BoostQtyByte2": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/BoostQtyByte2", 552, None
            ),
            "BoostQtyByte3": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/BoostQtyByte3", 553, None
            ),
            "RemainMinutes": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/RemainMinutes", 554, None
            ),
            "MaintenanceCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/MaintenanceCurrent", 556, None
            ),
            "BoostCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/BoostCurrent", 558, None
            ),
            "NeededCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/NeededCurrent", 560, None
            ),
            "SupplyVoltage": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/SupplyVoltage", 562, None
            ),
            "CellCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/CellCurrent", 564, None
            ),
            "PwmValue": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/PwmValue", 566, None
            ),
            "Resistivity": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/Resistivity", 568, None
            ),
            "LoSupplyError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/LoSupplyError", 570, 0, None
            ),
            "LoSaltError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/LoSaltError", 570, 1, None
            ),
            "LoSaltWarning": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/LoSaltWarning", 570, 2, None
            ),
            "HiSaltWarning": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/HiSaltWarning", 570, 3, None
            ),
            "HiSaltError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/HiSaltError", 570, 5, None
            ),
            "FloError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/FloError", 570, 6, None
            ),
            "CompatibilityError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/CompatibilityError", 570, 7, None
            ),
            "NumberOfResets": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/NumberOfResets", 571, None
            ),
            "Action": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/Action",
                573,
                None,
                [
                    "IDLE",
                    "SYSTEM_OFF",
                    "SYSTEM_ON",
                    "BOOST_OFF",
                    "BOOST_ON",
                    "DIAGNOSTIC_OFF",
                    "DIAGNOSTIC_ON",
                ],
                None,
                None,
                "ALL",
            ),
            "Menu": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/Menu",
                574,
                None,
                [
                    "NORMAL",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "NBR_RESET_MENU",
                    "NBR_RESET_TITLE",
                    "LOWLEVEL_ADJ",
                    "LOWLEVEL_TITLE",
                    "DIAGNOSTIC_MENU",
                ],
                None,
                None,
                None,
            ),
            "BootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/BootID", 575, None
            ),
            "BootRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/BootRev", 577, None
            ),
            "BootRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/BootRel", 578, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/PackType",
                579,
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
                ],
                None,
                None,
                None,
            ),
            "MemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/MemRange",
                580,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "FirmwareID": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/FirmwareID", 581, None
            ),
            "FirmwareRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/FirmwareRev", 583, None
            ),
            "FirmwareRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/FirmwareRel", 584, None
            ),
            "ConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/ConfigLib", 585, None
            ),
            "StatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/StatusLib", 586, None
            ),
            "ResVariation": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/ResVariation", 587, None
            ),
            "MinimumFlowTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/MinimumFlowTime", 588, None
            ),
            "InvalidRemoteFlow": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/InvalidRemoteFlow",
                589,
                0,
                ["USE_PACK_FLOW", "NOT_USE_PACK_FLOW"],
                None,
                2,
                "ALL",
            ),
            "DoNotForceFilter": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/DoNotForceFilter",
                589,
                1,
                ["FORCE_FILTER", "NOT_FORCE_FILTER"],
                None,
                2,
                "ALL",
            ),
            "PSNotInstalled": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/PSNotInstalled",
                589,
                2,
                ["WITH_PS", "WITHOUT_PS"],
                None,
                2,
                None,
            ),
        }
