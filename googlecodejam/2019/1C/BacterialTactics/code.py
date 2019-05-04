import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())

class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
    def clear(self):
        self.cache = {}

def nextBoard(G, r, c, move):
    newG = []
    for r1 in xrange(R):
        newG.append(list(G[r1*C:(r1+1)*C]))
    newG[r][c] = 'C'

    if move == 'V':
        return vmove(newG, r, c)
    else:
        return hmove(newG, r, c)

def toStr(G):
    return ''.join([
        ''.join(row) for row in G
    ])

def vmove(G, r, c):
    for nextR in xrange(r+1, R):
        if G[nextR][c] == '#':
            return None
        if G[nextR][c] == 'C':
            break
        G[nextR][c] = 'C'
    for nextR in xrange(r-1, -1, -1):
        if G[nextR][c] == '#':
            return None
        if G[nextR][c] == 'C':
            break
        G[nextR][c] = 'C'
    return toStr(G)

def hmove(G, r, c):
    for nextC in xrange(c+1, C):
        if G[r][nextC] == '#':
            return None
        if G[r][nextC] == 'C':
            break
        G[r][nextC] = 'C'
    for nextC in xrange(c-1, -1, -1):
        if G[r][nextC] == '#':
            return None
        if G[r][nextC] == 'C':
            break
        G[r][nextC] = 'C'
    return toStr(G)

@memoized
def solve(G):
    res = 0

    # Horizontal moves
    for r in xrange(R):
        lastRes = None
        for c in xrange(C):
            if G[r*C+c] != '.':
                lastRes = None
                continue
            if lastRes is None:
                newG = nextBoard(G, r, c, 'H')
                lastRes = newG is not None and solve(newG) == 0
            if lastRes:
                res += 1

    # Vertical moves
    for c in xrange(C):
        lastRes = None
        for r in xrange(R):
            if G[r*C+c] != '.':
                lastRes = None
                continue
            if lastRes is None:
                newG = nextBoard(G, r, c, 'V')
                lastRes = (newG is not None and solve(newG) == 0)
            if lastRes:
                res += 1
    return res

T = int(raw_input())
for testId in range(T):
    solve.clear()

    R, C = inputInts()

    G = ''
    for r in xrange(R):
        G += raw_input()

    print "Case #{:d}: {:d}".format(testId+1, solve(G))
