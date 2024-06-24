#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v1'
"""

from . import (
    GeckoByteStructAccessor,
    GeckoWordStructAccessor,
    GeckoTimeStructAccessor,
    GeckoBoolStructAccessor,
    GeckoEnumStructAccessor,
    GeckoTempStructAccessor,
)


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return 1

    @property
    def output_keys(self):
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
    def accessors(self):
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigNumber", 1, "ALL"
            ),
            "Out1A": GeckoEnumStructAccessor(
                self.struct,
                "Out1A",
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
                "Out1B",
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
                "Out2A",
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
                "Out2B",
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
                "Out3A",
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
                "OutHeater",
                209,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "PumpActivationOrder": GeckoEnumStructAccessor(
                self.struct,
                "PumpActivationOrder",
                18,
                2,
                ["Ascendant", "Descendant"],
                None,
                2,
                "ALL",
            ),
            "Out4A": GeckoEnumStructAccessor(
                self.struct,
                "Out4A",
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
                "Out5A",
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
                "Out6A",
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
                "Out7A",
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
                "OutLi",
                210,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                "ALL",
            ),
            "LightInts": GeckoByteStructAccessor(self.struct, "LightInts", 87, "ALL"),
            "LightActivationOrder": GeckoEnumStructAccessor(
                self.struct,
                "LightActivationOrder",
                18,
                0,
                ["Ascendant", "Descendant"],
                None,
                2,
                "ALL",
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 19, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "FiberTimeOut", 20, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 21, "ALL"
            ),
            "LightResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "LightResetTimeOut",
                18,
                1,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "PumpResetTimeOut",
                18,
                3,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpTimeOutShare": GeckoBoolStructAccessor(
                self.struct, "PumpTimeOutShare", 18, 4, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "QuietTimeOut", 72, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                38,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(self.struct, "CleanP1", 36, 1, "ALL"),
            "CleanCP": GeckoBoolStructAccessor(self.struct, "CleanCP", 36, 2, "ALL"),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "CPAlwaysON", 36, 3, "ALL"
            ),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltOTOption", 37, 0, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltCPOTOption", 37, 1, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct, "FiltSuspendBy", 37, 2, ["AnyUD", "PumpUD"], None, 2, "ALL"
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "FiltCPOTLimitOption",
                37,
                3,
                ["AlwaysEnabled", "LimitedIfSPBelow95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "PurgeSpeed", 36, 0, ["Lo", "Hi"], None, 2, "ALL"
            ),
            "FiltDefPurgeTime": GeckoByteStructAccessor(
                self.struct, "FiltDefPurgeTime", 56, "ALL"
            ),
            "FiltDefP1PurgeTime": GeckoByteStructAccessor(
                self.struct, "FiltDefP1PurgeTime", 57, "ALL"
            ),
            "FiltMinDur": GeckoByteStructAccessor(self.struct, "FiltMinDur", 60, "ALL"),
            "FiltOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltOTActTemp", 58, "ALL"
            ),
            "FiltOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltOTDeadband", 59, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 65, "ALL"
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltCPOTActTemp", 61, "ALL"
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltCPOTDeadband", 62, "ALL"
            ),
            "FiltCPMinOnTime": GeckoByteStructAccessor(
                self.struct, "FiltCPMinOnTime", 63, "ALL"
            ),
            "FiltCPOTMaxDur": GeckoByteStructAccessor(
                self.struct, "FiltCPOTMaxDur", 64, "ALL"
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 66, 0, ["NONE", "P1", "CP", ""], None, 4, "ALL"
            ),
            "O3AlwaysON": GeckoBoolStructAccessor(
                self.struct, "O3AlwaysON", 66, 2, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "O3DuringFilt", 66, 3, "ALL"
            ),
            "O3Toggling": GeckoBoolStructAccessor(
                self.struct, "O3Toggling", 66, 4, "ALL"
            ),
            "O3UserDemand": GeckoBoolStructAccessor(
                self.struct, "O3UserDemand", 66, 5, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "O3SuspendBy",
                66,
                6,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "O3FilterDelay", 67, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 68, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "O3TogglePeriod", 69, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 39, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 40, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 42, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 74, "ALL"),
            "EconStop": GeckoTimeStructAccessor(self.struct, "EconStop", 76, "ALL"),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 71, 3, "ALL"
            ),
            "EconProgEnable": GeckoBoolStructAccessor(
                self.struct, "EconProgEnable", 71, 4, "ALL"
            ),
            "EconUserDemand": GeckoBoolStructAccessor(
                self.struct, "EconUserDemand", 71, 5, "ALL"
            ),
            "EconProgMode": GeckoBoolStructAccessor(
                self.struct, "EconProgMode", 71, 6, "ALL"
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "BlowerKeyOption",
                18,
                5,
                ["LastPumpKey", "NextFreePumpKey", "AnyFreePump"],
                None,
                4,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct, "QuickOnOffKeyEnable", 18, 7, "ALL"
            ),
            "SWMPurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "SWMPurgeSpeed", 70, 0, ["Low", "High"], None, 2, "ALL"
            ),
            "SWMPurgeBlower": GeckoBoolStructAccessor(
                self.struct, "SWMPurgeBlower", 70, 1, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct, "LineFrequency", 86, 4, ["60HZ", "50HZ"], None, 2, "ALL"
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct, "LineVoltage", 86, 5, ["240Vac", "230VAC"], None, 2, "ALL"
            ),
            "FuseMapping": GeckoEnumStructAccessor(
                self.struct,
                "FuseMapping",
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
                self.struct, "BrNbSettings", 88, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(self.struct, "BrSetIndex", 89, None),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "BreakerSet1", 90, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "BreakerSet2", 91, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "BreakerSet3", 92, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "BreakerSet4", 93, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "BreakerSet5", 94, "ALL"
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "QuietActionOnHeater",
                22,
                4,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "UDActionOnQuiet",
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
                "QuietActionOnUD",
                71,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct, "FanPump", 23, 3, ["None", "P1", "CP"], None, 4, "ALL"
            ),
            "FanTempOption": GeckoBoolStructAccessor(
                self.struct, "FanTempOption", 22, 6, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnPumpRun", 22, 7, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "FanForceOFFOption", 23, 0, "ALL"
            ),
            "FanSetAOTTempAdc16": GeckoByteStructAccessor(
                self.struct, "FanSetAOTTempAdc16", 26, "ALL"
            ),
            "FanClrAOTTempAdc16": GeckoByteStructAccessor(
                self.struct, "FanClrAOTTempAdc16", 28, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "FanActiveDelayAfterPumpRun", 30, "ALL"
            ),
            "FanSetForceOffTempAdc16": GeckoByteStructAccessor(
                self.struct, "FanSetForceOffTempAdc16", 31, "ALL"
            ),
            "FanClrForceOffTempAdc16": GeckoByteStructAccessor(
                self.struct, "FanClrForceOffTempAdc16", 33, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "FanForceOffInhibitDelay", 35, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 22, None, ["", "CP", "P1"], None, 4, "ALL"
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "HeatRestriction",
                86,
                6,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 22, 2, ["C", "F"], None, 2, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 24, "ALL"),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct, "EconBelowSetpoint", 73, "ALL"
            ),
            "AmbiantOTEnable": GeckoBoolStructAccessor(
                self.struct, "AmbiantOTEnable", 23, 1, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct, "TimeFormat", 86, 0, ["AmPm", "24h"], None, 2, "ALL"
            ),
            "InStateUserDemand": GeckoBoolStructAccessor(
                self.struct, "InStateUserDemand", 22, 3, "ALL"
            ),
            "KineticProtection": GeckoBoolStructAccessor(
                self.struct, "KineticProtection", 23, 2, "ALL"
            ),
        }
