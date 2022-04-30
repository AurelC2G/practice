import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))


def solve(N, Sraw):
    letters = set([c for s in Sraw for c in s])

    starts_with = {}
    ends_with = {}
    only_has = {c: [] for c in letters}
    contained = {}

    for i in range(N):
        s = Sraw[i]
        s2 = [s[0]]
        for c in s:
            if c != s2[-1]:
                s2.append(c)

        asSet = set(s2)
        if len(asSet) != len(s2):
            return "IMPOSSIBLE"

        if len(s2) == 1:
            only_has[s2[0]].append(i)
            continue

        if s2[0] in starts_with:
            return "IMPOSSIBLE"
        if s2[-1] in ends_with:
            return "IMPOSSIBLE"
        starts_with[s2[0]] = i
        ends_with[s2[-1]] = i

        for c in s2[1:-1]:
            if c in contained:
                return "IMPOSSIBLE"
            contained[c] = i

    for c in contained.keys():
        if c in starts_with or c in ends_with or len(only_has[c]) > 0:
            return "IMPOSSIBLE"
        # can ignore "contained" from now on

    used = [False] * N
    chunks = []
    for firstUnused in range(N):
        if used[firstUnused]:
            continue
        
        chunk = Sraw[firstUnused]
        used[firstUnused] = True
        c = chunk[-1]
        while c is not None:
            if c in only_has:
                for i in only_has[c]:
                    if not used[i]:
                        chunk += Sraw[i]
                        used[i] = True
            if c in starts_with:
                i = starts_with[c]
                if used[i]:
                    return "IMPOSSIBLE"
                chunk += Sraw[i]
                used[i] = True
                c = chunk[-1]
            else:
                c = None
        # Complete before
        c = chunk[0][0]
        while c is not None:
            if c in only_has:
                for i in only_has[c]:
                    if not used[i]:
                        chunk = Sraw[i] + chunk
                        used[i] = True
            if c in ends_with:
                i = ends_with[c]
                if used[i]:
                    return "IMPOSSIBLE"
                chunk = Sraw[i] + chunk
                used[i] = True
                c = chunk[0]
            else:
                c = None
        chunks.append(chunk)

    return "".join(chunks)

T = int(input())
for testId in range(T):
    N = int(input())
    Sraw = input().split()
    print("Case #{:d}: {}".format(testId+1, solve(N, Sraw)))
