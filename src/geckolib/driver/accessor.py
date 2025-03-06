"""Structure accessor."""

from __future__ import annotations

import logging
import struct
from typing import TYPE_CHECKING, Any

from geckolib.const import GeckoConstants

from .observable import Observable

if TYPE_CHECKING:
    from .async_spastruct import GeckoAsyncStructure

_LOGGER = logging.getLogger(__name__)


class GeckoStructAccessor(Observable):
    """
    Class to access the spa data structure.

    Uses the declaration in the specific modules.
    """

    @staticmethod
    def pack_data(length: int, data: Any) -> bytes:
        """Pack the data into bytes."""
        if isinstance(data, bytes):
            return data
        if length == 1:
            return struct.pack(">B", data)
        if length == 2:  # noqa: PLR2004
            return struct.pack(">H", data)
        raise OverflowError(length)

    def __init__(  # noqa: PLR0913
        self,
        struct_: GeckoAsyncStructure,
        path: str,
        pos: int,
        accessor_type: str,
        bitpos: int | None,
        items: str | list[str] | None,
        size: int | None,
        maxitems: int | None,
        rw: str | None,
    ) -> None:
        """Initialize the accessor class."""
        super().__init__()

        self.path: str = path
        self.tag: str = path.split("/")[-1]
        self.struct: GeckoAsyncStructure = struct_
        self.pos: int = pos
        self.accessor_type: str = accessor_type
        self.bitpos: int | None = bitpos
        self.items: list[str] | None = None
        self.maxitems: int | None = None
        self.direct_update: bool = False

        if bitpos is not None:
            self.bitmask = 1

        if items is not None:
            if isinstance(items, str):
                self.items = items.split("|")
            else:
                self.items = items

        self.length = 1
        self.format = ">B"

        if size is not None:
            self.length = size
            if self.length == 2:  # noqa: PLR2004
                self.format = ">H"

        if self.accessor_type in (
            GeckoConstants.SPA_PACK_STRUCT_WORD_TYPE,
            GeckoConstants.SPA_PACK_STRUCT_TIME_TYPE,
        ):
            self.length = 2
            self.format = ">H"

        if maxitems is not None:
            self.maxitems = int(maxitems)
            if self.maxitems > 8:  # noqa: PLR2004
                self.bitmask = 15
            elif self.maxitems > 4:  # noqa: PLR2004
                self.bitmask = 7
            elif self.maxitems > 2:  # noqa: PLR2004
                self.bitmask = 3

        self.read_write: str | None = rw

    def set_read_write(self, mode: str | None) -> None:
        """Set read/write state. Used by simulator."""
        self.read_write = mode

    def status_block_changed(self, offset: int, length: int, previous: bytes) -> None:
        """Status block has changed."""
        # Does the notified range intersect us, if not then we don't care!
        intersection_start = max(offset, self.pos)
        intersection_end = min(offset + length, self.pos + self.length)
        if intersection_end - intersection_start <= 0:
            return

        old_value = self._get_value(previous)
        new_value = self.value

        # No reason to notify if there is no change
        if new_value == old_value:
            return

        _LOGGER.info(
            "Status block changed value of %s from %s to %s",
            self.tag,
            old_value,
            new_value,
        )

        self._on_change(self, old_value, new_value)

    def _get_raw_value(self, status_block: bytes | None = None) -> Any:
        """
        Get a value from the pack structure.

        Either use the initialized declaration or using the optionally
        supplied status_block (used by change notification).
        """
        if status_block is None:
            status_block = self.struct.status_block
        data = struct.unpack(
            self.format, status_block[self.pos : self.pos + self.length]
        )[0]
        if self.bitpos is not None:
            data = (data >> self.bitpos) & self.bitmask
        return data

    def _get_value(self, status_block: bytes | None = None) -> Any:
        data = self._get_raw_value(status_block)
        if self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE:
            data = data == 1
        elif self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            try:
                assert self.items is not None  # noqa: S101
                data = self.items[data]
            except IndexError:
                data = "Unknown"
                _LOGGER.debug(
                    "Enum accessor %s out-of-range for %s. Value is %s",
                    self.tag,
                    self.items,
                    data,
                )
        elif self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_TIME_TYPE:
            data = f"{int(data / 256):02}:{data % 256:02}"
        return data

    @property
    def value(self) -> Any:
        """Get a value from the pack structure using the initialized declaration."""
        return self._get_value()

    @property
    def raw_value(self) -> Any:
        """
        Get a raw integer value from the pack structure.

        Uses the initialized declaration.
        """
        return self._get_raw_value()

    async def async_set_value(
        self, newvalue: Any, *, always_send: bool = False
    ) -> None:
        """Set a value in the pack structure using the initialized declaration."""
        if self.read_write is None:
            raise AttributeError(
                GeckoConstants.EXCEPTION_MESSAGE_NOT_WRITABLE.format(self.tag)
            )

        if self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            try:
                assert self.items is not None  # noqa: S101
                newvalue = self.items.index(newvalue)
            except ValueError:
                _LOGGER.exception(
                    "Can't set %s to %s, the list(%s) doesn't contain it",
                    self,
                    newvalue,
                    self.items,
                )
                raise
        elif self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_TIME_TYPE:
            bits = newvalue.split(":")
            newvalue = (int(bits[0]) * 256) + (int(bits[1]) % 256)
        elif (
            self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BYTE_TYPE
            and isinstance(newvalue, str)
        ) or (
            self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_WORD_TYPE
            and isinstance(newvalue, str)
        ):
            newvalue = int(newvalue)
        elif (
            self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE
            and isinstance(newvalue, str)
        ):
            newvalue = newvalue.lower() == "true"

        # If it is a bitpos, then mask it with the existing value
        existing = struct.unpack(
            self.format, self.struct.status_block[self.pos : self.pos + self.length]
        )[0]
        if self.bitpos is not None:
            newvalue = (existing & ~(self.bitmask << self.bitpos)) | (
                (newvalue & self.bitmask) << self.bitpos
            )

        if newvalue == existing and not always_send:
            return

        _LOGGER.debug(
            "Accessor %s @ %s, %s setting value to %s, existing value was %s. "
            "Length is %d",
            self.tag,
            self.pos,
            self.accessor_type,
            newvalue,
            existing,
            self.length,
        )

        if self.direct_update:
            self.struct.replace_status_block_segment(
                self.pos, GeckoStructAccessor.pack_data(self.length, newvalue)
            )
        else:
            # We can't handle this here, we must delegate via the structure
            await self.struct.async_set_value(self.pos, self.length, newvalue)

    def diag_info(self) -> str:
        """Get diagnostic data for this accessor."""
        info = f"{self.tag} = {self.value}\n"
        info += "-------------------------------\n"
        info += f"Path: {self.path}\n"
        info += f"Pos: {self.pos}\n"
        if self.bitpos:
            info += f"Bitpos: {self.bitpos}\n"
        info += f"Len: {self.length}\n"
        info += f"Type: {self.accessor_type}"
        if self.accessor_type == GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE:
            info += f" one of {self.items}"
        info += "\n"
        info += f"Raw Value: {self.raw_value}"
        info += f" ({self.struct.status_block[self.pos : self.pos + self.length]})\n"
        info += f"R/W: {self.read_write}"
        return info

    def __repr__(self) -> str:
        """Get string representation."""
        return f"{self.path!r}: {self.value!r}"

    def __eq__(self, other: GeckoStructAccessor) -> bool:
        """Equality comparator."""
        return self.value == other.value


