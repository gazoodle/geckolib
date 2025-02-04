"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v11'."""  # noqa: N999

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
        return 11

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return ["Out1", "Out2", "Out3", "Out4", "Out5", "OutHtr"]

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
                9,
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
            "Out2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out2",
                10,
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
            "Out3": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out3",
                11,
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
            "Out4": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out4",
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
            "Out5": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out5",
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
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/OutHtr",
                14,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out1Cur", 24, "ALL"
            ),
            "Out2Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out2Cur", 25, "ALL"
            ),
            "Out3Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out3Cur", 26, "ALL"
            ),
            "Out4Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out4Cur", 27, "ALL"
            ),
            "Out5Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out5Cur", 28, "ALL"
            ),
            "OutHtRCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/OutHtRCur", 29, "ALL"
            ),
            "DirectCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/DirectCur", 30, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 34, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 35, "ALL"
            ),
            "L120TimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/L120TimeOut", 36, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                20,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
                None,
                None,
                "ALL",
            ),
            "CPAlwaysON": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/CPAlwaysON", 15, 0, "ALL"
            ),
            "OTActSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/OTActSetpointG",
                37,
                "ALL",
            ),
            "OTTriggerG": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/AdvanceFilterConfig/OTTriggerG", 39, "ALL"
            ),
            "CPOTMaxOnTime": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CPOTMaxOnTime",
                40,
                "ALL",
            ),
            "CPOTMaxOffTime": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CPOTMaxOffTime",
                42,
                "ALL",
            ),
            "FiltOTDuration24H": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTDuration24H",
                44,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                46,
                "ALL",
            ),
            "O3Usage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Usage",
                16,
                None,
                ["Filter", "Always"],
                None,
                None,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Pump",
                17,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Type",
                18,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3Config/O3SuspendTime", 47, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/SetpointG",
                1,
                "ALL",
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeaterPump",
                19,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                21,
                None,
                ["F", "C"],
                None,
                None,
                "ALL",
            ),
            "CooldownTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/CooldownTime",
                23,
                "ALL",
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/MinSetpointG",
                50,
                "ALL",
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/MaxSetpointG",
                52,
                "ALL",
            ),
            "EconType": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/EconType",
                54,
                None,
                ["Standard", "Night"],
                None,
                None,
                "ALL",
            ),
            "NoHeatPeriod": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/NoHeatPeriod",
                61,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/NbPhases", 32, "ALL"
            ),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/InputCurrent", 33, "ALL"
            ),
            "InputMenu": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/InputMenu",
                58,
                None,
                ["Standard", "DualPack"],
                None,
                None,
                "ALL",
            ),
            "FiltFreq": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltFreq", 4, "ALL"
            ),
            "FiltStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltStart",
                5,
                "ALL",
            ),
            "FiltDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltDur", 3, "ALL"
            ),
            "EconStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStart",
                7,
                "ALL",
            ),
            "EconDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/EconDur", 8, "ALL"
            ),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgAvailable",
                55,
                None,
                ["NA", "Available"],
                None,
                None,
                "ALL",
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/SoakOnCustomKey",
                56,
                0,
                "ALL",
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OffOnCustomKey",
                56,
                1,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                56,
                2,
                "ALL",
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/MasterSlave",
                57,
                None,
                ["Unconfigured", "Master", "Slave"],
                None,
                None,
                "ALL",
            ),
            "SlaveConfig": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/SlaveConfig",
                59,
                "ALL",
            ),
            "MultiKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/MultiKeyOption",
                60,
                None,
                ["NoBlowerOnI2C", "BlowerOnI2C"],
                None,
                None,
                "ALL",
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                22,
                None,
                ["NA", "AmPm", "24h"],
                None,
                None,
                "ALL",
            ),
            "AmbiantOHTrigADC": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOHTrigADC", 48, "ALL"
            ),
        }
