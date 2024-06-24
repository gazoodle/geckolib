#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v1'
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
        return 1

    @property
    def output_keys(self):
        return []

    @property
    def accessors(self):
        return {
            "Prog1Setpoint": GeckoByteStructAccessor(
                self.struct, "Prog1Setpoint", 0, "ALL"
            ),
            "Prog1Runtime": GeckoWordStructAccessor(
                self.struct, "Prog1Runtime", 1, "ALL"
            ),
            "Prog1Aroma": GeckoEnumStructAccessor(
                self.struct, "Prog1Aroma", 3, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "Prog2Setpoint": GeckoByteStructAccessor(
                self.struct, "Prog2Setpoint", 4, "ALL"
            ),
            "Prog2Runtime": GeckoWordStructAccessor(
                self.struct, "Prog2Runtime", 5, "ALL"
            ),
            "Prog2Aroma": GeckoEnumStructAccessor(
                self.struct, "Prog2Aroma", 7, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct, "TempUnits", 8, None, ["F", "C"], None, None, "ALL"
            ),
        }
