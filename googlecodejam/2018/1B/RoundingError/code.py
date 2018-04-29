import sys
import itertools
import math
import collections
import functools
import heapq

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())


T = int(raw_input())
for testId in range(T):
    N, L = inputInts()
    C = inputInts()

    # how much does each person contribute?
    pctPerOne = 100 / float(N)

    remains = []

    res = 0
    total = 0
    for c in C:
        total += c
        pct = c * pctPerOne
        rounded = int(round(pct))
        res += rounded

        if pct > rounded:
            remains.append(rounded - pct)

    heapq.heapify(remains)

    while total < N:
        if len(remains):
            pct = pctPerOne - heapq.heappop(remains)
        else:
            pct = pctPerOne

        rounded = int(round(pct))
        res += rounded
        total += 1
        if pct > rounded:
            heapq.heappush(remains, rounded - pct)

    print "Case #{:d}: {:d}".format(testId+1, res)
