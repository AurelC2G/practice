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
    N = input()
    hikers = []
    for n in xrange(N):
        D, H, M = inputInts()
        for h in xrange(H):
            revolutionTime = M+h
            hikers.append([(360 - D) * revolutionTime / 360.0, revolutionTime])

    # We will arrive immediately after one of the hikers. Which one?
    best = len(hikers)
    for h in hikers:
        # Let's arrive right after hiker h
        res = 0
        for i in hikers:
            if i[0] > h[0]:
                # this one is slower, we will meet him once
                res += 1
            elif i[0] < h[0]:
                # this one is faster, he might take us over
                remaining = h[0] - i[0]
                d = remaining / i[1]
                res += int(d)
        best = min(best, res)

    print "Case #{:d}: {:d}".format(testId+1, best)
