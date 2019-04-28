import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(100000)

def inputInts():
    return map(int, raw_input().split())

def check(v1, v2):
    return abs(v1 - v2) <= K

def solve(start, end):
    if start == end:
        return 0

    # Find largest C in the interval
    mid = (end-start)/2
    bestC = start
    for i in xrange(start, end):
        if C[i] > C[bestC]:
            bestC = i
        elif C[i] == C[bestC] and abs(mid - i) < abs(mid-bestC):
            bestC = i

    # Sum up all intervals that exclude this max
    excluded = solve(start, bestC) + solve(bestC + 1, end)

    Cval = C[bestC]

    if D[bestC] > Cval + K:
        # Anything that includes bestC will fail because C is too weak
        return excluded

    # 3 states:
    # * we have found a D that is too high, any interval that includes that D would fail, so we stop
    # * all the D found so far are too low, so we keep extending the interval to find a valid one
    # * we have found a D that is good enough, now we can extend until we find one that is too high


    if check(Cval, D[bestC]):
        lastValidUpper = end-1
        for upper in xrange(bestC, end-1):
            if D[upper+1] > Cval + K:
                # would be too high, stop here
                lastValidUpper = upper
                break

        lastValidLower = start
        for lower in xrange(bestC, start, -1):
            if D[lower-1] > Cval + K:
                # would be too high, stop here
                lastValidLower = lower
                break

        # add all intervals from lastValidLower to lastValidUpper that include bestC
        return excluded + (bestC - lastValidLower + 1) * (lastValidUpper - bestC + 1)


    firstValidUpper = None
    lastValidUpper = end-1
    for upper in xrange(bestC, end-1):
        if D[upper+1] > Cval + K:
            # would be too high, stop here
            lastValidUpper = upper
            break
        if firstValidUpper is None and check(Cval, D[upper+1]):
            firstValidUpper = upper+1

    firstValidLower = None
    lastValidLower = start
    for lower in xrange(bestC, start, -1):
        if D[lower-1] > Cval + K:
            # would be too high, stop here
            lastValidLower = lower
            break
        if firstValidLower is None and check(Cval, D[lower-1]):
            firstValidLower = lower-1

    res = excluded
    if firstValidUpper is not None:
        # all intervals that have upper in the valid range, and any valid lower
        res += (lastValidUpper - firstValidUpper + 1) * (bestC - lastValidLower + 1)
    if firstValidLower is not None:
        # all intervals that have lower in the valid range, and any valid upper
        res += (firstValidLower - lastValidLower + 1) * (lastValidUpper - bestC + 1)

    if firstValidLower is not None and firstValidUpper is not None:
        # We double counted a bunch of intervals!
        res -= (lastValidUpper - firstValidUpper + 1) * (firstValidLower - lastValidLower + 1)

    return res

T = int(raw_input())
for testId in range(T):
    N, K = inputInts()
    C = inputInts()
    D = inputInts()

    print "Case #{:d}: {:d}".format(testId+1, solve(0, N))
