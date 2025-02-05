"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v3'."""  # noqa: N999

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
        return 3

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
                self.struct, "ConfigStructure/LVOutputConfig/LightInts", 96, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 18, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/FiberTimeOut", 19, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 20, "ALL"
            ),
            "L120Timer": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/L120Timer",
                21,
                6,
                ["Shared", "Own"],
                None,
                2,
                "ALL",
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/QuietTimeOut", 73, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                41,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CleanP1", 40, 1, "ALL"
            ),
            "CleanCP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CleanCP", 40, 2, "ALL"
            ),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltOTOption", 40, 4, "ALL"
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CPAlwaysON", 40, 3, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltCPOTOption", 40, 5, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltSuspendBy",
                40,
                6,
                ["AnyUD", "PumpUD"],
                None,
                2,
                "ALL",
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltCPOTLimitOption",
                40,
                7,
                ["AlwaysEnabled", "LimitedIfSPBelow95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/PurgeSpeed",
                40,
                0,
                ["Lo", "Hi"],
                None,
                2,
                "ALL",
            ),
            "FiltMinDur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/AdvanceFilterConfig/FiltMinDur", 61, "ALL"
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTActTemp",
                62,
                "ALL",
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTDeadband",
                63,
                "ALL",
            ),
            "FiltCPMinOnTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPMinOnTime",
                64,
                "ALL",
            ),
            "FiltCPOTMaxDur": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTMaxDur",
                65,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                66,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3/O3Pump",
                67,
                0,
                ["NONE", "P1", "CP", ""],
                None,
                4,
                "ALL",
            ),
            "O3FollowPump": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3FollowPump", 67, 2, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3DuringFilt", 67, 3, "ALL"
            ),
            "O3Toggling": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3Toggling", 67, 4, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3/O3SuspendBy",
                67,
                6,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3FilterDelay", 68, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3SuspendTime", 69, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3TogglePeriod", 70, "ALL"
            ),
            "SaniLevel": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Sanitation/SaniLevel", 59, "ALL"
            ),
            "SaniOnTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Sanitation/SaniOnTime", 60, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltFreq",
                42,
                "ALL",
            ),
            "FiltStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltStart",
                43,
                "ALL",
            ),
            "FiltDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltDur", 45, "ALL"
            ),
            "OnzenStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OnzenStart",
                51,
                "ALL",
            ),
            "OnzenDur": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OnzenDur",
                53,
                "ALL",
            ),
            "OnzenFreq": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OnzenFreq",
                55,
                "ALL",
            ),
            "EconStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStart",
                75,
                "ALL",
            ),
            "EconStop": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStop",
                77,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                72,
                3,
                "ALL",
            ),
            "EconProgStatus": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgStatus",
                72,
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
                0,
                ["LastPumpKey", "NextFreePumpKey"],
                None,
                2,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/QuickOnOffKeyEnable",
                17,
                1,
                "ALL",
            ),
            "K600Msg1": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg1",
                79,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg2",
                80,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg3": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg3",
                81,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg4": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg4",
                82,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg5": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg5",
                83,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg6": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg6",
                84,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg7": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg7",
                85,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg8": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg8",
                86,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg1NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg1NbWeek", 87, "ALL"
            ),
            "K600Msg2NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg2NbWeek", 88, "ALL"
            ),
            "K600Msg3NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg3NbWeek", 89, "ALL"
            ),
            "K600Msg4NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg4NbWeek", 90, "ALL"
            ),
            "K600Msg5NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg5NbWeek", 91, "ALL"
            ),
            "K600Msg6NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg6NbWeek", 92, "ALL"
            ),
            "K600Msg7NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg7NbWeek", 93, "ALL"
            ),
            "K600Msg8NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg8NbWeek", 94, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineFrequency",
                95,
                4,
                ["60HZ", "50HZ"],
                None,
                2,
                "ALL",
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineVoltage",
                95,
                5,
                ["240Vac", "230VAC"],
                None,
                2,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/NbPhases", 97, None
            ),
            "BrNbSettings": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrNbSettings", 98, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrSetIndex", 99, None
            ),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet1", 100, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet2", 101, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet3", 102, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet4", 103, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet5", 104, "ALL"
            ),
            "CE_2x20Allowed": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/InputSupply/CE_2x20Allowed", 72, 6, "ALL"
            ),
            "FuseMapping": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/FuseMapping",
                95,
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
            "BreakerMenu": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/BreakerMenu",
                95,
                7,
                ["Available", "NotAvailable"],
                None,
                2,
                "ALL",
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/QuietActionOnHeater",
                30,
                3,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/UDActionOnQuiet",
                72,
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
                72,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Fan/FanPump",
                31,
                1,
                ["None", "P1", "CP"],
                None,
                4,
                "ALL",
            ),
            "FanAsCoolingDevice": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanAsCoolingDevice", 31, 3, "ALL"
            ),
            "FanActiveOnAmbiantOT": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnAmbiantOT", 30, 5, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnPumpRun", 30, 6, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOFFOption", 30, 7, "ALL"
            ),
            "FanSetAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetAOTTempAdc", 34, "ALL"
            ),
            "FanClrAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrAOTTempAdc", 35, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveDelayAfterPumpRun", 36, "ALL"
            ),
            "FanSetForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetForceOffTempAdc", 37, "ALL"
            ),
            "FanClrForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrForceOffTempAdc", 38, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOffInhibitDelay", 39, "ALL"
            ),
            "Pump1AsVSP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/VSP/Pump1AsVSP", 23, 0, "ALL"
            ),
            "Pump3AsVSP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/VSP/Pump3AsVSP", 23, 2, "ALL"
            ),
            "VSPCheckfloSpeed": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPCheckfloSpeed", 24, "ALL"
            ),
            "VSPFilterSpeed": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPFilterSpeed", 25, "ALL"
            ),
            "VSPSpeedLevel0": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel0", 26, "ALL"
            ),
            "VSPSpeedLevel1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel1", 27, "ALL"
            ),
            "VSPSpeedLevel2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel2", 28, "ALL"
            ),
            "VSPSpeedLevel3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel3", 29, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeaterPump",
                30,
                None,
                ["", "CP", "P1"],
                None,
                4,
                "ALL",
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeatRestriction",
                95,
                6,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "ExtProbeEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/ExtProbeEnable",
                31,
                4,
                "ALL",
            ),
            "OverSetpointEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/OverSetpointEnable",
                31,
                5,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                30,
                2,
                ["C", "F"],
                None,
                2,
                "ALL",
            ),
            "SetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/SetpointG",
                32,
                "ALL",
            ),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/EconBelowSetpoint",
                74,
                "ALL",
            ),
            "CPPWMDefault": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/CPPWMDefault",
                22,
                "ALL",
            ),
            "AmbiantOTEnable": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOTEnable", 31, 0, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                95,
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
            "Aux2AsOnzen": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/Aux2AsOnzen", 21, 6, "ALL"
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
