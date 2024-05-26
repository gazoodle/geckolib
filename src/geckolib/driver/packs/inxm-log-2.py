#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v2'
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
        return 2

    @property
    def begin(self):
        return 256

    @property
    def end(self):
        return 511

    @property
    def all_device_keys(self):
        return [
            "P1",
            "P2",
            "P3",
            "P4",
            "P5",
            "BLOWER",
            "CP",
            "OZONE",
            "L120",
            "FAN",
            "RH_DutyCycle",
            "VSP1_AvantPlanSpeed",
            "VSP1_MinimumSpeed",
            "VSP3_AvantPlanSpeed",
            "VSP3_MinimumSpeed",
            "LI",
        ]

    @property
    def user_demand_keys(self):
        return []

    @property
    def error_keys(self):
        return [
            "RH_DutyCycleErr",
            "AmbiantOHLevel2",
            "RH_CommErr",
            "ThermistanceErr",
            "rHId",
            "Fuse3Err",
            "SupplyErr",
            "Fuse2Err",
            "RegOverHeatFlag",
            "KinPumpOff",
            "ScanErr",
            "ContactorCoilFailErr",
            "OHCondition",
            "RelayStuck",
            "LearnDetectionErr",
            "NoHeaterCurrentErr",
            "AmbiantOHLevel1",
            "RH_RegProbeErr",
            "Fuse1Err",
        ]

    @property
    def accessors(self):
        return {
            "Hours": GeckoByteStructAccessor(self.struct, "Hours", 256, "ALL"),
            "BrMenu": GeckoBoolStructAccessor(self.struct, "BrMenu", 279, 6, None),
            "HeaterPhase": GeckoByteStructAccessor(
                self.struct, "HeaterPhase", 300, None
            ),
            "LearningCurrentOUT1A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT1A", 280, None
            ),
            "LearningCurrentOUT1B": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT1B", 282, None
            ),
            "LearningCurrentOUT2A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT2A", 284, None
            ),
            "LearningCurrentOUT2B": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT2B", 286, None
            ),
            "LearningCurrentOUT3A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT3A", 288, None
            ),
            "LearningCurrentOUT4A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT4A", 290, None
            ),
            "LearningCurrentOUT5A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT5A", 292, None
            ),
            "LearningCurrentOUT6A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT6A", 294, None
            ),
            "LearningCurrentOUT7A": GeckoWordStructAccessor(
                self.struct, "LearningCurrentOUT7A", 296, None
            ),
            "CurrentHeater": GeckoWordStructAccessor(
                self.struct, "CurrentHeater", 298, "ALL"
            ),
            "UD_P1": GeckoEnumStructAccessor(
                self.struct, "UD_P1", 275, 14, ["OFF", "LOW", "HIGH"], 2, 4, "ALL"
            ),
            "UD_P2": GeckoEnumStructAccessor(
                self.struct, "UD_P2", 275, 12, ["OFF", "LOW", "HIGH"], 2, 4, "Gecko"
            ),
            "UD_P3": GeckoEnumStructAccessor(
                self.struct, "UD_P3", 275, 11, ["OFF", "HIGH"], 2, 2, "RD"
            ),
            "UD_P4": GeckoEnumStructAccessor(
                self.struct, "UD_P4", 275, 10, ["OFF", "HIGH"], 2, 2, "ALL"
            ),
            "UD_P5": GeckoEnumStructAccessor(
                self.struct, "UD_P5", 275, 9, ["OFF", "HIGH"], 2, 2, "ALL"
            ),
            "UD_BLOWER": GeckoEnumStructAccessor(
                self.struct, "UD_BLOWER", 275, 8, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UD_AUX1": GeckoEnumStructAccessor(
                self.struct, "UD_AUX1", 275, 5, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UD_AUX2": GeckoEnumStructAccessor(
                self.struct, "UD_AUX2", 275, 4, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UD_FB_LT": GeckoEnumStructAccessor(
                self.struct,
                "UD_FB_LT",
                275,
                2,
                ["OFF", "FIXCOLOR", "SCAN"],
                2,
                4,
                "ALL",
            ),
            "UD_LIGHT120": GeckoEnumStructAccessor(
                self.struct, "UD_LIGHT120", 275, 1, ["OFF", "ON"], 2, 2, "ALL"
            ),
            "UD_QUIET_PAUSE": GeckoEnumStructAccessor(
                self.struct, "UD_QUIET_PAUSE", 275, 0, [" ", "QUIET"], 2, 2, "ALL"
            ),
            "VSP1_UDSpeed": GeckoByteStructAccessor(
                self.struct, "VSP1_UDSpeed", 304, "ALL"
            ),
            "VSP3_UDSpeed": GeckoByteStructAccessor(
                self.struct, "VSP3_UDSpeed", 305, "ALL"
            ),
            "LightIntensity": GeckoByteStructAccessor(
                self.struct, "LightIntensity", 308, "ALL"
            ),
            "P1": GeckoEnumStructAccessor(
                self.struct, "P1", 316, 0, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P2": GeckoEnumStructAccessor(
                self.struct, "P2", 316, 2, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P3": GeckoEnumStructAccessor(
                self.struct, "P3", 316, 4, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P4": GeckoEnumStructAccessor(
                self.struct, "P4", 316, 6, ["OFF", "HIGH", "LOW"], None, 4, None
            ),
            "P5": GeckoEnumStructAccessor(
                self.struct, "P5", 315, 0, ["OFF", "HIGH"], None, 2, None
            ),
            "BLOWER": GeckoEnumStructAccessor(
                self.struct, "BLOWER", 315, 1, ["OFF", "HIGH"], None, 2, None
            ),
            "CP": GeckoEnumStructAccessor(
                self.struct, "CP", 315, 2, ["OFF", "ON"], None, 2, None
            ),
            "OZONE": GeckoEnumStructAccessor(
                self.struct, "OZONE", 315, 3, ["OFF", "ON"], None, 2, None
            ),
            "L120": GeckoEnumStructAccessor(
                self.struct, "L120", 315, 4, ["OFF", "ON"], None, 2, None
            ),
            "FAN": GeckoEnumStructAccessor(
                self.struct, "FAN", 315, 7, ["OFF", "ON"], None, 2, None
            ),
            "RH_DutyCycle": GeckoByteStructAccessor(
                self.struct, "RH_DutyCycle", 274, None
            ),
            "VSP1_AvantPlanSpeed": GeckoByteStructAccessor(
                self.struct, "VSP1_AvantPlanSpeed", 302, None
            ),
            "VSP1_MinimumSpeed": GeckoByteStructAccessor(
                self.struct, "VSP1_MinimumSpeed", 306, None
            ),
            "VSP3_AvantPlanSpeed": GeckoByteStructAccessor(
                self.struct, "VSP3_AvantPlanSpeed", 303, None
            ),
            "VSP3_MinimumSpeed": GeckoByteStructAccessor(
                self.struct, "VSP3_MinimumSpeed", 307, None
            ),
            "RemoteFiltAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteFiltAction",
                309,
                None,
                ["USE_INTERNAL", "IDLE", "STOP", "START", "NEW", "FILTER"],
                None,
                6,
                "ALL",
            ),
            "RemoteFiltDur": GeckoTimeStructAccessor(
                self.struct, "RemoteFiltDur", 310, "ALL"
            ),
            "RemoteOnzenAction": GeckoEnumStructAccessor(
                self.struct,
                "RemoteOnzenAction",
                312,
                None,
                ["USE_INTERNAL", "IDLE", "STOP", "START", "NEW", "FILTER"],
                None,
                6,
                "ALL",
            ),
            "RemoteOnzenDur": GeckoTimeStructAccessor(
                self.struct, "RemoteOnzenDur", 313, "ALL"
            ),
            "FiltPurge": GeckoBoolStructAccessor(
                self.struct, "FiltPurge", 269, 7, None
            ),
            "FiltClean": GeckoBoolStructAccessor(
                self.struct, "FiltClean", 269, 5, None
            ),
            "FiltCleanSuspended": GeckoBoolStructAccessor(
                self.struct, "FiltCleanSuspended", 269, 4, None
            ),
            "FiltPurgeSuspendUD": GeckoBoolStructAccessor(
                self.struct, "FiltPurgeSuspendUD", 279, 2, None
            ),
            "FiltCleanSuspendUD": GeckoBoolStructAccessor(
                self.struct, "FiltCleanSuspendUD", 279, 3, None
            ),
            "FilterOT": GeckoBoolStructAccessor(self.struct, "FilterOT", 279, 0, None),
            "CPOT": GeckoBoolStructAccessor(self.struct, "CPOT", 279, 1, None),
            "SWM_Active": GeckoByteStructAccessor(self.struct, "SWM_Active", 267, None),
            "SWM_Risk": GeckoEnumStructAccessor(
                self.struct,
                "SWM_Risk",
                268,
                None,
                ["NO", "LOW", "MEDIUM", "HIGH", "EXTREME"],
                None,
                8,
                None,
            ),
            "SWMPurge": GeckoBoolStructAccessor(self.struct, "SWMPurge", 269, 3, None),
            "SWMPurge_Susp": GeckoBoolStructAccessor(
                self.struct, "SWMPurge_Susp", 269, 2, None
            ),
            "DisplayedTemp_G": GeckoTempStructAccessor(
                self.struct, "DisplayedTemp_G", 265, None
            ),
            "PumpRun": GeckoBoolStructAccessor(self.struct, "PumpRun", 269, 1, None),
            "CheckFlow": GeckoBoolStructAccessor(
                self.struct, "CheckFlow", 269, 0, None
            ),
            "Heating": GeckoBoolStructAccessor(self.struct, "Heating", 270, 7, None),
            "CoolingDown": GeckoBoolStructAccessor(
                self.struct, "CoolingDown", 270, 6, None
            ),
            "KineticPurgeActive": GeckoBoolStructAccessor(
                self.struct, "KineticPurgeActive", 270, 5, None
            ),
            "EconomyActive": GeckoBoolStructAccessor(
                self.struct, "EconomyActive", 271, 0, None
            ),
            "ProgEconomyActive": GeckoBoolStructAccessor(
                self.struct, "ProgEconomyActive", 271, 2, None
            ),
            "ExtProbeActive": GeckoBoolStructAccessor(
                self.struct, "ExtProbeActive", 301, 0, None
            ),
            "ThermistanceErr": GeckoBoolStructAccessor(
                self.struct, "ThermistanceErr", 277, 5, None
            ),
            "ContactorCoilFailErr": GeckoBoolStructAccessor(
                self.struct, "ContactorCoilFailErr", 277, 4, None
            ),
            "NoHeaterCurrentErr": GeckoBoolStructAccessor(
                self.struct, "NoHeaterCurrentErr", 277, 3, None
            ),
            "LearnDetectionErr": GeckoBoolStructAccessor(
                self.struct, "LearnDetectionErr", 277, 2, None
            ),
            "Fuse3Err": GeckoBoolStructAccessor(self.struct, "Fuse3Err", 277, 1, None),
            "Fuse2Err": GeckoBoolStructAccessor(self.struct, "Fuse2Err", 277, 0, None),
            "Fuse1Err": GeckoBoolStructAccessor(self.struct, "Fuse1Err", 278, 7, None),
            "SupplyErr": GeckoBoolStructAccessor(
                self.struct, "SupplyErr", 278, 6, None
            ),
            "ScanErr": GeckoBoolStructAccessor(self.struct, "ScanErr", 278, 5, None),
            "RegOverHeatFlag": GeckoBoolStructAccessor(
                self.struct, "RegOverHeatFlag", 278, 4, None
            ),
            "AmbiantOHLevel2": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHLevel2", 278, 3, None
            ),
            "AmbiantOHLevel1": GeckoBoolStructAccessor(
                self.struct, "AmbiantOHLevel1", 278, 2, None
            ),
            "RelayStuck": GeckoBoolStructAccessor(
                self.struct, "RelayStuck", 278, 1, None
            ),
            "rHId": GeckoBoolStructAccessor(self.struct, "rHId", 278, 0, None),
            "KinPumpOff": GeckoBoolStructAccessor(
                self.struct, "KinPumpOff", 279, 4, None
            ),
            "OHCondition": GeckoBoolStructAccessor(
                self.struct, "OHCondition", 279, 5, None
            ),
            "RH_WaterTemp": GeckoTempStructAccessor(
                self.struct, "RH_WaterTemp", 261, None
            ),
            "RH_TriacTemp": GeckoTempStructAccessor(
                self.struct, "RH_TriacTemp", 263, None
            ),
            "RH_CommErr": GeckoBoolStructAccessor(
                self.struct, "RH_CommErr", 257, 7, None
            ),
            "RH_NotEnoughHeat": GeckoBoolStructAccessor(
                self.struct, "RH_NotEnoughHeat", 257, 3, None
            ),
            "RH_RegSlope": GeckoBoolStructAccessor(
                self.struct, "RH_RegSlope", 257, 2, None
            ),
            "RH_LowFlo": GeckoBoolStructAccessor(
                self.struct, "RH_LowFlo", 257, 0, None
            ),
            "RH_DutyCycleErr": GeckoBoolStructAccessor(
                self.struct, "RH_DutyCycleErr", 258, 7, None
            ),
            "RH_NoFloRetry": GeckoBoolStructAccessor(
                self.struct, "RH_NoFloRetry", 258, 6, None
            ),
            "RH_NoFloTemp": GeckoBoolStructAccessor(
                self.struct, "RH_NoFloTemp", 258, 5, None
            ),
            "RH_NoFloXTries": GeckoBoolStructAccessor(
                self.struct, "RH_NoFloXTries", 258, 4, None
            ),
            "RH_HR_HL": GeckoBoolStructAccessor(self.struct, "RH_HR_HL", 258, 3, None),
            "RH_HW_HL": GeckoBoolStructAccessor(self.struct, "RH_HW_HL", 258, 2, None),
            "RH_RegProbeErr": GeckoBoolStructAccessor(
                self.struct, "RH_RegProbeErr", 258, 1, None
            ),
            "RH_RegOverHeat": GeckoBoolStructAccessor(
                self.struct, "RH_RegOverHeat", 258, 0, None
            ),
            "RH_HrTriacPr": GeckoBoolStructAccessor(
                self.struct, "RH_HrTriacPr", 259, 7, None
            ),
            "RH_HrTriacOH": GeckoBoolStructAccessor(
                self.struct, "RH_HrTriacOH", 259, 6, None
            ),
            "RH_SWTriacOH": GeckoBoolStructAccessor(
                self.struct, "RH_SWTriacOH", 259, 5, None
            ),
            "RH_HwTriacOH": GeckoBoolStructAccessor(
                self.struct, "RH_HwTriacOH", 259, 4, None
            ),
            "RH_HrKin": GeckoBoolStructAccessor(self.struct, "RH_HrKin", 259, 3, None),
            "RH_HrKinNoFlo": GeckoBoolStructAccessor(
                self.struct, "RH_HrKinNoFlo", 259, 2, None
            ),
            "RH_SwKinTemp": GeckoBoolStructAccessor(
                self.struct, "RH_SwKinTemp", 259, 1, None
            ),
            "RH_HWKinetic": GeckoBoolStructAccessor(
                self.struct, "RH_HWKinetic", 259, 0, None
            ),
            "RH_HeaterDisable": GeckoBoolStructAccessor(
                self.struct, "RH_HeaterDisable", 260, 4, None
            ),
            "RH_FlowDetected": GeckoBoolStructAccessor(
                self.struct, "RH_FlowDetected", 260, 3, None
            ),
            "RH_FlowCheck": GeckoBoolStructAccessor(
                self.struct, "RH_FlowCheck", 260, 2, None
            ),
            "RH_HeaterSuspended": GeckoBoolStructAccessor(
                self.struct, "RH_HeaterSuspended", 260, 1, None
            ),
            "RH_FloCheckReady": GeckoBoolStructAccessor(
                self.struct, "RH_FloCheckReady", 260, 0, None
            ),
        }
