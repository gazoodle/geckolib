""" Automation interface support classes. """


class GeckoAutomationBase:
    """ Base of all the automation helper classes """

    def __init__(self, facade, name):
        self._facade = facade
        self._spa = facade._spa
        self._name = name

    @property
    def name(self):
        """ All automation items have a name """
        return self._name
