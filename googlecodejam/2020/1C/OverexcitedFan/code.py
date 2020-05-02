import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

def solve(X, Y, M):
    if X == 0 and Y == 0:
        return 0

    i = 0
    for c in M:
        i += 1
        if c == 'N':
            Y += 1
        elif c == 'S':
            Y -= 1
        elif c == 'E':
            X += 1
        elif c == 'W':
            X -= 1

        if abs(X) + abs(Y) <= i:
            return i


T = int(input())
for testId in range(T):
    X, Y, M = input().split()

    res = solve(int(X), int(Y), M)
    if res is None:
        print("Case #{:d}: IMPOSSIBLE".format(testId+1))
    else:
        print("Case #{:d}: {:d}".format(testId+1, res))
