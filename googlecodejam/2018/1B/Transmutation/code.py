import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())

def consumeOne(what):
    if G[what]:
        G[what] -= 1
        return True

    if reserved[what]:
        # we are trying to produce this, there must be a loop
        return False

    Tr = transforms[what]

    if Tr[0] == what or Tr[1] == what:
        # this transformation just wastes resources
        return False

    reserved[what] = True
    out = consumeOne(Tr[0]) and consumeOne(Tr[1])
    reserved[what] = False

    return out

T = int(raw_input())
for testId in range(T):
    M = int(raw_input())

    transforms = []
    for i in xrange(M):
        a,b = inputInts()
        transforms.append([a-1, b-1])

    G = inputInts()

    reserved = [False for i in xrange(M)]

    res = 0
    while consumeOne(0):
        res += 1

    print "Case #{:d}: {:d}".format(testId+1, res)
