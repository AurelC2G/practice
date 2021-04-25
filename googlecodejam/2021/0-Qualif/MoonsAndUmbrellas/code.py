import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

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

@memoized
def solve(i, last):
    if i == len(S):
        return 0

    if S[i] == '?':
        return min(solveAux(i, 'C', last), solveAux(i, 'J', last))

    return solveAux(i, S[i], last)

def solveAux(i, val_i, val_i_m_1):
    return (Y if (val_i == 'C' and val_i_m_1 == 'J') else 0) + (X if (val_i == 'J' and val_i_m_1 == 'C') else 0) + solve(i+1, val_i)

T = int(input())
for testId in range(T):
    X, Y, S = input().split()
    X = int(X) #CJ
    Y = int(Y) #JC

    solve.clear()

    print("Case #{:d}: {:d}".format(testId+1, solve(0, '')))
