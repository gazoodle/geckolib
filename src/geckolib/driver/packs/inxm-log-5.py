#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v5'
"""

from . import (
    GeckoByteStructAccessor,
    GeckoWordStructAccessor,
    GeckoTimeStructAccessor,
    GeckoBoolStructAccessor,
    GeckoEnumStructAccessor,
    GeckoTempStructAccessor,
)


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return 5

    @property
    def begin(self):
        return 256

    @property
    def end(self):
        return 479

    @property
    def all_device_keys(self):
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
    def user_demand_keys(self):
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
            "UdPumpTime",
            "UdQuietTime",
            "UdLightTime",
            "UdL120Time",
            "UdDrain",
        ]

    @property
    def error_keys(self):
        return [
            "AmbiantOHLevel2",
            "RegOverHeat",
            "RhDutyErr",
            "ThermistanceErr",
            "LearnPhaseErr",
            "rHId",
            "Fuse3Err",
            "SupplyErr",
            "Fuse2Err",
            "TempNotValid",
            "RhCommErr",
            "FreqDetecErr",
            "KinPumpOff",
            "ScanErr",
            "ContactorCoilFailErr",
            "RelayStuck",
            "RhRegProbeErr",
            "NoHeaterCurrentErr",
            "AmbiantOHLevel1",
            "Fuse1Err",
        ]

    @property
    def accessors(self):
        return {
            "RhWaterTemp": GeckoTempStructAccessor(
                self.struct, "RhWaterTemp", 261, None
            ),
            "RhTriacTemp": GeckoTempStructAccessor(
                self.struct, "RhTriacTemp", 263, None
            ),
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 256, None),
            "Menu": GeckoEnumStructAccessor(
                self.struct,
                "Menu",
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
                self.struct, "HeaterPhaseSign", 300, None
            ),
            "OUT1ARead": GeckoWordStructAccessor(self.struct, "OUT1ARead", 280, None),
            "OUT1BRead": GeckoWordStructAccessor(self.struct, "OUT1BRead", 282, None),
            "OUT2ARead": GeckoWordStructAccessor(self.struct, "OUT2ARead", 284, None),
            "OUT2BRead": GeckoWordStructAccessor(self.struct, "OUT2BRead", 286, None),
            "OUT3ARead": GeckoWordStructAccessor(self.struct, "OUT3ARead", 288, None),
            "OUT4ARead": GeckoWordStructAccessor(self.struct, "OUT4ARead", 290, None),
            "OUT5ARead": GeckoWordStructAccessor(self.struct, "OUT5ARead", 292, None),
            "OUT6ARead": GeckoWordStructAccessor(self.struct, "OUT6ARead", 294, None),
            "OUT7ARead": GeckoWordStructAccessor(self.struct, "OUT7ARead", 296, None),
            "HeaterRead": GeckoWordStructAccessor(self.struct, "HeaterRead", 298, None),
            "UdP1": GeckoEnumStructAccessor(
                self.struct, "UdP1", 275, 14, ["OFF", "LO", "HI"], 2, 4, "ALL"
            ),
            "UdP2": GeckoEnumStructAccessor(
                self.struct, "UdP2", 275, 12, ["OFF", "LO", "HI"], 2, 4, "ALL"
            ),
            "UdP3": GeckoEnumStructAccessor(
                self.struct, "UdP3", 275, 11, ["OFF", "HI"], 2, 2, "ALL"
            ),
            "UdP4": GeckoEnumStructAccessor(
                self.struct, "UdP4", 275, 10, ["OFF", "HI"], 2, 2, "ALL"
            ),
            "UdP5": GeckoEnumStructAccessor(
                self.struct, "UdP5", 275, 9, ["OFF", "HI"], 2, 2, "ALL"
            ),
            "UdBL": GeckoEnumStructAccessor(
                self.struct, "UdBL", 275, 8, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UdTvLift": GeckoEnumStructAccessor(
                self.struct, "UdTvLift", 275, 5, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UdSpkrLift": GeckoEnumStructAccessor(
                self.struct, "UdSpkrLift", 275, 4, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UdFb": GeckoEnumStructAccessor(
                self.struct, "UdFb", 275, 2, ["OFF", "FIX", "NA", "SCAN"], 2, 4, "ALL"
            ),
            "UdL120": GeckoEnumStructAccessor(
                self.struct, "UdL120", 275, 1, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UdQuiet": GeckoBoolStructAccessor(self.struct, "UdQuiet", 275, 0, "ALL"),
            "UdLi": GeckoEnumStructAccessor(
                self.struct, "UdLi", 306, 0, ["OFF", "LO", "MED", "HI"], None, 4, "ALL"
            ),
            "UdVSP1": GeckoByteStructAccessor(self.struct, "UdVSP1", 303, "ALL"),
            "UdVSP3": GeckoByteStructAccessor(self.struct, "UdVSP3", 304, "ALL"),
            "UdPumpTime": GeckoByteStructAccessor(
                self.struct, "UdPumpTime", 358, "ALL"
            ),
            "UdQuietTime": GeckoByteStructAccessor(
                self.struct, "UdQuietTime", 359, "ALL"
            ),
            "UdLightTime": GeckoByteStructAccessor(
                self.struct, "UdLightTime", 360, "ALL"
            ),
            "UdL120Time": GeckoByteStructAccessor(
                self.struct, "UdL120Time", 361, "ALL"
            ),
            "UdDrain": GeckoBoolStructAccessor(
                self.struct, "UdDrain", 362, None, "ALL"
            ),
            "P1": GeckoEnumStructAccessor(
                self.struct, "P1", 356, 0, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P2": GeckoEnumStructAccessor(
                self.struct, "P2", 356, 2, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P3": GeckoEnumStructAccessor(
                self.struct, "P3", 356, 4, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P4": GeckoEnumStructAccessor(
                self.struct, "P4", 356, 6, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P5": GeckoEnumStructAccessor(
                self.struct, "P5", 355, 0, ["OFF", "HIGH"], None, 2, None
            ),
            "BL": GeckoEnumStructAccessor(
                self.struct, "BL", 355, 1, ["OFF", "ON"], None, 2, None
            ),
            "CP": GeckoEnumStructAccessor(
                self.struct, "CP", 355, 2, ["OFF", "ON"], None, 2, None
            ),
            "O3": GeckoEnumStructAccessor(
                self.struct, "O3", 355, 3, ["OFF", "ON"], None, 2, None
            ),
            "L120": GeckoEnumStructAccessor(
                self.struct, "L120", 355, 4, ["OFF", "ON"], None, 2, None
            ),
            "FAN": GeckoEnumStructAccessor(
                self.struct, "FAN", 355, 7, ["OFF", "ON"], None, 2, None
            ),
            "Fb": GeckoEnumStructAccessor(
                self.struct, "Fb", 354, 0, ["OFF", "OFF", "FIX", "SCAN"], None, 4, None
            ),
            "AlwayOn": GeckoEnumStructAccessor(
                self.struct, "AlwayOn", 354, 2, ["OFF", "ON"], None, 2, None
            ),
            "TvLift": GeckoEnumStructAccessor(
                self.struct, "TvLift", 354, 3, ["DOWN", "UP"], None, 2, None
            ),
            "SpkrLift": GeckoEnumStructAccessor(
                self.struct, "SpkrLift", 354, 4, ["DOWN", "UP"], None, 2, None
            ),
            "Sani": GeckoEnumStructAccessor(
                self.struct, "Sani", 354, 5, ["OFF", "ON"], None, 2, None
            ),
            "Onzen": GeckoEnumStructAccessor(
                self.struct, "Onzen", 354, 6, ["OFF", "ON"], None, 2, None
            ),
            "RhDuty": GeckoByteStructAccessor(self.struct, "RhDuty", 274, None),
            "Vsp1Front": GeckoByteStructAccessor(self.struct, "Vsp1Front", 301, None),
            "Vsp1Min": GeckoByteStructAccessor(self.struct, "Vsp1Min", 305, None),
            "VSP3Front": GeckoByteStructAccessor(self.struct, "VSP3Front", 302, None),
            "FilterAccess": GeckoEnumStructAccessor(
                self.struct,
                "FilterAccess",
                348,
                0,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteFiltAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteFiltAction",
                307,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteFiltDur": GeckoTimeStructAccessor(
                self.struct, "RemoteFiltDur", 308, "ALL"
            ),
            "RemoteFiltDurPerDay": GeckoByteStructAccessor(
                self.struct, "RemoteFiltDurPerDay", 316, "ALL"
            ),
            "OnzenAccess": GeckoEnumStructAccessor(
                self.struct,
                "OnzenAccess",
                348,
                1,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteOnzenAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteOnzenAction",
                310,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteOnzenDur": GeckoTimeStructAccessor(
                self.struct, "RemoteOnzenDur", 311, "ALL"
            ),
            "EconomyAccess": GeckoEnumStructAccessor(
                self.struct,
                "EconomyAccess",
                348,
                2,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteEconAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteEconAction",
                313,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteEconDur": GeckoTimeStructAccessor(
                self.struct, "RemoteEconDur", 314, "ALL"
            ),
            "RemoteConfigIndex": GeckoByteStructAccessor(
                self.struct, "RemoteConfigIndex", 350, "ALL"
            ),
            "RemoteNbOfPhases": GeckoByteStructAccessor(
                self.struct, "RemoteNbOfPhases", 351, "ALL"
            ),
            "RemoteBreakerIndex": GeckoByteStructAccessor(
                self.struct, "RemoteBreakerIndex", 352, "ALL"
            ),
            "Purge": GeckoBoolStructAccessor(self.struct, "Purge", 269, 7, None),
            "Clean": GeckoBoolStructAccessor(self.struct, "Clean", 269, 5, None),
            "CleanSuspended": GeckoBoolStructAccessor(
                self.struct, "CleanSuspended", 269, 4, None
            ),
            "CleanSuspendUD": GeckoBoolStructAccessor(
                self.struct, "CleanSuspendUD", 279, 3, None
            ),
            "FiltOT": GeckoBoolStructAccessor(self.struct, "FiltOT", 279, 0, None),
            "CPOT": GeckoBoolStructAccessor(self.struct, "CPOT", 279, 1, None),
            "Drainning": GeckoBoolStructAccessor(
                self.struct, "Drainning", 279, 7, None
            ),
            "SwmActive": GeckoBoolStructAccessor(
                self.struct, "SwmActive", 267, None, None
            ),
            "SwmRisk": GeckoEnumStructAccessor(
                self.struct,
                "SwmRisk",
                268,
                None,
                ["NO", "LO", "MED", "HI", "EXTREME"],
                None,
                None,
                None,
            ),
            "SwmPurge": GeckoBoolStructAccessor(self.struct, "SwmPurge", 269, 3, None),
            "SwmPurgeSusp": GeckoBoolStructAccessor(
                self.struct, "SwmPurgeSusp", 269, 2, None
            ),
            "RealSetPointG": GeckoTempStructAccessor(
                self.struct, "RealSetPointG", 272, None
            ),
            "DisplayedTempG": GeckoTempStructAccessor(
                self.struct, "DisplayedTempG", 265, None
            ),
            "TempNotValid": GeckoBoolStructAccessor(
                self.struct, "TempNotValid", 349, 1, None
            ),
            "PumpRun": GeckoBoolStructAccessor(self.struct, "PumpRun", 269, 1, None),
            "CheckFlo": GeckoBoolStructAccessor(self.struct, "CheckFlo", 269, 0, None),
            "Heating": GeckoBoolStructAccessor(self.struct, "Heating", 270, 7, None),
            "CoolingDown": GeckoBoolStructAccessor(
                self.struct, "CoolingDown", 270, 6, None
            ),
            "KinPurgeActive": GeckoBoolStructAccessor(
                self.struct, "KinPurgeActive", 270, 5, None
            ),
            "EconActive": GeckoBoolStructAccessor(
                self.struct, "EconActive", 271, 0, None
            ),
            "ProgEconActive": GeckoBoolStructAccessor(
                self.struct, "ProgEconActive", 271, 2, None
            ),
            "FreqDetecErr": GeckoBoolStructAccessor(
                self.struct, "FreqDetecErr", 277, 6, None
            ),
            "ThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "ThermistanceErr", 277, 5, None
            ),
            "ContactorCoilFailErr": GeckoBoolStructAccessor(
                self.struct, "ContactorCoilFailErr", 277, 4, None
            ),
            "NoHeaterCurrentErr": GeckoBoolStructAccessor(
                self.struct, "NoHeaterCurrentErr", 277, 3, None
            ),
            "LearnPhaseErr": GeckoBoolStructAccessor(
                self.struct, "LearnPhaseErr", 277, 2, None
            ),
            "Fuse3Err": GeckoBoolStructAccessor(self.struct, "Fuse3Err", 277, 1, None),
            "Fuse2Err": GeckoBoolStructAccessor(self.struct, "Fuse2Err", 277, 0, None),
            "Fuse1Err": GeckoBoolStructAccessor(self.struct, "Fuse1Err", 278, 7, None),
            "SupplyErr": GeckoBoolStructAccessor(
                self.struct, "SupplyErr", 278, 6, None
            ),
            "ScanErr": GeckoBoolStructAccessor(self.struct, "ScanErr", 278, 5, None),
            "RegOverHeat": GeckoBoolStructAccessor(
                self.struct, "RegOverHeat", 278, 4, None
            ),
            "AmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHLevel2", 278, 3, None
            ),
            "AmbiantOHLevel1": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHLevel1", 278, 2, None
            ),
            "RelayStuck": GeckoBoolStructAccessor(
                self.struct, "RelayStuck", 278, 1, None
            ),
            "rHId": GeckoBoolStructAccessor(self.struct, "rHId", 278, 0, None),
            "KinPumpOff": GeckoBoolStructAccessor(
                self.struct, "KinPumpOff", 279, 4, None
            ),
            "RhCommErr": GeckoBoolStructAccessor(
                self.struct, "RhCommErr", 257, 7, None
            ),
            "RhNotEnoughHeat": GeckoBoolStructAccessor(
                self.struct, "RhNotEnoughHeat", 257, 3, None
            ),
            "RhRegSlope": GeckoBoolStructAccessor(
                self.struct, "RhRegSlope", 257, 2, None
            ),
            "RhLowFlo": GeckoBoolStructAccessor(self.struct, "RhLowFlo", 257, 0, None),
            "RhDutyErr": GeckoBoolStructAccessor(
                self.struct, "RhDutyErr", 258, 7, None
            ),
            "RhNoFloRetry": GeckoBoolStructAccessor(
                self.struct, "RhNoFloRetry", 258, 6, None
            ),
            "RhNoFloTemp": GeckoBoolStructAccessor(
                self.struct, "RhNoFloTemp", 258, 5, None
            ),
            "RhNoFloXTries": GeckoBoolStructAccessor(
                self.struct, "RhNoFloXTries", 258, 4, None
            ),
            "RhHrHL": GeckoBoolStructAccessor(self.struct, "RhHrHL", 258, 3, None),
            "RhHwHL": GeckoBoolStructAccessor(self.struct, "RhHwHL", 258, 2, None),
            "RhRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "RhRegProbeErr", 258, 1, None
            ),
            "RhRegOverHeat": GeckoBoolStructAccessor(
                self.struct, "RhRegOverHeat", 258, 0, None
            ),
            "RhHrTriacPr": GeckoBoolStructAccessor(
                self.struct, "RhHrTriacPr", 259, 7, None
            ),
            "RhHrTriacOH": GeckoBoolStructAccessor(
                self.struct, "RhHrTriacOH", 259, 6, None
            ),
            "RhSWTriacOH": GeckoBoolStructAccessor(
                self.struct, "RhSWTriacOH", 259, 5, None
            ),
            "RhHwTriacOH": GeckoBoolStructAccessor(
                self.struct, "RhHwTriacOH", 259, 4, None
            ),
            "RhHrKin": GeckoBoolStructAccessor(self.struct, "RhHrKin", 259, 3, None),
            "RhHrKinNoFlo": GeckoBoolStructAccessor(
                self.struct, "RhHrKinNoFlo", 259, 2, None
            ),
            "RhSwKinTemp": GeckoBoolStructAccessor(
                self.struct, "RhSwKinTemp", 259, 1, None
            ),
            "RhHWKin": GeckoBoolStructAccessor(self.struct, "RhHWKin", 259, 0, None),
            "RhHeaterDisabled": GeckoBoolStructAccessor(
                self.struct, "RhHeaterDisabled", 260, 4, None
            ),
            "RhFloDetected": GeckoBoolStructAccessor(
                self.struct, "RhFloDetected", 260, 3, None
            ),
            "RhFloCheck": GeckoBoolStructAccessor(
                self.struct, "RhFloCheck", 260, 2, None
            ),
            "RhHeaterSuspended": GeckoBoolStructAccessor(
                self.struct, "RhHeaterSuspended", 260, 1, None
            ),
            "RhFloCheckReady": GeckoBoolStructAccessor(
                self.struct, "RhFloCheckReady", 260, 0, None
            ),
            "PackBootID": GeckoWordStructAccessor(self.struct, "PackBootID", 317, None),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "PackBootRev", 319, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "PackBootRel", 320, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "PackType",
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
                "PackMemRange",
                322,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackRegion": GeckoEnumStructAccessor(
                self.struct, "PackRegion", 322, 2, ["UL", "CE"], None, 2, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "PackStatusLib", 323, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "PackConfigLib", 324, None
            ),
            "PackCoreID": GeckoWordStructAccessor(self.struct, "PackCoreID", 325, None),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "PackCoreRev", 327, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "PackCoreRel", 328, None
            ),
            "PackConfID": GeckoWordStructAccessor(self.struct, "PackConfID", 329, None),
            "PackConfRev": GeckoByteStructAccessor(
                self.struct, "PackConfRev", 331, None
            ),
            "PackConfRel": GeckoByteStructAccessor(
                self.struct, "PackConfRel", 332, None
            ),
            "PackNumberOfConf": GeckoWordStructAccessor(
                self.struct, "PackNumberOfConf", 333, None
            ),
            "PackLogTrig": GeckoEnumStructAccessor(
                self.struct,
                "PackLogTrig",
                357,
                None,
                ["Restricted", "Full"],
                None,
                2,
                "ALL",
            ),
            "inThermID": GeckoWordStructAccessor(self.struct, "inThermID", 335, None),
            "inThermRev": GeckoByteStructAccessor(self.struct, "inThermRev", 337, None),
            "inThermRel": GeckoByteStructAccessor(self.struct, "inThermRel", 338, None),
            "inThermCur1KW": GeckoWordStructAccessor(
                self.struct, "inThermCur1KW", 339, None
            ),
            "inThermCurFull": GeckoWordStructAccessor(
                self.struct, "inThermCurFull", 341, None
            ),
        }
