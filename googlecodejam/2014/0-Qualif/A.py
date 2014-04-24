import sys
import itertools
import math
import collections
import functools

T = int(raw_input())
for testId in range(T):
    ans = int(raw_input()) - 1
    for i in range(4):
        row = map(int, raw_input().split())
        if i == ans:
            options = row

    res = []
    ans = int(raw_input()) - 1
    for i in range(4):
        row = map(int, raw_input().split())
        if i == ans:
            for val in row:
                if val in options:
                    res.append(val)

    if len(res) == 1:
        print "Case #{:d}: {:d}".format(testId+1, res[0])
    elif len(res) == 0:
        print "Case #{:d}: Volunteer cheated!".format(testId+1)
    else:
        print "Case #{:d}: Bad magician!".format(testId+1)
