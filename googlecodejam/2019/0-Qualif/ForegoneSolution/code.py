import sys
import itertools
import math
import collections
import functools

T = int(raw_input())
for testId in range(T):
    Nstr = raw_input()

    A = 0
    B = 0

    for i in Nstr:
        A *= 10
        B *= 10
        if i == '4':
            A += 2
            B += 2
        else:
            A += int(i)

    print "Case #{:d}: {:d} {:d}".format(testId+1, A, B)
