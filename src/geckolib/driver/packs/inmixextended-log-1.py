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
    def all_device_keys(self) -> list[str]:
        """Get all device keys."""
        return ["LI"]

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
                "Synchro1",
                704,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode1": GeckoEnumStructAccessor(
                self.struct,
                "Mode1",
                705,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color1": GeckoEnumStructAccessor(
                self.struct,
                "Color1",
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
            "Speed1": GeckoEnumStructAccessor(
                self.struct,
                "Speed1",
                707,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel1": GeckoByteStructAccessor(self.struct, "RedLevel1", 708, "ALL"),
            "GreenLevel1": GeckoByteStructAccessor(
                self.struct, "GreenLevel1", 709, "ALL"
            ),
            "BlueLevel1": GeckoByteStructAccessor(
                self.struct, "BlueLevel1", 710, "ALL"
            ),
            "Synchro2": GeckoEnumStructAccessor(
                self.struct,
                "Synchro2",
                711,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode2": GeckoEnumStructAccessor(
                self.struct,
                "Mode2",
                712,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color2": GeckoEnumStructAccessor(
                self.struct,
                "Color2",
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
            "Speed2": GeckoEnumStructAccessor(
                self.struct,
                "Speed2",
                714,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel2": GeckoByteStructAccessor(self.struct, "RedLevel2", 715, "ALL"),
            "GreenLevel2": GeckoByteStructAccessor(
                self.struct, "GreenLevel2", 716, "ALL"
            ),
            "BlueLevel2": GeckoByteStructAccessor(
                self.struct, "BlueLevel2", 717, "ALL"
            ),
            "Synchro3": GeckoEnumStructAccessor(
                self.struct,
                "Synchro3",
                718,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode3": GeckoEnumStructAccessor(
                self.struct,
                "Mode3",
                719,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color3": GeckoEnumStructAccessor(
                self.struct,
                "Color3",
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
            "Speed3": GeckoEnumStructAccessor(
                self.struct,
                "Speed3",
                721,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel3": GeckoByteStructAccessor(self.struct, "RedLevel3", 722, "ALL"),
            "GreenLevel3": GeckoByteStructAccessor(
                self.struct, "GreenLevel3", 723, "ALL"
            ),
            "BlueLevel3": GeckoByteStructAccessor(
                self.struct, "BlueLevel3", 724, "ALL"
            ),
            "Synchro4": GeckoEnumStructAccessor(
                self.struct,
                "Synchro4",
                725,
                None,
                ["ZONE1", "ZONE2", "ZONE3", "ZONE4"],
                None,
                None,
                "ALL",
            ),
            "Mode4": GeckoEnumStructAccessor(
                self.struct,
                "Mode4",
                726,
                None,
                ["STATIC", "VERY_SLOW_FADE", "SLOW_FADE", "BENOIT1", "BENOIT2", "RGB"],
                None,
                None,
                "ALL",
            ),
            "Color4": GeckoEnumStructAccessor(
                self.struct,
                "Color4",
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
            "Speed4": GeckoEnumStructAccessor(
                self.struct,
                "Speed4",
                728,
                None,
                ["PRESET", "LOW", "MEDIUM", "HIGH", "PAUSE"],
                None,
                None,
                "ALL",
            ),
            "RedLevel4": GeckoByteStructAccessor(self.struct, "RedLevel4", 729, "ALL"),
            "GreenLevel4": GeckoByteStructAccessor(
                self.struct, "GreenLevel4", 730, "ALL"
            ),
            "BlueLevel4": GeckoByteStructAccessor(
                self.struct, "BlueLevel4", 731, "ALL"
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "PackType",
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
            "MemRange": GeckoEnumStructAccessor(
                self.struct,
                "MemRange",
                733,
                0,
                ["8K", "16K", "32K", "64K"],
                None,
                4,
                None,
            ),
            "FirmwareID": GeckoWordStructAccessor(self.struct, "FirmwareID", 734, None),
            "FirmwareRev": GeckoByteStructAccessor(
                self.struct, "FirmwareRev", 736, None
            ),
            "FirmwareRel": GeckoByteStructAccessor(
                self.struct, "FirmwareRel", 737, None
            ),
            "ConfigLib": GeckoByteStructAccessor(self.struct, "ConfigLib", 738, None),
            "StatusLib": GeckoByteStructAccessor(self.struct, "StatusLib", 739, None),
            "ErrorFlag": GeckoBoolStructAccessor(
                self.struct, "ErrorFlag", 740, None, None
            ),
            "ReminderFlag": GeckoBoolStructAccessor(
                self.struct, "ReminderFlag", 741, None, None
            ),
        }
