import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())

def solve(V):
    evens = sorted(V[0::2])
    odds = sorted(V[1::2])
    for i in xrange(len(evens)):
        if i < len(odds) and evens[i] > odds[i]:
            return 2*i
        if i+1 < len(evens) and odds[i] > evens[i+1]:
            return 2*i + 1

T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    V = inputInts()

    res = solve(V)
    if res is None:
        print "Case #{:d}: OK".format(testId+1)
    else:
        print "Case #{:d}: {:d}".format(testId+1, res)
