#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v6'
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
        return 6

    @property
    def output_keys(self):
        return [
            "Out1A",
            "Out1B",
            "Out2A",
            "Out2B",
            "Out3A",
            "OutHtr",
            "Out4A",
            "Out5A",
            "Out6A",
            "Out7A",
            "Direct",
            "OutLi",
            "OutIO2",
            "OutIO4",
        ]

    @property
    def accessors(self):
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigNumber", 0, "ALL"
            ),
            "Out1A": GeckoEnumStructAccessor(
                self.struct,
                "Out1A",
                95,
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
                    "",
                    "",
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
                96,
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
                    "",
                    "",
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
                97,
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
                    "",
                    "",
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
                98,
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
                    "",
                    "",
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
                99,
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
                    "",
                    "",
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
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "OutHtr",
                104,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1ACur": GeckoByteStructAccessor(self.struct, "Out1ACur", 108, "ALL"),
            "Out1BCur": GeckoByteStructAccessor(self.struct, "Out1BCur", 109, "ALL"),
            "Out2ACur": GeckoByteStructAccessor(self.struct, "Out2ACur", 110, "ALL"),
            "Out2BCur": GeckoByteStructAccessor(self.struct, "Out2BCur", 111, "ALL"),
            "Out3ACur": GeckoByteStructAccessor(self.struct, "Out3ACur", 112, "ALL"),
            "Out4A": GeckoEnumStructAccessor(
                self.struct,
                "Out4A",
                100,
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
                    "",
                    "",
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
                101,
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
                    "",
                    "",
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
                102,
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
                    "",
                    "",
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
                103,
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
                    "",
                    "",
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
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "Direct",
                118,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Out4ACur": GeckoByteStructAccessor(self.struct, "Out4ACur", 113, "ALL"),
            "Out5ACur": GeckoByteStructAccessor(self.struct, "Out5ACur", 114, "ALL"),
            "Out6ACur": GeckoByteStructAccessor(self.struct, "Out6ACur", 115, "ALL"),
            "Out7ACur": GeckoByteStructAccessor(self.struct, "Out7ACur", 116, "ALL"),
            "DirectCur": GeckoByteStructAccessor(self.struct, "DirectCur", 117, "ALL"),
            "OutLi": GeckoEnumStructAccessor(
                self.struct,
                "OutLi",
                105,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                "ALL",
            ),
            "OutIO2": GeckoEnumStructAccessor(
                self.struct,
                "OutIO2",
                106,
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
                    "",
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
                "OutIO4",
                107,
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
                    "",
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
            "LightInts": GeckoByteStructAccessor(self.struct, "LightInts", 86, "ALL"),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 4, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 2, "ALL"
            ),
            "L120Timer": GeckoEnumStructAccessor(
                self.struct, "L120Timer", 1, 2, ["Shared", "Own"], None, 2, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "FiberTimeOut", 3, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "QuietTimeOut", 63, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                27,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(self.struct, "CleanP1", 23, 0, "ALL"),
            "CleanCP": GeckoBoolStructAccessor(self.struct, "CleanCP", 24, 0, "ALL"),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "CPAlwaysON", 25, 0, "ALL"
            ),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltOTOption", 26, 4, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltCPOTOption", 26, 5, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct, "FiltSuspendBy", 26, 6, ["AnyUD", "PumpUD"], None, 2, "ALL"
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "FiltCPOTLimitOption",
                26,
                7,
                ["AlwaysEnabled", "WithSPOver95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "PurgeSpeed", 26, 0, ["Lo", "Hi"], None, 2, "ALL"
            ),
            "FiltOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltOTActTemp", 47, "ALL"
            ),
            "FiltOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltOTDeadband", 48, "ALL"
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltCPOTActTemp", 50, "ALL"
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltCPOTDeadband", 51, "ALL"
            ),
            "CpOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct, "CpOnTimeDuringOT", 52, "ALL"
            ),
            "CpOffTimeDuringOT": GeckoByteStructAccessor(
                self.struct, "CpOffTimeDuringOT", 53, "ALL"
            ),
            "FiltOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct, "FiltOnTimeDuringOT", 49, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 54, "ALL"
            ),
            "DrainMode": GeckoEnumStructAccessor(
                self.struct,
                "DrainMode",
                119,
                None,
                ["NA", "P1", "CP"],
                None,
                None,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 55, None, ["CP", "P1"], None, None, "ALL"
            ),
            "O3FollowPump": GeckoBoolStructAccessor(
                self.struct, "O3FollowPump", 56, 0, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "O3DuringFilt", 57, 0, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 60, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "O3SuspendBy",
                58,
                None,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "O3FilterDelay", 59, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "O3TogglePeriod", 61, "ALL"
            ),
            "SaniLevel": GeckoByteStructAccessor(self.struct, "SaniLevel", 45, "ALL"),
            "SaniOnTime": GeckoByteStructAccessor(self.struct, "SaniOnTime", 46, "ALL"),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 15, "ALL"),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 13, 2, ["C", "F"], None, 2, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 12, None, ["CP", "P1"], None, None, "ALL"
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "HeatRestriction",
                85,
                3,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "ExtProbeEnable": GeckoBoolStructAccessor(
                self.struct, "ExtProbeEnable", 14, 4, "ALL"
            ),
            "OverSetpointEnable": GeckoBoolStructAccessor(
                self.struct, "OverSetpointEnable", 14, 5, "ALL"
            ),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct, "EconBelowSetpoint", 64, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct, "LineFrequency", 85, 1, ["60HZ", "50HZ"], None, 2, "ALL"
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct, "LineVoltage", 85, 2, ["240Vac", "230VAC"], None, 2, "ALL"
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 87, None),
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
            "CE_2x20Allowed": GeckoBoolStructAccessor(
                self.struct, "CE_2x20Allowed", 62, 6, "ALL"
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "UDActionOnQuiet",
                62,
                1,
                ["IgnoreUD", "RestoreAllUD", "NA", "CancelOtherUD"],
                None,
                4,
                "ALL",
            ),
            "QuietActionOnUD": GeckoEnumStructAccessor(
                self.struct,
                "QuietActionOnUD",
                62,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "QuietActionOnHeater",
                13,
                3,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "FanActiveOnAmbiantOT": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnAmbiantOT", 13, 5, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnPumpRun", 13, 6, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "FanForceOFFOption", 13, 7, "ALL"
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct, "FanPump", 14, 1, ["NA", "P1", "CP"], None, 4, "ALL"
            ),
            "FanAsCoolingDevice": GeckoBoolStructAccessor(
                self.struct, "FanAsCoolingDevice", 14, 3, "ALL"
            ),
            "FanSetAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "FanSetAOTTempAdc", 17, "ALL"
            ),
            "FanClrAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "FanClrAOTTempAdc", 18, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "FanActiveDelayAfterPumpRun", 19, "ALL"
            ),
            "FanSetForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "FanSetForceOffTempAdc", 20, "ALL"
            ),
            "FanClrForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "FanClrForceOffTempAdc", 21, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "FanForceOffInhibitDelay", 22, "ALL"
            ),
            "Pump1AsVSP": GeckoBoolStructAccessor(
                self.struct, "Pump1AsVSP", 5, 0, "ALL"
            ),
            "Pump3AsVSP": GeckoBoolStructAccessor(
                self.struct, "Pump3AsVSP", 5, 2, "ALL"
            ),
            "VSPCheckfloSpeed": GeckoByteStructAccessor(
                self.struct, "VSPCheckfloSpeed", 6, "ALL"
            ),
            "VSPFilterSpeed": GeckoByteStructAccessor(
                self.struct, "VSPFilterSpeed", 7, "ALL"
            ),
            "VSPSpeedLevel0": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel0", 8, "ALL"
            ),
            "VSPSpeedLevel1": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel1", 9, "ALL"
            ),
            "VSPSpeedLevel2": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel2", 10, "ALL"
            ),
            "VSPSpeedLevel3": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel3", 11, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 28, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 29, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 31, "ALL"),
            "OnzenStart": GeckoTimeStructAccessor(self.struct, "OnzenStart", 37, "ALL"),
            "OnzenDur": GeckoTimeStructAccessor(self.struct, "OnzenDur", 39, "ALL"),
            "OnzenFreq": GeckoByteStructAccessor(self.struct, "OnzenFreq", 41, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 65, "ALL"),
            "EconStop": GeckoTimeStructAccessor(self.struct, "EconStop", 67, "ALL"),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "EconProgAvailable",
                62,
                4,
                ["NA", "Available"],
                None,
                2,
                "ALL",
            ),
            "UDProgEcon": GeckoBoolStructAccessor(
                self.struct, "UDProgEcon", 62, 5, "ALL"
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 62, 3, "ALL"
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "BlowerKeyOption",
                1,
                0,
                ["LastPumpKey", "FreePumpKey"],
                None,
                2,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct, "QuickOnOffKeyEnable", 1, 1, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct, "TimeFormat", 85, 0, ["AmPm", "24h"], None, 2, "ALL"
            ),
            "AmbiantOHEnable": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHEnable", 14, 0, "ALL"
            ),
        }
