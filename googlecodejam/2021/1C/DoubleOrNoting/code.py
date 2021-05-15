import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

M = 65536

def myNot(d):
    return int(''.join([str(1 - int(c)) for c in '{0:b}'.format(d)]), 2)

T = int(input())
for testId in range(T):
    S, E = input().split()
    if len(S) > 8 or len(E) > 8:
        print("Case #{:d}: UNSUPPORTED".format(testId+1))
        continue

    S = int(S, 2)
    E = int(E, 2)

    distances = [None] * M
    distances[S] = 0
    openList = set([S])

    while len(openList) > 0:
        oldList = openList
        openList = set()

        for i in oldList:
            d = distances[i] + 1

            doubled = 2*i
            if doubled < M and (distances[doubled] is None or distances[doubled] > d):
                distances[doubled] = d
                openList.add(doubled)

            noted = myNot(i)
            if noted < M and (distances[noted] is None or distances[noted] > d):
                distances[noted] = d
                openList.add(noted)

    if distances[E] is None:
        print("Case #{:d}: IMPOSSIBLE".format(testId+1))
    else:
        print("Case #{:d}: {:d}".format(testId+1, distances[E]))
