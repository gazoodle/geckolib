"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v7'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
    GeckoTempStructAccessor,
    GeckoTimeStructAccessor,
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
        return [
            "Out1A",
            "Out1B",
            "Out2A",
            "Out2B",
            "Out3A",
            "OutHtr",
            "Out4A",
            "Out5A",
            "Out6A",
            "Out7A",
            "Direct",
            "OutLi",
            "OutIO2",
            "OutIO4",
        ]

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "ConfigNumber": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/ConfigNumber", 0, "ALL"
            ),
            "Out1A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out1A",
                93,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out1B": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out1B",
                94,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out2A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out2A",
                95,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out2B": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out2B",
                96,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out3A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out3A",
                97,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "OutHtr": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/OutHtr",
                102,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "HTR"],
                None,
                None,
                "ALL",
            ),
            "Out1ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out1ACur", 106, "ALL"
            ),
            "Out1BCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out1BCur", 107, "ALL"
            ),
            "Out2ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out2ACur", 108, "ALL"
            ),
            "Out2BCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out2BCur", 109, "ALL"
            ),
            "Out3ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out3ACur", 110, "ALL"
            ),
            "Out4A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out4A",
                98,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out5A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out5A",
                99,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out6A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out6A",
                100,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Out7A": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out7A",
                101,
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
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Direct",
                116,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Out4ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out4ACur", 111, "ALL"
            ),
            "Out5ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out5ACur", 112, "ALL"
            ),
            "Out6ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out6ACur", 113, "ALL"
            ),
            "Out7ACur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out7ACur", 114, "ALL"
            ),
            "DirectCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/DirectCur", 115, "ALL"
            ),
            "OutLi": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutLi",
                103,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "LI"],
                None,
                None,
                "ALL",
            ),
            "OutIO2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutIO2",
                104,
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
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "OutIO4": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LVOutputConfig/OutIO4",
                105,
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
                    "LI",
                    "FAN",
                    "FbMtr",
                    "FbLi",
                    "FullOn",
                    "TvLift",
                    "SpLift",
                    "SANI",
                    "ONZEN",
                    "VALVE",
                ],
                None,
                None,
                "ALL",
            ),
            "LightInts": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LVOutputConfig/LightInts", 84, "ALL"
            ),
            "PumpTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/PumpTimeOut", 4, "ALL"
            ),
            "LightTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/LightTimeOut", 2, "ALL"
            ),
            "L120Timer": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/TimeOut/L120Timer",
                1,
                2,
                ["Shared", "Own"],
                None,
                2,
                "ALL",
            ),
            "FiberTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/FiberTimeOut", 3, "ALL"
            ),
            "QuietTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/QuietTimeOut", 61, "ALL"
            ),
            "FiltInterface": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltInterface",
                26,
                None,
                ["PurgeOnly", "FiltCP", "FiltP1"],
                None,
                None,
                "ALL",
            ),
            "CpUsage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/CpUsage",
                24,
                None,
                ["STANDARD", "ALWAYS_ON"],
                None,
                None,
                "ALL",
            ),
            "FiltOTOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/FilterConfig/FiltOTOption", 25, 4, "ALL"
            ),
            "CpOtOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/CpOtOption",
                23,
                None,
                ["Disabled", "AlwaysEnabled", "WithSPOver95F"],
                None,
                None,
                "ALL",
            ),
            "FiltSuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/FilterConfig/FiltSuspendBy",
                25,
                6,
                ["AnyUD", "PumpUD"],
                None,
                2,
                "ALL",
            ),
            "PurgeSpeed": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/PurgeSpeed",
                25,
                0,
                ["Lo", "Hi"],
                None,
                2,
                "ALL",
            ),
            "FiltOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTActTemp",
                46,
                "ALL",
            ),
            "FiltOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOTDeadband",
                47,
                "ALL",
            ),
            "FiltCPOTActTemp": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTActTemp",
                49,
                "ALL",
            ),
            "FiltCPOTDeadband": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltCPOTDeadband",
                50,
                "ALL",
            ),
            "CpOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CpOnTimeDuringOT",
                51,
                "ALL",
            ),
            "CpOffTimeDuringOT": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/CpOffTimeDuringOT",
                52,
                "ALL",
            ),
            "FiltOnTimeDuringOT": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltOnTimeDuringOT",
                48,
                "ALL",
            ),
            "FiltSuspendTime": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/FiltSuspendTime",
                53,
                "ALL",
            ),
            "DrainMode": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/AdvanceFilterConfig/DrainMode",
                117,
                None,
                ["NA", "P1", "CP"],
                None,
                None,
                "ALL",
            ),
            "O3Usage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Usage",
                55,
                None,
                ["Filter", "Always"],
                None,
                None,
                "ALL",
            ),
            "O3Pump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Pump",
                54,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "O3Type": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3Type",
                59,
                None,
                ["Standard", "Toggle"],
                None,
                None,
                "ALL",
            ),
            "O3SuspendTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3Config/O3SuspendTime", 58, "ALL"
            ),
            "O3SuspendBy": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/O3Config/O3SuspendBy",
                56,
                None,
                ["AnyUD", "PumpUD"],
                None,
                None,
                "ALL",
            ),
            "O3FilterDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/O3Config/O3FilterDelay", 57, "ALL"
            ),
            "SaniLevel": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Sanitation/SaniLevel", 44, "ALL"
            ),
            "SaniOnTime": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Sanitation/SaniOnTime", 45, "ALL"
            ),
            "SetpointG": GeckoTempStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/SetpointG",
                15,
                "ALL",
            ),
            "TempUnits": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/TempUnits",
                13,
                2,
                ["C", "F"],
                None,
                2,
                "ALL",
            ),
            "HeaterPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeaterPump",
                12,
                None,
                ["CP", "P1"],
                None,
                None,
                "ALL",
            ),
            "HeatRestriction": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/HeatRestriction",
                83,
                3,
                ["No", "FullPowerOnly"],
                None,
                2,
                "ALL",
            ),
            "ExtProbeEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/ExtProbeEnable",
                14,
                4,
                "ALL",
            ),
            "OverSetpointEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/OverSetpointEnable",
                14,
                5,
                "ALL",
            ),
            "EconBelowSetpoint": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/WaterTemperatureControl/EconBelowSetpoint",
                62,
                "ALL",
            ),
            "LineFrequency": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineFrequency",
                83,
                1,
                ["60HZ", "50HZ"],
                None,
                2,
                "ALL",
            ),
            "LineVoltage": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/LineVoltage",
                83,
                2,
                ["240Vac", "230VAC"],
                None,
                2,
                "ALL",
            ),
            "NbPhases": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/NbPhases", 85, None
            ),
            "BrNbSettings": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrNbSettings", 86, None
            ),
            "BrSetIndex": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BrSetIndex", 87, None
            ),
            "BreakerSet1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet1", 88, "ALL"
            ),
            "BreakerSet2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet2", 89, "ALL"
            ),
            "BreakerSet3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet3", 90, "ALL"
            ),
            "BreakerSet4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet4", 91, "ALL"
            ),
            "BreakerSet5": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/BreakerSet5", 92, "ALL"
            ),
            "CE_2x20Allowed": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/InputSupply/CE_2x20Allowed", 60, 6, "ALL"
            ),
            "UDActionOnQuiet": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/UDActionOnQuiet",
                60,
                1,
                ["IgnoreUD", "RestoreAllUD", "NA", "CancelOtherUD"],
                None,
                4,
                "ALL",
            ),
            "QuietActionOnUD": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/QuietActionOnUD",
                60,
                0,
                ["Cancel", "Pause"],
                None,
                2,
                "ALL",
            ),
            "QuietActionOnHeater": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Quiet/QuietActionOnHeater",
                13,
                3,
                ["NoAction", "ForceMaxPower", "KeepOff", ""],
                None,
                4,
                "ALL",
            ),
            "FanActiveOnAmbiantOT": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnAmbiantOT", 13, 5, "ALL"
            ),
            "FanActiveOnPumpRun": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveOnPumpRun", 13, 6, "ALL"
            ),
            "FanForceOFFOption": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOFFOption", 13, 7, "ALL"
            ),
            "FanPump": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/Fan/FanPump",
                14,
                1,
                ["NA", "P1", "CP"],
                None,
                4,
                "ALL",
            ),
            "FanAsCoolingDevice": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/Fan/FanAsCoolingDevice", 14, 3, "ALL"
            ),
            "FanSetAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetAOTTempAdc", 17, "ALL"
            ),
            "FanClrAOTTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrAOTTempAdc", 18, "ALL"
            ),
            "FanActiveDelayAfterPumpRun": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanActiveDelayAfterPumpRun", 19, "ALL"
            ),
            "FanSetForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanSetForceOffTempAdc", 20, "ALL"
            ),
            "FanClrForceOffTempAdc": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanClrForceOffTempAdc", 21, "ALL"
            ),
            "FanForceOffInhibitDelay": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/Fan/FanForceOffInhibitDelay", 22, "ALL"
            ),
            "Pump1AsVSP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/VSP/Pump1AsVSP", 5, 0, "ALL"
            ),
            "Pump3AsVSP": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/VSP/Pump3AsVSP", 5, 2, "ALL"
            ),
            "VSPCheckfloSpeed": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPCheckfloSpeed", 6, "ALL"
            ),
            "VSPFilterSpeed": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPFilterSpeed", 7, "ALL"
            ),
            "VSPSpeedLevel0": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel0", 8, "ALL"
            ),
            "VSPSpeedLevel1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel1", 9, "ALL"
            ),
            "VSPSpeedLevel2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel2", 10, "ALL"
            ),
            "VSPSpeedLevel3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/VSP/VSPSpeedLevel3", 11, "ALL"
            ),
            "FiltFreq": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltFreq",
                27,
                "ALL",
            ),
            "FiltStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/FiltStart",
                28,
                "ALL",
            ),
            "FiltDur": GeckoTimeStructAccessor(
                self.struct, "ConfigStructure/SpaPackInternalOptions/FiltDur", 30, "ALL"
            ),
            "OnzenStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OnzenStart",
                36,
                "ALL",
            ),
            "OnzenDur": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OnzenDur",
                38,
                "ALL",
            ),
            "OnzenFreq": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/OnzenFreq",
                40,
                "ALL",
            ),
            "EconStart": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStart",
                63,
                "ALL",
            ),
            "EconStop": GeckoTimeStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconStop",
                65,
                "ALL",
            ),
            "EconProgAvailable": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconProgAvailable",
                60,
                4,
                ["NA", "Available"],
                None,
                2,
                "ALL",
            ),
            "UDProgEcon": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/UDProgEcon",
                60,
                5,
                "ALL",
            ),
            "EconControlableManually": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/EconControlableManually",
                60,
                3,
                "ALL",
            ),
            "BlowerKeyOption": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/BlowerKeyOption",
                1,
                0,
                ["LastPumpKey", "FreePumpKey"],
                None,
                2,
                "ALL",
            ),
            "QuickOnOffKeyEnable": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/QuickOnOffKeyEnable",
                1,
                1,
                "ALL",
            ),
            "K600ForMay": GeckoBoolStructAccessor(
                self.struct,
                "ConfigStructure/SpaPackInternalOptions/K600ForMay",
                60,
                7,
                "ALL",
            ),
            "K600Msg1": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg1",
                67,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg2",
                68,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg3": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg3",
                69,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg4": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg4",
                70,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg5": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg5",
                71,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg6": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg6",
                72,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg7": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg7",
                73,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg8": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/K600Reminders/K600Msg8",
                74,
                None,
                [
                    "CleanFilter",
                    "PH",
                    "CheckGFCI",
                    "ChangeWater",
                    "CleanCover",
                    "ReplaceFilter",
                ],
                None,
                None,
                "ALL",
            ),
            "K600Msg1NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg1NbWeek", 75, "ALL"
            ),
            "K600Msg2NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg2NbWeek", 76, "ALL"
            ),
            "K600Msg3NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg3NbWeek", 77, "ALL"
            ),
            "K600Msg4NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg4NbWeek", 78, "ALL"
            ),
            "K600Msg5NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg5NbWeek", 79, "ALL"
            ),
            "K600Msg6NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg6NbWeek", 80, "ALL"
            ),
            "K600Msg7NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg7NbWeek", 81, "ALL"
            ),
            "K600Msg8NbWeek": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/K600Reminders/K600Msg8NbWeek", 82, "ALL"
            ),
            "TimeFormat": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/MiscCfg/TimeFormat",
                83,
                0,
                ["AmPm", "24h"],
                None,
                2,
                "ALL",
            ),
            "AmbiantOHEnable": GeckoBoolStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/AmbiantOHEnable", 14, 0, "ALL"
            ),
        }
