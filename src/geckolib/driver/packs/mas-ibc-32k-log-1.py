"""GeckoLogStruct - A class to manage the LogStruct for 'MAS-IBC-32K v1'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
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
        return 256

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 285

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def all_device_keys(self) -> list[str]:
        """Get all device keys."""
        return [
            "KeypadID",
            "KeypadRev",
            "BlowerState",
            "PurgeStart",
            "PurgeDelayTimer",
            "PurgeStandby",
            "PowerState",
            "KeypadLock",
            "LI",
        ]

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
            "UserBlowerIntensity": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UserBlowerIntensity", 256, "ALL"
            ),
            "UserChroma": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UserChroma",
                257,
                None,
                [
                    "OFF",
                    "WHITE",
                    "RED",
                    "GREEN",
                    "BLUE",
                    "PURPLE",
                    "YELLOW",
                    "SCAN",
                    "ORANGE",
                    "PAUSE",
                ],
                None,
                None,
                "ALL",
            ),
            "UserBathTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UserBathTime", 258, "ALL"
            ),
            "UserHeater1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UserHeater1",
                259,
                None,
                ["OFF", "LOW", "MED", "HIGH"],
                None,
                None,
                "ALL",
            ),
            "UserHeater2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UserHeater2",
                260,
                None,
                ["OFF", "LOW", "MED", "HIGH"],
                None,
                None,
                "ALL",
            ),
            "UserGeysair": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UserGeysair",
                261,
                None,
                ["OFF", "ON"],
                None,
                None,
                None,
            ),
            "UserDryingCycle": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UserDryingCycle",
                262,
                0,
                ["AfterBath", "Daily"],
                None,
                2,
                "ALL",
            ),
            "UserDryingHour": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UserDryingHour", 263, "ALL"
            ),
            "UserDryingMinute": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UserDryingMinute", 264, "ALL"
            ),
            "UserDryingSecond": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UserDryingSecond", 265, "ALL"
            ),
            "UserDryingDelay": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UserDryingDelay",
                266,
                0,
                [
                    "0",
                    "",
                    "",
                    "",
                    "",
                    "5",
                    "",
                    "",
                    "",
                    "",
                    "10",
                    "",
                    "",
                    "",
                    "",
                    "15",
                    "",
                    "",
                    "",
                    "",
                    "20",
                    "",
                    "",
                    "",
                    "",
                    "25",
                    "",
                    "",
                    "",
                    "",
                    "30",
                    "",
                    "",
                    "",
                    "",
                    "35",
                    "",
                    "",
                    "",
                    "",
                    "40",
                    "",
                    "",
                    "",
                    "",
                    "45",
                    "",
                    "",
                    "",
                    "",
                    "50",
                    "",
                    "",
                    "",
                    "",
                    "55",
                    "",
                    "",
                    "",
                    "",
                    "60",
                ],
                None,
                63,
                "ALL",
            ),
            "KeypadID": GeckoWordStructAccessor(
                self.struct, "LogStructure/DeviceStatus/KeypadID", 267, None
            ),
            "KeypadRev": GeckoWordStructAccessor(
                self.struct, "LogStructure/DeviceStatus/KeypadRev", 269, None
            ),
            "BlowerState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/BlowerState",
                271,
                None,
                ["PAUSE", "RUN", "STATE10"],
                None,
                None,
                None,
            ),
            "PurgeStart": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/PurgeStart",
                262,
                1,
                ["DEACTIVATE", "ACTIVATE"],
                None,
                None,
                None,
            ),
            "PurgeDelayTimer": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/PurgeDelayTimer",
                262,
                2,
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
                    "16",
                    "17",
                    "18",
                    "19",
                    "20",
                    "21",
                    "22",
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29",
                    "30",
                    "31",
                    "32",
                    "33",
                    "34",
                    "35",
                    "36",
                    "37",
                    "38",
                    "39",
                    "40",
                    "41",
                    "42",
                    "43",
                    "44",
                    "45",
                    "46",
                    "47",
                    "48",
                    "49",
                    "50",
                    "51",
                    "52",
                    "53",
                    "54",
                    "55",
                    "56",
                    "57",
                    "58",
                    "59",
                    "60",
                ],
                None,
                None,
                None,
            ),
            "PurgeStandby": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/PurgeStandby",
                266,
                6,
                ["STOP", "START"],
                None,
                None,
                None,
            ),
            "PowerState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/PowerState",
                283,
                None,
                ["OFF", "ON"],
                None,
                None,
                None,
            ),
            "KeypadLock": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/KeypadLock",
                284,
                None,
                ["OFF", "ON"],
                None,
                None,
                None,
            ),
            "BootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/BootID", 272, None
            ),
            "BootRev": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/BootRev", 274, None
            ),
            "PackCoreID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreID", 276, None
            ),
            "PackCoreRev": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRev", 278, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRel", 280, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackType",
                281,
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
                ],
                None,
                None,
                None,
            ),
            "PackMemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackMemRange",
                282,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
        }
