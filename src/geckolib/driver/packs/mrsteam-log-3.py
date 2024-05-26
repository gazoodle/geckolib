#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v3'
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
        return 3

    @property
    def begin(self):
        return 256

    @property
    def end(self):
        return 337

    @property
    def all_device_keys(self):
        return ["LI"]

    @property
    def user_demand_keys(self):
        return []

    @property
    def error_keys(self):
        return [
            "PowerFailErr",
            "Prr2Err",
            "SlaveH2O2Err",
            "KeyStuckErr",
            "Prr3Err",
            "Prr1Err",
            "Prr4Err",
            "H2O2Err",
            "FlashErr",
        ]

    @property
    def accessors(self):
        return {
            "UserMode": GeckoEnumStructAccessor(
                self.struct,
                "UserMode",
                256,
                None,
                ["OFF", "ON", "DIAGNOSTIC"],
                None,
                None,
                "ALL",
            ),
            "UserPause": GeckoBoolStructAccessor(
                self.struct, "UserPause", 257, 1, "ALL"
            ),
            "UserAroma": GeckoEnumStructAccessor(
                self.struct, "UserAroma", 258, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "UserChroma": GeckoEnumStructAccessor(
                self.struct, "UserChroma", 259, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "UserSetpointG": GeckoTempStructAccessor(
                self.struct, "UserSetpointG", 264, "ALL"
            ),
            "UserRuntime": GeckoWordStructAccessor(
                self.struct, "UserRuntime", 261, "ALL"
            ),
            "UserProg": GeckoEnumStructAccessor(
                self.struct,
                "UserProg",
                263,
                None,
                ["User", "Prog1", "Prog2"],
                None,
                None,
                "ALL",
            ),
            "UserValvePower": GeckoEnumStructAccessor(
                self.struct,
                "UserValvePower",
                302,
                None,
                ["ON", "OFF"],
                None,
                None,
                "ALL",
            ),
            "UserValveOutput": GeckoByteStructAccessor(
                self.struct, "UserValveOutput", 303, "ALL"
            ),
            "UserValveDisinfection": GeckoBoolStructAccessor(
                self.struct, "UserValveDisinfection", 304, None, "ALL"
            ),
            "UserValveFlowUp": GeckoBoolStructAccessor(
                self.struct, "UserValveFlowUp", 306, None, "ALL"
            ),
            "UserValveFlowDown": GeckoBoolStructAccessor(
                self.struct, "UserValveFlowDown", 307, None, "ALL"
            ),
            "UserValveTempUp": GeckoBoolStructAccessor(
                self.struct, "UserValveTempUp", 308, None, "ALL"
            ),
            "UserValveTempDown": GeckoBoolStructAccessor(
                self.struct, "UserValveTempDown", 309, None, "ALL"
            ),
            "UserValveLearning": GeckoBoolStructAccessor(
                self.struct, "UserValveLearning", 310, None, "All"
            ),
            "UserValveAutoClean": GeckoBoolStructAccessor(
                self.struct, "UserValveAutoClean", 311, None, "All"
            ),
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 268, None),
            "ModeState": GeckoEnumStructAccessor(
                self.struct, "ModeState", 269, 0, ["OFF", "ON"], None, 2, None
            ),
            "PauseState": GeckoBoolStructAccessor(
                self.struct, "PauseState", 269, 1, None
            ),
            "DiagnosticState": GeckoEnumStructAccessor(
                self.struct, "DiagnosticState", 269, 2, ["OFF", "ON"], None, 2, None
            ),
            "ExternalProbe": GeckoBoolStructAccessor(
                self.struct, "ExternalProbe", 269, 3, None
            ),
            "WaterDetected": GeckoBoolStructAccessor(
                self.struct, "WaterDetected", 269, 4, None
            ),
            "NoRegulation": GeckoBoolStructAccessor(
                self.struct, "NoRegulation", 269, 5, None
            ),
            "MasterSlave": GeckoEnumStructAccessor(
                self.struct, "MasterSlave", 269, 6, ["SLAVE", "MASTER"], None, 2, None
            ),
            "KeypadProbe": GeckoBoolStructAccessor(
                self.struct, "KeypadProbe", 270, 0, None
            ),
            "ExpressCycle": GeckoBoolStructAccessor(
                self.struct, "ExpressCycle", 270, 1, None
            ),
            "SlaveOnState": GeckoBoolStructAccessor(
                self.struct, "SlaveOnState", 271, 1, None
            ),
            "SlaveHeaterState": GeckoEnumStructAccessor(
                self.struct, "SlaveHeaterState", 271, 3, ["OFF", "ON"], None, 2, None
            ),
            "PowerFailErr": GeckoBoolStructAccessor(
                self.struct, "PowerFailErr", 272, 0, None
            ),
            "Prr2Err": GeckoBoolStructAccessor(self.struct, "Prr2Err", 272, 1, None),
            "Prr1Err": GeckoBoolStructAccessor(self.struct, "Prr1Err", 272, 2, None),
            "H2O2Err": GeckoBoolStructAccessor(self.struct, "H2O2Err", 272, 3, None),
            "SlaveH2O2Err": GeckoBoolStructAccessor(
                self.struct, "SlaveH2O2Err", 272, 4, None
            ),
            "KeyStuckErr": GeckoBoolStructAccessor(
                self.struct, "KeyStuckErr", 272, 5, None
            ),
            "FlashErr": GeckoBoolStructAccessor(self.struct, "FlashErr", 272, 6, None),
            "Prr3Err": GeckoBoolStructAccessor(self.struct, "Prr3Err", 272, 7, None),
            "Prr4Err": GeckoBoolStructAccessor(self.struct, "Prr4Err", 273, 0, None),
            "Jumper9": GeckoBoolStructAccessor(self.struct, "Jumper9", 274, 0, None),
            "Jumper2": GeckoBoolStructAccessor(self.struct, "Jumper2", 274, 1, None),
            "Jumper3": GeckoBoolStructAccessor(self.struct, "Jumper3", 274, 2, None),
            "Jumper4": GeckoBoolStructAccessor(self.struct, "Jumper4", 274, 3, None),
            "Jumper5": GeckoBoolStructAccessor(self.struct, "Jumper5", 274, 4, None),
            "Jumper6": GeckoBoolStructAccessor(self.struct, "Jumper6", 274, 5, None),
            "Jumper7": GeckoBoolStructAccessor(self.struct, "Jumper7", 274, 6, None),
            "Jumper8": GeckoBoolStructAccessor(self.struct, "Jumper8", 274, 7, None),
            "MaxRuntime": GeckoWordStructAccessor(self.struct, "MaxRuntime", 275, None),
            "KeypadType": GeckoEnumStructAccessor(
                self.struct,
                "KeypadType",
                277,
                None,
                ["NO_TSC", "SC_54", "TSC_53", "AUX_SW", "COLOR_SERIES"],
                None,
                None,
                None,
            ),
            "KeypadID": GeckoWordStructAccessor(self.struct, "KeypadID", 298, None),
            "KeypadRev": GeckoByteStructAccessor(self.struct, "KeypadRev", 300, None),
            "KeypadRel": GeckoByteStructAccessor(self.struct, "KeypadRel", 301, None),
            "RoomTempG": GeckoTempStructAccessor(self.struct, "RoomTempG", 278, None),
            "K1000TempG": GeckoTempStructAccessor(
                self.struct, "K1000TempG", 296, "ALL"
            ),
            "RemainingRuntime": GeckoWordStructAccessor(
                self.struct, "RemainingRuntime", 293, None
            ),
            "DrainValveOutput": GeckoBoolStructAccessor(
                self.struct, "DrainValveOutput", 295, 0, None
            ),
            "AromaOutput": GeckoBoolStructAccessor(
                self.struct, "AromaOutput", 295, 1, None
            ),
            "HeaterOutput": GeckoBoolStructAccessor(
                self.struct, "HeaterOutput", 295, 2, None
            ),
            "WaterValveOutput": GeckoBoolStructAccessor(
                self.struct, "WaterValveOutput", 295, 3, None
            ),
            "ChromaOutput": GeckoBoolStructAccessor(
                self.struct, "ChromaOutput", 295, 4, None
            ),
            "ShowerValveStatus": GeckoWordStructAccessor(
                self.struct, "ShowerValveStatus", 312, None
            ),
            "ShowerValveTempC": GeckoTempStructAccessor(
                self.struct, "ShowerValveTempC", 314, None
            ),
            "ShowerFlowRate": GeckoWordStructAccessor(
                self.struct, "ShowerFlowRate", 316, None
            ),
            "AvailableOutlet": GeckoWordStructAccessor(
                self.struct, "AvailableOutlet", 318, None
            ),
            "ShowerValveAlarm": GeckoWordStructAccessor(
                self.struct, "ShowerValveAlarm", 322, None
            ),
            "PackBootID": GeckoWordStructAccessor(self.struct, "PackBootID", 281, None),
            "PackBootRev": GeckoByteStructAccessor(
                self.struct, "PackBootRev", 283, None
            ),
            "PackBootRel": GeckoByteStructAccessor(
                self.struct, "PackBootRel", 284, None
            ),
            "PackType": GeckoEnumStructAccessor(
                self.struct,
                "PackType",
                285,
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
                    "Color_Keypad",
                    "inYJ",
                    "MrSteam",
                ],
                None,
                None,
                None,
            ),
            "PackMemRange": GeckoEnumStructAccessor(
                self.struct,
                "PackMemRange",
                286,
                0,
                ["16K", "32K", "48K", "64K"],
                None,
                4,
                None,
            ),
            "PackCoreID": GeckoWordStructAccessor(self.struct, "PackCoreID", 287, None),
            "PackCoreRev": GeckoByteStructAccessor(
                self.struct, "PackCoreRev", 289, None
            ),
            "PackCoreRel": GeckoByteStructAccessor(
                self.struct, "PackCoreRel", 290, None
            ),
            "PackConfigLib": GeckoByteStructAccessor(
                self.struct, "PackConfigLib", 291, None
            ),
            "PackStatusLib": GeckoByteStructAccessor(
                self.struct, "PackStatusLib", 292, None
            ),
            "I2CtoRS485ConverterID": GeckoWordStructAccessor(
                self.struct, "I2CtoRS485ConverterID", 334, None
            ),
            "I2CtoRS485ConverterRev": GeckoByteStructAccessor(
                self.struct, "I2CtoRS485ConverterRev", 336, None
            ),
            "I2CtoRS485ConverterRel": GeckoByteStructAccessor(
                self.struct, "I2CtoRS485ConverterRel", 337, None
            ),
        }
