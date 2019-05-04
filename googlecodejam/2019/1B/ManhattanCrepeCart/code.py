import sys
import itertools
import math
import collections
import functools
import numpy

def inputInts():
    return map(int, raw_input().split())


T = int(raw_input())
for testId in range(T):
    P, Q = inputInts()

    G = numpy.zeros([Q+1, Q+1], int)
    for p in xrange(P):
        X, Y, D = raw_input().split()
        X = int(X)
        Y = int(Y)

        if D == 'W':
            for x in xrange(X):
                for y in xrange(Q+1):
                    G[x][y] += 1
        elif D == 'E':
            for x in xrange(X+1, Q+1):
                for y in xrange(Q+1):
                    G[x][y] += 1
        elif D == 'N':
            for x in xrange(Q+1):
                for y in xrange(Y+1, Q+1):
                    G[x][y] += 1
        elif D == 'S':
            for x in xrange(Q+1):
                for y in xrange(Y):
                    G[x][y] += 1

    best = G[0][0]
    res = [0, 0]
    for x in xrange(Q+1):
        for y in xrange(Q+1):
            if G[x][y] > best:
                res = [x, y]
                best = G[x][y]

    print "Case #{:d}: {:d} {:d}".format(testId+1, res[0], res[1])
