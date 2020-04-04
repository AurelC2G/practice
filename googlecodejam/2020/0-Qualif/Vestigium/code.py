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
    N, = inputInts()

    M = []
    for i in range(N):
        M.append(inputInts())

    trace = 0
    r = 0
    c = 0

    for i in range(N):
        trace += M[i][i]
        if len(set(M[i])) < N:
            r += 1
        if len(set([M[j][i] for j in range(N)])) < N:
            c += 1

    print("Case #{:d}: {:d} {:d} {:d}".format(testId+1, trace, r, c))
