import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))


T = int(input())
for testId in range(T):
    N, M = inputInts()

    res = 0

    print("Case #{:d}: {:d}".format(testId+1, res))
