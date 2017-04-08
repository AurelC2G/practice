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
    N, K = inputInts()

    currentBatch = 1

    intervals = {N: 1}
    lastSize = N
    while K >= currentBatch:
        lastSize = min(intervals.keys())

        newIntervals = {}
        for sz,count in intervals.iteritems():
            sz -= 1 # using one stall
            half = int(sz/2)
            if half not in newIntervals:
                newIntervals[half] = 0

            if sz % 2 == 0:
                newIntervals[half] += 2 * count
            else:
                newIntervals[half] += count
                if (half+1) not in newIntervals:
                    newIntervals[half+1] = 0
                newIntervals[half + 1] += count

        K -= currentBatch
        currentBatch *= 2
        intervals = newIntervals

    for sz in sorted(intervals.keys(), reverse=True):
        if K == 0:
            break
        lastSize = sz

        count = intervals[sz]
        if K > count:
            K -= count
        else:
            break

    lastSize -= 1 # Using that stall
    z = int(lastSize/2)
    y = z if lastSize % 2 == 0 else z+1

    print "Case #{:d}: {:d} {:d}".format(testId+1, y, z)
