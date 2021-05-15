import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))


T = int(input())
for testId in range(T):
    N, K = inputInts()
    P = sorted(inputInts())

    singleTicketOptions = [0]
    doubleTicketOptions = [0]

    a = None
    for b in P:
        if a is None:
            # We can pick the digit immediately before b, and win for all digits <= b
            singleTicketOptions.append(b-1)
        elif b > a+1:
            # We are within the range [a,b].

            # We can capture the full interval by picking tickets a+1 and b-1
            doubleTicketOptions.append(b-a-1)

            # We could also just drop one ticket in that interval, and capture half of it
            singleTicketOptions.append((b-a)//2)

        a = b

    # We can also pick the digit immediately after the last and win for digits greater
    singleTicketOptions.append(K-a)

    # Prob 1: best 2 single ticket options
    singleTicketOptions = sorted(singleTicketOptions)
    chances1 = singleTicketOptions[-1] + singleTicketOptions[-2]

    # Prob 2: best 2 tickets option
    chances2 = max(doubleTicketOptions)

    print("Case #{:d}: {:f}".format(testId+1, max(chances1, chances2) / K))
