""" Observable class """

import logging
from typing import List, Callable, Any

_LOGGER = logging.getLogger(__name__)


class Observable:
    """Class to manage observables"""

    def __init__(self) -> None:
        self._observers: List[Callable[[Any, Any, Any], None]] = []

    def watch(self, observer: Callable[[Any, Any, Any], None]) -> None:
        """Add an observer to this observable class"""
        if observer in self._observers:
            _LOGGER.warning(
                "Observer %s already in list, not going to add again", observer
            )
            return
        self._observers.append(observer)

    def unwatch(self, observer: Callable[[Any, Any, Any], None]) -> None:
        """Remove an observer to this observable class"""
        self._observers.remove(observer)

    def unwatch_all(self):
        """Remove all observers on this observable class"""
        _LOGGER.debug("Remove all observers from %s", self)
        self._observers.clear()

    def _on_change(
        self, sender: Any = None, old_value: Any = None, new_value: Any = None
    ) -> None:
        """Trigger the change notification for all observers"""
        _LOGGER.debug(
            (
                f"{self.__class__.__name__} {sender} changed "
                f"from {old_value} to {new_value}"
            )
        )
        for observer in self._observers:
            observer(sender, old_value, new_value)

    @property
    def has_observers(self) -> bool:
        return len(self._observers) > 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} watched by={self._observers!r}"
