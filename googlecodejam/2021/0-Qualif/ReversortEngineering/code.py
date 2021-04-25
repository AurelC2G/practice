import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

def solve(N, C):
    # If the end of our input list is sorted, then each iteration adds 1 to the cost.
    # The minimum cost we can have is thus N-1.
    if C < N-1:
        return None

    # If we revert the full sublist each time, the cost is N + (N-1) + ... + 2
    if C > N * (N+1) / 2 - 1:
        return None

    S = list(range(1, N+1))

    i = N-2
    while i >= 0:
        # How much cost can we get at this iteration?
        maxCostThisIteration = N - i

        # How many iterations left?
        remainingIterations = i

        if maxCostThisIteration + remainingIterations <= C:
            # Use the max cost here
            S[i:] = S[i:][::-1]
            C -= maxCostThisIteration
            i -= 1
        else:
            # we need to only use the C - remainingIterations
            lastToSwap = i + (C - remainingIterations - 1)
            S[i:lastToSwap+1] =  S[i:lastToSwap+1][::-1]
            break
    return S

T = int(input())
for testId in range(T):
    N, C = inputInts()
    res = solve(N, C)
    if res is None:
        print("Case #{:d}: IMPOSSIBLE".format(testId+1))
    else:
        print("Case #{:d}: {:s}".format(testId+1, ' '.join(map(str, res))))
