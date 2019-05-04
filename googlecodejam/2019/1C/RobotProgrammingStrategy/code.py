import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())


WinningPlay = {
    'R': 'P',
    'P': 'S',
    'S': 'R',
}

def solve(C, i):
    enemyMoves = set([c[i % len(c)] for c in C])
    if len(enemyMoves) == 3:
        return None
    if len(enemyMoves) == 1:
        return [WinningPlay[next(iter(enemyMoves))]]

    # Play the move that doesn't lose to anyone, and beats some people
    for play in ['R', 'P', 'S']:
        if WinningPlay[play] in enemyMoves:
            continue
        remainingEnemies = [c for c in C if WinningPlay[c[i % len(c)]] != play]
        remainingRes = solve(remainingEnemies, i+1)
        if remainingRes is not None:
            return [play] + remainingRes

T = int(raw_input())
for testId in range(T):
    A = int(raw_input())

    C = []
    for i in xrange(A):
        C.append(raw_input())

    res = solve(C, 0)
    if res is None:
        print "Case #{:d}: IMPOSSIBLE".format(testId+1)
    else:
        print "Case #{:d}: {:s}".format(testId+1, ''.join(res))
