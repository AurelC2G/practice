import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())

# For easy case, W=6 so we can just try in the first 6 days and get the answer
# For hard case. W=2. What to do?

def getAnswer():
    ans = int(raw_input())
    if ans == -1:
        sys.exit(1)
    return ans

T, W = inputInts()
for testId in range(T):
    print 7
    sys.stdout.flush()
    A7 = getAnswer()

    print 6
    sys.stdout.flush()
    A6 = getAnswer()
    R1 = int((A7 - A6) / 64)

    print 5
    sys.stdout.flush()
    A5 = getAnswer()

    print 4
    sys.stdout.flush()
    A4 = getAnswer()
    R5 = A5 - A4 - 16 * R1


    print 3
    sys.stdout.flush()
    A3 = getAnswer()

    print 2
    sys.stdout.flush()
    A2 = getAnswer()
    R3 = A3 - A2 - 4 * R1

    # 1: 2 1 1 1 1 1
    # 2: 4 2 1 1 1 1
    # 3: 8 2 2 1 1 1
    # 4: 16 4 2 2 1 1
    # 5: 32 4 2 2 2 1
    # 6: 64 8 4 2 2 2
    # 7: 128 8 4 2 2 2

    A6 - A5 = 32 R1 - 4 R2 - 2 R3 - R6


    A4 - A2 - 12 R1 - R3 = 2 R2 +R4

    A7 - A5 = xxx R1 + 4 R2 + 2 R3 + R6
    
    
    R2 = A6-A5-R1-R3
    
    R4 = A4-A3-R1-R2

    R6 = A2-3*R1-2*R2 -R3-R4-R5

    print " ".join(map(str, [R1, R2, R3, R4, R5, R6]))
    sys.stdout.flush()
    res = getAnswer()
