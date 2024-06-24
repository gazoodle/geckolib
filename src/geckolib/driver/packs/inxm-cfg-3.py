#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v3'
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
        return 3

    @property
    def output_keys(self):
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
            "Out1ACurrent": GeckoByteStructAccessor(
                self.struct, "Out1ACurrent", 220, "ALL"
            ),
            "Out1BCurrent": GeckoByteStructAccessor(
                self.struct, "Out1BCurrent", 221, "ALL"
            ),
            "Out2ACurrent": GeckoByteStructAccessor(
                self.struct, "Out2ACurrent", 222, "ALL"
            ),
            "Out2BCurrent": GeckoByteStructAccessor(
                self.struct, "Out2BCurrent", 223, "ALL"
            ),
            "Out3ACurrent": GeckoByteStructAccessor(
                self.struct, "Out3ACurrent", 224, "ALL"
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
            "Out4ACurrent": GeckoByteStructAccessor(
                self.struct, "Out4ACurrent", 225, "ALL"
            ),
            "Out5ACurrent": GeckoByteStructAccessor(
                self.struct, "Out5ACurrent", 226, "ALL"
            ),
            "Out6ACurrent": GeckoByteStructAccessor(
                self.struct, "Out6ACurrent", 227, "ALL"
            ),
            "Out7ACurrent": GeckoByteStructAccessor(
                self.struct, "Out7ACurrent", 228, "ALL"
            ),
            "DirectCurrent": GeckoByteStructAccessor(
                self.struct, "DirectCurrent", 123, "ALL"
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
            "OutIO2": GeckoEnumStructAccessor(
                self.struct,
                "OutIO2",
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
                "OutIO4",
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
            "LightInts": GeckoByteStructAccessor(self.struct, "LightInts", 96, "ALL"),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 18, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "FiberTimeOut", 19, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 20, "ALL"
            ),
            "L120Timer": GeckoEnumStructAccessor(
                self.struct, "L120Timer", 21, 6, ["Shared", "Own"], None, 2, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "QuietTimeOut", 73, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                41,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(self.struct, "CleanP1", 40, 1, "ALL"),
            "CleanCP": GeckoBoolStructAccessor(self.struct, "CleanCP", 40, 2, "ALL"),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltOTOption", 40, 4, "ALL"
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "CPAlwaysON", 40, 3, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltCPOTOption", 40, 5, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct, "FiltSuspendBy", 40, 6, ["AnyUD", "PumpUD"], None, 2, "ALL"
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "FiltCPOTLimitOption",
                40,
                7,
                ["AlwaysEnabled", "LimitedIfSPBelow95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "PurgeSpeed", 40, 0, ["Lo", "Hi"], None, 2, "ALL"
            ),
            "FiltMinDur": GeckoByteStructAccessor(self.struct, "FiltMinDur", 61, "ALL"),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltCPOTActTemp", 62, "ALL"
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltCPOTDeadband", 63, "ALL"
            ),
            "FiltCPMinOnTime": GeckoByteStructAccessor(
                self.struct, "FiltCPMinOnTime", 64, "ALL"
            ),
            "FiltCPOTMaxDur": GeckoByteStructAccessor(
                self.struct, "FiltCPOTMaxDur", 65, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 66, "ALL"
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 67, 0, ["NONE", "P1", "CP", ""], None, 4, "ALL"
            ),
            "O3FollowPump": GeckoBoolStructAccessor(
                self.struct, "O3FollowPump", 67, 2, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "O3DuringFilt", 67, 3, "ALL"
            ),
            "O3Toggling": GeckoBoolStructAccessor(
                self.struct, "O3Toggling", 67, 4, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "O3SuspendBy",
                67,
                6,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "O3FilterDelay", 68, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 69, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "O3TogglePeriod", 70, "ALL"
            ),
            "SaniLevel": GeckoByteStructAccessor(self.struct, "SaniLevel", 59, "ALL"),
            "SaniOnTime": GeckoByteStructAccessor(self.struct, "SaniOnTime", 60, "ALL"),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 42, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 43, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 45, "ALL"),
            "OnzenStart": GeckoTimeStructAccessor(self.struct, "OnzenStart", 51, "ALL"),
            "OnzenDur": GeckoTimeStructAccessor(self.struct, "OnzenDur", 53, "ALL"),
            "OnzenFreq": GeckoByteStructAccessor(self.struct, "OnzenFreq", 55, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 75, "ALL"),
            "EconStop": GeckoTimeStructAccessor(self.struct, "EconStop", 77, "ALL"),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 72, 3, "ALL"
            ),
            "EconProgStatus": GeckoEnumStructAccessor(
                self.struct,
                "EconProgStatus",
                72,
                4,
                ["Disabled", "NotActive", "NA", "Active"],
                None,
                4,
                "ALL",
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "BlowerKeyOption",
                17,
                0,
                ["LastPumpKey", "NextFreePumpKey"],
                None,
                2,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct, "QuickOnOffKeyEnable", 17, 1, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct, "LineFrequency", 95, 4, ["60HZ", "50HZ"], None, 2, "ALL"
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct, "LineVoltage", 95, 5, ["240Vac", "230VAC"], None, 2, "ALL"
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 97, None),
            "BrNbSettings": GeckoByteStructAccessor(
                self.struct, "BrNbSettings", 98, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(self.struct, "BrSetIndex", 99, None),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "BreakerSet1", 100, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "BreakerSet2", 101, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "BreakerSet3", 102, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "BreakerSet4", 103, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "BreakerSet5", 104, "ALL"
            ),
            "CE_2x20Allowed": GeckoBoolStructAccessor(
                self.struct, "CE_2x20Allowed", 72, 6, "ALL"
            ),
            "FuseMapping": GeckoEnumStructAccessor(
                self.struct,
                "FuseMapping",
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
                "BreakerMenu",
                95,
                7,
                ["Available", "NotAvailable"],
                None,
                2,
                "ALL",
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "QuietActionOnHeater",
                30,
                3,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "UDActionOnQuiet",
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
                "QuietActionOnUD",
                72,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct, "FanPump", 31, 1, ["None", "P1", "CP"], None, 4, "ALL"
            ),
            "FanAsCoolingDevice": GeckoBoolStructAccessor(
                self.struct, "FanAsCoolingDevice", 31, 3, "ALL"
            ),
            "FanActiveOnAmbiantOT": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnAmbiantOT", 30, 5, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnPumpRun", 30, 6, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "FanForceOFFOption", 30, 7, "ALL"
            ),
            "FanSetAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "FanSetAOTTempAdc", 34, "ALL"
            ),
            "FanClrAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "FanClrAOTTempAdc", 35, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "FanActiveDelayAfterPumpRun", 36, "ALL"
            ),
            "FanSetForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "FanSetForceOffTempAdc", 37, "ALL"
            ),
            "FanClrForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "FanClrForceOffTempAdc", 38, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "FanForceOffInhibitDelay", 39, "ALL"
            ),
            "Pump1AsVSP": GeckoBoolStructAccessor(
                self.struct, "Pump1AsVSP", 23, 0, "ALL"
            ),
            "Pump3AsVSP": GeckoBoolStructAccessor(
                self.struct, "Pump3AsVSP", 23, 2, "ALL"
            ),
            "VSPCheckfloSpeed": GeckoByteStructAccessor(
                self.struct, "VSPCheckfloSpeed", 24, "ALL"
            ),
            "VSPFilterSpeed": GeckoByteStructAccessor(
                self.struct, "VSPFilterSpeed", 25, "ALL"
            ),
            "VSPSpeedLevel0": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel0", 26, "ALL"
            ),
            "VSPSpeedLevel1": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel1", 27, "ALL"
            ),
            "VSPSpeedLevel2": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel2", 28, "ALL"
            ),
            "VSPSpeedLevel3": GeckoByteStructAccessor(
                self.struct, "VSPSpeedLevel3", 29, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 30, None, ["", "CP", "P1"], None, 4, "ALL"
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "HeatRestriction",
                95,
                6,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "ExtProbeEnable": GeckoBoolStructAccessor(
                self.struct, "ExtProbeEnable", 31, 4, "ALL"
            ),
            "OverSetpointEnable": GeckoBoolStructAccessor(
                self.struct, "OverSetpointEnable", 31, 5, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 30, 2, ["C", "F"], None, 2, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 32, "ALL"),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct, "EconBelowSetpoint", 74, "ALL"
            ),
            "CPPWMDefault": GeckoByteStructAccessor(
                self.struct, "CPPWMDefault", 22, "ALL"
            ),
            "AmbiantOTEnable": GeckoBoolStructAccessor(
                self.struct, "AmbiantOTEnable", 31, 0, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct, "TimeFormat", 95, 0, ["AmPm", "24h"], None, 2, "ALL"
            ),
            "Aux1AsTVLifter": GeckoBoolStructAccessor(
                self.struct, "Aux1AsTVLifter", 21, 0, "ALL"
            ),
            "Aux2AsSpeakerLifter": GeckoBoolStructAccessor(
                self.struct, "Aux2AsSpeakerLifter", 21, 1, "ALL"
            ),
            "Aux2AsOnzen": GeckoBoolStructAccessor(
                self.struct, "Aux2AsOnzen", 21, 6, "ALL"
            ),
            "DJS_No1": GeckoEnumStructAccessor(
                self.struct,
                "DJS_No1",
                21,
                2,
                ["NA", "OnP1", "OnP2", "OnP3"],
                None,
                4,
                "ALL",
            ),
            "DJS_No2": GeckoEnumStructAccessor(
                self.struct,
                "DJS_No2",
                21,
                4,
                ["NA", "OnP1", "OnP2", "OnP3"],
                None,
                4,
                "ALL",
            ),
        }
