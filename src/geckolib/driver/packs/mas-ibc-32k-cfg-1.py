"""GeckoConfigStruct - A class to manage the ConfigStruct for 'MAS-IBC-32K v1'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
)


class GeckoConfigStruct:
    """Config Struct Class."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the config struct class."""
        self.struct = struct_

    @property
    def version(self) -> int:
        """Get the config struct class version."""
        return 1

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "LL_Backrest": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Backrest",
                0,
                None,
                ["SINGLE", "DUAL", "DUAL_THERMOPLACE", "DUAL_LITESTREME"],
                None,
                None,
                None,
            ),
            "LL_Heater_1": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Heater_1",
                1,
                None,
                ["Intensity1", "Intensity2", "Intensity3", "Intensity4"],
                None,
                None,
                None,
            ),
            "LL_Heater_2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Heater_2",
                2,
                None,
                ["Intensity1", "Intensity2", "Intensity3", "Intensity4"],
                None,
                None,
                None,
            ),
            "LL_Blower": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Blower",
                3,
                None,
                ["STANDARD", "HIGH", "LOW"],
                None,
                None,
                None,
            ),
            "LL_Chromo": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Chromo",
                4,
                None,
                ["NONE", "BASIC", "DELUXE"],
                None,
                None,
                None,
            ),
            "LL_Audio": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Audio",
                5,
                None,
                ["NONE", "MP3"],
                None,
                None,
                None,
            ),
            "LL_Menu": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Menu",
                6,
                None,
                ["STANDARD", "HOTEL"],
                None,
                None,
                None,
            ),
            "LL_ComfortJet": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_ComfortJet",
                7,
                None,
                ["DEACTIVATE", "ACTIVATE"],
                None,
                None,
                None,
            ),
            "LL_Aromacloud": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/LL_Aromacloud",
                8,
                None,
                ["DEACTIVATE", "ACTIVATE"],
                None,
                None,
                None,
            ),
        }
