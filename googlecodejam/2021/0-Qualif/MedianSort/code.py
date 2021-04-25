import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

def debug(msg, *args):
    print(msg.format(*args), file=sys.stderr)

def output(msg, *args):
    print(msg.format(*args))
    sys.stdout.flush()

def question(a, b, c):
    output('{:d} {:d} {:d}', a, b, c)
    ans = int(input())
    if ans == -1:
        raise Exception('Too many questions')
    
    #debug('Question: {:d} {:d} {:d} --> {:d}', a, b, c, ans)
    return ans

def answer(res):
    output('{:s}', ' '.join(map(str, res)))
    ans = int(input())
    if ans != 1:
        raise Exception('Wrong answer')
    #debug('Correct answer!')

T, N, Q = inputInts()
for testId in range(T):
    res = [1, 2]
    while len(res) < N:
        #debug('[{:s}]', ' '.join(map(str, res)))
        i = len(res)+1

        lowerBound = None
        upperBound = None

        while True:
            #debug('Bounds: {:d} {:d}', lowerBound or -1, upperBound or -1)

            third = ((upperBound or len(res)) - (lowerBound or 0)) / 3.
            if third < 1:
                a = (lowerBound or 0)
                b = a + 1
            else:
                a = int((lowerBound or 0) + third)
                b = int((lowerBound or 0) + 2 * third)
            #debug('Third = {:f}, a={:d}, b={:d}', third, a, b)


            mid = question(res[a], res[b], i)

            if mid == res[a]:
                upperBound = a
            elif mid == res[b]:
                lowerBound = b
            else:
                lowerBound = a
                upperBound = b

            if upperBound == 0:
                res.insert(0, i)
                break

            if lowerBound == len(res)-1:
                res.append(i)
                break

            if lowerBound is not None and upperBound is not None and lowerBound == upperBound - 1:
                res.insert(upperBound, i)
                break

    answer(res)
