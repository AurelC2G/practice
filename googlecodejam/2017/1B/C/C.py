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

@memoized
def solve(currentCity, remainingDistance, currentSpeed):
    if currentCity == N-1:
        return 0

    distanceToNext = D[currentCity][currentCity+1]

    # if we keep the horse
    r1 = None
    if remainingDistance >= distanceToNext:
        r1 = solve(currentCity+1, remainingDistance-distanceToNext, currentSpeed) + distanceToNext/float(currentSpeed)

    # change horse
    r2 = None
    if horses[currentCity][0] >= distanceToNext:
        r2 = solve(currentCity+1, horses[currentCity][0]-distanceToNext, horses[currentCity][1]) + distanceToNext/float(horses[currentCity][1])

    if r1 is None:
        return r2
    if r2 is None:
        return r1
    return min(r1, r2)

T = int(raw_input())
for testId in range(T):
    solve.clear()
    N, Q = inputInts()

    horses = []
    for i in xrange(N):
        horses.append(inputInts())

    D = []
    for i in xrange(N):
        D.append(inputInts())

    U,V = inputInts()

    res = solve(0, horses[0][0], horses[0][1])

    print "Case #{:d}: {}".format(testId+1, res)
