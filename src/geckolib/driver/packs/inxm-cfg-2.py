"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v2'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoTempStructAccessor,
    GeckoTimeStructAccessor,
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
        return [
            "Out1A",
            "Out1B",
            "Out2A",
            "Out2B",
            "Out3A",
            "OutHeater",
            "Out4A",
            "Out5A",
            "Out6A",
            "Out7A",
            "OutLi",
            "OutIO2",
            "OutIO4",
            "LightActivationOrder",
        ]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/ConfigNumber", 1, "ALL"
            ),
            "Out1A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out1A",
                200,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out1B": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out1B",
                201,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out2A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out2A",
                202,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out2B": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out2B",
                203,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out3A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out3A",
                204,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "OutHeater": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/OutHeater",
                209,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out1ACurrent", 220, "ALL"
            ),
            "Out1BCurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out1BCurrent", 221, "ALL"
            ),
            "Out2ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out2ACurrent", 222, "ALL"
            ),
            "Out2BCurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out2BCurrent", 223, "ALL"
            ),
            "Out3ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out3ACurrent", 224, "ALL"
            ),
            "Out4A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out4A",
                205,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out5A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out5A",
                206,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out6A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out6A",
                207,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out7A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out7A",
                208,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out4ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out4ACurrent", 225, "ALL"
            ),
            "Out5ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out5ACurrent", 226, "ALL"
            ),
            "Out6ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out6ACurrent", 227, "ALL"
            ),
            "Out7ACurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out7ACurrent", 228, "ALL"
            ),
            "DirectCurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/DirectCurrent", 123, "ALL"
            ),
            "OutLi": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutLi",
                210,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                "ALL",
            ),
            "OutIO2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutIO2",
                211,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "OutIO4": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutIO4",
                212,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "HTR",
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "LightInts": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LVOutputConfig/LightInts", 84, "ALL"
            ),
            "LightActivationOrder": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/LightActivationOrder",
                17,
                0,
                ["Ascendant", "Descendant"],
                None,
                2,
                "ALL",
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 18, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/FiberTimeOut", 19, "ALL"
            ),
            "LightResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/LightResetTimeOut",
                17,
                1,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 20, "ALL"
            ),
            "PumpResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/PumpResetTimeOut",
                17,
                2,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpTimeOutShare": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOutShare", 17, 3, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/QuietTimeOut", 69, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                35,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CleanP1", 33, 1, "ALL"
            ),
            "CleanCP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CleanCP", 33, 2, "ALL"
            ),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltOTOption", 34, 0, "ALL"
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CPAlwaysON", 33, 3, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltCPOTOption", 34, 1, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltSuspendBy",
                34,
                2,
                ["AnyUD", "PumpUD"],
                None,
                2,
                "ALL",
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltCPOTLimitOption",
                34,
                3,
                ["AlwaysEnabled", "LimitedIfSPBelow95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/PurgeSpeed",
                33,
                0,
                ["Lo", "Hi"],
                None,
                2,
                "ALL",
            ),
            "FiltMinDur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/AdvanceFilterConfig/FiltMinDur", 57, "ALL"
            ),
            "FiltOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTActTemp",
                55,
                "ALL",
            ),
            "FiltOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTDeadband",
                56,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                62,
                "ALL",
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTActTemp",
                58,
                "ALL",
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTDeadband",
                59,
                "ALL",
            ),
            "FiltCPMinOnTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPMinOnTime",
                60,
                "ALL",
            ),
            "FiltCPOTMaxDur": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTMaxDur",
                61,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3/O3Pump",
                63,
                0,
                ["NONE", "P1", "CP", ""],
                None,
                4,
                "ALL",
            ),
            "O3FollowPump": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3FollowPump", 63, 2, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3DuringFilt", 63, 3, "ALL"
            ),
            "O3Toggling": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3Toggling", 63, 4, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3/O3SuspendBy",
                63,
                6,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3FilterDelay", 64, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3SuspendTime", 65, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3TogglePeriod", 66, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltFreq",
                36,
                "ALL",
            ),
            "FiltStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltStart",
                37,
                "ALL",
            ),
            "FiltDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltDur", 39, "ALL"
            ),
            "EconStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStart",
                71,
                "ALL",
            ),
            "EconStop": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStop",
                73,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                68,
                3,
                "ALL",
            ),
            "EconProgStatus": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgStatus",
                68,
                4,
                ["Disabled", "NotActive", "NA", "Active"],
                None,
                4,
                "ALL",
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/BlowerKeyOption",
                17,
                4,
                ["LastPumpKey", "NextFreePumpKey", "AnyFreePump"],
                None,
                4,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/QuickOnOffKeyEnable",
                17,
                6,
                "ALL",
            ),
            "K600Msg1NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg1NbWeek", 75, "ALL"
            ),
            "K600Msg2NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg2NbWeek", 76, "ALL"
            ),
            "K600Msg3NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg3NbWeek", 77, "ALL"
            ),
            "K600Msg4NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg4NbWeek", 78, "ALL"
            ),
            "K600Msg5NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg5NbWeek", 79, "ALL"
            ),
            "K600Msg6NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg6NbWeek", 80, "ALL"
            ),
            "K600Msg7NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg7NbWeek", 81, "ALL"
            ),
            "K600Msg8NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg8NbWeek", 82, "ALL"
            ),
            "SWMPurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SWM/SWMPurgeSpeed",
                67,
                0,
                ["Low", "High"],
                None,
                2,
                "ALL",
            ),
            "SWMPurgeBlower": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/SWM/SWMPurgeBlower", 67, 1, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineFrequency",
                83,
                4,
                ["60HZ", "50HZ"],
                None,
                2,
                "ALL",
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineVoltage",
                83,
                5,
                ["240Vac", "230VAC"],
                None,
                2,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/NbPhases", 85, None
            ),
            "BrNbSettings": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrNbSettings", 86, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrSetIndex", 87, None
            ),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet1", 88, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet2", 89, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet3", 90, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet4", 91, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet5", 92, "ALL"
            ),
            "BreakerMenu": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/BreakerMenu",
                83,
                7,
                ["Available", "NotAvailable"],
                None,
                2,
                "ALL",
            ),
            "FuseMapping": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/FuseMapping",
                83,
                1,
                [
                    "UL",
                    "CE_Jmp1_3_Installed",
                    "CE_Jmp1_4_Installed",
                    "CE_Jmp2_3_Installed",
                    "CE_Jmp2_4_Installed",
                    "",
                    "",
                    "",
                ],
                None,
                8,
                "ALL",
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/QuietActionOnHeater",
                23,
                3,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/UDActionOnQuiet",
                68,
                1,
                [
                    "IgnoreUD",
                    "ExitQuietAndRestoreAllUD",
                    "NA",
                    "ExitQuietAndCancelOtherUD",
                ],
                None,
                4,
                "ALL",
            ),
            "QuietActionOnUD": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/QuietActionOnUD",
                68,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Fan/FanPump",
                24,
                1,
                ["None", "P1", "CP"],
                None,
                4,
                "ALL",
            ),
            "FanAsCoolingDevice": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanAsCoolingDevice", 24, 3, "ALL"
            ),
            "FanActiveOnAmbiantOT": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnAmbiantOT", 23, 5, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnPumpRun", 23, 6, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOFFOption", 23, 7, "ALL"
            ),
            "FanSetAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetAOTTempAdc", 27, "ALL"
            ),
            "FanClrAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrAOTTempAdc", 28, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveDelayAfterPumpRun", 29, "ALL"
            ),
            "FanSetForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetForceOffTempAdc", 30, "ALL"
            ),
            "FanClrForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrForceOffTempAdc", 31, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOffInhibitDelay", 32, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeaterPump",
                23,
                None,
                ["", "CP", "P1"],
                None,
                4,
                "ALL",
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeatRestriction",
                83,
                6,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "ExtProbeEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/ExtProbeEnable",
                24,
                4,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                23,
                2,
                ["C", "F"],
                None,
                2,
                "ALL",
            ),
            "SetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/SetpointG",
                25,
                "ALL",
            ),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/EconBelowSetpoint",
                70,
                "ALL",
            ),
            "AmbiantOTEnable": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOTEnable", 24, 0, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                83,
                0,
                ["AmPm", "24h"],
                None,
                2,
                "ALL",
            ),
            "Aux1AsTVLifter": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/Aux1AsTVLifter", 21, 0, "ALL"
            ),
            "Aux2AsSpeakerLifter": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/Aux2AsSpeakerLifter", 21, 1, "ALL"
            ),
            "DJS_No1": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/DJS_No1",
                21,
                2,
                ["NA", "OnP1", "OnP2", "OnP3"],
                None,
                4,
                "ALL",
            ),
            "DJS_No2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/DJS_No2",
                21,
                4,
                ["NA", "OnP1", "OnP2", "OnP3"],
                None,
                4,
                "ALL",
            ),
        }
