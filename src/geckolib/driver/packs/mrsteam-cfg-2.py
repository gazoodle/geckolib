#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v2'
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
        return []

    @property
    def accessors(self):
        return {
            "Prog1SetpointG": GeckoTempStructAccessor(
                self.struct, "Prog1SetpointG", 0, "ALL"
            ),
            "Prog1Runtime": GeckoWordStructAccessor(
                self.struct, "Prog1Runtime", 2, "ALL"
            ),
            "Prog1Aroma": GeckoEnumStructAccessor(
                self.struct, "Prog1Aroma", 4, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "Prog2SetpointG": GeckoTempStructAccessor(
                self.struct, "Prog2SetpointG", 5, "ALL"
            ),
            "Prog2Runtime": GeckoWordStructAccessor(
                self.struct, "Prog2Runtime", 7, "ALL"
            ),
            "Prog2Aroma": GeckoEnumStructAccessor(
                self.struct, "Prog2Aroma", 9, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 10, None, ["F", "C"], None, None, "ALL"
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct, "MinSetpointG", 11, "ALL"
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct, "MaxSetpointG", 13, "ALL"
            ),
        }
