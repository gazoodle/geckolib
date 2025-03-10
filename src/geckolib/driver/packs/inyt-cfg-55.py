"""GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v55'."""  # noqa: N999

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
        return 55

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return [
            "Out1",
            "Out2",
            "Out3",
            "Out4",
            "Out5",
            "OutHtr",
            "Out6",
            "Out7",
            "Out8",
            "Out9",
            "Out10",
            "Out11",
            "Out12",
            "Direct",
            "Direct2",
            "OutLi",
        ]

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
            "Out4": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out4",
                15,
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
            "Out5": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/HCOutputConfig/Out5",
                16,
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
                26,
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
            "Out4Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out4Cur", 39, "ALL"
            ),
            "Out5Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/Out5Cur", 40, "ALL"
            ),
            "OutHtRCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/HCOutputConfig/OutHtRCur", 50, "ALL"
            ),
            "Out6": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out6",
                17,
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
            "Out7": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out7",
                18,
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
            "Out8": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out8",
                19,
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
            "Out9": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out9",
                20,
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
            "Out10": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out10",
                21,
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
            "Out11": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out11",
                22,
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
            "Out12": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Out12",
                23,
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
            "Direct": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Direct",
                24,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Direct2": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/LCOutputConfig/Direct2",
                25,
                None,
                ["NA", "", "", "", "", "", "", "", "", "", "", "CP"],
                None,
                None,
                "ALL",
            ),
            "Out6Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out6Cur", 41, "ALL"
            ),
            "Out7Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out7Cur", 42, "ALL"
            ),
            "Out8Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out8Cur", 43, "ALL"
            ),
            "Out9Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out9Cur", 44, "ALL"
            ),
            "Out10Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out10Cur", 45, "ALL"
            ),
            "Out11Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out11Cur", 46, "ALL"
            ),
            "Out12Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Out12Cur", 47, "ALL"
            ),
            "DirectCur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/DirectCur", 48, "ALL"
            ),
            "Direct2Cur": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/LCOutputConfig/Direct2Cur", 49, "ALL"
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
            "P1LTimeOut": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/TimeOut/P1LTimeOut", 118, "ALL"
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
                115,
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
                self.struct, "ConfigStructure/InputSupply/MaxNumberOfPhases", 114, "ALL"
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
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out2Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out2Fuse",
                84,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out3Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out3Fuse",
                85,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out4Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out4Fuse",
                86,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out5Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out5Fuse",
                87,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out6Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out6Fuse",
                88,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out7Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out7Fuse",
                89,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out8Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out8Fuse",
                90,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out9Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out9Fuse",
                91,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out10Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out10Fuse",
                92,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out11Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out11Fuse",
                93,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Out12Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Out12Fuse",
                94,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Direct1Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Direct1Fuse",
                95,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "Direct2Fuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/Direct2Fuse",
                96,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "OutHtrFuse": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/OutHtrFuse",
                97,
                None,
                ["F1", "F2", "F3", "F21", "F22", "F23", "Line1", "Line2", "Line3"],
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
            "F21Current": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/F21Current", 101, "ALL"
            ),
            "F22Current": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/F22Current", 102, "ALL"
            ),
            "F23Current": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/InputSupply/F23Current", 103, "ALL"
            ),
            "F1Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F1Line",
                104,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F2Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F2Line",
                105,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F3Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F3Line",
                106,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F21Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F21Line",
                107,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F22Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F22Line",
                108,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
                None,
                None,
                "ALL",
            ),
            "F23Line": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/InputSupply/F23Line",
                109,
                None,
                ["", "", "", "", "", "", "Line1", "Line2", "Line3"],
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
                116,
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
            "KeypadOptions1": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions1", 110, "ALL"
            ),
            "KeypadOptions2": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions2", 111, "ALL"
            ),
            "KeypadOptions3": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions3", 112, "ALL"
            ),
            "KeypadOptions4": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/MiscCfg/KeypadOptions4", 113, "ALL"
            ),
        }
