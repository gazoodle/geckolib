#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE-2 v61'
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
        return 61

    @property
    def output_keys(self):
        return ["Out1", "Out2", "Out3", "Out4", "Out5", "OutHtr", "Direct", "OutLi"]

    @property
    def accessors(self):
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigNumber", 0, "ALL"
            ),
            "Out1": GeckoEnumStructAccessor(
                self.struct,
                "Out1",
                12,
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
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out2": GeckoEnumStructAccessor(
                self.struct,
                "Out2",
                13,
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
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out3": GeckoEnumStructAccessor(
                self.struct,
                "Out3",
                14,
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
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out4": GeckoEnumStructAccessor(
                self.struct,
                "Out4",
                15,
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
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out5": GeckoEnumStructAccessor(
                self.struct,
                "Out5",
                16,
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
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "OutHtr",
                18,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1Cur": GeckoByteStructAccessor(self.struct, "Out1Cur", 36, "ALL"),
            "Out2Cur": GeckoByteStructAccessor(self.struct, "Out2Cur", 37, "ALL"),
            "Out3Cur": GeckoByteStructAccessor(self.struct, "Out3Cur", 38, "ALL"),
            "Out4Cur": GeckoByteStructAccessor(self.struct, "Out4Cur", 39, "ALL"),
            "Out5Cur": GeckoByteStructAccessor(self.struct, "Out5Cur", 40, "ALL"),
            "OutHtRCur": GeckoByteStructAccessor(self.struct, "OutHtRCur", 42, "ALL"),
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "Direct",
                17,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "DirectCur": GeckoByteStructAccessor(self.struct, "DirectCur", 41, "ALL"),
            "WaterfallAsCP": GeckoBoolStructAccessor(
                self.struct, "WaterfallAsCP", 47, 2, "ALL"
            ),
            "OutLi": GeckoEnumStructAccessor(
                self.struct,
                "OutLi",
                79,
                None,
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                None,
            ),
            "LightInts": GeckoByteStructAccessor(self.struct, "LightInts", 80, None),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 54, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 55, "ALL"
            ),
            "L120TimeOut": GeckoByteStructAccessor(
                self.struct, "L120TimeOut", 56, "ALL"
            ),
            "L120Timer": GeckoEnumStructAccessor(
                self.struct, "L120Timer", 81, 0, ["Shared", "Own"], None, 2, "ALL"
            ),
            "WaterfallTimeOut": GeckoByteStructAccessor(
                self.struct, "WaterfallTimeOut", 118, "ALL"
            ),
            "AuxTimeOut": GeckoByteStructAccessor(self.struct, "AuxTimeOut", 48, "ALL"),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                32,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1", "FiltP1DurOnly"],
                None,
                None,
                "ALL",
            ),
            "CpUsage": GeckoEnumStructAccessor(
                self.struct,
                "CpUsage",
                27,
                None,
                ["STANDARD", "ALWAYS_ON"],
                None,
                None,
                "ALL",
            ),
            "OtOption": GeckoEnumStructAccessor(
                self.struct,
                "OtOption",
                57,
                None,
                ["Disabled", "AlwaysEnabled", "WithSPOver95F"],
                None,
                None,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct, "PurgeSpeed", 81, 2, ["Lo", "Hi"], None, 2, "ALL"
            ),
            "OTTriggerG": GeckoByteStructAccessor(self.struct, "OTTriggerG", 58, "ALL"),
            "CpOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct, "CpOnTimeDuringOT", 59, "ALL"
            ),
            "CpOffTimeDuringOT": GeckoByteStructAccessor(
                self.struct, "CpOffTimeDuringOT", 60, "ALL"
            ),
            "FiltOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct, "FiltOnTimeDuringOT", 61, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 62, "ALL"
            ),
            "DrainMode": GeckoEnumStructAccessor(
                self.struct,
                "DrainMode",
                78,
                None,
                ["NA", "P1", "CP"],
                None,
                None,
                "ALL",
            ),
            "O3Usage": GeckoEnumStructAccessor(
                self.struct,
                "O3Usage",
                28,
                None,
                ["Filter", "Always"],
                None,
                None,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 29, None, ["CP", "P1"], None, None, "ALL"
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "O3Type",
                30,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 63, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 1, "ALL"),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 33, None, ["F", "C"], None, None, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 31, None, ["CP", "P1"], None, None, "ALL"
            ),
            "ProbeLocation": GeckoEnumStructAccessor(
                self.struct,
                "ProbeLocation",
                81,
                3,
                ["IntoPiping", "IntoTub"],
                None,
                2,
                "ALL",
            ),
            "CooldownTime": GeckoByteStructAccessor(
                self.struct, "CooldownTime", 35, "ALL"
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "MinSetpointG", 66, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "MaxSetpointG", 68, "ALL"
            ),
            "EconType": GeckoEnumStructAccessor(
                self.struct,
                "EconType",
                70,
                None,
                ["Standard", "Night"],
                None,
                None,
                "ALL",
            ),
            "NoHeatPeriod": GeckoByteStructAccessor(
                self.struct, "NoHeatPeriod", 77, "ALL"
            ),
            "MaxNumberOfPhases": GeckoByteStructAccessor(
                self.struct, "MaxNumberOfPhases", 26, "ALL"
            ),
            "UL_CE": GeckoEnumStructAccessor(
                self.struct, "UL_CE", 51, None, ["UL", "CE"], None, None, "ALL"
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 52, "ALL"),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "InputCurrent", 53, "ALL"
            ),
            "MinimumInputCurrent": GeckoByteStructAccessor(
                self.struct, "MinimumInputCurrent", 122, "ALL"
            ),
            "InputMenu": GeckoEnumStructAccessor(
                self.struct,
                "InputMenu",
                74,
                None,
                ["Standard", "DualPack"],
                None,
                None,
                "ALL",
            ),
            "Out1Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out1Fuse",
                83,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Out2Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out2Fuse",
                84,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Out3Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out3Fuse",
                85,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Out4Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out4Fuse",
                86,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Out5Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out5Fuse",
                87,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "DirectFuse": GeckoEnumStructAccessor(
                self.struct,
                "DirectFuse",
                88,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "OutHtrFuse": GeckoEnumStructAccessor(
                self.struct,
                "OutHtrFuse",
                89,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "F1Current": GeckoByteStructAccessor(self.struct, "F1Current", 98, "ALL"),
            "F2Current": GeckoByteStructAccessor(self.struct, "F2Current", 99, "ALL"),
            "F3Current": GeckoByteStructAccessor(self.struct, "F3Current", 100, "ALL"),
            "F1Line": GeckoEnumStructAccessor(
                self.struct,
                "F1Line",
                104,
                None,
                ["", "", "", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "F2Line": GeckoEnumStructAccessor(
                self.struct,
                "F2Line",
                105,
                None,
                ["", "", "", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "F3Line": GeckoEnumStructAccessor(
                self.struct,
                "F3Line",
                106,
                None,
                ["", "", "", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 3, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 4, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 6, "ALL"),
            "FiltDur2": GeckoTimeStructAccessor(self.struct, "FiltDur2", 23, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 8, "ALL"),
            "EconDur": GeckoTimeStructAccessor(self.struct, "EconDur", 10, "ALL"),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "EconProgAvailable",
                71,
                None,
                ["NA", "STANDARD", "OUTSIDE_FILTER"],
                None,
                None,
                "ALL",
            ),
            "UDProgEcon": GeckoBoolStructAccessor(
                self.struct, "UDProgEcon", 82, 0, "ALL"
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 72, 2, "ALL"
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "SoakOnCustomKey", 72, 0, "ALL"
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "OffOnCustomKey", 72, 1, "ALL"
            ),
            "CleanupOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "CleanupOnCustomKey", 72, 3, "ALL"
            ),
            "QuickOnOffCustomKey": GeckoBoolStructAccessor(
                self.struct, "QuickOnOffCustomKey", 72, 5, "ALL"
            ),
            "MultiKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "MultiKeyOption",
                76,
                None,
                ["NoBlowerOnI2C", "BlowerOnI2C"],
                None,
                None,
                "ALL",
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct,
                "MasterSlave",
                73,
                None,
                ["", "Master", "Slave"],
                None,
                None,
                "ALL",
            ),
            "SlaveConfig": GeckoByteStructAccessor(
                self.struct, "SlaveConfig", 75, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "TimeFormat",
                34,
                None,
                ["NA", "AmPm", "24h"],
                None,
                None,
                "ALL",
            ),
            "AmbiantOHTrigADC": GeckoWordStructAccessor(
                self.struct, "AmbiantOHTrigADC", 64, "ALL"
            ),
            "Pump1UserAccess": GeckoEnumStructAccessor(
                self.struct,
                "Pump1UserAccess",
                81,
                1,
                ["BothSpeeds", "HighSpeedOnly"],
                None,
                2,
                "ALL",
            ),
            "SelfCleanMsg": GeckoBoolStructAccessor(
                self.struct, "SelfCleanMsg", 81, 4, "ALL"
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "BlowerKeyOption",
                81,
                5,
                ["FreePumpKey", "LastPumpKey"],
                None,
                2,
                "ALL",
            ),
            "HeaterSoftStart": GeckoBoolStructAccessor(
                self.struct, "HeaterSoftStart", 81, 6, "ALL"
            ),
            "HeaterSoftStop": GeckoBoolStructAccessor(
                self.struct, "HeaterSoftStop", 81, 7, "ALL"
            ),
            "KeypadTherapySupport": GeckoBoolStructAccessor(
                self.struct, "KeypadTherapySupport", 43, 0, "ALL"
            ),
            "CustomKeyEnabled": GeckoBoolStructAccessor(
                self.struct, "CustomKeyEnabled", 43, 1, "ALL"
            ),
            "ConfigChange": GeckoEnumStructAccessor(
                self.struct,
                "ConfigChange",
                43,
                2,
                ["NO_RESTRICTION", "PASSWORD_PROTECTED"],
                None,
                2,
                "ALL",
            ),
            "BreakerChange": GeckoEnumStructAccessor(
                self.struct,
                "BreakerChange",
                43,
                3,
                ["NO_RESTRICTION", "PASSWORD_PROTECTED"],
                None,
                2,
                "ALL",
            ),
            "KeypadBacklightColor": GeckoEnumStructAccessor(
                self.struct,
                "KeypadBacklightColor",
                43,
                4,
                ["OFF", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"],
                None,
                8,
                "ALL",
            ),
            "KeypadBacklightEdit": GeckoEnumStructAccessor(
                self.struct,
                "KeypadBacklightEdit",
                43,
                7,
                ["Disable", "Enable"],
                None,
                2,
                "ALL",
            ),
            "ModeKeyAsInvertDisplayKey": GeckoBoolStructAccessor(
                self.struct, "ModeKeyAsInvertDisplayKey", 45, 1, "ALL"
            ),
            "InfoMsgConfig": GeckoEnumStructAccessor(
                self.struct,
                "InfoMsgConfig",
                45,
                2,
                ["HIDE_DETAILED_MSG", "SHOW_ALL_MSG", "", ""],
                None,
                4,
                "ALL",
            ),
            "LowerSetpointMenu": GeckoBoolStructAccessor(
                self.struct, "LowerSetpointMenu", 45, 4, "ALL"
            ),
            "KeypadOptions4": GeckoByteStructAccessor(
                self.struct, "KeypadOptions4", 46, "ALL"
            ),
            "DealerLockSupport": GeckoBoolStructAccessor(
                self.struct, "DealerLockSupport", 47, 0, "ALL"
            ),
            "LockEnabled": GeckoByteStructAccessor(
                self.struct, "LockEnabled", 121, "ALL"
            ),
            "Zone1Led": GeckoEnumStructAccessor(
                self.struct, "Zone1Led", 123, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone1Type": GeckoEnumStructAccessor(
                self.struct, "Zone1Type", 123, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone2Led": GeckoEnumStructAccessor(
                self.struct, "Zone2Led", 124, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone2Type": GeckoEnumStructAccessor(
                self.struct, "Zone2Type", 124, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone3Led": GeckoEnumStructAccessor(
                self.struct, "Zone3Led", 125, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone3Type": GeckoEnumStructAccessor(
                self.struct, "Zone3Type", 125, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone4Led": GeckoEnumStructAccessor(
                self.struct, "Zone4Led", 126, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone4Type": GeckoEnumStructAccessor(
                self.struct, "Zone4Type", 126, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "NumberOfZones": GeckoEnumStructAccessor(
                self.struct, "NumberOfZones", 127, 0, ["", "1", "2", "3"], None, 8, None
            ),
            "MappingEnable": GeckoBoolStructAccessor(
                self.struct, "MappingEnable", 127, 7, None
            ),
            "MapZone1ToOut1": GeckoBoolStructAccessor(
                self.struct, "MapZone1ToOut1", 123, 4, None
            ),
            "MapZone1ToOut2": GeckoBoolStructAccessor(
                self.struct, "MapZone1ToOut2", 123, 5, None
            ),
            "MapZone1ToOut3": GeckoBoolStructAccessor(
                self.struct, "MapZone1ToOut3", 123, 6, None
            ),
            "MapZone1ToOut4": GeckoBoolStructAccessor(
                self.struct, "MapZone1ToOut4", 123, 7, None
            ),
            "MapZone2ToOut1": GeckoBoolStructAccessor(
                self.struct, "MapZone2ToOut1", 124, 4, None
            ),
            "MapZone2ToOut2": GeckoBoolStructAccessor(
                self.struct, "MapZone2ToOut2", 124, 5, None
            ),
            "MapZone2ToOut3": GeckoBoolStructAccessor(
                self.struct, "MapZone2ToOut3", 124, 6, None
            ),
            "MapZone2ToOut4": GeckoBoolStructAccessor(
                self.struct, "MapZone2ToOut4", 124, 7, None
            ),
            "MapZone3ToOut1": GeckoBoolStructAccessor(
                self.struct, "MapZone3ToOut1", 125, 4, None
            ),
            "MapZone3ToOut2": GeckoBoolStructAccessor(
                self.struct, "MapZone3ToOut2", 125, 5, None
            ),
            "MapZone3ToOut3": GeckoBoolStructAccessor(
                self.struct, "MapZone3ToOut3", 125, 6, None
            ),
            "MapZone3ToOut4": GeckoBoolStructAccessor(
                self.struct, "MapZone3ToOut4", 125, 7, None
            ),
            "MapZone4ToOut1": GeckoBoolStructAccessor(
                self.struct, "MapZone4ToOut1", 126, 4, None
            ),
            "MapZone4ToOut2": GeckoBoolStructAccessor(
                self.struct, "MapZone4ToOut2", 126, 5, None
            ),
            "MapZone4ToOut3": GeckoBoolStructAccessor(
                self.struct, "MapZone4ToOut3", 126, 6, None
            ),
            "MapZone4ToOut4": GeckoBoolStructAccessor(
                self.struct, "MapZone4ToOut4", 126, 7, None
            ),
        }
