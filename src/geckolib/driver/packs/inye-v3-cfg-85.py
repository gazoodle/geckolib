#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'inYE-V3 v85'
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
        return 85

    @property
    def output_keys(self):
        return [
            "Out1",
            "Out2",
            "Out3",
            "Out4",
            "Out5",
            "OutHtr",
            "HeatPumpCurrent",
            "HeatPumpFuse",
            "Out6",
            "Out7",
            "Out8",
            "Out9",
            "Out10",
            "Out11",
            "Out12",
            "Direct",
            "Direct2",
            "OutLi",
            "LightActivationSafety",
        ]

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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
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
                26,
                None,
                [
                    "NA",
                    "P1H",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "HTR",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "HTR2",
                ],
                None,
                None,
                "ALL",
            ),
            "Out1Cur": GeckoByteStructAccessor(self.struct, "Out1Cur", 36, "ALL"),
            "Out2Cur": GeckoByteStructAccessor(self.struct, "Out2Cur", 37, "ALL"),
            "Out3Cur": GeckoByteStructAccessor(self.struct, "Out3Cur", 38, "ALL"),
            "Out4Cur": GeckoByteStructAccessor(self.struct, "Out4Cur", 39, "ALL"),
            "Out5Cur": GeckoByteStructAccessor(self.struct, "Out5Cur", 40, "ALL"),
            "OutHtRCur": GeckoByteStructAccessor(self.struct, "OutHtRCur", 50, "ALL"),
            "HeatPumpCurrent": GeckoEnumStructAccessor(
                self.struct,
                "HeatPumpCurrent",
                161,
                None,
                [
                    "Not_Set",
                    "0A",
                    "1A",
                    "2A",
                    "3A",
                    "4A",
                    "5A",
                    "6A",
                    "7A",
                    "8A",
                    "9A",
                    "10A",
                    "11A",
                    "12A",
                    "13A",
                    "14A",
                    "15A",
                ],
                None,
                None,
                "ALL",
            ),
            "HeatPumpFuse": GeckoEnumStructAccessor(
                self.struct,
                "HeatPumpFuse",
                163,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out6": GeckoEnumStructAccessor(
                self.struct,
                "Out6",
                17,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out7": GeckoEnumStructAccessor(
                self.struct,
                "Out7",
                18,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out8": GeckoEnumStructAccessor(
                self.struct,
                "Out8",
                19,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out9": GeckoEnumStructAccessor(
                self.struct,
                "Out9",
                20,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out10": GeckoEnumStructAccessor(
                self.struct,
                "Out10",
                21,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out11": GeckoEnumStructAccessor(
                self.struct,
                "Out11",
                22,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out12": GeckoEnumStructAccessor(
                self.struct,
                "Out12",
                23,
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
                    "Fan",
                    "ColdPump",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "Protection",
                    "HTR2",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "Direct",
                24,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Direct2": GeckoEnumStructAccessor(
                self.struct,
                "Direct2",
                25,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Out6Cur": GeckoByteStructAccessor(self.struct, "Out6Cur", 41, "ALL"),
            "Out7Cur": GeckoByteStructAccessor(self.struct, "Out7Cur", 42, "ALL"),
            "Out8Cur": GeckoByteStructAccessor(self.struct, "Out8Cur", 43, "ALL"),
            "Out9Cur": GeckoByteStructAccessor(self.struct, "Out9Cur", 44, "ALL"),
            "Out10Cur": GeckoByteStructAccessor(self.struct, "Out10Cur", 45, "ALL"),
            "Out11Cur": GeckoByteStructAccessor(self.struct, "Out11Cur", 46, "ALL"),
            "Out12Cur": GeckoByteStructAccessor(self.struct, "Out12Cur", 47, "ALL"),
            "DirectCur": GeckoByteStructAccessor(self.struct, "DirectCur", 48, "ALL"),
            "Direct2Cur": GeckoByteStructAccessor(self.struct, "Direct2Cur", 49, "ALL"),
            "WaterfallAsCP": GeckoBoolStructAccessor(
                self.struct, "WaterfallAsCP", 119, 2, "ALL"
            ),
            "WaterfallValveOnCP": GeckoBoolStructAccessor(
                self.struct, "WaterfallValveOnCP", 119, 4, "ALL"
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
            "LightActivationSafety": GeckoEnumStructAccessor(
                self.struct,
                "LightActivationSafety",
                180,
                None,
                ["Disable", "Enable"],
                None,
                None,
                None,
            ),
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
            "AuxTimeOut": GeckoByteStructAccessor(
                self.struct, "AuxTimeOut", 120, "ALL"
            ),
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
            "AuxAsBubbleGen": GeckoBoolStructAccessor(
                self.struct, "AuxAsBubbleGen", 119, 1, "ALL"
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
            "FlowDetector": GeckoEnumStructAccessor(
                self.struct,
                "FlowDetector",
                164,
                None,
                ["inFlo", "NotInstalled", "PressureSwitch"],
                None,
                None,
                "ALL",
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
            "CoolZoneMode": GeckoEnumStructAccessor(
                self.struct,
                "CoolZoneMode",
                115,
                None,
                [
                    "CHILL",
                    "HEAT_W_BOOST",
                    "HEAT_SAVER",
                    "AUTO_W_BOOST",
                    "AUTO_SAVER",
                    "INTERNAL_HEAT",
                    "BOTH_HEAT",
                ],
                None,
                None,
                "ALL",
            ),
            "GenericHeatPumpID": GeckoByteStructAccessor(
                self.struct, "GenericHeatPumpID", 162, "ALL"
            ),
            "UL_CE": GeckoEnumStructAccessor(
                self.struct, "UL_CE", 51, None, ["UL", "CE"], None, None, "ALL"
            ),
            "MaxNumberOfPhases": GeckoByteStructAccessor(
                self.struct, "MaxNumberOfPhases", 114, "ALL"
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 52, "ALL"),
            "Max1phaseSinglePackCurrent": GeckoByteStructAccessor(
                self.struct, "Max1phaseSinglePackCurrent", 165, "ALL"
            ),
            "Max2phaseSinglePackCurrent": GeckoByteStructAccessor(
                self.struct, "Max2phaseSinglePackCurrent", 166, "ALL"
            ),
            "Max3phaseSinglePackCurrent": GeckoByteStructAccessor(
                self.struct, "Max3phaseSinglePackCurrent", 167, "ALL"
            ),
            "Max1phaseDualPackCurrent": GeckoByteStructAccessor(
                self.struct, "Max1phaseDualPackCurrent", 168, "ALL"
            ),
            "Max2phaseDualPackCurrent": GeckoByteStructAccessor(
                self.struct, "Max2phaseDualPackCurrent", 169, "ALL"
            ),
            "Max3phaseDualPackCurrent": GeckoByteStructAccessor(
                self.struct, "Max3phaseDualPackCurrent", 170, "ALL"
            ),
            "RealPackType": GeckoEnumStructAccessor(
                self.struct,
                "RealPackType",
                171,
                None,
                ["", "", "", "", "", "", "", "", "", "", "inYT", "", "inYJ"],
                None,
                None,
                None,
            ),
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
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out2Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out2Fuse",
                84,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out3Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out3Fuse",
                85,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out4Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out4Fuse",
                86,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out5Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out5Fuse",
                87,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out6Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out6Fuse",
                88,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out7Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out7Fuse",
                89,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out8Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out8Fuse",
                90,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out9Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out9Fuse",
                91,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out10Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out10Fuse",
                92,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out11Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out11Fuse",
                93,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out12Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Out12Fuse",
                94,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Direct1Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Direct1Fuse",
                95,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Direct2Fuse": GeckoEnumStructAccessor(
                self.struct,
                "Direct2Fuse",
                96,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "OutHtrFuse": GeckoEnumStructAccessor(
                self.struct,
                "OutHtrFuse",
                97,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F1Current": GeckoByteStructAccessor(self.struct, "F1Current", 98, "ALL"),
            "F2Current": GeckoByteStructAccessor(self.struct, "F2Current", 99, "ALL"),
            "F3Current": GeckoByteStructAccessor(self.struct, "F3Current", 100, "ALL"),
            "F21Current": GeckoByteStructAccessor(
                self.struct, "F21Current", 101, "ALL"
            ),
            "F22Current": GeckoByteStructAccessor(
                self.struct, "F22Current", 102, "ALL"
            ),
            "F23Current": GeckoByteStructAccessor(
                self.struct, "F23Current", 103, "ALL"
            ),
            "F1Line": GeckoEnumStructAccessor(
                self.struct,
                "F1Line",
                104,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F2Line": GeckoEnumStructAccessor(
                self.struct,
                "F2Line",
                105,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F3Line": GeckoEnumStructAccessor(
                self.struct,
                "F3Line",
                106,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F21Line": GeckoEnumStructAccessor(
                self.struct,
                "F21Line",
                107,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F22Line": GeckoEnumStructAccessor(
                self.struct,
                "F22Line",
                108,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F23Line": GeckoEnumStructAccessor(
                self.struct,
                "F23Line",
                109,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 3, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 4, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 6, "ALL"),
            "FiltDur2": GeckoTimeStructAccessor(self.struct, "FiltDur2", 116, "ALL"),
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
            "AuxOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "AuxOnCustomKey", 72, 4, "ALL"
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
            "ProgOutAccessory": GeckoEnumStructAccessor(
                self.struct,
                "ProgOutAccessory",
                160,
                None,
                [
                    "NA",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "ONZEN",
                    "",
                    "",
                    "",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "ProgOutStart": GeckoTimeStructAccessor(
                self.struct, "ProgOutStart", 128, "ALL"
            ),
            "ProgOutDur": GeckoTimeStructAccessor(
                self.struct, "ProgOutDur", 130, "ALL"
            ),
            "ProgOutFreq": GeckoByteStructAccessor(
                self.struct, "ProgOutFreq", 132, "ALL"
            ),
            "SilentMode": GeckoEnumStructAccessor(
                self.struct,
                "SilentMode",
                157,
                None,
                ["NA", "OFF", "ECONOMY", "SLEEP", "NIGHT"],
                None,
                None,
                "ALL",
            ),
            "SilentDuration": GeckoTimeStructAccessor(
                self.struct, "SilentDuration", 158, "ALL"
            ),
            "SuspendSilentToRegulate": GeckoEnumStructAccessor(
                self.struct,
                "SuspendSilentToRegulate",
                119,
                3,
                ["NOT_ALLOWED", "ALLOWED"],
                None,
                2,
                "ALL",
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
                self.struct, "KeypadTherapySupport", 110, 0, "ALL"
            ),
            "CustomKeyEnabled": GeckoBoolStructAccessor(
                self.struct, "CustomKeyEnabled", 110, 1, "ALL"
            ),
            "ConfigChange": GeckoEnumStructAccessor(
                self.struct,
                "ConfigChange",
                110,
                2,
                ["NO_RESTRICTION", "PASSWORD_PROTECTED"],
                None,
                2,
                "ALL",
            ),
            "BreakerChange": GeckoEnumStructAccessor(
                self.struct,
                "BreakerChange",
                110,
                3,
                ["NO_RESTRICTION", "PASSWORD_PROTECTED"],
                None,
                2,
                "ALL",
            ),
            "KeypadBacklightColor": GeckoEnumStructAccessor(
                self.struct,
                "KeypadBacklightColor",
                110,
                4,
                ["OFF", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"],
                None,
                8,
                "ALL",
            ),
            "KeypadBacklightEdit": GeckoEnumStructAccessor(
                self.struct,
                "KeypadBacklightEdit",
                110,
                7,
                ["Disable", "Enable"],
                None,
                2,
                "ALL",
            ),
            "ModeKeyAsInvertDisplayKey": GeckoBoolStructAccessor(
                self.struct, "ModeKeyAsInvertDisplayKey", 112, 1, "ALL"
            ),
            "InfoMsgConfig": GeckoEnumStructAccessor(
                self.struct,
                "InfoMsgConfig",
                112,
                2,
                ["HIDE_DETAILED_MSG", "SHOW_ALL_MSG", "", ""],
                None,
                4,
                "ALL",
            ),
            "LowerSetpointMenu": GeckoBoolStructAccessor(
                self.struct, "LowerSetpointMenu", 112, 4, "ALL"
            ),
            "SinglePumpKey": GeckoEnumStructAccessor(
                self.struct,
                "SinglePumpKey",
                112,
                6,
                ["NA", "ForSpeeds", "ForZones", ""],
                None,
                4,
                "ALL",
            ),
            "KeypadOptions4": GeckoByteStructAccessor(
                self.struct, "KeypadOptions4", 113, "ALL"
            ),
            "DealerLockSupport": GeckoBoolStructAccessor(
                self.struct, "DealerLockSupport", 119, 0, "ALL"
            ),
            "LockEnabled": GeckoByteStructAccessor(
                self.struct, "LockEnabled", 121, "ALL"
            ),
            "VSPType": GeckoEnumStructAccessor(
                self.struct,
                "VSPType",
                181,
                None,
                ["NoVsp", "Hydropool", "Gecko_VMS_OnModbus"],
                None,
                None,
                "ALL",
            ),
            "VSPHeatingSpeed": GeckoByteStructAccessor(
                self.struct, "VSPHeatingSpeed", 182, "ALL"
            ),
            "VSPFilteringSpeed": GeckoByteStructAccessor(
                self.struct, "VSPFilteringSpeed", 183, "ALL"
            ),
            "AssignVSP1": GeckoEnumStructAccessor(
                self.struct,
                "AssignVSP1",
                173,
                None,
                ["NA", "P1", "P2", "P3", "P4", "P5"],
                None,
                None,
                "ALL",
            ),
            "AssignVSP2": GeckoEnumStructAccessor(
                self.struct,
                "AssignVSP2",
                174,
                None,
                ["NA", "P1", "P2", "P3", "P4", "P5"],
                None,
                None,
                "ALL",
            ),
            "AssignVSP3": GeckoEnumStructAccessor(
                self.struct,
                "AssignVSP3",
                175,
                None,
                ["NA", "P1", "P2", "P3", "P4", "P5"],
                None,
                None,
                "ALL",
            ),
            "AssignVSP4": GeckoEnumStructAccessor(
                self.struct,
                "AssignVSP4",
                176,
                None,
                ["NA", "P1", "P2", "P3", "P4", "P5"],
                None,
                None,
                "ALL",
            ),
            "AssignVSP5": GeckoEnumStructAccessor(
                self.struct,
                "AssignVSP5",
                177,
                None,
                ["NA", "P1", "P2", "P3", "P4", "P5"],
                None,
                None,
                "ALL",
            ),
            "ExerciseType": GeckoEnumStructAccessor(
                self.struct,
                "ExerciseType",
                133,
                None,
                ["NO_EXERCISE", "SWIM_EXERCISE"],
                None,
                None,
                "ALL",
            ),
            "ExerciseControl": GeckoEnumStructAccessor(
                self.struct,
                "ExerciseControl",
                134,
                None,
                ["USE_STANDARD_PUMPS", "USE_VARIABLE_SPEED_PUMPS"],
                None,
                None,
                "ALL",
            ),
            "ExercisePumpsUsed": GeckoEnumStructAccessor(
                self.struct,
                "ExercisePumpsUsed",
                135,
                0,
                [
                    "NO_PUMP",
                    "ALL_PUMPS",
                    "P2_TO_P5",
                    "P3_TO_P5",
                    "P4_AND_P5",
                    "P5_ONLY",
                    "",
                    "",
                ],
                None,
                8,
                "ALL",
            ),
            "ExerciseDedicatedPumps": GeckoBoolStructAccessor(
                self.struct, "ExerciseDedicatedPumps", 135, 7, "ALL"
            ),
            "ExerciseBuoyancyPump": GeckoEnumStructAccessor(
                self.struct,
                "ExerciseBuoyancyPump",
                178,
                None,
                ["NA", "P1", "P2", "P3", "P4", "P5"],
                None,
                None,
                "ALL",
            ),
            "ExerciseNumberOfIntensity": GeckoByteStructAccessor(
                self.struct, "ExerciseNumberOfIntensity", 136, "ALL"
            ),
            "ExcercisePumpIntensity1": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity1", 137, "ALL"
            ),
            "ExcercisePumpIntensity2": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity2", 139, "ALL"
            ),
            "ExcercisePumpIntensity3": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity3", 141, "ALL"
            ),
            "ExcercisePumpIntensity4": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity4", 143, "ALL"
            ),
            "ExcercisePumpIntensity5": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity5", 145, "ALL"
            ),
            "ExcercisePumpIntensity6": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity6", 147, "ALL"
            ),
            "ExcercisePumpIntensity7": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity7", 149, "ALL"
            ),
            "ExcercisePumpIntensity8": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity8", 151, "ALL"
            ),
            "ExcercisePumpIntensity9": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity9", 153, "ALL"
            ),
            "ExcercisePumpIntensity10": GeckoWordStructAccessor(
                self.struct, "ExcercisePumpIntensity10", 155, "ALL"
            ),
            "MassageEnablePump1": GeckoBoolStructAccessor(
                self.struct, "MassageEnablePump1", 185, 0, None
            ),
            "MassageEnablePump2": GeckoBoolStructAccessor(
                self.struct, "MassageEnablePump2", 185, 1, None
            ),
            "MassageEnablePump3": GeckoBoolStructAccessor(
                self.struct, "MassageEnablePump3", 185, 2, None
            ),
            "MassageEnablePump4": GeckoBoolStructAccessor(
                self.struct, "MassageEnablePump4", 185, 3, None
            ),
            "MassageEnablePump5": GeckoBoolStructAccessor(
                self.struct, "MassageEnablePump5", 185, 4, None
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
                self.struct,
                "NumberOfZones",
                127,
                0,
                ["", "1", "2", "3", "4"],
                None,
                8,
                None,
            ),
            "StatusLightNormalColor": GeckoEnumStructAccessor(
                self.struct,
                "StatusLightNormalColor",
                127,
                3,
                ["BLUE", "WHITE", "GREEN", "PURPLE", "YELLOW", "CYAN", "ORANGE", "OFF"],
                None,
                8,
                "ALL",
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
            "InMixZoneToFollow": GeckoEnumStructAccessor(
                self.struct,
                "InMixZoneToFollow",
                172,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4", "AS_12V_SUPPLY"],
                None,
                None,
                None,
            ),
            "StatusLightRemindersColor": GeckoEnumStructAccessor(
                self.struct,
                "StatusLightRemindersColor",
                179,
                4,
                [
                    "SAME_AS_NORMAL",
                    "WHITE",
                    "GREEN",
                    "PURPLE",
                    "YELLOW",
                    "CYAN",
                    "ORANGE",
                    "OFF",
                ],
                None,
                8,
                "ALL",
            ),
            "RemindersNotBlinkingLED": GeckoBoolStructAccessor(
                self.struct, "RemindersNotBlinkingLED", 179, 7, None
            ),
            "StatusLightFading": GeckoBoolStructAccessor(
                self.struct, "StatusLightFading", 184, 0, None
            ),
        }
