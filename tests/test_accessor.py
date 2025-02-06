"""Unit tests for the structure accessor class."""  # noqa: INP001

from typing import Any

import pytest
from context import (
    GeckoAsyncStructure,
    GeckoBoolStructAccessor,
    GeckoByteStructAccessor,
    GeckoEnumStructAccessor,
    GeckoWordStructAccessor,
)

from geckolib.driver.accessor import GeckoStructAccessor


class MockStructure(GeckoAsyncStructure):
    """Wrapper to help testing."""

    last_pos: int | None = None
    last_len: int | None = None
    last_data: bytes | None = None
    last_value: Any | None = None

    def __init__(self) -> None:
        """Initialize the mock structure."""
        super().__init__(self.set_value_cb)
        self.set_status_block(
            # Bytes 0-16 are identity values
            b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
            # Bytes 17-18 are a temperature in farenheit 10ths from freezing
            b"\x02\xbe"
            # Bytes 19-20 are a sized bitpos enum
            b"\x11\x70"
            # Bytes 21-22 are an empty sized bitpos enum
            b"\x00\x00"
        )

    async def set_value_cb(self, pos: int, len_: int, newvalue: Any) -> None:
        self.last_pos = pos
        self.last_len = len_
        self.last_data = GeckoStructAccessor.pack_data(len_, newvalue)
        self.replace_status_block_segment(pos, self.last_data)
        self.last_value = newvalue


