#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v1'
"""

from . import (
    GeckoByteStructAccessor,
    GeckoWordStructAccessor,
    GeckoTimeStructAccessor,
    GeckoBoolStructAccessor,
    GeckoEnumStructAccessor,
    GeckoTempStructAccessor,
)


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return 1

    @property
    def begin(self):
        return 256

    @property
    def end(self):
        return 280

    @property
    def all_device_keys(self):
        return ["LI"]

    @property
    def user_demand_keys(self):
        return []

    @property
    def error_keys(self):
        return [
            "PowerFailErr",
            "Prr2Err",
            "SlaveH2O2Err",
            "KeyStuckErr",
            "Prr1Err",
            "H2O2Err",
        ]

    @property
    def accessors(self):
        return {
            "Mode": GeckoEnumStructAccessor(
                self.struct, "Mode", 257, 0, ["OFF", "ON"], None, 2, "ALL"
            ),
            "Pause": GeckoBoolStructAccessor(self.struct, "Pause", 257, 1, "ALL"),
            "Diagnostic": GeckoBoolStructAccessor(
                self.struct, "Diagnostic", 257, 2, "ALL"
            ),
            "ChromaState": GeckoEnumStructAccessor(
                self.struct, "ChromaState", 257, 3, ["OFF", "ON"], None, 2, "ALL"
            ),
            "SelectedProg": GeckoEnumStructAccessor(
                self.struct,
                "SelectedProg",
                261,
                None,
                ["User", "Prog1", "Prog2"],
                None,
                None,
                "ALL",
            ),
            "UserSetpoint": GeckoByteStructAccessor(
                self.struct, "UserSetpoint", 262, "ALL"
            ),
            "UserRuntime": GeckoWordStructAccessor(
                self.struct, "UserRuntime", 263, "ALL"
            ),
            "UserAroma": GeckoEnumStructAccessor(
                self.struct, "UserAroma", 265, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 256, None),
            "ExternalProbe": GeckoBoolStructAccessor(
                self.struct, "ExternalProbe", 258, 0, None
            ),
            "WaterDetected": GeckoBoolStructAccessor(
                self.struct, "WaterDetected", 2658, 1, None
            ),
            "NoKeypad": GeckoBoolStructAccessor(self.struct, "NoKeypad", 258, 2, None),
            "NoRegulation": GeckoBoolStructAccessor(
                self.struct, "NoRegulation", 258, 3, None
            ),
            "ExpressCycle": GeckoBoolStructAccessor(
                self.struct, "ExpressCycle", 258, 5, None
            ),
            "SlaveMode": GeckoEnumStructAccessor(
                self.struct, "SlaveMode", 259, 1, ["OFF", "ON"], None, 2, None
            ),
            "SlaveHeaterState": GeckoEnumStructAccessor(
                self.struct, "SlaveHeaterState", 259, 3, ["OFF", "ON"], None, 2, None
            ),
            "PowerFailErr": GeckoBoolStructAccessor(
                self.struct, "PowerFailErr", 260, 0, None
            ),
            "Prr2Err": GeckoBoolStructAccessor(self.struct, "Prr2Err", 260, 1, None),
            "Prr1Err": GeckoBoolStructAccessor(self.struct, "Prr1Err", 260, 2, None),
            "H2O2Err": GeckoBoolStructAccessor(self.struct, "H2O2Err", 260, 3, None),
            "SlaveH2O2Err": GeckoBoolStructAccessor(
                self.struct, "SlaveH2O2Err", 260, 4, None
            ),
            "KeyStuckErr": GeckoBoolStructAccessor(
                self.struct, "KeyStuckErr", 260, 5, None
            ),
            "Jumper9": GeckoBoolStructAccessor(self.struct, "Jumper9", 266, 0, None),
            "Jumper2": GeckoBoolStructAccessor(self.struct, "Jumper2", 266, 1, None),
            "Jumper3": GeckoBoolStructAccessor(self.struct, "Jumper3", 266, 2, None),
            "Jumper4": GeckoBoolStructAccessor(self.struct, "Jumper4", 266, 3, None),
            "Jumper5": GeckoBoolStructAccessor(self.struct, "Jumper5", 266, 4, None),
            "Jumper6": GeckoBoolStructAccessor(self.struct, "Jumper6", 266, 5, None),
            "Jumper7": GeckoBoolStructAccessor(self.struct, "Jumper7", 266, 6, None),
            "Jumper8": GeckoBoolStructAccessor(self.struct, "Jumper8", 266, 7, None),
            "MaxRuntime": GeckoWordStructAccessor(self.struct, "MaxRuntime", 267, None),
            "PackBootID": GeckoWordStructAccessor(self.struct, "PackBootID", 269, None),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "PackBootRev", 271, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "PackBootRel", 272, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "PackType",
                273,
                None,
                [
                    "Unknown",
                    "inXE",
                    "MasIBC",
                    "MIA",
                    "DJS4",
                    "inClear",
                    "inXM",
                    "K600",
                    "inTerface",
                    "inTouch",
                    "inYT",
                    "Color_Keypad",
                    "inYJ",
                    "MrSteam",
                ],
                None,
                None,
                None,
            ),
            "PackMemRange": GeckoEnumStructAccessor(
                self.struct,
                "PackMemRange",
                274,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackCoreID": GeckoWordStructAccessor(self.struct, "PackCoreID", 275, None),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "PackCoreRev", 277, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "PackCoreRel", 278, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "PackConfigLib", 279, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "PackStatusLib", 280, None
            ),
        }
