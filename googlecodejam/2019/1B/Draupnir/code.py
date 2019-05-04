import sys
import itertools
import math
import collections
import functools
import numpy

def inputInts():
    return map(int, raw_input().split())

# For easy case, W=6 so we can just try in the first 6 days and get the answer
# For hard case. W=2. What to do?

def getAnswer(n):
    print n
    sys.stdout.flush()
    ans = int(raw_input())
    if ans == -1:
        sys.exit(1)
    return ans

a = numpy.array([
    [2, 1, 1, 1, 1, 1],
    [4, 2, 1, 1, 1, 1],
    [8, 2, 2, 1, 1, 1],
    [16, 4, 2, 2, 1, 1],
    [32, 4, 2, 2, 2, 1],
    [64, 8, 4, 2, 2, 2],
])

T, W = inputInts()
for testId in range(T):
    res = map(int, numpy.linalg.solve(a, numpy.array([
        getAnswer(1),
        getAnswer(2),
        getAnswer(3),
        getAnswer(4),
        getAnswer(5),
        getAnswer(6),
    ])))

    print " ".join(map(str, res))
    sys.stdout.flush()
    if int(raw_input()) == -1:
        sys.exit(1)