class TestStructAccessor:
    """Test the GeckoStructAccessor class."""

    struct = MockStructure()

    def test_read_byte(self) -> None:
        """Can we read a byte from the structure."""
        accessor = GeckoByteStructAccessor(self.struct, "PackBootRev", 5, None)
        assert accessor.value == 5

    @pytest.mark.asyncio
    async def test_write_byte_fails(self) -> None:
        """Can we write a byte to the structure without the RW tag."""
        accessor = GeckoByteStructAccessor(self.struct, "PackBootRev", 5, None)
        with pytest.raises(AttributeError):
            await accessor.async_set_value(6)

    @pytest.mark.asyncio
    async def test_write_byte(self) -> None:
        """Can we write a byte to the structure."""
        accessor = GeckoByteStructAccessor(self.struct, "PackBootRev", 5, "ALL")
        await accessor.async_set_value(6)
        assert self.struct.last_pos == 5
        assert self.struct.last_data == b"\x06"

    @pytest.mark.asyncio
    async def test_write_byte_from_string(self) -> None:
        """Can we write a byte (as a string) to the structure."""
        accessor = GeckoByteStructAccessor(self.struct, "PackBootRev", 5, "ALL")
        await accessor.async_set_value("6")
        assert self.struct.last_pos == 5
        assert self.struct.last_data == b"\x06"

    def test_read_word(self) -> None:
        """Can we read a word from the structure."""
        accessor = GeckoWordStructAccessor(self.struct, "RealSetPointG", 17, None)
        assert accessor.value == 702

    @pytest.mark.asyncio
    async def test_write_word(self) -> None:
        """Can we write a word to the structure."""
        accessor = GeckoWordStructAccessor(self.struct, "RealSetPointG", 17, "All")
        await accessor.async_set_value(726)
        assert self.struct.last_pos == 17
        assert self.struct.last_data == b"\x02\xd6"

    @pytest.mark.asyncio
    async def test_write_word_as_string(self) -> None:
        """Can we write a word (as a string) to the structure."""
        accessor = GeckoWordStructAccessor(self.struct, "RealSetPointG", 17, "All")
        await accessor.async_set_value("726")
        assert self.struct.last_pos == 17
        assert self.struct.last_data == b"\x02\xd6"

    def test_read_enum(self) -> None:
        """Can we read an enum from the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct,
            "PackType",
            6,
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
                "K800",
                "inYJ",
            ],
            None,
            None,
            None,
        )
        assert accessor.value == "inXM"

    @pytest.mark.asyncio
    async def test_write_enum(self) -> None:
        """Can we write an enum to the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct,
            "PackType",
            6,
            None,
            (
                "Unknown|inXE|MasIBC|MIA|DJS4|inClear|inXM|K600"
                "|inTerface|inTouch|inYT|K800|inYJ"
            ),
            None,
            None,
            "All",
        )
        await accessor.async_set_value("inYJ")
        assert self.struct.last_pos == 6
        assert self.struct.last_data == b"\x0c"

    @pytest.mark.asyncio
    async def test_write_enum_not_member(self) -> None:
        """Can we write an enum to the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct,
            "PackType",
            6,
            None,
            (
                "Unknown|inXE|MasIBC|MIA|DJS4|inClear|inXM|K600"
                "|inTerface|inTouch|inYT|K800|inYJ"
            ),
            None,
            None,
            "All",
        )
        with pytest.raises(ValueError, match="Not A Member"):
            await accessor.async_set_value("Not A Member")

    def test_read_bool(self) -> None:
        """Can we read a bool from the structure."""
        accessor = GeckoBoolStructAccessor(self.struct, "RelayStuck", 2, 6, None)
        assert not accessor.value

    @pytest.mark.asyncio
    async def test_write_bool(self) -> None:
        """Can we write a bool to the structure."""
        accessor = GeckoBoolStructAccessor(self.struct, "RelayStuck", 2, 6, "All")
        await accessor.async_set_value(True)  # noqa: FBT003
        assert self.struct.last_pos == 2
        assert self.struct.last_data == b"B"

    @pytest.mark.asyncio
    async def test_write_bool_as_string(self) -> None:
        """Can we write a bool (as a string) to the structure."""
        accessor = GeckoBoolStructAccessor(self.struct, "RelayStuck", 2, 6, "All")
        await accessor.async_set_value("True")
        assert self.struct.last_pos == 2
        assert self.struct.last_data == b"B"

    def test_read_bitpos_enum(self) -> None:
        """Can we read a bitpos enum from the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct, "UdP3", 3, 4, "OFF|LO|HI", None, 4, None
        )
        assert accessor.value == "OFF"
        assert accessor.raw_value == 0

    @pytest.mark.asyncio
    async def test_write_bitpos_enum(self) -> None:
        """Can we write an enum to the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct, "UdP3", 3, 4, "OFF|LO|HI", None, 4, "All"
        )
        await accessor.async_set_value("HI")
        assert self.struct.last_pos == 3
        assert self.struct.last_data == b"#"
        assert accessor.value == "HI"
        assert accessor.raw_value == 2
        await accessor.async_set_value("LO")
        assert self.struct.last_data == b"\x13"
        assert accessor.raw_value == 1
        await accessor.async_set_value("OFF")
        assert self.struct.last_data == b"\x03"
        assert accessor.raw_value == 0

    def test_read_sized_bitpos_enum(self) -> None:
        """Can we read a sized bitpos enum from the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct, "UdP2", 19, 12, "OFF|LO|HI", 2, 4, None
        )
        assert accessor.value == "LO"

    @pytest.mark.asyncio
    async def test_write_sized_bitpos_enum(self) -> None:
        """Can we write a sized bitpos enum to the structure."""
        accessor = GeckoEnumStructAccessor(
            self.struct, "UdP2", 19, 12, "OFF|LO|HI", 2, 4, "All"
        )
        await accessor.async_set_value("HI")
        assert self.struct.last_pos == 19
        assert self.struct.last_data is not None
        assert chr(0b00100001) + chr(0b01110000) == self.struct.last_data.decode(
            "latin-1"
        )
        await accessor.async_set_value("LO")
        assert chr(0b00010001) + chr(0b01110000) == self.struct.last_data.decode(
            "latin-1"
        )
        await accessor.async_set_value("OFF")
        assert chr(0b00000001) + chr(0b01110000) == self.struct.last_data.decode(
            "latin-1"
        )

    @pytest.mark.asyncio
    async def test_multiple_write_bitpos_enum(self) -> None:
        """Can we write multiple bitpos enums to the structure."""
        accessor_p1 = GeckoEnumStructAccessor(
            self.struct, "UdP1", 21, 14, "OFF|LO|HI", 2, 4, "ALL"
        )
        accessor_p2 = GeckoEnumStructAccessor(
            self.struct, "UdP2", 21, 12, "OFF|LO|HI", 2, 4, "All"
        )

        await accessor_p2.async_set_value("HI")
        assert self.struct.last_pos == 21
        assert self.struct.last_data == b"\x20\x00"
        assert self.struct.last_len == 2
        assert self.struct.last_data is not None
        assert len(self.struct.last_data) == 2

        await accessor_p1.async_set_value("HI")
        assert self.struct.last_pos == 21
        assert self.struct.last_data == b"\xa0\x00"
        assert self.struct.last_len == 2
        assert len(self.struct.last_data) == 2
