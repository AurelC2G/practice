import sys

sys.setrecursionlimit(1500)

facts = {0: 1}

def factorial(n):
    if n not in facts:
        facts[n] = n * factorial(n-1)
    return facts[n]

def solve(N, X, Y):
    if X == Y == 0:
        return 1.0

    # Fill all the layers before the target one
    nbLayers = (abs(X)+Y)/2
    N = N - (nbLayers + 2 * nbLayers * (nbLayers-1))
    if N <= 0:
        return 0.0

    # How many in the target layer?
    targetLayerSize = 1 + 4 * nbLayers
    if N >= targetLayerSize:
        return 1.0

    if X == 0:
        return 0.0

    # We need Y+1 diamonds on the target side. This means that, to fail,
    # we can have at most (nb in other side + Y) = 2*nbLayers+Y
    if N > 2*nbLayers + Y:
        return 1.0

    # What is the proba of not getting enough?
    if N < Y+1:
        return 0.0
    s = 0
    for i in range(Y+1):
        s = s + factorial(N) / (factorial(i) * factorial(N-i))
    return 1.0 - s/(2.0**N)

T = int(raw_input())
for testId in range(T):
    N, X, Y = map(int, raw_input().split())
    print "Case #{:d}: {:.10f}".format(testId+1, solve(N,X,Y))
