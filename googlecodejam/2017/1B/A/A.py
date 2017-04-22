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
    D, N = inputInts()
    maxTime = 0
    for n in xrange(N):
        start, speed = inputInts()
        time = (D - start) / float(speed)
        if time > maxTime:
            maxTime = time
    res = D / float(maxTime)

    print "Case #{:d}: {}".format(testId+1, res)
