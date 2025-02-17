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
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "inClear-32K-Hours": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-Hours", 544, None
            ),
            "inClear-32K-FlowState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-FlowState",
                545,
                0,
                ["NO_FLOW", "FLOW"],
                None,
                2,
                None,
            ),
            "inClear-32K-CellPolarity": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-CellPolarity",
                545,
                1,
                ["OUT1", "OUT2"],
                None,
                2,
                None,
            ),
            "inClear-32K-PowerUp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-PowerUp", 545, 2, None
            ),
            "inClear-32K-ResistivityCheck": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-ResistivityCheck",
                545,
                3,
                None,
            ),
            "inClear-32K-MaintenanceQtyByte0": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-MaintenanceQtyByte0",
                546,
                None,
            ),
            "inClear-32K-MaintenanceQtyByte1": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-MaintenanceQtyByte1",
                547,
                None,
            ),
            "inClear-32K-MaintenanceQtyByte2": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-MaintenanceQtyByte2",
                548,
                None,
            ),
            "inClear-32K-MaintenanceQtyByte3": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-MaintenanceQtyByte3",
                549,
                None,
            ),
            "inClear-32K-BoostQtyByte0": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BoostQtyByte0", 550, None
            ),
            "inClear-32K-BoostQtyByte1": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BoostQtyByte1", 551, None
            ),
            "inClear-32K-BoostQtyByte2": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BoostQtyByte2", 552, None
            ),
            "inClear-32K-BoostQtyByte3": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BoostQtyByte3", 553, None
            ),
            "inClear-32K-RemainMinutes": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-RemainMinutes", 554, None
            ),
            "inClear-32K-MaintenanceCurrent": GeckoWordStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-MaintenanceCurrent",
                556,
                None,
            ),
            "inClear-32K-BoostCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BoostCurrent", 558, None
            ),
            "inClear-32K-NeededCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-NeededCurrent", 560, None
            ),
            "inClear-32K-SupplyVoltage": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-SupplyVoltage", 562, None
            ),
            "inClear-32K-CellCurrent": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-CellCurrent", 564, None
            ),
            "inClear-32K-PwmValue": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-PwmValue", 566, None
            ),
            "inClear-32K-Resistivity": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-Resistivity", 568, None
            ),
            "inClear-32K-LoSupplyError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-LoSupplyError", 570, 0, None
            ),
            "inClear-32K-LoSaltError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-LoSaltError", 570, 1, None
            ),
            "inClear-32K-LoSaltWarning": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-LoSaltWarning", 570, 2, None
            ),
            "inClear-32K-HiSaltWarning": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-HiSaltWarning", 570, 3, None
            ),
            "inClear-32K-HiSaltError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-HiSaltError", 570, 5, None
            ),
            "inClear-32K-FloError": GeckoBoolStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-FloError", 570, 6, None
            ),
            "inClear-32K-CompatibilityError": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-CompatibilityError",
                570,
                7,
                None,
            ),
            "inClear-32K-NumberOfResets": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-NumberOfResets", 571, None
            ),
            "inClear-32K-Action": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-Action",
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
            "inClear-32K-Menu": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-Menu",
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
            "inClear-32K-BootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BootID", 575, None
            ),
            "inClear-32K-BootRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BootRev", 577, None
            ),
            "inClear-32K-BootRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-BootRel", 578, None
            ),
            "inClear-32K-PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-PackType",
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
            "inClear-32K-MemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-MemRange",
                580,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "inClear-32K-FirmwareID": GeckoWordStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-FirmwareID", 581, None
            ),
            "inClear-32K-FirmwareRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-FirmwareRev", 583, None
            ),
            "inClear-32K-FirmwareRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-FirmwareRel", 584, None
            ),
            "inClear-32K-ConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-ConfigLib", 585, None
            ),
            "inClear-32K-StatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-StatusLib", 586, None
            ),
            "inClear-32K-ResVariation": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-ResVariation", 587, None
            ),
            "inClear-32K-MinimumFlowTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/All/inClear-32K-MinimumFlowTime", 588, None
            ),
            "inClear-32K-InvalidRemoteFlow": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-InvalidRemoteFlow",
                589,
                0,
                ["USE_PACK_FLOW", "NOT_USE_PACK_FLOW"],
                None,
                2,
                "ALL",
            ),
            "inClear-32K-DoNotForceFilter": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-DoNotForceFilter",
                589,
                1,
                ["FORCE_FILTER", "NOT_FORCE_FILTER"],
                None,
                2,
                "ALL",
            ),
            "inClear-32K-PSNotInstalled": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/All/inClear-32K-PSNotInstalled",
                589,
                2,
                ["WITH_PS", "WITHOUT_PS"],
                None,
                2,
                None,
            ),
        }
