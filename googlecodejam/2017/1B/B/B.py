import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)


def solveAux(counts):
    res = []

    first = sorted(counts.items(), key=lambda x:-x[1])[0][0]
    counts[first] -= 1
    res.append(first)

    last = first
    while sum(counts.values()) > 0:
        idx = [i for i in counts.keys() if i != last]

        if counts['R'] == counts['B'] and counts['R'] == counts['Y']:
            if first == last:
                res.append((idx[0] + last + idx[1]) * counts['R'])
            else:
                third = [i for i in idx if i != first][0]
                res.append((first + last + third) * counts['R'])
            return res

        if counts[idx[0]] > counts[idx[1]]:
            res.append(idx[0])
            counts[idx[0]] -= 1
            last = idx[0]
        elif counts[idx[1]] > counts[idx[0]]:
            res.append(idx[1])
            counts[idx[1]] -= 1
            last = idx[1]
        elif counts[idx[0]] + counts[idx[1]] == 0:
            return None
        elif idx[0] == first or counts[idx[0]] == 0:
            res.append(idx[1])
            counts[idx[1]] -= 1
            last = idx[1]
        else:
            res.append(idx[0])
            counts[idx[0]] -= 1
            last = idx[0]

    if first == last:
        return None
    return res

def inputInts():
    return map(int, raw_input().split())

def solve(R, O, Y, G, B, V):
    if G == R and B+Y == 0:
        return 'GR' * G
    if G >= R and G > 0:
        return 'IMPOSSIBLE'
    R -= G

    if O == B and R+Y == 0:
        return 'OB' * O
    if O >= B and O > 0:
        return 'IMPOSSIBLE'
    B -= O

    if V == Y and R+B == 0:
        return 'VY' * V
    if V >= Y and V > 0:
        return 'IMPOSSIBLE'
    Y -= V

    res = solveAux({'R': R, 'Y': Y, 'B': B})
    if res is None:
        return 'IMPOSSIBLE'

    realRes = []
    for c in res:
        if c == 'R' and G > 0:
            for i in xrange(G):
                realRes.append('RG')
            realRes.append('R')
            G = 0
        elif c == 'B' and O > 0:
            for i in xrange(O):
                realRes.append('BO')
            realRes.append('B')
            O = 0
        elif c == 'Y' and V > 0:
            for i in xrange(V):
                realRes.append('YV')
            realRes.append('Y')
            V = 0
        else:
            realRes.append(c)
    return ''.join(realRes)

T = int(raw_input())
for testId in range(T):
    N, R, O, Y, G, B, V = inputInts()
    print "Case #{:d}: {}".format(testId+1, solve(R, O, Y, G, B, V))
