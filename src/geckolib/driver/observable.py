""" Observable class """


class Observable:
    """Class to manage observables"""

    def __init__(self):
        self.observers = []

    def watch(self, observer):
        """ Add an observer to this observable class """
        self.observers.append(observer)

    def unwatch(self, observer):
        """ Remove an observer to this observable class """
        self.observers.remove(observer)

    def _on_change(self, sender, old_value, new_value):
        """ Trigger the change notification for all observers """
        for observer in self.observers:
            observer(sender, old_value, new_value)

    @property
    def has_observers(self):
        return self.observers
