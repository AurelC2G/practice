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
    U = int(input())

    samples = []
    for i in range(10000):
        Q, R = input().split()
        # if Q == -1, we don't know M_i. Otherwise, M_i == Q_i.
        samples.append((int(Q), R))

    most_sig = {}
    all_letters = set()
    for s in samples:
        R = s[1]
        most_sig[R[0]] = most_sig.get(R[0], 0) + 1
        for c in R:
            all_letters.add(c)

    if len(all_letters) < 10:
        sys.exit(10)

    for c in all_letters:
        if c not in most_sig:
            most_sig[c] = 1e9

    D = [k for k, v in sorted(most_sig.items(), key=lambda item: -item[1])]

    print("Case #{:d}: {:s}".format(testId+1, ''.join(D)))
