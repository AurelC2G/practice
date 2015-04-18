import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

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

def modPow(b, e, mod):
    res = 1
    b = b % mod
    while e > 0:
        if e%2 == 1:
            res = (res * b) % mod
        e = e // 2
        b = (b * b) % mod
    return res

def inputInts():
    return map(int, raw_input().split())


T = int(raw_input())
for testId in range(T):
    line = raw_input().split()
    S = int(line[0])
    v = line[1]

    res = 0
    tot = int(v[0])
    for i in xrange(1, S+1):
        n = int(v[i])
        if n == 0:
            continue
        if i > tot:
            res += i - tot
            tot = i
        tot += n

    print "Case #{:d}: {:d}".format(testId+1, res)
