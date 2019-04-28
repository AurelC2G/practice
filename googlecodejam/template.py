import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())


T = int(raw_input())
for testId in range(T):
    N, M = inputInts()

    res = 0


    print "Case #{:d}: {:d}".format(testId+1, res)
