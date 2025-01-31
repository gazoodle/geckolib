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
            "Mode": GeckoEnumStructAccessor(
                self.struct, "Mode", 512, None, ["OFF", "ON"], None, None, "ALL"
            ),
            "MaintenanceLevel": GeckoByteStructAccessor(
                self.struct, "MaintenanceLevel", 513, "ALL"
            ),
            "BoostLevel": GeckoByteStructAccessor(
                self.struct, "BoostLevel", 514, "ALL"
            ),
            "MaxCellCurrent": GeckoWordStructAccessor(
                self.struct, "MaxCellCurrent", 515, "ALL"
            ),
            "MaxMaintenanceLevel": GeckoWordStructAccessor(
                self.struct, "MaxMaintenanceLevel", 517, "ALL"
            ),
            "ErrDelayAfterReset": GeckoWordStructAccessor(
                self.struct, "ErrDelayAfterReset", 519, "ALL"
            ),
            "Boost1Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost1Durx6Minutes", 521, "ALL"
            ),
            "Boost2Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost2Durx6Minutes", 523, "ALL"
            ),
            "Boost3Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost3Durx6Minutes", 525, "ALL"
            ),
            "Boost4Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost4Durx6Minutes", 527, "ALL"
            ),
            "Boost5Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost5Durx6Minutes", 529, "ALL"
            ),
            "Boost6Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost6Durx6Minutes", 531, "ALL"
            ),
            "Boost7Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost7Durx6Minutes", 533, "ALL"
            ),
            "Boost8Durx6Minutes": GeckoWordStructAccessor(
                self.struct, "Boost8Durx6Minutes", 535, "ALL"
            ),
            "ValidRemoteFlow": GeckoWordStructAccessor(
                self.struct, "ValidRemoteFlow", 537, "ALL"
            ),
        }
