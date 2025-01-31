"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InMixExtended v5'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
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
        return 5

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Zone1Led": GeckoEnumStructAccessor(
                self.struct, "Zone1Led", 696, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone1Type": GeckoEnumStructAccessor(
                self.struct, "Zone1Type", 696, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone1Supply": GeckoEnumStructAccessor(
                self.struct, "Zone1Supply", 696, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone1UseOut1": GeckoBoolStructAccessor(
                self.struct, "Zone1UseOut1", 696, 4, None
            ),
            "Zone1UseOut2": GeckoBoolStructAccessor(
                self.struct, "Zone1UseOut2", 696, 5, None
            ),
            "Zone1UseOut3": GeckoBoolStructAccessor(
                self.struct, "Zone1UseOut3", 696, 6, None
            ),
            "Zone1UseOut4": GeckoBoolStructAccessor(
                self.struct, "Zone1UseOut4", 696, 7, None
            ),
            "Zone2Led": GeckoEnumStructAccessor(
                self.struct, "Zone2Led", 697, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone2Type": GeckoEnumStructAccessor(
                self.struct, "Zone2Type", 697, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone2Supply": GeckoEnumStructAccessor(
                self.struct, "Zone2Supply", 697, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone2UseOut1": GeckoBoolStructAccessor(
                self.struct, "Zone2UseOut1", 697, 4, None
            ),
            "Zone2UseOut2": GeckoBoolStructAccessor(
                self.struct, "Zone2UseOut2", 697, 5, None
            ),
            "Zone2UseOut3": GeckoBoolStructAccessor(
                self.struct, "Zone2UseOut3", 697, 6, None
            ),
            "Zone2UseOut4": GeckoBoolStructAccessor(
                self.struct, "Zone2UseOut4", 697, 7, None
            ),
            "Zone3Led": GeckoEnumStructAccessor(
                self.struct, "Zone3Led", 698, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone3Type": GeckoEnumStructAccessor(
                self.struct, "Zone3Type", 698, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone3Supply": GeckoEnumStructAccessor(
                self.struct, "Zone3Supply", 698, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone3UseOut1": GeckoBoolStructAccessor(
                self.struct, "Zone3UseOut1", 698, 4, None
            ),
            "Zone3UseOut2": GeckoBoolStructAccessor(
                self.struct, "Zone3UseOut2", 698, 5, None
            ),
            "Zone3UseOut3": GeckoBoolStructAccessor(
                self.struct, "Zone3UseOut3", 698, 6, None
            ),
            "Zone3UseOut4": GeckoBoolStructAccessor(
                self.struct, "Zone3UseOut4", 698, 7, None
            ),
            "Zone4Led": GeckoEnumStructAccessor(
                self.struct, "Zone4Led", 699, 0, ["RGB", "WHITE"], None, 2, None
            ),
            "Zone4Type": GeckoEnumStructAccessor(
                self.struct, "Zone4Type", 699, 1, ["NORMAL", "STATUS"], None, 2, None
            ),
            "Zone4Supply": GeckoEnumStructAccessor(
                self.struct, "Zone4Supply", 699, 2, ["12V", "5V"], None, 2, None
            ),
            "Zone4UseOut1": GeckoBoolStructAccessor(
                self.struct, "Zone4UseOut1", 699, 4, None
            ),
            "Zone4UseOut2": GeckoBoolStructAccessor(
                self.struct, "Zone4UseOut2", 699, 5, None
            ),
            "Zone4UseOut3": GeckoBoolStructAccessor(
                self.struct, "Zone4UseOut3", 699, 6, None
            ),
            "Zone4UseOut4": GeckoBoolStructAccessor(
                self.struct, "Zone4UseOut4", 699, 7, None
            ),
            "NumberOfZones": GeckoEnumStructAccessor(
                self.struct,
                "NumberOfZones",
                700,
                0,
                ["0", "1", "2", "3", "4"],
                None,
                5,
                "ALL",
            ),
            "StatusLightNormalColor": GeckoEnumStructAccessor(
                self.struct,
                "StatusLightNormalColor",
                700,
                3,
                ["BLUE", "WHITE", "GREEN", "PURPLE", "YELLOW", "CYAN", "ORANGE", "OFF"],
                None,
                8,
                "ALL",
            ),
            "OutputAttribution": GeckoBoolStructAccessor(
                self.struct, "OutputAttribution", 700, 7, None
            ),
            "MinimumFadeIntensity": GeckoEnumStructAccessor(
                self.struct,
                "MinimumFadeIntensity",
                701,
                0,
                [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                ],
                None,
                16,
                "ALL",
            ),
            "StatusLightRemindersColor": GeckoEnumStructAccessor(
                self.struct,
                "StatusLightRemindersColor",
                701,
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
                self.struct, "RemindersNotBlinkingLED", 701, 7, None
            ),
            "StatusLightFading": GeckoBoolStructAccessor(
                self.struct, "StatusLightFading", 702, 0, None
            ),
        }
