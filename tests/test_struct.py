"""Unit tests for the structure class."""  # noqa: INP001

from typing import Any

from context import (
    GeckoAsyncStructure,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
)


class MockStructure(GeckoAsyncStructure):
    """Wrapper to help testing."""

    last_pos: int | None = None
    last_len: int | None = None
    last_value: Any | None = None

    def __init__(self):
        super().__init__(self.set_value_cb)

        class log_class:
            def __init__(self, struct_):
                self.struct = struct_

            @property
            def temperature_keys(self):
                return []

            @property
            def output_keys(self):
                return []

            @property
            def accessors(self):
                return {
                    # <QuietState Type="Enum" Pos="362" Items="NOT_SET|QUIET|DRAIN|SOAK|OFF" RW="ALL" />
                    "QuietState": GeckoEnumStructAccessor(
                        self.struct,
                        "QuietState",
                        362,
                        None,
                        "NOT_SET|QUIET|DRAIN|SOAK|OFF",
                        None,
                        None,
                        "All",
                    ),
                    # <UdP1 Type="Enum" Pos="275" BitPos="14" Size="2" MaxItems="4" Items="OFF|LO|HI" RW="ALL" />
                    "UdP1": GeckoEnumStructAccessor(
                        self.struct, "UdP1", 275, 14, "OFF|LO|HI", 2, 4, "All"
                    ),
                    # <UdP2 Type="Enum" Pos="275" BitPos="12" Size="2" MaxItems="4" Items="OFF|LO|HI" RW="ALL" />
                    "UdP2": GeckoEnumStructAccessor(
                        self.struct, "UdP2", 275, 12, "OFF|LO|HI", 2, 4, "All"
                    ),
                    # <UdP3 Type="Enum" Pos="275" BitPos="11" Size="2" MaxItems="2" Items="OFF|HI" RW="ALL" />
                    "UdP3": GeckoEnumStructAccessor(
                        self.struct, "UdP3", 275, 11, "OFF|HI", 2, 2, "All"
                    ),
                    # <UdP4 Type="Enum" Pos="275" BitPos="10" Size="2" MaxItems="2" Items="OFF|HI" RW="ALL" />
                    "UdP4": GeckoEnumStructAccessor(
                        self.struct, "UdP4", 275, 10, "OFF|HI", 2, 2, "All"
                    ),
                    # <UdP5 Type="Enum" Pos="275" BitPos="9" Size="2" MaxItems="2" Items="OFF|HI" RW="ALL" />
                    "UdP5": GeckoEnumStructAccessor(
                        self.struct, "UdP5", 275, 9, "OFF|HI", 2, 2, "All"
                    ),
                    # <UdBL Type="Enum" Pos="275" BitPos="8" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
                    "UdBL": GeckoEnumStructAccessor(
                        self.struct, "UdBL", 275, 8, "OFF|ON", 2, 2, "All"
                    ),
                    # <UdL120 Type="Enum" Pos="275" BitPos="1" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
                    "UdL120": GeckoEnumStructAccessor(
                        self.struct, "UdL120", 275, 1, "OFF|ON", 2, 2, "All"
                    ),
                    # <UdLi Type="Enum" Pos="306" BitPos="0" MaxItems="4" Items="OFF|LO|MED|HI" RW="ALL" />
                    "UdLi": GeckoEnumStructAccessor(
                        self.struct, "UdLi", 306, 0, "OFF|LO|MED|HI", None, 4, "All"
                    ),
                }

        class cfg_class:
            def __init__(self, struct_):
                self.struct = struct_

            @property
            def temperature_keys(self):
                return []

            @property
            def all_device_keys(self):
                return []

            @property
            def user_demand_keys(self):
                return []

            @property
            def error_keys(self):
                return []

            @property
            def accessors(self):
                return {
                    # <UdValve Type="Enum" Pos="275" BitPos="7" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
                    # <UdTvLift Type="Enum" Pos="275" BitPos="5" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
                    # <UdSpkrLift Type="Enum" Pos="275" BitPos="4" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
                    # <UdVSP1 Type="Byte" Pos="303" Min="0" Max="100" RW="ALL" />
                    "UdVSP1": GeckoByteStructAccessor(
                        self.struct, "UdVSP1", 303, "All"
                    ),
                    # <UdVSP3 Type="Byte" Pos="304" Min="0" Max="100" RW="ALL" />
                    # <UdPumpTime Type="Byte" Pos="358" RW="ALL" />
                    # <UdQuietTime Type="Byte" Pos="359" Max="90" RW="ALL" />
                    # <UdLightTime Type="Byte" Pos="360" RW="ALL" />
                    # <UdL120Time Type="Byte" Pos="361" RW="ALL" />
                }

        self.build_accessors(log_class(self), cfg_class(self))

    async def set_value_cb(self, pos: int, len_: int, newvalue: Any) -> None:
        self.last_pos = pos
        self.last_len = len_
        self.last_value = newvalue


class TestStruct:
    """Test the GeckoStruct class."""

    struct = MockStructure()

    def test_constructor(self) -> None:
        assert self.struct.status_block == b"\x00" * 1024
        assert len(self.struct.accessors) == 10
        assert self.struct.accessors["UdL120"].value == "OFF"

    async def test_set_value_callback(self) -> None:
        await self.struct.accessors["UdP1"].async_set_value("HI")
        assert self.struct.last_pos == 275
        assert self.struct.last_len == 2
        assert self.struct.last_value == 32768

    def test_observer_callback(self) -> None:
        P2_info = {"oldvalue": None, "newvalue": None}

        def P2_Watch(sender, oldvalue, newvalue):
            P2_info["oldvalue"] = oldvalue
            P2_info["newvalue"] = newvalue

        self.struct.accessors["UdP2"].watch(P2_Watch)
        self.struct.replace_status_block_segment(275, b"\x20\x00")
        assert P2_info["newvalue"] == "HI"
