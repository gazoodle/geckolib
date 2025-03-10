"""GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v60'."""  # noqa: N999

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
        return 60

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
        return [
            "SOut1",
            "SOut2",
            "SOut3",
            "SOut4",
            "SOut5",
            "SOutHtr",
            "SOut6",
            "SOut7",
            "SOut8",
            "SOut9",
            "SOut10",
            "SOut11",
            "SOut12",
            "SDirect",
            "SDirect2",
        ]

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
    def user_demand_keys(self) -> list[str]:
        """Get all user demand keys."""
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
    def error_keys(self) -> list[str]:
        """Get all error keys."""
        return [
            "AmbiantOHLevel2",
            "FLCErr",
            "FiltSuspendedByErr",
            "HeaterStuck",
            "KinPumpOff",
            "OverTemp",
            "P1HStuck",
            "P2HStuck",
            "RegOverHeat",
            "RelayStuck",
            "RhRegProbeErr",
            "SlaveAmbiantOHLevel2",
            "SlaveHLErr",
            "SlaveHtrStuck",
            "SlaveKinNoFloErr",
            "SlaveKinPumpOff",
            "SlaveMissingErr",
            "SlaveNoFloErr",
            "SlaveOverTemp",
            "SlaveP1HStuck",
            "SlaveP2HStuck",
            "SlaveRegOverHeat",
            "SlaveRegProbeErr",
            "SlaveRelayStuck",
            "SlaveThermFuseErr",
            "SlaveThermistanceErr",
            "TempNotValid",
            "ThermFuseErr",
            "ThermistanceErr",
        ]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "RhWaterTemp": GeckoTempStructAccessor(
                self.struct, "LogStructure/RealTimeTemp/RhWaterTemp", 317, None
            ),
            "Hours": GeckoByteStructAccessor(
                self.struct, "LogStructure/MiscStatus/Hours", 256, None
            ),
            "StickDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/MiscStatus/StickDetected", 274, 6, None
            ),
            "Menu": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/MiscStatus/Menu",
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
                "LogStructure/UserDemands/QuietState",
                257,
                None,
                ["NOT_SET", "DRAIN", "SOAK", "OFF"],
                None,
                None,
                "ALL",
            ),
            "UdP1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP1",
                259,
                0,
                ["OFF", "LO", "HI"],
                None,
                4,
                "ALL",
            ),
            "UdP2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP2",
                259,
                2,
                ["OFF", "LO", "HI"],
                None,
                4,
                "ALL",
            ),
            "UdP3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP3",
                259,
                4,
                ["OFF", "LO", "HI"],
                None,
                4,
                "ALL",
            ),
            "UdP4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP4",
                259,
                6,
                ["OFF", "LO", "HI"],
                None,
                4,
                "ALL",
            ),
            "UdP5": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdP5",
                258,
                0,
                ["OFF", "HI"],
                None,
                2,
                "ALL",
            ),
            "UdBL": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdBL",
                258,
                1,
                ["OFF", "ON"],
                None,
                2,
                "ALL",
            ),
            "UdL120": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdL120",
                308,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "UdLi": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdLi",
                307,
                None,
                ["OFF", "HI"],
                None,
                None,
                "ALL",
            ),
            "UdWaterfall": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdWaterfall",
                363,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "UdAux": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/UserDemands/UdAux",
                370,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "UdPumpTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdPumpTime", 303, "ALL"
            ),
            "UdQuietTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdQuietTime", 304, "ALL"
            ),
            "UdLightTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdLightTime", 305, "ALL"
            ),
            "UdL120Time": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdL120Time", 306, "ALL"
            ),
            "UdWaterFallTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdWaterFallTime", 362, "ALL"
            ),
            "UdAuxTime": GeckoByteStructAccessor(
                self.struct, "LogStructure/UserDemands/UdAuxTime", 369, "ALL"
            ),
            "P1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P1",
                261,
                0,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P2",
                261,
                2,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P3",
                261,
                4,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P4": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P4",
                261,
                6,
                ["OFF", "HIGH", "LOW"],
                None,
                4,
                None,
            ),
            "P5": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/P5",
                260,
                0,
                ["OFF", "HIGH"],
                None,
                2,
                None,
            ),
            "BL": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/BL",
                260,
                1,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "CP": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/CP",
                260,
                2,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "O3": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/O3",
                260,
                3,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "L120": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/L120",
                260,
                4,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "MSTR_HEATER": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/MSTR_HEATER",
                260,
                5,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "SLV_HEATER": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/SLV_HEATER",
                260,
                6,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "Waterfall": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/Waterfall",
                260,
                7,
                ["OFF", "ON"],
                None,
                2,
                None,
            ),
            "LockMode": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/LockMode",
                310,
                None,
                ["UNLOCK", "PARTIAL", "FULL"],
                None,
                None,
                "ALL",
            ),
            "DealerLockStatus": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/DeviceStatus/DealerLockStatus",
                364,
                None,
                ["UNLOCK", "PARTIAL", "FULL"],
                None,
                None,
                None,
            ),
            "DealerLockSeed": GeckoWordStructAccessor(
                self.struct, "LogStructure/DeviceStatus/DealerLockSeed", 365, None
            ),
            "DealerLockKey": GeckoWordStructAccessor(
                self.struct, "LogStructure/DeviceStatus/DealerLockKey", 367, "ALL"
            ),
            "FilterAccess": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/FilterAccess",
                262,
                0,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteFiltAction": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteFiltAction",
                263,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteFiltDur": GeckoTimeStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteFiltDur", 264, "ALL"
            ),
            "RemoteFiltDurPerDay": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteFiltDurPerDay",
                266,
                "ALL",
            ),
            "EconomyAccess": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/EconomyAccess",
                262,
                2,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteEconAction": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteEconAction",
                267,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteEconDur": GeckoTimeStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteEconDur", 268, "ALL"
            ),
            "RemoteConfigIndex": GeckoByteStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteConfigIndex", 270, "ALL"
            ),
            "RemoteNbOfPhases": GeckoByteStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteNbOfPhases", 271, "ALL"
            ),
            "RemoteBreakerIndex": GeckoByteStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteBreakerIndex",
                272,
                "ALL",
            ),
            "OnzenAccess": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/OnzenAccess",
                262,
                1,
                ["INTERNAL", "REMOTE"],
                None,
                2,
                "ALL",
            ),
            "RemoteOnzenAction": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RemoteCommands/RemoteOnzenAction",
                380,
                None,
                ["IDLE", "STOP", "START", "NEW", "ACTIVE"],
                None,
                None,
                "ALL",
            ),
            "RemoteOnzenDur": GeckoTimeStructAccessor(
                self.struct, "LogStructure/RemoteCommands/RemoteOnzenDur", 381, "ALL"
            ),
            "Clean": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/Clean", 273, 0, None
            ),
            "Purge": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/Purge", 273, 2, None
            ),
            "FiltSuspendByUD": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/FiltSuspendByUD", 273, 3, None
            ),
            "FiltSuspendedByOT": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/FiltSuspendedByOT", 273, 4, None
            ),
            "FiltSuspendedByErr": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/FilterStatus/FiltSuspendedByErr",
                273,
                5,
                None,
            ),
            "CPOT": GeckoBoolStructAccessor(
                self.struct, "LogStructure/FilterStatus/CPOT", 274, 2, None
            ),
            "SwmPurgeSusp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmPurgeSusp", 282, 3, None
            ),
            "SwmPurge": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmPurge", 282, 5, None
            ),
            "SwmActive": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmActive", 282, 6, None
            ),
            "SwmRisk": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/SWMStatus/SwmRisk",
                313,
                None,
                ["NO", "LO", "MED", "HI", "EXTREME"],
                None,
                None,
                None,
            ),
            "SlaveSwmPurge": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SlaveSwmPurge", 353, 5, None
            ),
            "SlaveSwmActive": GeckoBoolStructAccessor(
                self.struct, "LogStructure/SWMStatus/SlaveSwmActive", 353, 6, None
            ),
            "SwmAdc": GeckoWordStructAccessor(
                self.struct, "LogStructure/SWMStatus/SwmAdc", 355, None
            ),
            "OverTemp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/OverTemp", 274, 1, None
            ),
            "RealSetPointG": GeckoTempStructAccessor(
                self.struct, "LogStructure/RegulationStatus/RealSetPointG", 275, None
            ),
            "DisplayedTempG": GeckoTempStructAccessor(
                self.struct, "LogStructure/RegulationStatus/DisplayedTempG", 277, None
            ),
            "Heating": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/Heating",
                260,
                5,
                ["", "Heating", "Heating", "Heating"],
                None,
                4,
                None,
            ),
            "TempNotValid": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/TempNotValid", 279, 2, None
            ),
            "ExtProbeDetected": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/ExtProbeDetected",
                279,
                6,
                None,
            ),
            "CheckFlo": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/CheckFlo", 280, 2, None
            ),
            "ProgEconActive": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/ProgEconActive",
                281,
                1,
                None,
            ),
            "EconActive": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/EconActive", 281, 2, "ALL"
            ),
            "SlaveOverTemp": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/SlaveOverTemp", 352, 1, None
            ),
            "SideHeatingDegG": GeckoByteStructAccessor(
                self.struct, "LogStructure/RegulationStatus/SideHeatingDegG", 377, None
            ),
            "HPCDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/RegulationStatus/HPCDetected", 378, 0, None
            ),
            "HPCResHeaterRequest": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/HPCResHeaterRequest",
                378,
                4,
                None,
            ),
            "HPCHeatRequest": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/HPCHeatRequest",
                378,
                5,
                None,
            ),
            "HPCChillRequest": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/HPCChillRequest",
                378,
                6,
                None,
            ),
            "HPCAutoMode": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/HPCAutoMode",
                378,
                7,
                ["HEAT", "CHILL"],
                None,
                2,
                "ALL",
            ),
            "HPCState": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/HPCState",
                379,
                None,
                [
                    "IDLE",
                    "HEAT_ON",
                    "CHILL_ON",
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
                    "INVALID_REQUEST",
                    "COIL_SENSOR_ERR",
                    "AMBIENT_TEMP_ERR",
                    "EE1_EE2_ERR",
                    "PRESSURE_ERR",
                    "OTHER_ERR",
                ],
                None,
                None,
                None,
            ),
            "HtrSuspendByPwrMng": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/HtrSuspendByPwrMng",
                284,
                0,
                None,
            ),
            "Htr2SuspendByPwrMng": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/Htr2SuspendByPwrMng",
                284,
                1,
                None,
            ),
            "SlaveHtrSuspendByPwrMng": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/SlaveHtrSuspendByPwrMng",
                350,
                0,
                None,
            ),
            "SlaveHtr2SuspendByPwrMng": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/RegulationStatus/SlaveHtr2SuspendByPwrMng",
                350,
                1,
                None,
            ),
            "ThermFuseErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/ThermFuseErr", 274, 3, None
            ),
            "ThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/ThermistanceErr", 282, 0, None
            ),
            "AmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/AmbiantOHLevel2", 282, 1, None
            ),
            "KinPumpOff": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/KinPumpOff", 283, 2, None
            ),
            "RegOverHeat": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/RegOverHeat", 283, 3, None
            ),
            "P1HStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/P1HStuck", 284, 3, None
            ),
            "P2HStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/P2HStuck", 284, 4, None
            ),
            "HeaterStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/HeaterStuck", 284, 5, None
            ),
            "RelayStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/RelayStuck", 284, 6, None
            ),
            "SlaveP1HStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveP1HStuck", 350, 3, None
            ),
            "SlaveP2HStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveP2HStuck", 350, 4, None
            ),
            "SlaveHtrStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveHtrStuck", 350, 5, None
            ),
            "SlaveRelayStuck": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveRelayStuck", 350, 6, None
            ),
            "SlaveKinPumpOff": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveKinPumpOff", 351, 2, None
            ),
            "SlaveRegOverHeat": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveRegOverHeat", 351, 3, None
            ),
            "SlaveThermFuseErr": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/ErrorMessages/SlaveThermFuseErr",
                352,
                3,
                None,
            ),
            "SlaveThermistanceErr": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/ErrorMessages/SlaveThermistanceErr",
                353,
                0,
                None,
            ),
            "SlaveAmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/ErrorMessages/SlaveAmbiantOHLevel2",
                353,
                1,
                None,
            ),
            "SlaveMissingErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/ErrorMessages/SlaveMissingErr", 354, 0, None
            ),
            "RhFloDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhFloDetected", 280, 0, None
            ),
            "RhHwHL": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHwHL", 283, 0, None
            ),
            "RhRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhRegProbeErr", 283, 1, None
            ),
            "RhRegSlope": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhRegSlope", 283, 4, None
            ),
            "RhHrKinNoFlo": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/RhHrKinNoFlo", 309, 0, None
            ),
            "RhNoFloXTries": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/InthermStatus/RhNoFloXTries",
                309,
                1,
                ["", "RhNoFloXTries", "RhNoFloXTries", "RhNoFloXTries"],
                None,
                4,
                None,
            ),
            "FLCErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/FLCErr", 309, 3, None
            ),
            "inTCipDelay": GeckoWordStructAccessor(
                self.struct, "LogStructure/InthermStatus/inTCipDelay", 311, None
            ),
            "SlaveFloDetected": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/SlaveFloDetected", 314, 0, None
            ),
            "SlaveKinNoFloErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/SlaveKinNoFloErr", 315, 0, None
            ),
            "SlaveNoFloErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/SlaveNoFloErr", 315, 1, None
            ),
            "SlaveHLErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/SlaveHLErr", 351, 0, None
            ),
            "SlaveRegProbeErr": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/SlaveRegProbeErr", 351, 1, None
            ),
            "SlaveRegSlope": GeckoBoolStructAccessor(
                self.struct, "LogStructure/InthermStatus/SlaveRegSlope", 351, 4, None
            ),
            "PackBootID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootID", 285, None
            ),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRev", 287, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackBootRel", 288, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackType",
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
                "LogStructure/PackInfo/PackMemRange",
                290,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackRegion": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackRegion",
                290,
                2,
                ["UL", "CE"],
                None,
                2,
                None,
            ),
            "PackCoreID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreID", 291, None
            ),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRev", 293, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackCoreRel", 294, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfigLib", 295, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackStatusLib", 296, None
            ),
            "PackConfID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfID", 297, None
            ),
            "PackConfRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfRev", 299, None
            ),
            "PackConfRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/PackConfRel", 300, None
            ),
            "PackNumberOfConf": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/PackNumberOfConf", 301, None
            ),
            "PackLogTrig": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackLogTrig",
                316,
                None,
                ["Restricted", "Full"],
                None,
                2,
                "ALL",
            ),
            "KeypadType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/KeypadType",
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
            "KeypadID": GeckoWordStructAccessor(
                self.struct, "LogStructure/PackInfo/KeypadID", 358, None
            ),
            "KeypadRev": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/KeypadRev", 360, None
            ),
            "KeypadRel": GeckoByteStructAccessor(
                self.struct, "LogStructure/PackInfo/KeypadRel", 361, None
            ),
            "PackReset": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/PackInfo/PackReset",
                376,
                None,
                ["---", "RESET"],
                None,
                None,
                "ALL",
            ),
            "SOut1": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/SlaveHCOutputConfig/SOut1",
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
                "LogStructure/SlaveHCOutputConfig/SOut2",
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
                "LogStructure/SlaveHCOutputConfig/SOut3",
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
                "LogStructure/SlaveHCOutputConfig/SOut4",
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
                "LogStructure/SlaveHCOutputConfig/SOut5",
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
                "LogStructure/SlaveHCOutputConfig/SOutHtr",
                326,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "SOut1Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveHCOutputConfig/SOut1Cur", 327, "ALL"
            ),
            "SOut2Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveHCOutputConfig/SOut2Cur", 328, "ALL"
            ),
            "SOut3Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveHCOutputConfig/SOut3Cur", 329, "ALL"
            ),
            "SOut4Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveHCOutputConfig/SOut4Cur", 330, "ALL"
            ),
            "SOut5Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveHCOutputConfig/SOut5Cur", 331, "ALL"
            ),
            "SOutHtrCur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveHCOutputConfig/SOutHtrCur", 333, "ALL"
            ),
            "SOut6": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/SlaveLCOutputConfig/SOut6",
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
                "LogStructure/SlaveLCOutputConfig/SOut7",
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
                "LogStructure/SlaveLCOutputConfig/SOut8",
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
                "LogStructure/SlaveLCOutputConfig/SOut9",
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
                "LogStructure/SlaveLCOutputConfig/SOut10",
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
                "LogStructure/SlaveLCOutputConfig/SOut11",
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
                "LogStructure/SlaveLCOutputConfig/SOut12",
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
                "LogStructure/SlaveLCOutputConfig/SDirect",
                332,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "SDirect2": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/SlaveLCOutputConfig/SDirect2",
                333,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "SOut6Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut6Cur", 340, "ALL"
            ),
            "SOut7Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut7Cur", 341, "ALL"
            ),
            "SOut8Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut8Cur", 342, "ALL"
            ),
            "SOut9Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut9Cur", 343, "ALL"
            ),
            "SOut10Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut10Cur", 344, "ALL"
            ),
            "SOut11Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut11Cur", 345, "ALL"
            ),
            "SOut12Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SOut12Cur", 346, "ALL"
            ),
            "SDirectCur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SDirectCur", 347, "ALL"
            ),
            "SDirect2Cur": GeckoByteStructAccessor(
                self.struct, "LogStructure/SlaveLCOutputConfig/SDirect2Cur", 348, "ALL"
            ),
            "inFloPressureSwDetected": GeckoBoolStructAccessor(
                self.struct,
                "LogStructure/inFloStat/inFloPressureSwDetected",
                274,
                5,
                None,
            ),
            "inFloRatio": GeckoByteStructAccessor(
                self.struct, "LogStructure/inFloStat/inFloRatio", 371, "ALL"
            ),
            "inFloRatioMinimum": GeckoByteStructAccessor(
                self.struct, "LogStructure/inFloStat/inFloRatioMinimum", 372, "ALL"
            ),
            "inFloRatioMaximum": GeckoByteStructAccessor(
                self.struct, "LogStructure/inFloStat/inFloRatioMaximum", 373, "ALL"
            ),
            "inFloErrorType": GeckoEnumStructAccessor(
                self.struct,
                "LogStructure/inFloStat/inFloErrorType",
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
                self.struct, "LogStructure/inFloStat/ForceCheckFlo", 375, 0, "ALL"
            ),
            "inFloJustReset": GeckoBoolStructAccessor(
                self.struct, "LogStructure/inFloStat/inFloJustReset", 376, 0, None
            ),
        }
