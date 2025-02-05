"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InMix v4'."""  # noqa: N999

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
                592,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone1Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone1Type",
                592,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone1Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone1Supply",
                592,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone1UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut1", 592, 4, None
            ),
            "Zone1UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut2", 592, 5, None
            ),
            "Zone1UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut3", 592, 6, None
            ),
            "Zone1UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone1UseOut4", 592, 7, None
            ),
            "Zone2Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone2Led",
                593,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone2Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone2Type",
                593,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone2Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone2Supply",
                593,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone2UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut1", 593, 4, None
            ),
            "Zone2UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut2", 593, 5, None
            ),
            "Zone2UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut3", 593, 6, None
            ),
            "Zone2UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone2UseOut4", 593, 7, None
            ),
            "Zone3Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone3Led",
                594,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone3Type",
                594,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone3Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone3Supply",
                594,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone3UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut1", 594, 4, None
            ),
            "Zone3UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut2", 594, 5, None
            ),
            "Zone3UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut3", 594, 6, None
            ),
            "Zone3UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone3UseOut4", 594, 7, None
            ),
            "Zone4Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone4Led",
                595,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone4Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone4Type",
                595,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone4Supply": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Zone4Supply",
                595,
                2,
                ["12V", "5V"],
                None,
                2,
                None,
            ),
            "Zone4UseOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut1", 595, 4, None
            ),
            "Zone4UseOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut2", 595, 5, None
            ),
            "Zone4UseOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut3", 595, 6, None
            ),
            "Zone4UseOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Zone4UseOut4", 595, 7, None
            ),
            "NumberOfZones": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/NumberOfZones",
                596,
                0,
                ["0", "1", "2", "3", "4"],
                None,
                5,
                "ALL",
            ),
            "StatusLightNormalColor": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/StatusLightNormalColor",
                596,
                3,
                ["BLUE", "WHITE", "GREEN", "PURPLE", "YELLOW", "CYAN", "ORANGE", "OFF"],
                None,
                8,
                "ALL",
            ),
            "OutputAttribution": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/OutputAttribution", 596, 7, None
            ),
            "MinimumFadeIntensity": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MinimumFadeIntensity",
                597,
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
                597,
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
                self.struct, "ConfigStructure/RemindersNotBlinkingLED", 597, 7, None
            ),
        }
