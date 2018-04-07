import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())


def TroubleSort(L):
    done = False
    while not done:
        done = True
        for i in xrange(len(L)-2):
            if L[i] > L[i+2]:
                done = False
                L[i],L[i+2] = L[i+2],L[i]
    return L

def solve(V):
    V = TroubleSort(V)
    for i in xrange(len(V)-1):
        if V[i] > V[i+1]:
            return i

T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    V = inputInts()

    res = solve(V)
    if res is None:
        print "Case #{:d}: OK".format(testId+1)
    else:
        print "Case #{:d}: {:d}".format(testId+1, res)
