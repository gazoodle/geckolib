"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v53'."""  # noqa: N999

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
        return 53

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
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
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
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                32,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
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
                ["NA", "Available"],
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
            "KeypadOptions1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions1", 43, "ALL"
            ),
            "KeypadOptions2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions2", 44, "ALL"
            ),
            "KeypadOptions3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions3", 45, "ALL"
            ),
            "KeypadOptions4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions4", 46, "ALL"
            ),
        }
