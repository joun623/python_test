from collections import abc
import keyword

class FrozenJSON:
    """A read-only facade for navigating a JSON-like object
       using attribute notation
    """

    def __new__(cls, arg):
        """!!class method!!"""
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])


from osconfeed import load

raw_feed = load()
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.speakers))
print(sorted(feed.Schedule.keys()))
for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))

