"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InMixExtended v4'."""  # noqa: N999

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
        return 4

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "Zone1Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone1Led",
                696,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone1Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone1Type",
                696,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone1Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone1Supply",
                696,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone1UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut1", 696, 4, None
            ),
            "Zone1UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut2", 696, 5, None
            ),
            "Zone1UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut3", 696, 6, None
            ),
            "Zone1UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut4", 696, 7, None
            ),
            "Zone2Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone2Led",
                697,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone2Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone2Type",
                697,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone2Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone2Supply",
                697,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone2UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut1", 697, 4, None
            ),
            "Zone2UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut2", 697, 5, None
            ),
            "Zone2UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut3", 697, 6, None
            ),
            "Zone2UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut4", 697, 7, None
            ),
            "Zone3Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone3Led",
                698,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone3Type",
                698,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone3Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone3Supply",
                698,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone3UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut1", 698, 4, None
            ),
            "Zone3UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut2", 698, 5, None
            ),
            "Zone3UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut3", 698, 6, None
            ),
            "Zone3UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut4", 698, 7, None
            ),
            "Zone4Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone4Led",
                699,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone4Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone4Type",
                699,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone4Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone4Supply",
                699,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone4UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut1", 699, 4, None
            ),
            "Zone4UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut2", 699, 5, None
            ),
            "Zone4UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut3", 699, 6, None
            ),
            "Zone4UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut4", 699, 7, None
            ),
            "NumberOfZones": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/NumberOfZones",
                700,
                0,
                ["0", "1", "2", "3", "4"],
                None,
                5,
                "ALL",
            ),
            "StatusLightNormalColor": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/StatusLightNormalColor",
                700,
                3,
                ["BLUE", "WHITE", "GREEN", "PURPLE", "YELLOW", "CYAN", "ORANGE", "OFF"],
                None,
                8,
                "ALL",
            ),
            "OutputAttribution": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/OutputAttribution", 700, 7, None
            ),
            "MinimumFadeIntensity": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MinimumFadeIntensity",
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
                "ConfigStructure/StatusLightRemindersColor",
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
                self.struct, "ConfigStructure/RemindersNotBlinkingLED", 701, 7, None
            ),
        }
