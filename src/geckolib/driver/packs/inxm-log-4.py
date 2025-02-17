"""GeckoLogStruct - A class to manage the LogStruct for 'InXM v4'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoTempStructAccessor,
    GeckoTimeStructAccessor,
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
        return 4

    @property
    def begin(self) -> int:
        """Get the offset start."""
        return 256

    @property
    def end(self) -> int:
        """Get the offset end."""
        return 479

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def all_device_keys(self) -> list[str]:
        """Get all device keys."""
        return [
            "P1",
            "P2",
            "P3",
            "P4",
            "P5",
            "BL",
            "CP",
            "O3",
            "L120",
            "FAN",
            "Fb",
            "AlwayOn",
            "TvLift",
            "SpkrLift",
            "Sani",
            "Onzen",
            "RhDuty",
            "Vsp1Front",
            "Vsp1Min",
            "VSP3Front",
            "LI",
        ]

    @property
    def user_demand_keys(self) -> list[str]:
        """Get all user demand keys."""
        return [
            "UdP1",
            "UdP2",
            "UdP3",
            "UdP4",
            "UdP5",
            "UdBL",
            "UdTvLift",
            "UdSpkrLift",
            "UdFb",
            "UdL120",
            "UdQuiet",
            "UdLi",
            "UdVSP1",
            "UdVSP3",
        ]

    @property
    def error_keys(self) -> list[str]:
        """Get all error keys."""
        return [
            "AmbiantOHLevel1",
            "AmbiantOHLevel2",
            "ContactorCoilFailErr",
            "FreqDetecErr",
            "Fuse1Err",
            "Fuse2Err",
            "Fuse3Err",
            "KinPumpOff",
            "LearnPhaseErr",
            "NoHeaterCurrentErr",
            "RegOverHeat",
            "RelayStuck",
            "RhCommErr",
            "RhDutyErr",
            "RhRegProbeErr",
            "ScanErr",
            "SupplyErr",
            "TempNotValid",
            "ThermistanceErr",
            "rHId",
        ]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "RhWaterTemp": GeckoTempStructAccessor(
                self.struct, "LogStructure/RealTimeTemp/RhWaterTemp", 261, None
            ),
            "RhTriacTemp": GeckoTempStructAccessor(
                self.struct, "LogStructure/RealTimeTemp/RhTriacTemp", 263, None
            ),
            "Hours": GeckoByteStructAccessor(
                self.struct, "LogStructure/MiscStatus/Hours", 256, None
            ),
            "Menu": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/MiscStatus/Menu",
                353,
                None,
                [
                    "NORMAL",
                    "S1",
                    "S2",
                    "H1",
                    "H2",
                    "H3",
                    "H4",
                    "Fr",
                    "LearnFail",
                    "Learning",
                    "BreakerSelect",
                    "PhaseSelect",
                    "ConfigSelect",
                    "StickBank",
                    "K600Upload",
                    "Powerup",
                ],
                None,
                None,
                None,
            ),
            "HeaterPhaseSign": GeckoByteStructAccessor(
                self.struct, "LogStructure/MiscStatus/HeaterPhaseSign", 300, None
            ),
            "OUT1ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT1ARead", 280, None
            ),
            "OUT1BRead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT1BRead", 282, None
            ),
            "OUT2ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT2ARead", 284, None
            ),
            "OUT2BRead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT2BRead", 286, None
            ),
            "OUT3ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT3ARead", 288, None
            ),
            "OUT4ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT4ARead", 290, None
            ),
            "OUT5ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT5ARead", 292, None
            ),
            "OUT6ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT6ARead", 294, None
            ),
            "OUT7ARead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/OUT7ARead", 296, None
            ),
            "HeaterRead": GeckoWordStructAccessor(
                self.struct, "LogStructure/CurrentLearned/HeaterRead", 298, None
            ),
            "UdP1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP1",
                275,
                14,
                ["OFF", "LO", "HI"],
                2,
                4,
                "ALL",
            ),
            "UdP2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP2",
                275,
                12,
                ["OFF", "LO", "HI"],
                2,
                4,
                "ALL",
            ),
            "UdP3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP3",
                275,
                11,
                ["OFF", "HI"],
                2,
                2,
                "ALL",
            ),
            "UdP4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP4",
                275,
                10,
                ["OFF", "HI"],
                2,
                2,
                "ALL",
            ),
            "UdP5": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP5",
                275,
                9,
                ["OFF", "HI"],
                2,
                2,
                "ALL",
            ),
            "UdBL": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdBL",
                275,
                8,
                ["OFF", "ON"],
                2,
                2,
                "ALL",
            ),
            "UdTvLift": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdTvLift",
                275,
                5,
                ["OFF", "ON"],
                2,
                2,
                "ALL",
            ),
            "UdSpkrLift": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdSpkrLift",
                275,
                4,
                ["OFF", "ON"],
                2,
                2,
                "ALL",
            ),
            "UdFb": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdFb",
                275,
                2,
                ["OFF", "FIX", "NA", "SCAN"],
                2,
                4,
                "ALL",
            ),
            "UdL120": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdL120",
                275,
                1,
                ["OFF", "ON"],
                2,
                2,
                "ALL",
            ),
            "UdQuiet": GeckoBoolStructAccessor(
                self.struct, "LogStructure/UserDemands/UdQuiet", 275, 0, "ALL"
            ),
            "UdLi": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdLi",
                306,
                0,
                ["OFF", "LO", "MED", "HI"],
                None,
                4,
                "ALL",
            ),
            "UdVSP1": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdVSP1", 303, "ALL"
            ),
            "UdVSP3": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdVSP3", 304, "ALL"
            ),
            "P1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P1",
                356,
                0,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P2",
                356,
                2,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P3",
                356,
                4,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P4",
                356,
                6,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P5": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P5",
                355,
                0,
                ["OFF", "HIGH"],
                None,
                2,
                None,
            ),
            "BL": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/BL",
                355,
                1,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "CP": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/CP",
                355,
                2,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "O3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/O3",
                355,
                3,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "L120": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/L120",
                355,
                4,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "FAN": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/FAN",
                355,
                7,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "Fb": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/Fb",
                354,
                0,
                ["OFF", "OFF", "FIX", "SCAN"],
                None,
                4,
                None,
            ),
            "AlwayOn": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/AlwayOn",
                354,
                2,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "TvLift": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/TvLift",
                354,
                3,
                ["DOWN", "UP"],
                None,
                2,
                None,
            ),
            "SpkrLift": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/SpkrLift",
                354,
                4,
                ["DOWN", "UP"],
                None,
                2,
                None,
            ),
            "Sani": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/Sani",
                354,
                5,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "Onzen": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/Onzen",
                354,
                6,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "RhDuty": GeckoByteStructAccessor(
                self.struct, "LogStructure/DeviceStatus/RhDuty", 274, None
            ),
            "Vsp1Front": GeckoByteStructAccessor(
                self.struct, "LogStructure/DeviceStatus/Vsp1Front", 301, None
            ),
            "Vsp1Min": GeckoByteStructAccessor(
                self.struct, "LogStructure/DeviceStatus/Vsp1Min", 305, None
            ),
            "VSP3Front": GeckoByteStructAccessor(
                self.struct, "LogStructure/DeviceStatus/VSP3Front", 302, None
            ),
            "FilterAccess": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/FilterAccess",
                348,
                0,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteFiltAction": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteFiltAction",
                307,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteFiltDur": GeckoTimeStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteFiltDur", 308, "ALL"
            ),
            "RemoteFiltDurPerDay": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteFiltDurPerDay",
                316,
                "ALL",
            ),
            "OnzenAccess": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/OnzenAccess",
                348,
                1,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteOnzenAction": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteOnzenAction",
                310,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteOnzenDur": GeckoTimeStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteOnzenDur", 311, "ALL"
            ),
            "EconomyAccess": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/EconomyAccess",
                348,
                2,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteEconAction": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteEconAction",
                313,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteEconDur": GeckoTimeStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteEconDur", 314, "ALL"
            ),
            "RemoteConfigIndex": GeckoByteStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteConfigIndex", 350, "ALL"
            ),
            "RemoteNbOfPhases": GeckoByteStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteNbOfPhases", 351, "ALL"
            ),
            "RemoteBreakerIndex": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteBreakerIndex",
                352,
                "ALL",
            ),
            "Purge": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/Purge", 269, 7, None
            ),
            "Clean": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/Clean", 269, 5, None
            ),
            "CleanSuspended": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/CleanSuspended", 269, 4, None
            ),
            "CleanSuspendUD": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/CleanSuspendUD", 279, 3, None
            ),
            "FiltOT": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/FiltOT", 279, 0, None
            ),
            "CPOT": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/CPOT", 279, 1, None
            ),
            "SwmActive": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmActive", 267, None, None
            ),
            "SwmRisk": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/SWMStatus/SwmRisk",
                268,
                None,
                ["NO", "LO", "MED", "HI", "EXTREME"],
                None,
                None,
                None,
            ),
            "SwmPurge": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmPurge", 269, 3, None
            ),
            "SwmPurgeSusp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmPurgeSusp", 269, 2, None
            ),
            "RealSetPointG": GeckoTempStructAccessor(
                self.struct, "LogStructure/RegulationStatus/RealSetPointG", 272, None
            ),
            "DisplayedTempG": GeckoTempStructAccessor(
                self.struct, "LogStructure/RegulationStatus/DisplayedTempG", 265, None
            ),
            "TempNotValid": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/TempNotValid", 349, 1, None
            ),
            "PumpRun": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/PumpRun", 269, 1, None
            ),
            "CheckFlo": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/CheckFlo", 269, 0, None
            ),
            "Heating": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/Heating", 270, 7, None
            ),
            "CoolingDown": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/CoolingDown", 270, 6, None
            ),
            "KinPurgeActive": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/KinPurgeActive",
                270,
                5,
                None,
            ),
            "EconActive": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/EconActive", 271, 0, None
            ),
            "ProgEconActive": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/ProgEconActive",
                271,
                2,
                None,
            ),
            "FreqDetecErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/FreqDetecErr", 277, 6, None
            ),
            "ThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/ThermistanceErr", 277, 5, None
            ),
            "ContactorCoilFailErr": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/ErrorMessages/ContactorCoilFailErr",
                277,
                4,
                None,
            ),
            "NoHeaterCurrentErr": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/ErrorMessages/NoHeaterCurrentErr",
                277,
                3,
                None,
            ),
            "LearnPhaseErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/LearnPhaseErr", 277, 2, None
            ),
            "Fuse3Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/Fuse3Err", 277, 1, None
            ),
            "Fuse2Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/Fuse2Err", 277, 0, None
            ),
            "Fuse1Err": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/Fuse1Err", 278, 7, None
            ),
            "SupplyErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SupplyErr", 278, 6, None
            ),
            "ScanErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/ScanErr", 278, 5, None
            ),
            "RegOverHeat": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/RegOverHeat", 278, 4, None
            ),
            "AmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/AmbiantOHLevel2", 278, 3, None
            ),
            "AmbiantOHLevel1": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/AmbiantOHLevel1", 278, 2, None
            ),
            "RelayStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/RelayStuck", 278, 1, None
            ),
            "rHId": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/rHId", 278, 0, None
            ),
            "KinPumpOff": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/KinPumpOff", 279, 4, None
            ),
            "RhCommErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhCommErr", 257, 7, None
            ),
            "RhNotEnoughHeat": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhNotEnoughHeat", 257, 3, None
            ),
            "RhRegSlope": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhRegSlope", 257, 2, None
            ),
            "RhLowFlo": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhLowFlo", 257, 0, None
            ),
            "RhDutyErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhDutyErr", 258, 7, None
            ),
            "RhNoFloRetry": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhNoFloRetry", 258, 6, None
            ),
            "RhNoFloTemp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhNoFloTemp", 258, 5, None
            ),
            "RhNoFloXTries": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhNoFloXTries", 258, 4, None
            ),
            "RhHrHL": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHrHL", 258, 3, None
            ),
            "RhHwHL": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHwHL", 258, 2, None
            ),
            "RhRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhRegProbeErr", 258, 1, None
            ),
            "RhRegOverHeat": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhRegOverHeat", 258, 0, None
            ),
            "RhHrTriacPr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHrTriacPr", 259, 7, None
            ),
            "RhHrTriacOH": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHrTriacOH", 259, 6, None
            ),
            "RhSWTriacOH": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhSWTriacOH", 259, 5, None
            ),
            "RhHwTriacOH": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHwTriacOH", 259, 4, None
            ),
            "RhHrKin": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHrKin", 259, 3, None
            ),
            "RhHrKinNoFlo": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHrKinNoFlo", 259, 2, None
            ),
            "RhSwKinTemp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhSwKinTemp", 259, 1, None
            ),
            "RhHWKin": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHWKin", 259, 0, None
            ),
            "RhHeaterDisabled": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHeaterDisabled", 260, 4, None
            ),
            "RhFloDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhFloDetected", 260, 3, None
            ),
            "RhFloCheck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhFloCheck", 260, 2, None
            ),
            "RhHeaterSuspended": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/InthermStatus/RhHeaterSuspended",
                260,
                1,
                None,
            ),
            "RhFloCheckReady": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhFloCheckReady", 260, 0, None
            ),
            "PackBootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootID", 317, None
            ),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRev", 319, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRel", 320, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackType",
                321,
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
                ],
                None,
                None,
                None,
            ),
            "PackMemRange": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackMemRange",
                322,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackRegion": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackRegion",
                322,
                2,
                ["UL", "CE"],
                None,
                2,
                None,
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackStatusLib", 323, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfigLib", 324, None
            ),
            "PackCoreID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreID", 325, None
            ),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRev", 327, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRel", 328, None
            ),
            "PackConfID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfID", 329, None
            ),
            "PackConfRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfRev", 331, None
            ),
            "PackConfRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfRel", 332, None
            ),
            "PackNumberOfConf": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackNumberOfConf", 333, None
            ),
            "PackLogTrig": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackLogTrig",
                357,
                None,
                ["Restricted", "Full"],
                None,
                2,
                "ALL",
            ),
            "inThermID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/inThermID", 335, None
            ),
            "inThermRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/inThermRev", 337, None
            ),
            "inThermRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/inThermRel", 338, None
            ),
            "inThermCur1KW": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/inThermCur1KW", 339, None
            ),
            "inThermCurFull": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/inThermCurFull", 341, None
            ),
            "K600ID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/K600ID", 343, None
            ),
            "K600Rev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/K600Rev", 345, None
            ),
            "K600Rel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/K600Rel", 346, None
            ),
            "K600Protocol": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/K600Protocol", 347, None
            ),
        }
