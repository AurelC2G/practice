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
    N = int(input())
    S = sorted(inputInts())

    cur = 0
    curN = 0
    for s in S:
        if s > cur:
            cur += 1
            curN += 1

    print("Case #{:d}: {:d}".format(testId+1, curN))
