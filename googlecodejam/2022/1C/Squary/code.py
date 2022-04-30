import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))


def solve(cs, css, K):
    # Can we add between 1 and K elements such that:
    # (currentSum + x1 + x2 + ...)^2 = currentSquareSum + x1^2 + x2^2 + ...

    if cs == css:
        return [0]

    # Test set 1 only: K = 1
    if K != 1:
        return None # wrong answer

    # (cs + x)^2 = css + x^2
    # cs^2 + x^2 + 2x*cs = css + x^2
    # cs^2 + 2x*cs = css
    # x = (css - cs^2)/(2*cs)

    if cs == 0:
        return None

    res = (css - cs*cs)/(2*cs)
    if res != math.floor(res):
        return None
    return [int(res)]

T = int(input())
for testId in range(T):
    N, K = inputInts()
    l = inputInts()

    res = solve(sum(l), sum([i*i for i in l]), K)
    if res is None:
        print("Case #{:d}: IMPOSSIBLE".format(testId+1))
    else:
        print("Case #{:d}: {}".format(testId+1, " ".join(map(str, res))))

