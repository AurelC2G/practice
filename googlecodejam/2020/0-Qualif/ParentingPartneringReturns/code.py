import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))


def solve(A):
    busy = [0, 0]
    res = [None] * len(A)

    for task in sorted(A):
        if task[0] >= busy[0]:
            res[task[2]] = 'C'
            busy[0] = task[1]
        elif task[0] >= busy[1]:
            res[task[2]] = 'J'
            busy[1] = task[1]
        else:
            return 'IMPOSSIBLE'

    return ''.join(res)

T = int(input())
for testId in range(T):
    N, = inputInts()

    A = []
    for i in range(N):
        A.append(inputInts())
        A[i].append(i) # task index

    res = solve(A)

    print("Case #{:d}: {}".format(testId+1, res))
