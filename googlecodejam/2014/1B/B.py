import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(1000)


T = int(raw_input())
for testId in range(T):
    A, B, K = map(int, raw_input().split())

    res = 0
    for i in range(A):
        for j in range(B):
            if (i&j) < K:
                res += 1

    print "Case #{:d}: {:d}".format(testId+1, res)
