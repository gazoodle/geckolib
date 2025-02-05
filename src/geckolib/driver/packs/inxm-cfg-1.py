"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v1'."""  # noqa: N999

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
        return 1

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
            "PumpActivationOrder",
            "Out4A",
            "Out5A",
            "Out6A",
            "Out7A",
            "OutLi",
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
            "PumpActivationOrder": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/PumpActivationOrder",
                18,
                2,
                ["Ascendant", "Descendant"],
                None,
                2,
                "ALL",
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
            "LightInts": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LVOutputConfig/LightInts", 87, "ALL"
            ),
            "LightActivationOrder": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/LightActivationOrder",
                18,
                0,
                ["Ascendant", "Descendant"],
                None,
                2,
                "ALL",
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 19, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/FiberTimeOut", 20, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 21, "ALL"
            ),
            "LightResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/LightResetTimeOut",
                18,
                1,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/PumpResetTimeOut",
                18,
                3,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpTimeOutShare": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOutShare", 18, 4, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/QuietTimeOut", 72, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                38,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CleanP1", 36, 1, "ALL"
            ),
            "CleanCP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CleanCP", 36, 2, "ALL"
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CPAlwaysON", 36, 3, "ALL"
            ),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltOTOption", 37, 0, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltCPOTOption", 37, 1, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltSuspendBy",
                37,
                2,
                ["AnyUD", "PumpUD"],
                None,
                2,
                "ALL",
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltCPOTLimitOption",
                37,
                3,
                ["AlwaysEnabled", "LimitedIfSPBelow95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/PurgeSpeed",
                36,
                0,
                ["Lo", "Hi"],
                None,
                2,
                "ALL",
            ),
            "FiltDefPurgeTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltDefPurgeTime",
                56,
                "ALL",
            ),
            "FiltDefP1PurgeTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltDefP1PurgeTime",
                57,
                "ALL",
            ),
            "FiltMinDur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/AdvanceFilterConfig/FiltMinDur", 60, "ALL"
            ),
            "FiltOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTActTemp",
                58,
                "ALL",
            ),
            "FiltOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTDeadband",
                59,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                65,
                "ALL",
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTActTemp",
                61,
                "ALL",
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTDeadband",
                62,
                "ALL",
            ),
            "FiltCPMinOnTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPMinOnTime",
                63,
                "ALL",
            ),
            "FiltCPOTMaxDur": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTMaxDur",
                64,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3/O3Pump",
                66,
                0,
                ["NONE", "P1", "CP", ""],
                None,
                4,
                "ALL",
            ),
            "O3AlwaysON": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3AlwaysON", 66, 2, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3DuringFilt", 66, 3, "ALL"
            ),
            "O3Toggling": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3Toggling", 66, 4, "ALL"
            ),
            "O3UserDemand": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/O3/O3UserDemand", 66, 5, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3/O3SuspendBy",
                66,
                6,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3FilterDelay", 67, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3SuspendTime", 68, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3/O3TogglePeriod", 69, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltFreq",
                39,
                "ALL",
            ),
            "FiltStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltStart",
                40,
                "ALL",
            ),
            "FiltDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltDur", 42, "ALL"
            ),
            "EconStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStart",
                74,
                "ALL",
            ),
            "EconStop": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStop",
                76,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                71,
                3,
                "ALL",
            ),
            "EconProgEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgEnable",
                71,
                4,
                "ALL",
            ),
            "EconUserDemand": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconUserDemand",
                71,
                5,
                "ALL",
            ),
            "EconProgMode": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgMode",
                71,
                6,
                "ALL",
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/BlowerKeyOption",
                18,
                5,
                ["LastPumpKey", "NextFreePumpKey", "AnyFreePump"],
                None,
                4,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/QuickOnOffKeyEnable",
                18,
                7,
                "ALL",
            ),
            "K600Msg1NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg1NbWeek", 78, "ALL"
            ),
            "K600Msg2NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg2NbWeek", 79, "ALL"
            ),
            "K600Msg3NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg3NbWeek", 80, "ALL"
            ),
            "K600Msg4NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg4NbWeek", 81, "ALL"
            ),
            "K600Msg5NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg5NbWeek", 82, "ALL"
            ),
            "K600Msg6NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg6NbWeek", 83, "ALL"
            ),
            "K600Msg7NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg7NbWeek", 84, "ALL"
            ),
            "K600Msg8NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg8NbWeek", 85, "ALL"
            ),
            "SWMPurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SWM/SWMPurgeSpeed",
                70,
                0,
                ["Low", "High"],
                None,
                2,
                "ALL",
            ),
            "SWMPurgeBlower": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/SWM/SWMPurgeBlower", 70, 1, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineFrequency",
                86,
                4,
                ["60HZ", "50HZ"],
                None,
                2,
                "ALL",
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineVoltage",
                86,
                5,
                ["240Vac", "230VAC"],
                None,
                2,
                "ALL",
            ),
            "FuseMapping": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/FuseMapping",
                86,
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
            "BrNbSettings": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrNbSettings", 88, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrSetIndex", 89, None
            ),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet1", 90, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet2", 91, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet3", 92, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet4", 93, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet5", 94, "ALL"
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/QuietActionOnHeater",
                22,
                4,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/UDActionOnQuiet",
                71,
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
                71,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Fan/FanPump",
                23,
                3,
                ["None", "P1", "CP"],
                None,
                4,
                "ALL",
            ),
            "FanTempOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanTempOption", 22, 6, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnPumpRun", 22, 7, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOFFOption", 23, 0, "ALL"
            ),
            "FanSetAOTTempAdc16": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetAOTTempAdc16", 26, "ALL"
            ),
            "FanClrAOTTempAdc16": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrAOTTempAdc16", 28, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveDelayAfterPumpRun", 30, "ALL"
            ),
            "FanSetForceOffTempAdc16": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetForceOffTempAdc16", 31, "ALL"
            ),
            "FanClrForceOffTempAdc16": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrForceOffTempAdc16", 33, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOffInhibitDelay", 35, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeaterPump",
                22,
                None,
                ["", "CP", "P1"],
                None,
                4,
                "ALL",
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeatRestriction",
                86,
                6,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                22,
                2,
                ["C", "F"],
                None,
                2,
                "ALL",
            ),
            "SetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/SetpointG",
                24,
                "ALL",
            ),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/EconBelowSetpoint",
                73,
                "ALL",
            ),
            "AmbiantOTEnable": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOTEnable", 23, 1, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                86,
                0,
                ["AmPm", "24h"],
                None,
                2,
                "ALL",
            ),
            "InStateUserDemand": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/InStateUserDemand", 22, 3, "ALL"
            ),
            "KineticProtection": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KineticProtection", 23, 2, "ALL"
            ),
        }
