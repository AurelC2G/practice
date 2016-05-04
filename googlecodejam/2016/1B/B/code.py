import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

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

def score(C, J):
    return abs(int(C) - int(J))

@memoized
def solve(C, J, higher):
    C = list(C)
    J = list(J)
    n = len(C)
    for i in xrange(n):
        if C[i] != '?' and J[i] != '?':
            if higher == 0 and C[i] != J[i]:
                if C[i] > J[i]:
                    higher = -1
                else:
                    higher = 1
        elif C[i] != '?':
            if higher == -1:
                # The previous digits of C are higher, so we need J as high as possible
                J[i] = '9'
            elif higher == 1:
                # The previous digits of J are higher, so we need J as low as possible
                J[i] = '0'
            elif i == n-1:
                J[i] = C[i]
            else:
                subC = ''.join(C[i+1:])
                subJ = ''.join(J[i+1:])

                best = 1e30
                if C[i] > '0':
                    (C[i+1:],J[i+1:]) = solve(subC, subJ, -1)
                    J[i] = str(int(C[i]) - 1)
                    best = score(''.join(C[i:]), ''.join(J[i:]))

                (C2,J2) = solve(subC, subJ, 0)
                s = score(''.join(C2), ''.join(J2))
                if s < best:
                    J[i] = C[i]
                    C[i+1:] = C2
                    J[i+1:] = J2
                    best = s

                if C[i] < '9':
                    thisJ = str(int(C[i]) + 1)
                    (C2,J2) = solve(subC, subJ, 1)
                    s = score(C[i] + ''.join(C2), thisJ + ''.join(J2))
                    if s < best:
                        J[i] = thisJ
                        C[i+1:] = C2
                        J[i+1:] = J2
                        best = s

                return (C, J)
        elif J[i] != '?':
            if higher == -1:
                # The previous digits of C are higher, so we need C as low as possible
                C[i] = '0'
            elif higher == 1:
                # The previous digits of J are higher, so we need C as high as possible
                C[i] = '9'
            elif i == n-1:
                C[i] = J[i]
            else:
                subC = ''.join(C[i+1:])
                subJ = ''.join(J[i+1:])

                best = 1e30
                if J[i] > '0':
                    (C[i+1:],J[i+1:]) = solve(subC, subJ, 1)
                    C[i] = str(int(J[i]) - 1)
                    best = score(''.join(C[i:]), ''.join(J[i:]))

                (C2,J2) = solve(subC, subJ, 0)
                s = score(''.join(C2), ''.join(J2))
                if s < best:
                    C[i] = J[i]
                    C[i+1:] = C2
                    J[i+1:] = J2
                    best = s

                if J[i] < '9':
                    thisC = str(int(J[i]) + 1)
                    (C2,J2) = solve(subC, subJ, -1)
                    s = score(thisC + ''.join(C2), J[i] + ''.join(J2))
                    if s < best:
                        C[i] = thisC
                        C[i+1:] = C2
                        J[i+1:] = J2
                        best = s

                return (C, J)
        else:
            # Both are unknown!
            if higher == -1:
                C[i] = '0'
                J[i] = '9'
            elif higher == 1:
                C[i] = '9'
                J[i] = '0'
            elif i == n-1:
                # Last digit, we can just picks 0s
                C[i] = '0'
                J[i] = '0'
            else:
                # Options are (0,0), (0,1), (1,0)
                subC = ''.join(C[i+1:])
                subJ = ''.join(J[i+1:])

                (C[i+1:],J[i+1:]) = solve(subC, subJ, 0)
                C[i] = '0'
                J[i] = '0'
                best = score(''.join(C[i:]), ''.join(J[i:]))

                (C2,J2) = solve(subC, subJ, 1)
                s = score('0' + ''.join(C2), '1' + ''.join(J2))
                if s < best:
                    C[i] = '0'
                    J[i] = '1'
                    C[i+1:] = C2
                    J[i+1:] = J2
                    best = s

                (C2,J2) = solve(subC, subJ, -1)
                s = score('1' + ''.join(C2), '0' + ''.join(J2))
                if s < best:
                    C[i] = '1'
                    J[i] = '0'
                    C[i+1:] = C2
                    J[i+1:] = J2
                    best = s

                return (C, J)

    return (C, J)

T = int(raw_input())
for testId in range(T):
    C, J = raw_input().split()
    n = len(C)

    (C,J) = solve(C, J, 0)
            
    print "Case #{:d}: {} {}".format(testId+1, ''.join(C), ''.join(J))
