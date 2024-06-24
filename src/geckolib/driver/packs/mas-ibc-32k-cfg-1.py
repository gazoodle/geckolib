#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'MAS-IBC-32K v1'
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
            "LL_Backrest": GeckoEnumStructAccessor(
                self.struct,
                "LL_Backrest",
                0,
                None,
                ["SINGLE", "DUAL", "DUAL_THERMOPLACE", "DUAL_LITESTREME"],
                None,
                None,
                None,
            ),
            "LL_Heater_1": GeckoEnumStructAccessor(
                self.struct,
                "LL_Heater_1",
                1,
                None,
                ["Intensity1", "Intensity2", "Intensity3", "Intensity4"],
                None,
                None,
                None,
            ),
            "LL_Heater_2": GeckoEnumStructAccessor(
                self.struct,
                "LL_Heater_2",
                2,
                None,
                ["Intensity1", "Intensity2", "Intensity3", "Intensity4"],
                None,
                None,
                None,
            ),
            "LL_Blower": GeckoEnumStructAccessor(
                self.struct,
                "LL_Blower",
                3,
                None,
                ["STANDARD", "HIGH", "LOW"],
                None,
                None,
                None,
            ),
            "LL_Chromo": GeckoEnumStructAccessor(
                self.struct,
                "LL_Chromo",
                4,
                None,
                ["NONE", "BASIC", "DELUXE"],
                None,
                None,
                None,
            ),
            "LL_Audio": GeckoEnumStructAccessor(
                self.struct, "LL_Audio", 5, None, ["NONE", "MP3"], None, None, None
            ),
            "LL_Menu": GeckoEnumStructAccessor(
                self.struct, "LL_Menu", 6, None, ["STANDARD", "HOTEL"], None, None, None
            ),
            "LL_ComfortJet": GeckoEnumStructAccessor(
                self.struct,
                "LL_ComfortJet",
                7,
                None,
                ["DEACTIVATE", "ACTIVATE"],
                None,
                None,
                None,
            ),
            "LL_Aromacloud": GeckoEnumStructAccessor(
                self.struct,
                "LL_Aromacloud",
                8,
                None,
                ["DEACTIVATE", "ACTIVATE"],
                None,
                None,
                None,
            ),
        }
