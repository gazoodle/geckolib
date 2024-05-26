#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v50'
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
        return 50

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
            "MSTR_HEATER",
            "SLV_HEATER",
            "LockMode",
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
            "UdL120",
            "UdLi",
            "UdPumpTime",
            "UdQuietTime",
            "UdLightTime",
            "UdL120Time",
        ]

    @property
    def error_keys(self):
        return [
            "SlaveNoFloErr",
            "AmbiantOHLevel2",
            "RegOverHeat",
            "ThermistanceErr",
            "P1HStuck",
            "SlaveRelayStuck",
            "SlaveP2HStuck",
            "SlaveAmbiantOHLevel2",
            "SlaveRegProbeErr",
            "FiltSuspendedByErr",
            "SlaveKinPumpOff",
            "SlaveThermistanceErr",
            "TempNotValid",
            "SlaveP1HStuck",
            "KinPumpOff",
            "SlaveHtrStuck",
            "SlaveOverTemp",
            "ThermFuseErr",
            "SlaveRegOverHeat",
            "P2HStuck",
            "SlaveHLErr",
            "RelayStuck",
            "RhRegProbeErr",
            "SlaveMissingErr",
            "HeaterStuck",
            "SlaveThermFuseErr",
            "SlaveKinNoFloErr",
            "OverTemp",
        ]

    @property
    def accessors(self):
        return {
            "RhWaterTemp": GeckoTempStructAccessor(
                self.struct, "RhWaterTemp", 317, None
            ),
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 284, None),
            "Menu": GeckoEnumStructAccessor(
                self.struct,
                "Menu",
                319,
                None,
                [
                    "NORMAL",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "InstallerOpt",
                    "DealerOpt",
                    "AccessoryOpt",
                    "ConfigSelect",
                    "",
                    "StickBank",
                ],
                None,
                None,
                None,
            ),
            "QuietState": GeckoEnumStructAccessor(
                self.struct,
                "QuietState",
                256,
                None,
                ["NOT_SET", "DRAIN", "SOAK", "OFF"],
                None,
                None,
                "ALL",
            ),
            "UdP1": GeckoEnumStructAccessor(
                self.struct, "UdP1", 258, 0, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP2": GeckoEnumStructAccessor(
                self.struct, "UdP2", 258, 2, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP3": GeckoEnumStructAccessor(
                self.struct, "UdP3", 258, 4, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP4": GeckoEnumStructAccessor(
                self.struct, "UdP4", 258, 6, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP5": GeckoEnumStructAccessor(
                self.struct, "UdP5", 257, 0, ["OFF", "HI"], None, 2, "ALL"
            ),
            "UdBL": GeckoEnumStructAccessor(
                self.struct, "UdBL", 257, 1, ["OFF", "ON"], None, 2, "ALL"
            ),
            "UdL120": GeckoEnumStructAccessor(
                self.struct, "UdL120", 308, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "UdLi": GeckoEnumStructAccessor(
                self.struct, "UdLi", 307, None, ["OFF", "HI"], None, None, "ALL"
            ),
            "UdPumpTime": GeckoByteStructAccessor(
                self.struct, "UdPumpTime", 303, "ALL"
            ),
            "UdQuietTime": GeckoByteStructAccessor(
                self.struct, "UdQuietTime", 304, "ALL"
            ),
            "UdLightTime": GeckoByteStructAccessor(
                self.struct, "UdLightTime", 305, "ALL"
            ),
            "UdL120Time": GeckoByteStructAccessor(
                self.struct, "UdL120Time", 306, "ALL"
            ),
            "P1": GeckoEnumStructAccessor(
                self.struct, "P1", 260, 0, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P2": GeckoEnumStructAccessor(
                self.struct, "P2", 260, 2, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P3": GeckoEnumStructAccessor(
                self.struct, "P3", 260, 4, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P4": GeckoEnumStructAccessor(
                self.struct, "P4", 260, 6, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P5": GeckoEnumStructAccessor(
                self.struct, "P5", 259, 0, ["OFF", "HIGH"], None, 2, None
            ),
            "BL": GeckoEnumStructAccessor(
                self.struct, "BL", 259, 1, ["OFF", "ON"], None, 2, None
            ),
            "CP": GeckoEnumStructAccessor(
                self.struct, "CP", 259, 2, ["OFF", "ON"], None, 2, None
            ),
            "O3": GeckoEnumStructAccessor(
                self.struct, "O3", 259, 3, ["OFF", "ON"], None, 2, None
            ),
            "L120": GeckoEnumStructAccessor(
                self.struct, "L120", 259, 4, ["OFF", "ON"], None, 2, None
            ),
            "MSTR_HEATER": GeckoEnumStructAccessor(
                self.struct, "MSTR_HEATER", 259, 5, ["OFF", "ON"], None, 2, None
            ),
            "SLV_HEATER": GeckoEnumStructAccessor(
                self.struct, "SLV_HEATER", 259, 6, ["OFF", "ON"], None, 2, None
            ),
            "LockMode": GeckoEnumStructAccessor(
                self.struct,
                "LockMode",
                310,
                None,
                ["UNLOCK", "PARTIAL", "FULL"],
                None,
                None,
                "ALL",
            ),
            "FilterAccess": GeckoEnumStructAccessor(
                self.struct,
                "FilterAccess",
                261,
                0,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteFiltAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteFiltAction",
                262,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteFiltDur": GeckoTimeStructAccessor(
                self.struct, "RemoteFiltDur", 263, "ALL"
            ),
            "RemoteFiltDurPerDay": GeckoByteStructAccessor(
                self.struct, "RemoteFiltDurPerDay", 265, "ALL"
            ),
            "EconomyAccess": GeckoEnumStructAccessor(
                self.struct,
                "EconomyAccess",
                261,
                2,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteEconAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteEconAction",
                266,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteEconDur": GeckoTimeStructAccessor(
                self.struct, "RemoteEconDur", 267, "ALL"
            ),
            "RemoteConfigIndex": GeckoByteStructAccessor(
                self.struct, "RemoteConfigIndex", 269, "ALL"
            ),
            "RemoteNbOfPhases": GeckoByteStructAccessor(
                self.struct, "RemoteNbOfPhases", 270, "ALL"
            ),
            "RemoteBreakerIndex": GeckoByteStructAccessor(
                self.struct, "RemoteBreakerIndex", 271, "ALL"
            ),
            "Clean": GeckoBoolStructAccessor(self.struct, "Clean", 272, 0, None),
            "Purge": GeckoBoolStructAccessor(self.struct, "Purge", 272, 2, None),
            "FiltSuspendByUD": GeckoBoolStructAccessor(
                self.struct, "FiltSuspendByUD", 272, 3, None
            ),
            "FiltSuspendedByOT": GeckoBoolStructAccessor(
                self.struct, "FiltSuspendedByOT", 272, 4, None
            ),
            "FiltSuspendedByErr": GeckoBoolStructAccessor(
                self.struct, "FiltSuspendedByErr", 272, 5, None
            ),
            "CPOT": GeckoBoolStructAccessor(self.struct, "CPOT", 273, 2, None),
            "SwmPurgeSusp": GeckoBoolStructAccessor(
                self.struct, "SwmPurgeSusp", 281, 3, None
            ),
            "SwmPurge": GeckoBoolStructAccessor(self.struct, "SwmPurge", 281, 5, None),
            "SwmActive": GeckoBoolStructAccessor(
                self.struct, "SwmActive", 281, 6, None
            ),
            "SwmRisk": GeckoEnumStructAccessor(
                self.struct,
                "SwmRisk",
                313,
                None,
                ["NO", "LO", "MED", "HI", "EXTREME"],
                None,
                None,
                None,
            ),
            "SlaveSwmPurge": GeckoBoolStructAccessor(
                self.struct, "SlaveSwmPurge", 353, 5, None
            ),
            "SlaveSwmActive": GeckoBoolStructAccessor(
                self.struct, "SlaveSwmActive", 353, 6, None
            ),
            "OverTemp": GeckoBoolStructAccessor(self.struct, "OverTemp", 273, 1, None),
            "RealSetPointG": GeckoTempStructAccessor(
                self.struct, "RealSetPointG", 274, None
            ),
            "DisplayedTempG": GeckoTempStructAccessor(
                self.struct, "DisplayedTempG", 276, None
            ),
            "Heating": GeckoEnumStructAccessor(
                self.struct,
                "Heating",
                259,
                5,
                ["", "Heating", "Heating", "Heating"],
                None,
                4,
                None,
            ),
            "TempNotValid": GeckoBoolStructAccessor(
                self.struct, "TempNotValid", 278, 2, None
            ),
            "ExtProbeDetected": GeckoBoolStructAccessor(
                self.struct, "ExtProbeDetected", 278, 6, None
            ),
            "CheckFlo": GeckoBoolStructAccessor(self.struct, "CheckFlo", 279, 2, None),
            "ProgEconActive": GeckoBoolStructAccessor(
                self.struct, "ProgEconActive", 280, 1, None
            ),
            "EconActive": GeckoBoolStructAccessor(
                self.struct, "EconActive", 280, 2, "ALL"
            ),
            "SlaveOverTemp": GeckoBoolStructAccessor(
                self.struct, "SlaveOverTemp", 352, 1, None
            ),
            "ThermFuseErr": GeckoBoolStructAccessor(
                self.struct, "ThermFuseErr", 273, 3, None
            ),
            "ThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "ThermistanceErr", 281, 0, None
            ),
            "AmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHLevel2", 281, 1, None
            ),
            "KinPumpOff": GeckoBoolStructAccessor(
                self.struct, "KinPumpOff", 282, 2, None
            ),
            "RegOverHeat": GeckoBoolStructAccessor(
                self.struct, "RegOverHeat", 282, 3, None
            ),
            "P1HStuck": GeckoBoolStructAccessor(self.struct, "P1HStuck", 283, 3, None),
            "P2HStuck": GeckoBoolStructAccessor(self.struct, "P2HStuck", 283, 4, None),
            "HeaterStuck": GeckoBoolStructAccessor(
                self.struct, "HeaterStuck", 283, 5, None
            ),
            "RelayStuck": GeckoBoolStructAccessor(
                self.struct, "RelayStuck", 283, 6, None
            ),
            "SlaveP1HStuck": GeckoBoolStructAccessor(
                self.struct, "SlaveP1HStuck", 350, 3, None
            ),
            "SlaveP2HStuck": GeckoBoolStructAccessor(
                self.struct, "SlaveP2HStuck", 350, 4, None
            ),
            "SlaveHtrStuck": GeckoBoolStructAccessor(
                self.struct, "SlaveHtrStuck", 350, 5, None
            ),
            "SlaveRelayStuck": GeckoBoolStructAccessor(
                self.struct, "SlaveRelayStuck", 350, 6, None
            ),
            "SlaveKinPumpOff": GeckoBoolStructAccessor(
                self.struct, "SlaveKinPumpOff", 351, 2, None
            ),
            "SlaveRegOverHeat": GeckoBoolStructAccessor(
                self.struct, "SlaveRegOverHeat", 351, 3, None
            ),
            "SlaveThermFuseErr": GeckoBoolStructAccessor(
                self.struct, "SlaveThermFuseErr", 352, 3, None
            ),
            "SlaveThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "SlaveThermistanceErr", 353, 0, None
            ),
            "SlaveAmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "SlaveAmbiantOHLevel2", 353, 1, None
            ),
            "SlaveMissingErr": GeckoBoolStructAccessor(
                self.struct, "SlaveMissingErr", 354, 0, None
            ),
            "RhFloDetected": GeckoBoolStructAccessor(
                self.struct, "RhFloDetected", 279, 0, None
            ),
            "RhHwHL": GeckoBoolStructAccessor(self.struct, "RhHwHL", 282, 0, None),
            "RhRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "RhRegProbeErr", 282, 1, None
            ),
            "RhRegSlope": GeckoBoolStructAccessor(
                self.struct, "RhRegSlope", 282, 4, None
            ),
            "RhHrKinNoFlo": GeckoBoolStructAccessor(
                self.struct, "RhHrKinNoFlo", 309, 0, None
            ),
            "RhNoFloXTries": GeckoEnumStructAccessor(
                self.struct,
                "RhNoFloXTries",
                309,
                1,
                ["", "RhNoFloXTries", "RhNoFloXTries", "RhNoFloXTries"],
                None,
                4,
                None,
            ),
            "inTCipDelay": GeckoWordStructAccessor(
                self.struct, "inTCipDelay", 311, None
            ),
            "SlaveFloDetected": GeckoBoolStructAccessor(
                self.struct, "SlaveFloDetected", 314, 0, None
            ),
            "SlaveKinNoFloErr": GeckoBoolStructAccessor(
                self.struct, "SlaveKinNoFloErr", 315, 0, None
            ),
            "SlaveNoFloErr": GeckoBoolStructAccessor(
                self.struct, "SlaveNoFloErr", 315, 1, None
            ),
            "SlaveHLErr": GeckoBoolStructAccessor(
                self.struct, "SlaveHLErr", 351, 0, None
            ),
            "SlaveRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "SlaveRegProbeErr", 351, 1, None
            ),
            "SlaveRegSlope": GeckoBoolStructAccessor(
                self.struct, "SlaveRegSlope", 351, 4, None
            ),
            "PackBootID": GeckoWordStructAccessor(self.struct, "PackBootID", 285, None),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "PackBootRev", 287, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "PackBootRel", 288, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "PackType",
                289,
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
                "PackMemRange",
                290,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackRegion": GeckoEnumStructAccessor(
                self.struct, "PackRegion", 290, 2, ["UL", "CE"], None, 2, None
            ),
            "PackCoreID": GeckoWordStructAccessor(self.struct, "PackCoreID", 291, None),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "PackCoreRev", 293, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "PackCoreRel", 294, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "PackConfigLib", 295, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "PackStatusLib", 296, None
            ),
            "PackConfID": GeckoWordStructAccessor(self.struct, "PackConfID", 297, None),
            "PackConfRev": GeckoByteStructAccessor(
                self.struct, "PackConfRev", 299, None
            ),
            "PackConfRel": GeckoByteStructAccessor(
                self.struct, "PackConfRel", 300, None
            ),
            "PackNumberOfConf": GeckoWordStructAccessor(
                self.struct, "PackNumberOfConf", 301, None
            ),
            "PackLogTrig": GeckoEnumStructAccessor(
                self.struct,
                "PackLogTrig",
                316,
                None,
                ["Restricted", "Full"],
                None,
                2,
                "ALL",
            ),
            "SOut1": GeckoEnumStructAccessor(
                self.struct,
                "SOut1",
                320,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut2": GeckoEnumStructAccessor(
                self.struct,
                "SOut2",
                321,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut3": GeckoEnumStructAccessor(
                self.struct,
                "SOut3",
                322,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut4": GeckoEnumStructAccessor(
                self.struct,
                "SOut4",
                323,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut5": GeckoEnumStructAccessor(
                self.struct,
                "SOut5",
                324,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOutHtr": GeckoEnumStructAccessor(
                self.struct,
                "SOutHtr",
                325,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "SOut1Cur": GeckoByteStructAccessor(self.struct, "SOut1Cur", 335, "ALL"),
            "SOut2Cur": GeckoByteStructAccessor(self.struct, "SOut2Cur", 336, "ALL"),
            "SOut3Cur": GeckoByteStructAccessor(self.struct, "SOut3Cur", 337, "ALL"),
            "SOut4Cur": GeckoByteStructAccessor(self.struct, "SOut4Cur", 338, "ALL"),
            "SOut5Cur": GeckoByteStructAccessor(self.struct, "SOut5Cur", 339, "ALL"),
            "SOutHtrCur": GeckoByteStructAccessor(
                self.struct, "SOutHtrCur", 340, "ALL"
            ),
            "SOut6": GeckoEnumStructAccessor(
                self.struct,
                "SOut6",
                326,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut7": GeckoEnumStructAccessor(
                self.struct,
                "SOut7",
                327,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut8": GeckoEnumStructAccessor(
                self.struct,
                "SOut8",
                328,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut9": GeckoEnumStructAccessor(
                self.struct,
                "SOut9",
                329,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut10": GeckoEnumStructAccessor(
                self.struct,
                "SOut10",
                330,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut11": GeckoEnumStructAccessor(
                self.struct,
                "SOut11",
                331,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut12": GeckoEnumStructAccessor(
                self.struct,
                "SOut12",
                332,
                None,
                [
                    "NA",
                    "P1H",
                    "P1L",
                    "P2H",
                    "P2L",
                    "P3H",
                    "P3L",
                    "P4H",
                    "P4L",
                    "P5",
                    "BLO",
                    "CP",
                    "O3",
                    "L120",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                ],
                None,
                None,
                "ALL",
            ),
            "SDirect": GeckoEnumStructAccessor(
                self.struct,
                "SDirect",
                333,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "SDirect2": GeckoEnumStructAccessor(
                self.struct,
                "SDirect2",
                334,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "SOut6Cur": GeckoByteStructAccessor(self.struct, "SOut6Cur", 341, "ALL"),
            "SOut7Cur": GeckoByteStructAccessor(self.struct, "SOut7Cur", 342, "ALL"),
            "SOut8Cur": GeckoByteStructAccessor(self.struct, "SOut8Cur", 343, "ALL"),
            "SOut9Cur": GeckoByteStructAccessor(self.struct, "SOut9Cur", 344, "ALL"),
            "SOut10Cur": GeckoByteStructAccessor(self.struct, "SOut10Cur", 345, "ALL"),
            "SOut11Cur": GeckoByteStructAccessor(self.struct, "SOut11Cur", 346, "ALL"),
            "SOut12Cur": GeckoByteStructAccessor(self.struct, "SOut12Cur", 347, "ALL"),
            "SDirectCur": GeckoByteStructAccessor(
                self.struct, "SDirectCur", 348, "ALL"
            ),
            "SDirect2Cur": GeckoByteStructAccessor(
                self.struct, "SDirect2Cur", 349, "ALL"
            ),
        }
