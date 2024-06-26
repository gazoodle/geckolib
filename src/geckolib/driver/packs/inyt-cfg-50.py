#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v50'
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
        return 50

    @property
    def output_keys(self):
        return [
            "Out1",
            "Out2",
            "Out3",
            "Out4",
            "Out5",
            "OutHtr",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "OutHtr",
                17,
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
            "OutHtRCur": GeckoByteStructAccessor(self.struct, "OutHtRCur", 41, "ALL"),
            "Out6": GeckoEnumStructAccessor(
                self.struct,
                "Out6",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Out7": GeckoEnumStructAccessor(
                self.struct,
                "Out7",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Out8": GeckoEnumStructAccessor(
                self.struct,
                "Out8",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Out9": GeckoEnumStructAccessor(
                self.struct,
                "Out9",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Out10": GeckoEnumStructAccessor(
                self.struct,
                "Out10",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Out11": GeckoEnumStructAccessor(
                self.struct,
                "Out11",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Out12": GeckoEnumStructAccessor(
                self.struct,
                "Out12",
                24,
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
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "Direct",
                25,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Direct2": GeckoEnumStructAccessor(
                self.struct,
                "Direct2",
                26,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Out6Cur": GeckoByteStructAccessor(self.struct, "Out6Cur", 42, "ALL"),
            "Out7Cur": GeckoByteStructAccessor(self.struct, "Out7Cur", 43, "ALL"),
            "Out8Cur": GeckoByteStructAccessor(self.struct, "Out8Cur", 44, "ALL"),
            "Out9Cur": GeckoByteStructAccessor(self.struct, "Out9Cur", 45, "ALL"),
            "Out10Cur": GeckoByteStructAccessor(self.struct, "Out10Cur", 46, "ALL"),
            "Out11Cur": GeckoByteStructAccessor(self.struct, "Out11Cur", 47, "ALL"),
            "Out12Cur": GeckoByteStructAccessor(self.struct, "Out12Cur", 48, "ALL"),
            "DirectCur": GeckoByteStructAccessor(self.struct, "DirectCur", 49, "ALL"),
            "Direct2Cur": GeckoByteStructAccessor(self.struct, "Direct2Cur", 50, "ALL"),
            "OutLi": GeckoEnumStructAccessor(
                self.struct,
                "OutLi",
                83,
                None,
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                None,
            ),
            "LightInts": GeckoByteStructAccessor(self.struct, "LightInts", 84, None),
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
                self.struct, "L120Timer", 85, 0, ["Shared", "Own"], None, 2, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                32,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
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
            "OTActSetpointG": GeckoTempStructAccessor(
                self.struct, "OTActSetpointG", 57, "ALL"
            ),
            "OTTriggerG": GeckoByteStructAccessor(self.struct, "OTTriggerG", 59, "ALL"),
            "CpOnTimeDuringOT": GeckoWordStructAccessor(
                self.struct, "CpOnTimeDuringOT", 60, "ALL"
            ),
            "CpOffTimeDuringOT": GeckoWordStructAccessor(
                self.struct, "CpOffTimeDuringOT", 62, "ALL"
            ),
            "FiltOnTimeDuringOT": GeckoWordStructAccessor(
                self.struct, "FiltOnTimeDuringOT", 64, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 66, "ALL"
            ),
            "DrainMode": GeckoEnumStructAccessor(
                self.struct,
                "DrainMode",
                82,
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
                self.struct, "O3SuspendTime", 67, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 1, "ALL"),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 33, None, ["F", "C"], None, None, "ALL"
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 31, None, ["CP", "P1"], None, None, "ALL"
            ),
            "CooldownTime": GeckoByteStructAccessor(
                self.struct, "CooldownTime", 35, "ALL"
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "MinSetpointG", 70, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "MaxSetpointG", 72, "ALL"
            ),
            "EconType": GeckoEnumStructAccessor(
                self.struct,
                "EconType",
                74,
                None,
                ["Standard", "Night"],
                None,
                None,
                "ALL",
            ),
            "NoHeatPeriod": GeckoByteStructAccessor(
                self.struct, "NoHeatPeriod", 81, "ALL"
            ),
            "UL_CE": GeckoEnumStructAccessor(
                self.struct, "UL_CE", 51, None, ["UL", "CE"], None, None, "ALL"
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 52, "ALL"),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "InputCurrent", 53, "ALL"
            ),
            "InputMenu": GeckoEnumStructAccessor(
                self.struct,
                "InputMenu",
                78,
                None,
                ["Standard", "DualPack"],
                None,
                None,
                "ALL",
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 3, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 4, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 6, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 8, "ALL"),
            "EconDur": GeckoTimeStructAccessor(self.struct, "EconDur", 10, "ALL"),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "EconProgAvailable",
                75,
                None,
                ["NA", "Available"],
                None,
                None,
                "ALL",
            ),
            "UDProgEcon": GeckoBoolStructAccessor(
                self.struct, "UDProgEcon", 86, 0, "ALL"
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 76, 2, "ALL"
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "SoakOnCustomKey", 76, 0, "ALL"
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "OffOnCustomKey", 76, 1, "ALL"
            ),
            "CleanupOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "CleanupOnCustomKey", 76, 3, "ALL"
            ),
            "MultiKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "MultiKeyOption",
                80,
                None,
                ["NoBlowerOnI2C", "BlowerOnI2C"],
                None,
                None,
                "ALL",
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct,
                "MasterSlave",
                77,
                None,
                ["", "Master", "Slave"],
                None,
                None,
                "ALL",
            ),
            "SlaveConfig": GeckoByteStructAccessor(
                self.struct, "SlaveConfig", 79, "ALL"
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
                self.struct, "AmbiantOHTrigADC", 68, "ALL"
            ),
        }
