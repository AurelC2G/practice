import sys
import itertools
import math
import collections
import functools

def asList(s):
    out = []
    prev = False
    count = 0
    for c in s:
        if c != prev:
            if prev != False:
                out.append((prev, count))
            prev = c
            count = 0
        count += 1
    if count > 0:
        out.append((prev, count))
    return out

def solve(v):
    lengths = set()
    for l in v:
        lengths.add(len(l))
    if len(lengths) != 1:
        return "Fegla Won"

    moves = 0
    l = len(v[0])
    for i in range(l):
        # Make sure it's the same letter for all
        counts = []
        letters = set()
        for it in v:
            letters.add(it[i][0])
            counts.append(it[i][1])
        if len(letters) != 1:
            return "Fegla Won"

        avg = int(round(sum(counts) / float(len(counts))))
        for c in counts:
            moves += abs(avg - c)
        
    return str(moves)
        


T = int(raw_input())
for testId in range(T):
    N = int(raw_input())

    v = []
    for i in range(N):
        v.append(asList(raw_input()))

    print "Case #{:d}: {:s}".format(testId+1, solve(v))
