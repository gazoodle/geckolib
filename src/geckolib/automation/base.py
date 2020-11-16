""" Automation interface support classes. """

from ..driver import Observable


class GeckoAutomationBase(Observable):
    """ Base of all the automation helper classes """

    def __init__(self, facade, name, key):
        super().__init__()
        self._facade = facade
        self._spa = facade._spa
        self._name = name
        self._key = key

    @property
    def name(self):
        """ All automation items have a name """
        return self._name

    @property
    def unique_id(self):
        """ A unique id for the property """
        return f"{self._facade.unique_id}-{self._key}"

    @property
    def facade(self):
        """ Return the facade that is associated with this automation object """
        return self._facade
