import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return map(int, raw_input().split())

T = int(raw_input())
for testId in range(T):
    A = int(raw_input())

    grid = [[False for i in xrange(1001)] for j in xrange(1001)]
    dimX = int(math.sqrt(A))
    if dimX < 3:
        dimX = 3
    dimY = int(math.ceil(A/float(dimX)))
    if dimY < 3:
        dimY = 3
    if dimX * dimY < A:
        sys.stderr.write("Wrong dimensions: {}x{} < {}".format(dimX, dimY, A))
        sys.exit(1)

    sys.stderr.write("Dimensions: {}x{} >= {}\n".format(dimX, dimY, A))

    curX = 1
    curY = 1
    iterations = 0
    while True:
        if grid[curX][curY]:
            if curX == dimX:
                curX = 1
                curY += 1
            else:
                curX += 1
            continue

        a,b = min(curX+1, dimX-1), min(curY+1, dimY-1)

        #for i in xrange(7):
        #    sys.stderr.write(' '.join(map(str, map(int, grid[i][0:6]))))
        #    sys.stderr.write('\n')
        #sys.stderr.write("Target: {} {}\n".format(curX, curY))
        #sys.stderr.write("Dig: {} {}\n".format(a, b))

        print "{:d} {:d}".format(a, b)
        iterations += 1
        sys.stdout.flush()

        N, M = inputInts()
        if N == -1 and M == -1:
            sys.exit(0)
        if N == 0 and M == 0:
            sys.stderr.write("Finished test case (A={}) in {} iterations\n".format(A, iterations))
            break

        grid[N][M] = True
