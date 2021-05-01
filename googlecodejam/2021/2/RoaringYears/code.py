import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

#def nextRoaring(y):
#    for initialLength in range(1, len(y)//2):
#        curLen = initialLength
#        # Bounds for the initial segment
#        a = int(y[0:initialLength])
#        b = 10 ** initialLength - 1

#        i = curLen
#        while XXX:
            
            


    # At worst we can always solve this by adding one digit and have either:
    # 10...0 10...01 if even number of digits (e.g. 1000 1001)
    # (1) 2 3 4 5 6 7 8 9 10 11 12 13 if odd number of digits  (removing the leading digits as needed, with an odd number of single digits, but the most possible to still fit at least one pair)


def nextRoaring(y):   
    while True:
        if isRoaring(y):
            return y
        y += 1

def isRoaringWithStartingLength(s, initialLength):
    #print("length", initialLength)
    n = int(s[0:initialLength])
    pos = initialLength

    while pos < len(s):
        n += 1
        thisLen = len(str(n))
        #print("\t", n, thisLen)
        if pos + thisLen > len(s):
            #print("\ttoo long")
            return False
        if n != int(s[pos:(pos+thisLen)]):
            #print("\tmismatch", int(s[pos:(pos+thisLen)]))
            return False
        pos += thisLen

    return True
    
def isRoaring(y):
    s = str(y)

    for initialLength in range(1, len(s) // 2 + 1):
        if isRoaringWithStartingLength(s, initialLength):
            return True

    return False


T = int(input())
for testId in range(T):
    y = int(input())
    #y = [int(c) for c in input()]

    print("Case #{:d}: {:d}".format(testId+1, nextRoaring(y+1)))
