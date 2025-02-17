"""GeckoConfigStruct - A class to manage the ConfigStruct for 'inClear-32K v2'."""  # noqa: N999

from . import (
    GeckoAsyncStructure,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoStructAccessor,
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
        return 2

    @property
    def output_keys(self) -> list[str]:
        """Output keys property."""
        return []

    @property
    def accessors(self) -> dict[str, GeckoStructAccessor]:
        """The structure accessors."""
        return {
            "inClear-32K-Mode": GeckoEnumStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Mode",
                512,
                None,
                ["OFF", "ON"],
                None,
                None,
                "ALL",
            ),
            "inClear-32K-MaintenanceLevel": GeckoByteStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-MaintenanceLevel",
                513,
                "ALL",
            ),
            "inClear-32K-BoostLevel": GeckoByteStructAccessor(
                self.struct, "ConfigStructure/All/inClear-32K-BoostLevel", 514, "ALL"
            ),
            "inClear-32K-MaxCellCurrent": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-MaxCellCurrent",
                515,
                "ALL",
            ),
            "inClear-32K-MaxMaintenanceLevel": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-MaxMaintenanceLevel",
                517,
                "ALL",
            ),
            "inClear-32K-ErrDelayAfterReset": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-ErrDelayAfterReset",
                519,
                "ALL",
            ),
            "inClear-32K-Boost1Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost1Durx6Minutes",
                521,
                "ALL",
            ),
            "inClear-32K-Boost2Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost2Durx6Minutes",
                523,
                "ALL",
            ),
            "inClear-32K-Boost3Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost3Durx6Minutes",
                525,
                "ALL",
            ),
            "inClear-32K-Boost4Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost4Durx6Minutes",
                527,
                "ALL",
            ),
            "inClear-32K-Boost5Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost5Durx6Minutes",
                529,
                "ALL",
            ),
            "inClear-32K-Boost6Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost6Durx6Minutes",
                531,
                "ALL",
            ),
            "inClear-32K-Boost7Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost7Durx6Minutes",
                533,
                "ALL",
            ),
            "inClear-32K-Boost8Durx6Minutes": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-Boost8Durx6Minutes",
                535,
                "ALL",
            ),
            "inClear-32K-ValidRemoteFlow": GeckoWordStructAccessor(
                self.struct,
                "ConfigStructure/All/inClear-32K-ValidRemoteFlow",
                537,
                "ALL",
            ),
        }
