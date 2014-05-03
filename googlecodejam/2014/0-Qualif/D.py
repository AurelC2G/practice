import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(1000)

def deceitful(b1, b2):
    b1 = collections.deque(b1)
    b2 = collections.deque(b2)
    points = 0

    while len(b1):
        if b1[0] < b2[0]:
            # If we cannot beat any ennemi, we have to discard our worst
            b1.popleft()
            b2.pop()
        else:
            # We use our worst (pretending it's the best) and he uses his worst
            points = points + 1
            b1.popleft()
            b2.popleft()
    return points

def normal(b1, b2):
    e2 = N-1
    points = 0

    for i in range(N):
        if b1[N-1-i] > b2[e2]:
            points += 1
        else:
            e2 -= 1
    return points


T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    
    b1 = sorted(map(float, raw_input().split()))
    b2 = sorted(map(float, raw_input().split()))

    print "Case #{:d}: {:d} {:d}".format(testId+1, deceitful(b1, b2), normal(b1, b2))
