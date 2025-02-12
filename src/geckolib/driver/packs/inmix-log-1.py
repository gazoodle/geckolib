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
            "Synchro1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Synchro1",
                600,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Mode1",
                601,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Color1",
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
            "Speed1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Speed1",
                603,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/RedLevel1", 604, "ALL"
            ),
            "GreenLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/GreenLevel1", 605, "ALL"
            ),
            "BlueLevel1": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/BlueLevel1", 606, "ALL"
            ),
            "Synchro2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Synchro2",
                607,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Mode2",
                608,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Color2",
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
            "Speed2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Speed2",
                610,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/RedLevel2", 611, "ALL"
            ),
            "GreenLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/GreenLevel2", 612, "ALL"
            ),
            "BlueLevel2": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/BlueLevel2", 613, "ALL"
            ),
            "Synchro3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Synchro3",
                614,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Mode3",
                615,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Color3",
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
            "Speed3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Speed3",
                617,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/RedLevel3", 618, "ALL"
            ),
            "GreenLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/GreenLevel3", 619, "ALL"
            ),
            "BlueLevel3": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/BlueLevel3", 620, "ALL"
            ),
            "Synchro4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Synchro4",
                621,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Mode4",
                622,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Color4",
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
            "Speed4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/Status/Speed4",
                624,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/RedLevel4", 625, "ALL"
            ),
            "GreenLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/GreenLevel4", 626, "ALL"
            ),
            "BlueLevel4": GeckoByteStructAccessor(
                self.struct, "LogStructure/Status/BlueLevel4", 627, "ALL"
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackType",
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
            "MemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/MemRange",
                629,
                0,
                ["8K", "16K", "32K", "64K"],
                None,
                4,
                None,
            ),
            "FirmwareID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/FirmwareID", 630, None
            ),
            "FirmwareRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/FirmwareRev", 632, None
            ),
            "FirmwareRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/FirmwareRel", 633, None
            ),
            "ConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/ConfigLib", 634, None
            ),
            "StatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/StatusLib", 635, None
            ),
            "ErrorFlag": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Messages/ErrorFlag", 636, None, None
            ),
            "ReminderFlag": GeckoBoolStructAccessor(
                self.struct, "LogStructure/Messages/ReminderFlag", 637, None, None
            ),
        }
