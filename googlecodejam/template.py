import sys
import itertools
import math

sys.setrecursionlimit(1000)

T = int(raw_input())
for testId in range(T):
    N, M = map(int, raw_input().split())

    res = 0


    print "Case #{:d}: {:d}".format(testId+1, res)
