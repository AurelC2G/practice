import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(100000)


def solve(C, F, X):
    # Final number of farms:
    f_end = max(0, int(math.ceil(X/C - 1.0 - 2.0/F)))

    time = 0.0
    for f in range(f_end):
       time += C / (2.0 + f * F)
    time += X / (2.0 + f_end * F)
    return time


T = int(raw_input())
for testId in range(T):
    C, F, X = map(float, raw_input().split())

    res = solve(C, F, X)

    print "Case #{:d}: {:.7f}".format(testId+1, res)
