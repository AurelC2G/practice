import sys
import itertools
import math
import collections
import functools
import random

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

def firstPickFormula(k, L):
    l = int((math.sqrt(k*k + 4*L) - k)/2)
    return (l, L-l * (k+l))

def secondPickFormula(k, R):
    r = int((math.sqrt(k*k+2*k+4*R+1)-k-1)/2)
    return (r, R-r*r - (k+1)*r)

def solve(L, R):
    k = int((-1 + math.sqrt(1 + 8 * abs(L-R))) / 2)

    #print('initial:', L, R)
    eaten = int(k*(k+1)/2)
    if L > R:
        L -= eaten
    else:
        R -= eaten
    #print('after taking', k, 'times from a single pile:', L, R)

    if L >= R:
        #print('then will eat L first')
        (l, L) = firstPickFormula(k, L)
        (r, R) = secondPickFormula(k, R)
    else:
        #print('then will eat R first')
        (l, L) = secondPickFormula(k, L)
        (r, R) = firstPickFormula(k, R)
    #print('Eating', l, 'times from L and', r, 'times from right')

    return (k+l+r, L, R)

def simulate(L, R, Kans, Lans, Rans):
    L0 = L
    R0 = R
    if Lans < 0 or Rans < 0:
        print('Negative result for', L0, R0)
        return
    for k in range(1, Kans+1):
        if L >= R:
            L -= k
        else:
            R -= k
    if L != Lans or R != Rans:
        print('Simulation failed for', L0, R0)
    
T = int(input())
for testId in range(T):
    L, R = inputInts()

    (k, Lans, Rans) = solve(L, R)
    #simulate(L, R, k, Lans, Rans)
    print("Case #{:d}: {:d} {:d} {:d}".format(testId+1, k, Lans, Rans))
    #print()


#for bla in range(1000000):
#    L = random.randint(1, 10000)
#    R = random.randint(1, 10000)
#    (k, Lans, Rans) = solve(L, R)
#    simulate(L, R, k, Lans, Rans)
