import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(1000)

class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
    def clear(self):
        self.cache = {}




T = int(raw_input())
for testId in range(T):
    N, M = map(int, raw_input().split())

    res = 0


    print "Case #{:d}: {:d}".format(testId+1, res)
