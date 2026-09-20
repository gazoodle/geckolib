"""GeckoLib utilities."""

from typing import TYPE_CHECKING, Any

from .async_command import AsyncCmd
from .shell import GeckoShell
from .simulator import GeckoSimulator
from .snapshot import GeckoSnapshot

if TYPE_CHECKING:
    from .cui import CUI

__all__ = ["CUI", "AsyncCmd", "GeckoShell", "GeckoSimulator", "GeckoSnapshot"]


def __getattr__(name: str) -> Any:
    """
    Import the CUI on demand.

    It needs curses, which isn't part of the standard library on Windows, so
    importing it eagerly would stop the rest of the library being used there.
    """
    if name == "CUI":
        from .cui import CUI

        return CUI
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)
