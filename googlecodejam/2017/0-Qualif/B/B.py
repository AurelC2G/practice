import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

T = int(raw_input())
for testId in range(T):
    N = [int(c) for c in raw_input()]

    flip = None
    for i in range(len(N) - 1, -1, -1): # XXX excludes N[0]
        if flip == i+1:
            # We have to decrement self.
            if N[i] == 0:
                flip = i
                continue
            else:
                N[i] = N[i] - 1

        if i > 0 and N[i] < N[i-1]:
            flip = i # Decrement N[i-1], everything at and after N[i] becomes 9

    if flip is not None:
        N[flip:] = [9] * (len(N) - flip)

    # Remove head zeros
    while N[0] == 0:
        N.pop(0)

    res = int(''.join(map(str, N)))
    print "Case #{:d}: {:d}".format(testId+1, res)
