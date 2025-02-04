"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v7'."""  # noqa: N999

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
        return 7

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/ConfigNumber", 0, "ALL"
            ),
            "OutHtRCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/OutHtRCur", 27, "ALL"
            ),
            "DirectCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/DirectCur", 26, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 31, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 32, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                17,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
                None,
                None,
                "ALL",
            ),
            "OTActSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/OTActSetpointG",
                33,
                "ALL",
            ),
            "OTTriggerG": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/AdvanceFilterConfig/OTTriggerG", 35, "ALL"
            ),
            "CPOTMaxOnTime": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CPOTMaxOnTime",
                36,
                "ALL",
            ),
            "CPOTMaxOffTime": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CPOTMaxOffTime",
                38,
                "ALL",
            ),
            "FiltOTDuration24H": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTDuration24H",
                40,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                42,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Pump",
                14,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Type",
                15,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3Config/O3SuspendTime", 43, "ALL"
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
                16,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                18,
                None,
                ["F", "C"],
                None,
                None,
                "ALL",
            ),
            "MinSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/MinSetpointG",
                46,
                "ALL",
            ),
            "MaxSetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/MaxSetpointG",
                48,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/NbPhases", 29, "ALL"
            ),
            "InputCurrent": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/InputCurrent", 30, "ALL"
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
                50,
                None,
                ["NA", "Available"],
                None,
                None,
                "ALL",
            ),
            "SoakOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/SoakOnCustomKey",
                51,
                0,
                "ALL",
            ),
            "OffOnCustomKey": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OffOnCustomKey",
                51,
                1,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                51,
                2,
                "ALL",
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                19,
                None,
                ["NA", "AmPm", "24h"],
                None,
                None,
                "ALL",
            ),
            "AmbiantOHTrigADC": GeckoWordStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOHTrigADC", 44, "ALL"
            ),
        }
