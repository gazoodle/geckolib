#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v9'
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
        return 9

    @property
    def output_keys(self):
        return ["Out1", "Out2", "Out3", "Out4", "Out5", "OutHtr"]

    @property
    def accessors(self):
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigNumber", 0, "ALL"
            ),
            "Out1": GeckoEnumStructAccessor(
                self.struct,
                "Out1",
                9,
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
                10,
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
                11,
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
            "Out5": GeckoEnumStructAccessor(
                self.struct,
                "Out5",
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
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "OutHtr",
                14,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1Cur": GeckoByteStructAccessor(self.struct, "Out1Cur", 23, "ALL"),
            "Out2Cur": GeckoByteStructAccessor(self.struct, "Out2Cur", 24, "ALL"),
            "Out3Cur": GeckoByteStructAccessor(self.struct, "Out3Cur", 25, "ALL"),
            "Out4Cur": GeckoByteStructAccessor(self.struct, "Out4Cur", 26, "ALL"),
            "Out5Cur": GeckoByteStructAccessor(self.struct, "Out5Cur", 27, "ALL"),
            "OutHtRCur": GeckoByteStructAccessor(self.struct, "OutHtRCur", 28, "ALL"),
            "DirectCur": GeckoByteStructAccessor(self.struct, "DirectCur", 29, "ALL"),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 33, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 34, "ALL"
            ),
            "L120TimeOut": GeckoByteStructAccessor(
                self.struct, "L120TimeOut", 35, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                20,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
                None,
                None,
                "ALL",
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "CPAlwaysON", 15, 0, "ALL"
            ),
            "OTActSetpointG": GeckoTempStructAccessor(
                self.struct, "OTActSetpointG", 36, "ALL"
            ),
            "OTTriggerG": GeckoByteStructAccessor(self.struct, "OTTriggerG", 38, "ALL"),
            "CPOTMaxOnTime": GeckoWordStructAccessor(
                self.struct, "CPOTMaxOnTime", 39, "ALL"
            ),
            "CPOTMaxOffTime": GeckoWordStructAccessor(
                self.struct, "CPOTMaxOffTime", 41, "ALL"
            ),
            "FiltOTDuration24H": GeckoWordStructAccessor(
                self.struct, "FiltOTDuration24H", 43, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 45, "ALL"
            ),
            "O3Usage": GeckoEnumStructAccessor(
                self.struct,
                "O3Usage",
                16,
                None,
                ["Filter", "Always"],
                None,
                None,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 17, None, ["CP", "P1"], None, None, "ALL"
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "O3Type",
                18,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 46, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 1, "ALL"),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 19, None, ["CP", "P1"], None, None, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 21, None, ["F", "C"], None, None, "ALL"
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "MinSetpointG", 49, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "MaxSetpointG", 51, "ALL"
            ),
            "EconType": GeckoEnumStructAccessor(
                self.struct,
                "EconType",
                53,
                None,
                ["Standard", "Night"],
                None,
                None,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 31, "ALL"),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "InputCurrent", 32, "ALL"
            ),
            "InputMenu": GeckoEnumStructAccessor(
                self.struct,
                "InputMenu",
                57,
                None,
                ["Standard", "DualPack"],
                None,
                None,
                "ALL",
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 4, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 5, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 3, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 7, "ALL"),
            "EconDur": GeckoTimeStructAccessor(self.struct, "EconDur", 8, "ALL"),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "EconProgAvailable",
                54,
                None,
                ["NA", "Available"],
                None,
                None,
                "ALL",
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "SoakOnCustomKey", 55, 0, "ALL"
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "OffOnCustomKey", 55, 1, "ALL"
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 55, 2, "ALL"
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct,
                "MasterSlave",
                56,
                None,
                ["Unconfigured", "Master", "Slave"],
                None,
                None,
                "ALL",
            ),
            "SlaveConfig": GeckoByteStructAccessor(
                self.struct, "SlaveConfig", 58, "ALL"
            ),
            "MultiKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "MultiKeyOption",
                59,
                None,
                ["NoBlowerOnI2C", "BlowerOnI2C"],
                None,
                None,
                "ALL",
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "TimeFormat",
                22,
                None,
                ["NA", "AmPm", "24h"],
                None,
                None,
                "ALL",
            ),
            "AmbiantOHTrigADC": GeckoWordStructAccessor(
                self.struct, "AmbiantOHTrigADC", 47, "ALL"
            ),
        }
