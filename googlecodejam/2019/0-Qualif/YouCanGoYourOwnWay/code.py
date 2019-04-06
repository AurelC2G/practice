import sys
import itertools
import math
import collections
import functools

T = int(raw_input())
for testId in range(T):
    raw_input()
    P = raw_input()

    res = []
    for c in P:
        if c == 'E':
            res.append('S')
        else:
            res.append('E')

    print "Case #{:d}: {:s}".format(testId+1, ''.join(res))
