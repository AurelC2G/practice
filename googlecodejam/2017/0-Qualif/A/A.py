import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def solve(S, K):
    res = 0
    for i in xrange(len(S)):
        if S[i]:
            continue
        if i + K > len(S):
            return 'IMPOSSIBLE'
        res = res + 1
        S[i:i+K] = [not c for c in S[i:i+K]]
    return res
    
T = int(raw_input())
for testId in range(T):
    S, K = raw_input().split()
    res = solve([c == '+' for c in S], int(K))
    print "Case #{:d}: {}".format(testId+1, res)
