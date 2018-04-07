import sys
import itertools
import math
import collections
import functools

T = int(raw_input())
for testId in range(T):
    D,P = raw_input().split()
    D = int(D)

    cur = 1
    tot = 0
    for c in P:
        if c == 'C':
            cur *= 2
        else:
            tot += cur

    charges = [i for i in range(len(P)) if P[i] == 'C']
    moves = 0
    last = len(P) - 1
    cur /= 2
    while tot > D and len(charges):
        if charges[-1] == last:
            charges = charges[:-1]
            last -= 1
            cur /= 2
            continue

        boosted = last - charges[-1]
        if tot - boosted * cur >= D:
            steps = boosted
        else:
            steps = int(math.ceil((tot - D) / float(cur)))

        moves += steps
        charges[-1] += steps
        tot -= steps * cur

    if tot > D:
        print "Case #{:d}: IMPOSSIBLE".format(testId+1)
    else:
        print "Case #{:d}: {:d}".format(testId+1, moves)
