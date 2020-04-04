import sys
import itertools
import math
import collections
import functools

def inputInts():
    return list(map(int, input().split()))


T = int(input())
for testId in range(T):
    S = list(map(int, input()))

    res = []
    lvl = 0
    for n in S:
        res.extend(['(' for n in range(n-lvl)])
        res.extend([')' for n in range(lvl-n)])
        res.append(str(n))
        lvl = n
    res.extend([')' for n in range(lvl)])

    print("Case #{:d}: {}".format(testId+1, ''.join(res)))
