import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

cache = {}
class memoized(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        key = list(*args)
        key[0] = tuple(key[0])
        if key in cache:
            return cache[key]
        else:
            value = self.func(*args)
            cache[key] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

def inputInts():
    return map(int, raw_input().split())

def solve(taken, cur, likesPrev, first):
    if not likesPrev:
        if taken[F[cur]]:
            if F[cur] == first:
                return 1
            else:
                return 0

        taken[cur] = True
        thisOne = 1 + solve(taken, F[cur], F[F[cur]] == cur, first)
        taken[cur] = False
        if thisOne == 1:
            # Couldn't add F[cur] (it couldn't find any friend), so we cannot add cur either
            return 0
        return thisOne

    # The current node already likes the previous one. We can put anyone next.
    taken[cur] = True
    best = 1
    for i in xrange(N):
        if taken[i]:
            continue
        thisOne = 1 + solve(taken, i, F[i] == cur, first)
        if thisOne > best:
            best = thisOne
    taken[cur] = False

    return best

T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    F = [i-1 for i in inputInts()]

    cache = {}

    res = 0
    for i in xrange(N):
        thisOne = solve([False for j in xrange(N)], i, False, i)
        if thisOne > res:
            res = thisOne

    print "Case #{:d}: {:d}".format(testId+1, res)
