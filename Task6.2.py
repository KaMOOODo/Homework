"""Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys."""
from collections import deque


class HistoryDict:

    __history = deque() #was changed after my own implementation

    def __init__(self, d):
        self.d = d

    def set_value(self, key, value):
        self.d[key] = value
        self.__history.appendleft(key) #was changed after my own implementation

    def get_history(self):
        print(self.__history)
        return self.__history

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("foo1", 1)
d.set_value("bar1", 1)

d.get_history()

# ["bar"]