import sqlalchemy.types as sqltypes

import re

class Enum(object):
    def __init__(self, *values):
        self.values = set(values)

    def __call__(self, s):
        if s not in self.values:
            raise TypeError("Invalid enum value")
        return s

    def description(self):
        return "Enum(%s)" % (', '.join(map(repr, self.values))

class Time(object):
    def __init__(self, resolution):
        self.resolution = resolution

    def __call__(self, s):
        """ Accepts a string and returns it as a float rounded
            down to the nearest multiple of self.resolution
        """
        # Add epsilon to ensure that we don't round down exact multiples
        x = float(s) + 2**(-10)
        return x - x % self.resolution

    def description(self):
        return "Time(%s)" % self.resolution
