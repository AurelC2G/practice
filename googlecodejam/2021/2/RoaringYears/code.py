import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def nextRoaringForFixedLength(y, length):
    # All segments the same length
    nSegments = len(y) // length

    # Lowest possible value for the initial segment: the current digits
    a = int(y[0:length])

    for segI in range(nSegments):
        thisNumber = int(y[(segI*length):((segI+1)*length)])
        #print("\t", thisNumber, a+segI)
        if thisNumber > a + segI:
            # We have to bump the first digits to make this work
            a += 1
            break

    if a + nSegments >= 10 ** length:
        return None

    res = ''
    for segI in range(nSegments):
        res += str(a+segI)
    return int(res)

def nextRoaringForDifferentLengths(y, length, largeSegments):
    smallSegments = (len(y) - largeSegments * (length+1)) // length
    if smallSegments < 1:
        return None

    a = 10**length - smallSegments
    if a < 1:
        return None

    thisRes = ''
    for segI in range(smallSegments+largeSegments):
        thisRes += str(a+segI)
    thisRes = int(thisRes)
    if thisRes < int(y):
        return None

    return thisRes

def nextRoaringForInitialLength(y, length):
    res = []

    if len(y) % length == 0:
        res.append(nextRoaringForFixedLength(y, length))

    for largeSegments in range(1, 10, 2):
        res.append(nextRoaringForDifferentLengths(y, length, largeSegments))

    filtered = [r for r in res if r is not None]
    if len(filtered) == 0:
        return None
    return min(filtered)

def nextRoaring(y):
    #print("nextRoaring", y)
    bestOption = None
    for length in range(1, len(y)//2 + 1):
        thisOption = nextRoaringForInitialLength(y, length)
        #print("\ttry for length", length, "->", thisOption)
        if bestOption is None:
            bestOption = thisOption
        elif thisOption is not None and thisOption < bestOption:
            bestOption = thisOption

    if bestOption is not None:
        return bestOption

    #print('XXX RECURSE')
    return nextRoaring('0' + y)
            
T = int(input())
for testId in range(T):
    y = int(input())
    print("Case #{:d}: {:d}".format(testId+1, nextRoaring(str(y+1))))
