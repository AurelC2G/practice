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

def inputInts():
    return map(int, raw_input().split())


G = {
    '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
    'i': {'1': 'i', 'i': '1', 'j': 'k', 'k': 'j'},
    'j': {'1': 'j', 'i': 'k', 'j': '1', 'k': 'i'},
    'k': {'1': 'k', 'i': 'j', 'j': 'i', 'k': '1'},
}
S = {
    '1': {'1': 1, 'i': 1, 'j': 1, 'k': 1},
    'i': {'1': 1, 'i': -1, 'j': 1, 'k': -1},
    'j': {'1': 1, 'i': -1, 'j': -1, 'k': 1},
    'k': {'1': 1, 'i': 1, 'j': -1, 'k': -1},
}

def mul(a, b):
    la, signa = a
    lb, signb = b
    return [G[la][lb], signa * signb * S[la][lb]]

def compute(s):
    v = ['1', 1]
    for c in s:
        v = mul(v, [c, 1])
    return v

def myPow(v, e):
    res = ['1', 1]
    for i in xrange(e % 4):
        res = mul(res, v)
    return res

def solve(L, X, s):
    patternVal = compute(s)

    # repeating the same pattern X can only yield:
    # * if X = 1, only 1
    # * else, X, -1, -X and 
    # Every 4 repeats of s, we end up at -1. So we don't need that many.

    

    
    # How many repetitions of the full pattern before the first cut?
    #for repeat0 in xrange(X):
    #    # output of those repetitions?
    #    prev =

    for i in xrange(L*X):

T = int(raw_input())
for testId in range(T):
    L, X = inputInts()
    s = raw_input()

    if solve(L, X, s):
        res = "YES"
    else:
        res = "NO"
    
    print "Case #{:d}: {:s}".format(testId+1, res)
