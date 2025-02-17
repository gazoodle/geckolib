"""GeckoLogStruct - A class to manage the LogStruct for 'InMix v1'."""  # noqa: N999

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
        return 600

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 637

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
            "InMix-Synchro1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Synchro1",
                600,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMix-Mode1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Mode1",
                601,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMix-Color1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Color1",
                602,
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
            "InMix-Speed1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Speed1",
                603,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMix-RedLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-RedLevel1", 604, "ALL"
            ),
            "InMix-GreenLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-GreenLevel1", 605, "ALL"
            ),
            "InMix-BlueLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-BlueLevel1", 606, "ALL"
            ),
            "InMix-Synchro2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Synchro2",
                607,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMix-Mode2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Mode2",
                608,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMix-Color2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Color2",
                609,
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
            "InMix-Speed2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Speed2",
                610,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMix-RedLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-RedLevel2", 611, "ALL"
            ),
            "InMix-GreenLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-GreenLevel2", 612, "ALL"
            ),
            "InMix-BlueLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-BlueLevel2", 613, "ALL"
            ),
            "InMix-Synchro3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Synchro3",
                614,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMix-Mode3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Mode3",
                615,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMix-Color3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Color3",
                616,
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
            "InMix-Speed3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Speed3",
                617,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMix-RedLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-RedLevel3", 618, "ALL"
            ),
            "InMix-GreenLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-GreenLevel3", 619, "ALL"
            ),
            "InMix-BlueLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-BlueLevel3", 620, "ALL"
            ),
            "InMix-Synchro4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Synchro4",
                621,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "InMix-Mode4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Mode4",
                622,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "InMix-Color4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Color4",
                623,
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
            "InMix-Speed4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/InMix-Speed4",
                624,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "InMix-RedLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-RedLevel4", 625, "ALL"
            ),
            "InMix-GreenLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-GreenLevel4", 626, "ALL"
            ),
            "InMix-BlueLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/InMix-BlueLevel4", 627, "ALL"
            ),
            "InMix-PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/InMix-PackType",
                628,
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
            "InMix-MemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/InMix-MemRange",
                629,
                0,
                ["8K", "16K", "32K", "64K"],
                None,
                4,
                None,
            ),
            "InMix-FirmwareID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/InMix-FirmwareID", 630, None
            ),
            "InMix-FirmwareRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/InMix-FirmwareRev", 632, None
            ),
            "InMix-FirmwareRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/InMix-FirmwareRel", 633, None
            ),
            "InMix-ConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/InMix-ConfigLib", 634, None
            ),
            "InMix-StatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/InMix-StatusLib", 635, None
            ),
            "InMix-ErrorFlag": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Messages/InMix-ErrorFlag", 636, None, None
            ),
            "InMix-ReminderFlag": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Messages/InMix-ReminderFlag", 637, None, None
            ),
        }
