#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v8'
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
        return 8

    @property
    def output_keys(self):
        return []

    @property
    def accessors(self):
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigNumber", 0, "ALL"
            ),
            "OutHtRCur": GeckoByteStructAccessor(self.struct, "OutHtRCur", 27, "ALL"),
            "DirectCur": GeckoByteStructAccessor(self.struct, "DirectCur", 26, "ALL"),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "PumpTimeOut", 31, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "LightTimeOut", 32, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "FiltInterface",
                17,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
                None,
                None,
                "ALL",
            ),
            "OTActSetpointG": GeckoTempStructAccessor(
                self.struct, "OTActSetpointG", 33, "ALL"
            ),
            "OTTriggerG": GeckoByteStructAccessor(self.struct, "OTTriggerG", 35, "ALL"),
            "CPOTMaxOnTime": GeckoWordStructAccessor(
                self.struct, "CPOTMaxOnTime", 36, "ALL"
            ),
            "CPOTMaxOffTime": GeckoWordStructAccessor(
                self.struct, "CPOTMaxOffTime", 38, "ALL"
            ),
            "FiltOTDuration24H": GeckoWordStructAccessor(
                self.struct, "FiltOTDuration24H", 40, "ALL"
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct, "FiltSuspendTime", 42, "ALL"
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct, "O3Pump", 14, None, ["CP", "P1"], None, None, "ALL"
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "O3Type",
                15,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "O3SuspendTime", 43, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(self.struct, "SetpointG", 1, "ALL"),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct, "HeaterPump", 16, None, ["CP", "P1"], None, None, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 18, None, ["F", "C"], None, None, "ALL"
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "MinSetpointG", 46, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "MaxSetpointG", 48, "ALL"
            ),
            "EconType": GeckoEnumStructAccessor(
                self.struct,
                "EconType",
                50,
                None,
                ["Standard", "Night"],
                None,
                None,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(self.struct, "NbPhases", 29, "ALL"),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "InputCurrent", 30, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(self.struct, "FiltFreq", 4, "ALL"),
            "FiltStart": GeckoTimeStructAccessor(self.struct, "FiltStart", 5, "ALL"),
            "FiltDur": GeckoTimeStructAccessor(self.struct, "FiltDur", 3, "ALL"),
            "EconStart": GeckoTimeStructAccessor(self.struct, "EconStart", 7, "ALL"),
            "EconDur": GeckoTimeStructAccessor(self.struct, "EconDur", 8, "ALL"),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "EconProgAvailable",
                51,
                None,
                ["NA", "Available"],
                None,
                None,
                "ALL",
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "SoakOnCustomKey", 52, 0, "ALL"
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct, "OffOnCustomKey", 52, 1, "ALL"
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct, "EconControlableManually", 52, 2, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "TimeFormat",
                19,
                None,
                ["NA", "AmPm", "24h"],
                None,
                None,
                "ALL",
            ),
            "AmbiantOHTrigADC": GeckoWordStructAccessor(
                self.struct, "AmbiantOHTrigADC", 44, "ALL"
            ),
        }
