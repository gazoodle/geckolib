"""Observable class."""

import logging
from collections.abc import Callable
from typing import Any

_LOGGER = logging.getLogger(__name__)


class Observable:
    """
    Class to manage observables.

    Any class derived from this will support the ability to watch for changes.
    """

    def __init__(self) -> None:
        """Initialize the observable."""
        self._observers: list[Callable[[Any, Any, Any], None]] = []

    def watch(self, observer: Callable[[Any, Any, Any], None]) -> None:
        """Add an observer to this observable class."""
        if observer in self._observers:
            _LOGGER.warning(
                "Observer %s already in list, not going to add again", observer
            )
            return
        self._observers.append(observer)

    def unwatch(self, observer: Callable[[Any, Any, Any], None]) -> None:
        """Remove an observer to this observable class."""
        self._observers.remove(observer)

    def unwatch_all(self) -> None:
        """Remove all observers on this observable class."""
        _LOGGER.debug("Remove all observers from %r", self)
        self._observers.clear()

    def _on_change(
        self, sender: Any = None, old_value: Any = None, new_value: Any = None
    ) -> None:
        """Trigger the change notification for all observers."""
        _LOGGER.debug(
            f"{self.__class__.__name__} {sender} changed "  # noqa: G004
            f"from {old_value} to {new_value}"
        )
        for observer in self._observers:
            observer(sender, old_value, new_value)

    @property
    def has_observers(self) -> bool:
        """Determine if this has observers."""
        return len(self._observers) > 0

    def __repr__(self) -> str:
        """Get string reprosentation."""
        return f"{self.__class__.__name__} watched by={self._observers!r}"
