import sys
import itertools
import math
import collections
import functools
from operator import itemgetter

sys.setrecursionlimit(100000)

def inputInts():
    return list(map(int, input().split()))


def solve(i):
    if len(parents[i]) == 0:
        return [F[i], F[i]]

    parentSolutions = [solve(p) for p in parents[i]]

    tots = [s[0] for s in parentSolutions]
    mins = [s[1] for s in parentSolutions]

    smallestIdx = min(enumerate(mins), key=itemgetter(1))[0]

    if F[i] > mins[smallestIdx]:
        tots[smallestIdx] += F[i] - mins[smallestIdx]
        mins[smallestIdx] = F[i]

    return [sum(tots), mins[smallestIdx]]

T = int(input())
for testId in range(T):
    N = int(input())
    F = inputInts()
    P = inputInts()

    parents = []
    for i in range(N):
        parents.append([])
    for i in range(N):
        child = P[i] - 1
        if child >= 0:
            parents[child].append(i)

    res = sum([solve(i)[0] for i in range(N) if P[i] == 0])

    print("Case #{:d}: {:d}".format(testId+1, res))
