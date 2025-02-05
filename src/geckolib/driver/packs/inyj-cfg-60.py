"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v60'."""  # noqa: N999

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


class GeckoConfigStruct:
    """Config Struct Class."""

    def __init__(self, struct_: GeckoAsyncStructure) -> None:
        """Initialize the config struct class."""
        self.struct = struct_

    @property
    def version(self) -> int:
        """Get the config struct class version."""
        return 60

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return ["Out1", "Out2", "Out3", "OutHtr", "Direct", "OutLi"]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/ConfigNumber", 0, "ALL"
            ),
            "Out1": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out1",
                12,
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
                    "HTR",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "Protection",
                    "",
                    "",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out2",
                13,
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
                    "HTR",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "Protection",
                    "",
                    "",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "Out3": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out3",
                14,
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
                    "HTR",
                    "",
                    "",
                    "",
                    "",
                    "FullOn",
                    "",
                    "",
                    "",
                    "",
                    "Protection",
                    "",
                    "",
                    "AUX",
                ],
                None,
                None,
                "ALL",
            ),
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/OutHtr",
                16,
                None,
                ["NA", "P1H", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out1Cur", 36, "ALL"
            ),
            "Out2Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out2Cur", 37, "ALL"
            ),
            "Out3Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out3Cur", 38, "ALL"
            ),
            "OutHtRCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/OutHtRCur", 40, "ALL"
            ),
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Direct",
                15,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "DirectCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/DirectCur", 39, "ALL"
            ),
            "OutLi": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutLi",
                79,
                None,
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                None,
            ),
            "LightInts": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LVOutputConfig/LightInts", 80, None
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 54, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 55, "ALL"
            ),
            "L120TimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/L120TimeOut", 56, "ALL"
            ),
            "L120Timer": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/L120Timer",
                81,
                0,
                ["Shared", "Own"],
                None,
                2,
                "ALL",
            ),
            "AuxTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/AuxTimeOut", 48, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                32,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1", "FiltP1DurOnly"],
                None,
                None,
                "ALL",
            ),
            "CpUsage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/CpUsage",
                27,
                None,
                ["STANDARD", "ALWAYS_ON"],
                None,
                None,
                "ALL",
            ),
            "OtOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/OtOption",
                57,
                None,
                ["Disabled", "AlwaysEnabled", "WithSPOver95F"],
                None,
                None,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/PurgeSpeed",
                81,
                2,
                ["Lo", "Hi"],
                None,
                2,
                "ALL",
            ),
            "OTTriggerG": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/AdvanceFilterConfig/OTTriggerG", 58, "ALL"
            ),
            "CpOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CpOnTimeDuringOT",
                59,
                "ALL",
            ),
            "CpOffTimeDuringOT": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CpOffTimeDuringOT",
                60,
                "ALL",
            ),
            "FiltOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOnTimeDuringOT",
                61,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                62,
                "ALL",
            ),
            "DrainMode": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/DrainMode",
                78,
                None,
                ["NA", "P1", "CP"],
                None,
                None,
                "ALL",
            ),
            "O3Usage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Usage",
                28,
                None,
                ["Filter", "Always"],
                None,
                None,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Pump",
                29,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Type",
                30,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3Config/O3SuspendTime", 63, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/SetpointG",
                1,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                33,
                None,
                ["F", "C"],
                None,
                None,
                "ALL",
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeaterPump",
                31,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "FlowDetector": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/FlowDetector",
                25,
                None,
                ["inFlo", "NotInstalled", "PressureSwitch"],
                None,
                None,
                "ALL",
            ),
            "ProbeLocation": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/ProbeLocation",
                81,
                3,
                ["IntoPiping", "IntoTub"],
                None,
                2,
                "ALL",
            ),
            "CooldownTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/CooldownTime",
                35,
                "ALL",
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/MinSetpointG",
                66,
                "ALL",
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/MaxSetpointG",
                68,
                "ALL",
            ),
            "EconType": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/EconType",
                70,
                None,
                ["Standard", "Night"],
                None,
                None,
                "ALL",
            ),
            "NoHeatPeriod": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/NoHeatPeriod",
                77,
                "ALL",
            ),
            "MaxNumberOfPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/MaxNumberOfPhases", 26, "ALL"
            ),
            "UL_CE": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/UL_CE",
                51,
                None,
                ["UL", "CE"],
                None,
                None,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/NbPhases", 52, "ALL"
            ),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/InputCurrent", 53, "ALL"
            ),
            "InputMenu": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/InputMenu",
                74,
                None,
                ["Standard", "DualPack"],
                None,
                None,
                "ALL",
            ),
            "Out1Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out1Fuse",
                83,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Out2Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out2Fuse",
                84,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Out3Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out3Fuse",
                85,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "Direct1Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Direct1Fuse",
                86,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "OutHtrFuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/OutHtrFuse",
                87,
                None,
                ["F1", "F2", "F3", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "F1Current": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/F1Current", 98, "ALL"
            ),
            "F2Current": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/F2Current", 99, "ALL"
            ),
            "F3Current": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/F3Current", 100, "ALL"
            ),
            "F1Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F1Line",
                104,
                None,
                ["", "", "", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "F2Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F2Line",
                105,
                None,
                ["", "", "", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "F3Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F3Line",
                106,
                None,
                ["", "", "", "", "", "", "Line1", "Line2"],
                None,
                None,
                "ALL",
            ),
            "FiltFreq": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltFreq", 3, "ALL"
            ),
            "FiltStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltStart",
                4,
                "ALL",
            ),
            "FiltDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltDur", 6, "ALL"
            ),
            "FiltDur2": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltDur2",
                23,
                "ALL",
            ),
            "EconStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStart",
                8,
                "ALL",
            ),
            "EconDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/EconDur", 10, "ALL"
            ),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgAvailable",
                71,
                None,
                ["NA", "STANDARD", "OUTSIDE_FILTER"],
                None,
                None,
                "ALL",
            ),
            "UDProgEcon": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/UDProgEcon",
                82,
                0,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                72,
                2,
                "ALL",
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/SoakOnCustomKey",
                72,
                0,
                "ALL",
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OffOnCustomKey",
                72,
                1,
                "ALL",
            ),
            "CleanupOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/CleanupOnCustomKey",
                72,
                3,
                "ALL",
            ),
            "QuickOnOffCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/QuickOnOffCustomKey",
                72,
                5,
                "ALL",
            ),
            "MultiKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/MultiKeyOption",
                76,
                None,
                ["NoBlowerOnI2C", "BlowerOnI2C"],
                None,
                None,
                "ALL",
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/MasterSlave",
                73,
                None,
                ["", "Master", "Slave"],
                None,
                None,
                "ALL",
            ),
            "SlaveConfig": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/SlaveConfig",
                75,
                "ALL",
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                34,
                None,
                ["NA", "AmPm", "24h"],
                None,
                None,
                "ALL",
            ),
            "AmbiantOHTrigADC": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOHTrigADC", 64, "ALL"
            ),
            "Pump1UserAccess": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/Pump1UserAccess",
                81,
                1,
                ["BothSpeeds", "HighSpeedOnly"],
                None,
                2,
                "ALL",
            ),
            "SelfCleanMsg": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/SelfCleanMsg", 81, 4, "ALL"
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/BlowerKeyOption",
                81,
                5,
                ["FreePumpKey", "LastPumpKey"],
                None,
                2,
                "ALL",
            ),
            "HeaterSoftStart": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/HeaterSoftStart", 81, 6, "ALL"
            ),
            "HeaterSoftStop": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/HeaterSoftStop", 81, 7, "ALL"
            ),
            "KeypadTherapySupport": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/KeypadTherapySupport",
                43,
                0,
                "ALL",
            ),
            "CustomKeyEnabled": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/CustomKeyEnabled", 43, 1, "ALL"
            ),
            "ConfigChange": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/ConfigChange",
                43,
                2,
                ["NO_RESTRICTION", "PASSWORD_PROTECTED"],
                None,
                2,
                "ALL",
            ),
            "BreakerChange": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/BreakerChange",
                43,
                3,
                ["NO_RESTRICTION", "PASSWORD_PROTECTED"],
                None,
                2,
                "ALL",
            ),
            "KeypadBacklightColor": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/KeypadBacklightColor",
                43,
                4,
                ["OFF", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"],
                None,
                8,
                "ALL",
            ),
            "KeypadBacklightEdit": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/KeypadBacklightEdit",
                43,
                7,
                ["Disable", "Enable"],
                None,
                2,
                "ALL",
            ),
            "CustomerID": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/CustomerID",
                44,
                None,
                [
                    "Generic",
                    "Hydropool",
                    "EndlessPools",
                    "Wellis",
                    "Alps",
                    "Artesian",
                    "Arctic",
                    "Barefoot",
                    "Beachcomber",
                    "Bellagio",
                    "Leisure_Prod_Ind",
                    "Bullfrog",
                    "Coast",
                    "Dimension_one",
                    "Dynasty",
                    "Four_Wind",
                    "Hotspring",
                    "Jacuzzi",
                    "Jazzi",
                    "LA",
                    "Pro_Float",
                    "MAAX",
                    "Marquis",
                    "PDC",
                    "Premium_Leisure",
                    "Strong",
                    "Sunrans",
                    "Sunrise",
                    "SuperiorSpas",
                    "Spa_Industries",
                    "Viking",
                    "WWO_Whirlcare",
                    "Okeanos",
                    "Clearwater",
                    "Deluxe",
                    "Idol",
                    "Aspen",
                    "ThermoSpas",
                    "Titan_Spas",
                    "IberSpa",
                    "Master_Spas",
                ],
                None,
                None,
                "ALL",
            ),
            "QuickOffKeyEnable": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/QuickOffKeyEnable", 45, 0, "ALL"
            ),
            "ModeKeyAsInvertDisplayKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/ModeKeyAsInvertDisplayKey",
                45,
                1,
                "ALL",
            ),
            "InfoMsgConfig": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/InfoMsgConfig",
                45,
                2,
                ["HIDE_DETAILED_MSG", "SHOW_ALL_MSG", "", ""],
                None,
                4,
                "ALL",
            ),
            "KeypadOptions4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions4", 46, "ALL"
            ),
            "DealerLockSupport": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/DealerLockSupport", 47, 0, "ALL"
            ),
            "SilentMode": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/SilentMode", 47, 3, "ALL"
            ),
            "LockEnabled": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/LockEnabled", 121, "ALL"
            ),
            "Zone1Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone1Led",
                123,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone1Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone1Type",
                123,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone2Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone2Led",
                124,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone2Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone2Type",
                124,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone3Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone3Led",
                125,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone3Type",
                125,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "Zone4Led": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone4Led",
                126,
                0,
                ["RGB", "WHITE"],
                None,
                2,
                None,
            ),
            "Zone4Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/Zone4Type",
                126,
                1,
                ["NORMAL", "STATUS"],
                None,
                2,
                None,
            ),
            "NumberOfZones": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/inMixConfig/NumberOfZones",
                127,
                0,
                ["", "1", "2", "3", "4"],
                None,
                8,
                None,
            ),
            "MappingEnable": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MappingEnable", 127, 7, None
            ),
            "MapZone1ToOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone1ToOut1", 123, 4, None
            ),
            "MapZone1ToOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone1ToOut2", 123, 5, None
            ),
            "MapZone1ToOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone1ToOut3", 123, 6, None
            ),
            "MapZone1ToOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone1ToOut4", 123, 7, None
            ),
            "MapZone2ToOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone2ToOut1", 124, 4, None
            ),
            "MapZone2ToOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone2ToOut2", 124, 5, None
            ),
            "MapZone2ToOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone2ToOut3", 124, 6, None
            ),
            "MapZone2ToOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone2ToOut4", 124, 7, None
            ),
            "MapZone3ToOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone3ToOut1", 125, 4, None
            ),
            "MapZone3ToOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone3ToOut2", 125, 5, None
            ),
            "MapZone3ToOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone3ToOut3", 125, 6, None
            ),
            "MapZone3ToOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone3ToOut4", 125, 7, None
            ),
            "MapZone4ToOut1": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone4ToOut1", 126, 4, None
            ),
            "MapZone4ToOut2": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone4ToOut2", 126, 5, None
            ),
            "MapZone4ToOut3": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone4ToOut3", 126, 6, None
            ),
            "MapZone4ToOut4": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/inMixConfig/MapZone4ToOut4", 126, 7, None
            ),
        }
