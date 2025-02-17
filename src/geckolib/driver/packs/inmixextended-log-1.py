"""GeckoLogStruct - A class to manage the LogStruct for 'InMixExtended v1'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoWordStructAccessor,
)


class GeckoLogStruct:
    """Log Struct Class."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the log struct class."""
        self.struct = struct_

    @property
    def version(self) -> int:
        """Get the log struct class version."""
        return 1

    @property
    def begin(self) -> int:
        """Get the offset start."""
        return 704

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 741

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def all_device_keys(self) -> list[str]:
        """Get all device keys."""
        return []

    @property
    def user_demand_keys(self) -> list[str]:
        """Get all user demand keys."""
        return []

    @property
    def error_keys(self) -> list[str]:
        """Get all error keys."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "InMixExtended-Synchro1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Synchro1",
                704,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Mode1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Mode1",
                705,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Color1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Color1",
                706,
                None,
                [
                    "NO_COLOR",
                    "WHITE",
                    "RED",
                    "GREEN",
                    "BLUE",
                    "PURPLE",
                    "YELLOW",
                    "CYAN",
                    "ORANGE",
                ],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Speed1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Speed1",
                707,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-RedLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-RedLevel1", 708, "ALL"
            ),
            "InMixExtended-GreenLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-GreenLevel1", 709, "ALL"
            ),
            "InMixExtended-BlueLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-BlueLevel1", 710, "ALL"
            ),
            "InMixExtended-Synchro2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Synchro2",
                711,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Mode2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Mode2",
                712,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Color2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Color2",
                713,
                None,
                [
                    "NO_COLOR",
                    "WHITE",
                    "RED",
                    "GREEN",
                    "BLUE",
                    "PURPLE",
                    "YELLOW",
                    "CYAN",
                    "ORANGE",
                ],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Speed2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Speed2",
                714,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-RedLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-RedLevel2", 715, "ALL"
            ),
            "InMixExtended-GreenLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-GreenLevel2", 716, "ALL"
            ),
            "InMixExtended-BlueLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-BlueLevel2", 717, "ALL"
            ),
            "InMixExtended-Synchro3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Synchro3",
                718,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Mode3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Mode3",
                719,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Color3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Color3",
                720,
                None,
                [
                    "NO_COLOR",
                    "WHITE",
                    "RED",
                    "GREEN",
                    "BLUE",
                    "PURPLE",
                    "YELLOW",
                    "CYAN",
                    "ORANGE",
                ],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Speed3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Speed3",
                721,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-RedLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-RedLevel3", 722, "ALL"
            ),
            "InMixExtended-GreenLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-GreenLevel3", 723, "ALL"
            ),
            "InMixExtended-BlueLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-BlueLevel3", 724, "ALL"
            ),
            "InMixExtended-Synchro4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Synchro4",
                725,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Mode4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Mode4",
                726,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Color4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Color4",
                727,
                None,
                [
                    "NO_COLOR",
                    "WHITE",
                    "RED",
                    "GREEN",
                    "BLUE",
                    "PURPLE",
                    "YELLOW",
                    "CYAN",
                    "ORANGE",
                ],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-Speed4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMixExtended-Speed4",
                728,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMixExtended-RedLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-RedLevel4", 729, "ALL"
            ),
            "InMixExtended-GreenLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-GreenLevel4", 730, "ALL"
            ),
            "InMixExtended-BlueLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMixExtended-BlueLevel4", 731, "ALL"
            ),
            "InMixExtended-PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/InMixExtended-PackType",
                732,
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
                    "InMix",
                ],
                None,
                None,
                None,
            ),
            "InMixExtended-MemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/InMixExtended-MemRange",
                733,
                0,
                ["8K", "16K", "32K", "64K"],
                None,
                4,
                None,
            ),
            "InMixExtended-FirmwareID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/InMixExtended-FirmwareID", 734, None
            ),
            "InMixExtended-FirmwareRev": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/PackInfo/InMixExtended-FirmwareRev",
                736,
                None,
            ),
            "InMixExtended-FirmwareRel": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/PackInfo/InMixExtended-FirmwareRel",
                737,
                None,
            ),
            "InMixExtended-ConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/InMixExtended-ConfigLib", 738, None
            ),
            "InMixExtended-StatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/InMixExtended-StatusLib", 739, None
            ),
            "InMixExtended-ErrorFlag": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/Messages/InMixExtended-ErrorFlag",
                740,
                None,
                None,
            ),
            "InMixExtended-ReminderFlag": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/Messages/InMixExtended-ReminderFlag",
                741,
                None,
                None,
            ),
        }
