"""Automation interface support classes."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from geckolib.driver import Observable

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade

_LOGGER = logging.getLogger(__name__)


class GeckoAutomationBase(Observable):
    """Base of all the automation helper classes."""

    def __init__(self, unique_id: str, name: str, parent_name: str, key: str) -> None:
        """Initialize the base class."""
        super().__init__()
        self._unique_id: str = unique_id
        self._name: str = name
        self._parent_name: str = parent_name
        self._key: str = key
        self._is_available: bool = False
        self.mapping = {}
        self.reverse = {}

    def set_mapping(self, mapping: dict) -> None:
        """Set the mapping and the reverse mapping helpers."""
        self.mapping = mapping
        self.reverse = {v: k for k, v in self.mapping.items()}

    @property
    def name(self) -> str:
        """All automation items have a name."""
        return self._name

    @property
    def parent_name(self) -> str:
        """All automation items have a parent that has a name."""
        return self._parent_name

    @property
    def key(self) -> str:
        """Key into the spa pack."""
        return self._key

    @property
    def unique_id(self) -> str:
        """A unique id for the property."""
        return f"{self._unique_id}-{self._key}"

    @property
    def parent_unique_id(self) -> str:
        """The parent unique ID."""
        return f"{self._unique_id}"

    @property
    def monitor(self) -> str:
        """An abbreviated string for the monitor process in the shell."""
        return f"{self}"

    @property
    def is_available(self) -> bool:
        """Get the availability of this item."""
        return self._is_available

    def set_availability(self, *, is_available: bool) -> None:
        """Set the availability of this item."""
        self._is_available = is_available

    def __repr__(self) -> str:
        """Get string representation."""
        return (
            f"{super().__repr__()}(name={self.name},"
            f" parent={self.parent_name} key={self.key})"
        )


class GeckoAutomationFacadeBase(GeckoAutomationBase):
    """Base of all the automation helper classes from the Facade."""

    def __init__(self, facade: GeckoAsyncFacade, name: str, key: str) -> None:
        """Initialize the facade base class."""
        super().__init__(facade.unique_id, name, facade.name, key)
        self._facade = facade
        self._spa = facade.spa

    @property
    def facade(self) -> GeckoAsyncFacade:
        """Return the facade that is associated with this automation object."""
        return self._facade
