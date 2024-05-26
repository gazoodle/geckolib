#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v58'
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
        return 58

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
            "Waterfall",
            "LockMode",
            "DealerLockStatus",
            "DealerLockSeed",
            "DealerLockKey",
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
            "UdWaterfall",
            "UdAux",
            "UdPumpTime",
            "UdQuietTime",
            "UdLightTime",
            "UdL120Time",
            "UdWaterFallTime",
            "UdAuxTime",
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
            "FLCErr",
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
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 256, None),
            "StickDetected": GeckoBoolStructAccessor(
                self.struct, "StickDetected", 274, 6, None
            ),
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
                257,
                None,
                ["NOT_SET", "DRAIN", "SOAK", "OFF"],
                None,
                None,
                "ALL",
            ),
            "UdP1": GeckoEnumStructAccessor(
                self.struct, "UdP1", 259, 0, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP2": GeckoEnumStructAccessor(
                self.struct, "UdP2", 259, 2, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP3": GeckoEnumStructAccessor(
                self.struct, "UdP3", 259, 4, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP4": GeckoEnumStructAccessor(
                self.struct, "UdP4", 259, 6, ["OFF", "LO", "HI"], None, 4, "ALL"
            ),
            "UdP5": GeckoEnumStructAccessor(
                self.struct, "UdP5", 258, 0, ["OFF", "HI"], None, 2, "ALL"
            ),
            "UdBL": GeckoEnumStructAccessor(
                self.struct, "UdBL", 258, 1, ["OFF", "ON"], None, 2, "ALL"
            ),
            "UdL120": GeckoEnumStructAccessor(
                self.struct, "UdL120", 308, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "UdLi": GeckoEnumStructAccessor(
                self.struct, "UdLi", 307, None, ["OFF", "HI"], None, None, "ALL"
            ),
            "UdWaterfall": GeckoEnumStructAccessor(
                self.struct, "UdWaterfall", 363, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "UdAux": GeckoEnumStructAccessor(
                self.struct, "UdAux", 370, None, ["OFF", "ON"], None, None, "ALL"
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
            "UdWaterFallTime": GeckoByteStructAccessor(
                self.struct, "UdWaterFallTime", 362, "ALL"
            ),
            "UdAuxTime": GeckoByteStructAccessor(self.struct, "UdAuxTime", 369, "ALL"),
            "P1": GeckoEnumStructAccessor(
                self.struct, "P1", 261, 0, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P2": GeckoEnumStructAccessor(
                self.struct, "P2", 261, 2, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P3": GeckoEnumStructAccessor(
                self.struct, "P3", 261, 4, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P4": GeckoEnumStructAccessor(
                self.struct, "P4", 261, 6, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P5": GeckoEnumStructAccessor(
                self.struct, "P5", 260, 0, ["OFF", "HIGH"], None, 2, None
            ),
            "BL": GeckoEnumStructAccessor(
                self.struct, "BL", 260, 1, ["OFF", "ON"], None, 2, None
            ),
            "CP": GeckoEnumStructAccessor(
                self.struct, "CP", 260, 2, ["OFF", "ON"], None, 2, None
            ),
            "O3": GeckoEnumStructAccessor(
                self.struct, "O3", 260, 3, ["OFF", "ON"], None, 2, None
            ),
            "L120": GeckoEnumStructAccessor(
                self.struct, "L120", 260, 4, ["OFF", "ON"], None, 2, None
            ),
            "MSTR_HEATER": GeckoEnumStructAccessor(
                self.struct, "MSTR_HEATER", 260, 5, ["OFF", "ON"], None, 2, None
            ),
            "SLV_HEATER": GeckoEnumStructAccessor(
                self.struct, "SLV_HEATER", 260, 6, ["OFF", "ON"], None, 2, None
            ),
            "Waterfall": GeckoEnumStructAccessor(
                self.struct, "Waterfall", 260, 7, ["OFF", "ON"], None, 2, None
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
            "DealerLockStatus": GeckoEnumStructAccessor(
                self.struct,
                "DealerLockStatus",
                364,
                None,
                ["UNLOCK", "PARTIAL", "FULL"],
                None,
                None,
                None,
            ),
            "DealerLockSeed": GeckoWordStructAccessor(
                self.struct, "DealerLockSeed", 365, None
            ),
            "DealerLockKey": GeckoWordStructAccessor(
                self.struct, "DealerLockKey", 367, "ALL"
            ),
            "FilterAccess": GeckoEnumStructAccessor(
                self.struct,
                "FilterAccess",
                262,
                0,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteFiltAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteFiltAction",
                263,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteFiltDur": GeckoTimeStructAccessor(
                self.struct, "RemoteFiltDur", 264, "ALL"
            ),
            "RemoteFiltDurPerDay": GeckoByteStructAccessor(
                self.struct, "RemoteFiltDurPerDay", 266, "ALL"
            ),
            "EconomyAccess": GeckoEnumStructAccessor(
                self.struct,
                "EconomyAccess",
                262,
                2,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteEconAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteEconAction",
                267,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteEconDur": GeckoTimeStructAccessor(
                self.struct, "RemoteEconDur", 268, "ALL"
            ),
            "RemoteConfigIndex": GeckoByteStructAccessor(
                self.struct, "RemoteConfigIndex", 270, "ALL"
            ),
            "RemoteNbOfPhases": GeckoByteStructAccessor(
                self.struct, "RemoteNbOfPhases", 271, "ALL"
            ),
            "RemoteBreakerIndex": GeckoByteStructAccessor(
                self.struct, "RemoteBreakerIndex", 272, "ALL"
            ),
            "Clean": GeckoBoolStructAccessor(self.struct, "Clean", 273, 0, None),
            "Purge": GeckoBoolStructAccessor(self.struct, "Purge", 273, 2, None),
            "FiltSuspendByUD": GeckoBoolStructAccessor(
                self.struct, "FiltSuspendByUD", 273, 3, None
            ),
            "FiltSuspendedByOT": GeckoBoolStructAccessor(
                self.struct, "FiltSuspendedByOT", 273, 4, None
            ),
            "FiltSuspendedByErr": GeckoBoolStructAccessor(
                self.struct, "FiltSuspendedByErr", 273, 5, None
            ),
            "CPOT": GeckoBoolStructAccessor(self.struct, "CPOT", 274, 2, None),
            "SwmPurgeSusp": GeckoBoolStructAccessor(
                self.struct, "SwmPurgeSusp", 282, 3, None
            ),
            "SwmPurge": GeckoBoolStructAccessor(self.struct, "SwmPurge", 282, 5, None),
            "SwmActive": GeckoBoolStructAccessor(
                self.struct, "SwmActive", 282, 6, None
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
            "SwmAdc": GeckoWordStructAccessor(self.struct, "SwmAdc", 355, None),
            "OverTemp": GeckoBoolStructAccessor(self.struct, "OverTemp", 274, 1, None),
            "RealSetPointG": GeckoTempStructAccessor(
                self.struct, "RealSetPointG", 275, None
            ),
            "DisplayedTempG": GeckoTempStructAccessor(
                self.struct, "DisplayedTempG", 277, None
            ),
            "Heating": GeckoEnumStructAccessor(
                self.struct,
                "Heating",
                260,
                5,
                ["", "Heating", "Heating", "Heating"],
                None,
                4,
                None,
            ),
            "TempNotValid": GeckoBoolStructAccessor(
                self.struct, "TempNotValid", 279, 2, None
            ),
            "ExtProbeDetected": GeckoBoolStructAccessor(
                self.struct, "ExtProbeDetected", 279, 6, None
            ),
            "CheckFlo": GeckoBoolStructAccessor(self.struct, "CheckFlo", 280, 2, None),
            "ProgEconActive": GeckoBoolStructAccessor(
                self.struct, "ProgEconActive", 281, 1, None
            ),
            "EconActive": GeckoBoolStructAccessor(
                self.struct, "EconActive", 281, 2, "ALL"
            ),
            "SlaveOverTemp": GeckoBoolStructAccessor(
                self.struct, "SlaveOverTemp", 352, 1, None
            ),
            "ThermFuseErr": GeckoBoolStructAccessor(
                self.struct, "ThermFuseErr", 274, 3, None
            ),
            "ThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "ThermistanceErr", 282, 0, None
            ),
            "AmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHLevel2", 282, 1, None
            ),
            "KinPumpOff": GeckoBoolStructAccessor(
                self.struct, "KinPumpOff", 283, 2, None
            ),
            "RegOverHeat": GeckoBoolStructAccessor(
                self.struct, "RegOverHeat", 283, 3, None
            ),
            "P1HStuck": GeckoBoolStructAccessor(self.struct, "P1HStuck", 284, 3, None),
            "P2HStuck": GeckoBoolStructAccessor(self.struct, "P2HStuck", 284, 4, None),
            "HeaterStuck": GeckoBoolStructAccessor(
                self.struct, "HeaterStuck", 284, 5, None
            ),
            "RelayStuck": GeckoBoolStructAccessor(
                self.struct, "RelayStuck", 284, 6, None
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
                self.struct, "RhFloDetected", 280, 0, None
            ),
            "RhHwHL": GeckoBoolStructAccessor(self.struct, "RhHwHL", 283, 0, None),
            "RhRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "RhRegProbeErr", 283, 1, None
            ),
            "RhRegSlope": GeckoBoolStructAccessor(
                self.struct, "RhRegSlope", 283, 4, None
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
            "FLCErr": GeckoBoolStructAccessor(self.struct, "FLCErr", 309, 3, None),
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
            "KeypadType": GeckoEnumStructAccessor(
                self.struct,
                "KeypadType",
                357,
                None,
                [
                    "K200",
                    "K400",
                    "K85",
                    "K8",
                    "K4",
                    "K5",
                    "K600LE",
                    "K100",
                    "K800",
                    "",
                    "",
                    "",
                    "K600HE",
                    "K300",
                    "INVALID_TYPE",
                ],
                None,
                None,
                None,
            ),
            "KeypadID": GeckoWordStructAccessor(self.struct, "KeypadID", 358, None),
            "KeypadRev": GeckoByteStructAccessor(self.struct, "KeypadRev", 360, None),
            "KeypadRel": GeckoByteStructAccessor(self.struct, "KeypadRel", 361, None),
            "PackReset": GeckoEnumStructAccessor(
                self.struct, "PackReset", 376, None, ["---", "RESET"], None, None, "ALL"
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
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
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOutHtr": GeckoEnumStructAccessor(
                self.struct,
                "SOutHtr",
                326,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "SOut1Cur": GeckoByteStructAccessor(self.struct, "SOut1Cur", 327, "ALL"),
            "SOut2Cur": GeckoByteStructAccessor(self.struct, "SOut2Cur", 328, "ALL"),
            "SOut3Cur": GeckoByteStructAccessor(self.struct, "SOut3Cur", 329, "ALL"),
            "SOut4Cur": GeckoByteStructAccessor(self.struct, "SOut4Cur", 330, "ALL"),
            "SOut5Cur": GeckoByteStructAccessor(self.struct, "SOut5Cur", 331, "ALL"),
            "SOutHtrCur": GeckoByteStructAccessor(
                self.struct, "SOutHtrCur", 333, "ALL"
            ),
            "SOut6": GeckoEnumStructAccessor(
                self.struct,
                "SOut6",
                325,
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut7": GeckoEnumStructAccessor(
                self.struct,
                "SOut7",
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut8": GeckoEnumStructAccessor(
                self.struct,
                "SOut8",
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut9": GeckoEnumStructAccessor(
                self.struct,
                "SOut9",
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut10": GeckoEnumStructAccessor(
                self.struct,
                "SOut10",
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut11": GeckoEnumStructAccessor(
                self.struct,
                "SOut11",
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SOut12": GeckoEnumStructAccessor(
                self.struct,
                "SOut12",
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
                    "Fan",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Waterfall",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "SDirect": GeckoEnumStructAccessor(
                self.struct,
                "SDirect",
                332,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "SDirect2": GeckoEnumStructAccessor(
                self.struct,
                "SDirect2",
                333,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "SOut6Cur": GeckoByteStructAccessor(self.struct, "SOut6Cur", 340, "ALL"),
            "SOut7Cur": GeckoByteStructAccessor(self.struct, "SOut7Cur", 341, "ALL"),
            "SOut8Cur": GeckoByteStructAccessor(self.struct, "SOut8Cur", 342, "ALL"),
            "SOut9Cur": GeckoByteStructAccessor(self.struct, "SOut9Cur", 343, "ALL"),
            "SOut10Cur": GeckoByteStructAccessor(self.struct, "SOut10Cur", 344, "ALL"),
            "SOut11Cur": GeckoByteStructAccessor(self.struct, "SOut11Cur", 345, "ALL"),
            "SOut12Cur": GeckoByteStructAccessor(self.struct, "SOut12Cur", 346, "ALL"),
            "SDirectCur": GeckoByteStructAccessor(
                self.struct, "SDirectCur", 347, "ALL"
            ),
            "SDirect2Cur": GeckoByteStructAccessor(
                self.struct, "SDirect2Cur", 348, "ALL"
            ),
            "inFloPressureSwDetected": GeckoBoolStructAccessor(
                self.struct, "inFloPressureSwDetected", 274, 5, None
            ),
            "inFloRatio": GeckoByteStructAccessor(
                self.struct, "inFloRatio", 371, "ALL"
            ),
            "inFloRatioMinimum": GeckoByteStructAccessor(
                self.struct, "inFloRatioMinimum", 372, "ALL"
            ),
            "inFloRatioMaximum": GeckoByteStructAccessor(
                self.struct, "inFloRatioMaximum", 373, "ALL"
            ),
            "inFloErrorType": GeckoEnumStructAccessor(
                self.struct,
                "inFloErrorType",
                374,
                None,
                [
                    "FLOW_OK",
                    "MODE_1_FAIL",
                    "MODE_1_AND_2_FAIL",
                    "MODE_1_AND_HEATING_FAIL",
                    "HEATING_FAIL",
                ],
                None,
                None,
                "ALL",
            ),
            "ForceCheckFlo": GeckoBoolStructAccessor(
                self.struct, "ForceCheckFlo", 375, 0, "ALL"
            ),
            "inFloJustReset": GeckoBoolStructAccessor(
                self.struct, "inFloJustReset", 376, 0, None
            ),
        }
