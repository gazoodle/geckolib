""" Automation interface support classes. """
import logging

from ..driver import Observable

_LOGGER = logging.getLogger(__name__)


class GeckoAutomationBase(Observable):
    """Base of all the automation helper classes"""

    def __init__(self, unique_id, name, parent_name, key):
        super().__init__()
        self._unique_id = unique_id
        self._name = name
        self._parent_name = parent_name
        self._key = key

    @property
    def name(self):
        """All automation items have a name"""
        return self._name

    @property
    def parent_name(self):
        """All automation items have a parent that has a name"""
        return self._parent_name

    @property
    def key(self):
        """Key into the spa pack"""
        return self._key

    @property
    def unique_id(self):
        """A unique id for the property"""
        return f"{self._unique_id}-{self._key}"

    @property
    def parent_unique_id(self):
        """The parent unique ID"""
        return f"{self._unique_id}"

    @property
    def monitor(self):
        """An abbreviated string for the monitor process in the shell"""
        return f"{self}"

    def __repr__(self):
        return f"{super().__repr__()}(name={self.name}, parent={self.parent_name} key={self.key})"


class GeckoAutomationFacadeBase(GeckoAutomationBase):
    """Base of all the automation helper classes from the Facade"""

    def __init__(self, facade, name, key):
        super().__init__(facade.unique_id, name, facade.name, key)
        self._facade = facade
        self._spa = facade._spa

    @property
    def facade(self):
        """Return the facade that is associated with this automation object"""
        return self._facade
