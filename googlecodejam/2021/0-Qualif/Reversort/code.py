import sys
import itertools
import math
import collections
import functools

def inputInts():
    return list(map(int, input().split()))

def cost(L, N):
    res = 0
    for i in range(N-1):
        j = L.index(min(L[i:]))
        res += j - i + 1
        L[i:j+1] = L[i:j+1][::-1]
    return res

T = int(input())
for testId in range(T):
    N = int(input())
    L = inputInts()

    print("Case #{:d}: {:d}".format(testId+1, cost(L, N)))
