import sys
import itertools
import math
import collections
import functools

def inputInts():
    return map(int, raw_input().split())


T = int(raw_input())
for testId in range(T):
    N, K = inputInts()
    C = inputInts()
    D = inputInts()

    res = 0
    for L in xrange(0, N):
        bestC = L
        bestD = L
        for R in xrange(L, N):
            if C[R] > C[bestC]:
                bestC = R
            if D[R] > D[bestD]:
                bestD = R
            if abs(C[bestC] - D[bestD]) <= K:
                res += 1

    print "Case #{:d}: {:d}".format(testId+1, res)
