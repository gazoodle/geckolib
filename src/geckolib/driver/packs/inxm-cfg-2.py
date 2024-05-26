#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v2'
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
        return 2

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
            "LightInts": GeckoByteStructAccessor(self.struct, "LightInts", 84, "ALL"),
            "LightActivationOrder": GeckoEnumStructAccessor(
                self.struct,
                "LightActivationOrder",
                17,
                0,
                ["Ascendant", "Descendant"],
                None,
                2,
                "ALL",
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 18, "ALL"
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "FiberTimeOut", 19, "ALL"
            ),
            "LightResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "LightResetTimeOut",
                17,
                1,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 20, "ALL"
            ),
            "PumpResetTimeOut": GeckoEnumStructAccessor(
                self.struct,
                "PumpResetTimeOut",
                17,
                2,
                ["OnStart", "OnChange"],
                None,
                2,
                "ALL",
            ),
            "PumpTimeOutShare": GeckoBoolStructAccessor(
                self.struct, "PumpTimeOutShare", 17, 3, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "QuietTimeOut", 69, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                35,
                None,
                ["StartDurFre", "NotUsed1", "NotUsed2", "PurgeOnly"],
                None,
                None,
                "ALL",
            ),
            "CleanP1": GeckoBoolStructAccessor(self.struct, "CleanP1", 33, 1, "ALL"),
            "CleanCP": GeckoBoolStructAccessor(self.struct, "CleanCP", 33, 2, "ALL"),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltOTOption", 34, 0, "ALL"
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "CPAlwaysON", 33, 3, "ALL"
            ),
            "FiltCPOTOption": GeckoBoolStructAccessor(
                self.struct, "FiltCPOTOption", 34, 1, "ALL"
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct, "FiltSuspendBy", 34, 2, ["AnyUD", "PumpUD"], None, 2, "ALL"
            ),
            "FiltCPOTLimitOption": GeckoEnumStructAccessor(
                self.struct,
                "FiltCPOTLimitOption",
                34,
                3,
                ["AlwaysEnabled", "LimitedIfSPBelow95F"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "PurgeSpeed", 33, 0, ["Lo", "Hi"], None, 2, "ALL"
            ),
            "FiltMinDur": GeckoByteStructAccessor(self.struct, "FiltMinDur", 57, "ALL"),
            "FiltOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltOTActTemp", 55, "ALL"
            ),
            "FiltOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltOTDeadband", 56, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 62, "ALL"
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct, "FiltCPOTActTemp", 58, "ALL"
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct, "FiltCPOTDeadband", 59, "ALL"
            ),
            "FiltCPMinOnTime": GeckoByteStructAccessor(
                self.struct, "FiltCPMinOnTime", 60, "ALL"
            ),
            "FiltCPOTMaxDur": GeckoByteStructAccessor(
                self.struct, "FiltCPOTMaxDur", 61, "ALL"
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 63, 0, ["NONE", "P1", "CP", ""], None, 4, "ALL"
            ),
            "O3FollowPump": GeckoBoolStructAccessor(
                self.struct, "O3FollowPump", 63, 2, "ALL"
            ),
            "O3DuringFilt": GeckoBoolStructAccessor(
                self.struct, "O3DuringFilt", 63, 3, "ALL"
            ),
            "O3Toggling": GeckoBoolStructAccessor(
                self.struct, "O3Toggling", 63, 4, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "O3SuspendBy",
                63,
                6,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "O3FilterDelay", 64, "ALL"
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 65, "ALL"
            ),
            "O3TogglePeriod": GeckoByteStructAccessor(
                self.struct, "O3TogglePeriod", 66, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 36, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 37, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 39, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 71, "ALL"),
            "EconStop": GeckoTimeStructAccessor(self.struct, "EconStop", 73, "ALL"),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 68, 3, "ALL"
            ),
            "EconProgStatus": GeckoEnumStructAccessor(
                self.struct,
                "EconProgStatus",
                68,
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
                4,
                ["LastPumpKey", "NextFreePumpKey", "AnyFreePump"],
                None,
                4,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct, "QuickOnOffKeyEnable", 17, 6, "ALL"
            ),
            "SWMPurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "SWMPurgeSpeed", 67, 0, ["Low", "High"], None, 2, "ALL"
            ),
            "SWMPurgeBlower": GeckoBoolStructAccessor(
                self.struct, "SWMPurgeBlower", 67, 1, "ALL"
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct, "LineFrequency", 83, 4, ["60HZ", "50HZ"], None, 2, "ALL"
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct, "LineVoltage", 83, 5, ["240Vac", "230VAC"], None, 2, "ALL"
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 85, None),
            "BrNbSettings": GeckoByteStructAccessor(
                self.struct, "BrNbSettings", 86, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(self.struct, "BrSetIndex", 87, None),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "BreakerSet1", 88, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "BreakerSet2", 89, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "BreakerSet3", 90, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "BreakerSet4", 91, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "BreakerSet5", 92, "ALL"
            ),
            "BreakerMenu": GeckoEnumStructAccessor(
                self.struct,
                "BreakerMenu",
                83,
                7,
                ["Available", "NotAvailable"],
                None,
                2,
                "ALL",
            ),
            "FuseMapping": GeckoEnumStructAccessor(
                self.struct,
                "FuseMapping",
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
                "QuietActionOnHeater",
                23,
                3,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "UDActionOnQuiet",
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
                "QuietActionOnUD",
                68,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct, "FanPump", 24, 1, ["None", "P1", "CP"], None, 4, "ALL"
            ),
            "FanAsCoolingDevice": GeckoBoolStructAccessor(
                self.struct, "FanAsCoolingDevice", 24, 3, "ALL"
            ),
            "FanActiveOnAmbiantOT": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnAmbiantOT", 23, 5, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "FanActiveOnPumpRun", 23, 6, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "FanForceOFFOption", 23, 7, "ALL"
            ),
            "FanSetAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "FanSetAOTTempAdc", 27, "ALL"
            ),
            "FanClrAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "FanClrAOTTempAdc", 28, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "FanActiveDelayAfterPumpRun", 29, "ALL"
            ),
            "FanSetForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "FanSetForceOffTempAdc", 30, "ALL"
            ),
            "FanClrForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "FanClrForceOffTempAdc", 31, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "FanForceOffInhibitDelay", 32, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 23, None, ["", "CP", "P1"], None, 4, "ALL"
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "HeatRestriction",
                83,
                6,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "ExtProbeEnable": GeckoBoolStructAccessor(
                self.struct, "ExtProbeEnable", 24, 4, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 23, 2, ["C", "F"], None, 2, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 25, "ALL"),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct, "EconBelowSetpoint", 70, "ALL"
            ),
            "AmbiantOTEnable": GeckoBoolStructAccessor(
                self.struct, "AmbiantOTEnable", 24, 0, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct, "TimeFormat", 83, 0, ["AmPm", "24h"], None, 2, "ALL"
            ),
            "Aux1AsTVLifter": GeckoBoolStructAccessor(
                self.struct, "Aux1AsTVLifter", 21, 0, "ALL"
            ),
            "Aux2AsSpeakerLifter": GeckoBoolStructAccessor(
                self.struct, "Aux2AsSpeakerLifter", 21, 1, "ALL"
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
