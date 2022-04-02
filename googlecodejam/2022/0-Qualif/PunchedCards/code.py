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
    R, C = inputInts()

    res = 0

    print("Case #{:d}:".format(testId+1))

    print('..' + '-'.join(['+'] * C))
    print('..' + '.'.join(['|'] * C))
    for r in range(R-1):
        print('-'.join(['+'] * (C+1)))
        print('.'.join(['|'] * (C+1)))
    print('-'.join(['+'] * (C+1)))
