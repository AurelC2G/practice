import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

def solve(D, A):
    for i in A:
        if len([j for j in A if j == i]) >= D:
            return 0

    if D == 2:
        return 1 # cut any in half

    if D == 3:
        for i in A:
            if A.count(i) == 2 and i < max(A):
                return 1

        # If there's a piece that twice the size of another, we can cut that in half
        for i in A:
            if A.count(2*i) > 0:
                return 1

        # Cut any piece in 3 equal parts
        return 2

    # not covered in test set 1
    return 0


T = int(input())
for testId in range(T):
    N, D = inputInts()
    print("Case #{:d}: {:d}".format(testId+1, solve(D, inputInts())))
