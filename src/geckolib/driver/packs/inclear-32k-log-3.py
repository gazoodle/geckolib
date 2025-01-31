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
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 544, None),
            "FlowState": GeckoEnumStructAccessor(
                self.struct, "FlowState", 545, 0, ["NO_FLOW", "FLOW"], None, 2, None
            ),
            "CellPolarity": GeckoEnumStructAccessor(
                self.struct, "CellPolarity", 545, 1, ["OUT1", "OUT2"], None, 2, None
            ),
            "PowerUp": GeckoBoolStructAccessor(self.struct, "PowerUp", 545, 2, None),
            "ResistivityCheck": GeckoBoolStructAccessor(
                self.struct, "ResistivityCheck", 545, 3, None
            ),
            "MaintenanceQtyByte0": GeckoByteStructAccessor(
                self.struct, "MaintenanceQtyByte0", 546, None
            ),
            "MaintenanceQtyByte1": GeckoByteStructAccessor(
                self.struct, "MaintenanceQtyByte1", 547, None
            ),
            "MaintenanceQtyByte2": GeckoByteStructAccessor(
                self.struct, "MaintenanceQtyByte2", 548, None
            ),
            "MaintenanceQtyByte3": GeckoByteStructAccessor(
                self.struct, "MaintenanceQtyByte3", 549, None
            ),
            "BoostQtyByte0": GeckoByteStructAccessor(
                self.struct, "BoostQtyByte0", 550, None
            ),
            "BoostQtyByte1": GeckoByteStructAccessor(
                self.struct, "BoostQtyByte1", 551, None
            ),
            "BoostQtyByte2": GeckoByteStructAccessor(
                self.struct, "BoostQtyByte2", 552, None
            ),
            "BoostQtyByte3": GeckoByteStructAccessor(
                self.struct, "BoostQtyByte3", 553, None
            ),
            "RemainMinutes": GeckoWordStructAccessor(
                self.struct, "RemainMinutes", 554, None
            ),
            "MaintenanceCurrent": GeckoWordStructAccessor(
                self.struct, "MaintenanceCurrent", 556, None
            ),
            "BoostCurrent": GeckoWordStructAccessor(
                self.struct, "BoostCurrent", 558, None
            ),
            "NeededCurrent": GeckoWordStructAccessor(
                self.struct, "NeededCurrent", 560, None
            ),
            "SupplyVoltage": GeckoWordStructAccessor(
                self.struct, "SupplyVoltage", 562, None
            ),
            "CellCurrent": GeckoWordStructAccessor(
                self.struct, "CellCurrent", 564, None
            ),
            "PwmValue": GeckoWordStructAccessor(self.struct, "PwmValue", 566, None),
            "Resistivity": GeckoWordStructAccessor(
                self.struct, "Resistivity", 568, None
            ),
            "LoSupplyError": GeckoBoolStructAccessor(
                self.struct, "LoSupplyError", 570, 0, None
            ),
            "LoSaltError": GeckoBoolStructAccessor(
                self.struct, "LoSaltError", 570, 1, None
            ),
            "LoSaltWarning": GeckoBoolStructAccessor(
                self.struct, "LoSaltWarning", 570, 2, None
            ),
            "HiSaltWarning": GeckoBoolStructAccessor(
                self.struct, "HiSaltWarning", 570, 3, None
            ),
            "HiSaltError": GeckoBoolStructAccessor(
                self.struct, "HiSaltError", 570, 5, None
            ),
            "FloError": GeckoBoolStructAccessor(self.struct, "FloError", 570, 6, None),
            "CompatibilityError": GeckoBoolStructAccessor(
                self.struct, "CompatibilityError", 570, 7, None
            ),
            "NumberOfResets": GeckoWordStructAccessor(
                self.struct, "NumberOfResets", 571, None
            ),
            "Action": GeckoEnumStructAccessor(
                self.struct,
                "Action",
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
                "Menu",
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
            "BootID": GeckoWordStructAccessor(self.struct, "BootID", 575, None),
            "BootRev": GeckoByteStructAccessor(self.struct, "BootRev", 577, None),
            "BootRel": GeckoByteStructAccessor(self.struct, "BootRel", 578, None),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "PackType",
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
                "MemRange",
                580,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "FirmwareID": GeckoWordStructAccessor(self.struct, "FirmwareID", 581, None),
            "FirmwareRev": GeckoByteStructAccessor(
                self.struct, "FirmwareRev", 583, None
            ),
            "FirmwareRel": GeckoByteStructAccessor(
                self.struct, "FirmwareRel", 584, None
            ),
            "ConfigLib": GeckoByteStructAccessor(self.struct, "ConfigLib", 585, None),
            "StatusLib": GeckoByteStructAccessor(self.struct, "StatusLib", 586, None),
            "ResVariation": GeckoByteStructAccessor(
                self.struct, "ResVariation", 587, None
            ),
            "MinimumFlowTime": GeckoByteStructAccessor(
                self.struct, "MinimumFlowTime", 588, None
            ),
            "InvalidRemoteFlow": GeckoEnumStructAccessor(
                self.struct,
                "InvalidRemoteFlow",
                589,
                0,
                ["USE_PACK_FLOW", "NOT_USE_PACK_FLOW"],
                None,
                2,
                "ALL",
            ),
            "DoNotForceFilter": GeckoEnumStructAccessor(
                self.struct,
                "DoNotForceFilter",
                589,
                1,
                ["FORCE_FILTER", "NOT_FORCE_FILTER"],
                None,
                2,
                "ALL",
            ),
            "PSNotInstalled": GeckoEnumStructAccessor(
                self.struct,
                "PSNotInstalled",
                589,
                2,
                ["WITH_PS", "WITHOUT_PS"],
                None,
                2,
                None,
            ),
        }