class GeckoByteStructAccessor(GeckoStructAccessor):
    """Structure accessor for bytes."""

    def __init__(
        self, struct_: GeckoAsyncStructure, path: str, pos: int, rw: str | None
    ) -> None:
        """Initialize the byte accessor."""
        super().__init__(
            struct_,
            path,
            pos,
            GeckoConstants.SPA_PACK_STRUCT_BYTE_TYPE,
            None,
            None,
            None,
            None,
            rw,
        )


class GeckoWordStructAccessor(GeckoStructAccessor):
    """Structure accessor for words."""

    def __init__(
        self, struct_: GeckoAsyncStructure, path: str, pos: int, rw: str | None
    ) -> None:
        """Initialize the word accessor."""
        super().__init__(
            struct_,
            path,
            pos,
            GeckoConstants.SPA_PACK_STRUCT_WORD_TYPE,
            None,
            None,
            None,
            None,
            rw,
        )


class GeckoTimeStructAccessor(GeckoStructAccessor):
    """Structure accessor for times."""

    def __init__(
        self, struct_: GeckoAsyncStructure, path: str, pos: int, rw: str | None
    ) -> None:
        """Initialize the time accessor."""
        super().__init__(
            struct_,
            path,
            pos,
            GeckoConstants.SPA_PACK_STRUCT_TIME_TYPE,
            None,
            None,
            None,
            None,
            rw,
        )


class GeckoBoolStructAccessor(GeckoStructAccessor):
    """Structure accessor to bools."""

    def __init__(
        self,
        struct_: GeckoAsyncStructure,
        path: str,
        pos: int,
        bitpos: int | None,
        rw: str | None,
    ) -> None:
        """Initialie the bool accessor."""
        super().__init__(
            struct_,
            path,
            pos,
            GeckoConstants.SPA_PACK_STRUCT_BOOL_TYPE,
            bitpos,
            None,
            None,
            None,
            rw,
        )


class GeckoEnumStructAccessor(GeckoStructAccessor):
    """Structure accessopr for enumerations."""

    def __init__(  # noqa: PLR0913
        self,
        struct_: GeckoAsyncStructure,
        path: str,
        pos: int,
        bitpos: int | None,
        items: str | list[str] | None,
        size: int | None,
        maxitems: int | None,
        rw: str | None,
    ) -> None:
        """Initialize the enum accessor."""
        super().__init__(
            struct_,
            path,
            pos,
            GeckoConstants.SPA_PACK_STRUCT_ENUM_TYPE,
            bitpos,
            items,
            size,
            maxitems,
            rw,
        )


class GeckoTempStructAccessor(GeckoWordStructAccessor):
    """
    Handle Gecko temperatures.

    The spa handles all temperatures in tenths of a degree farenheit offset
    from freezing. This class handles that in one place.
    """

    def _get_value(self, status_block: bytes | None = None) -> float:
        """Get the temperature."""
        # Internally, temp is in farenheight tenths, offset from freezing point
        temp: float = super()._get_value(status_block)
        units = self.struct.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        return temp / 18.0 if units == "C" else (temp + 320) / 10.0

    async def async_set_value(self, temp: float) -> None:
        """Set the temperature."""
        units = self.struct.accessors[GeckoConstants.KEY_TEMP_UNITS].value
        temp = float(temp) * 18.0 if units == "C" else float(temp) * 10.0 - 320
        await super().async_set_value(int(temp))
