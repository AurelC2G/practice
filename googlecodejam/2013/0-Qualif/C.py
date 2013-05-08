# Note: only works for C-small and C-large-1. Some other solution is
# required to solve C-large-2.

def isFair(i):
    iReverted = long(str(i)[::-1])
    return i == iReverted


# palindromes in [0,10^7]
palindromes = set()
for i in range(1, 1000):
    iStr = str(i)
    iRev = iStr[::-1]
    palindromes.add(long(iStr + iRev))
    for mid in range(10):
        palindromes.add(long(iStr + str(mid) + iRev))
for i in range(1, 10):
    palindromes.add(i)

squares = [x*x for x in palindromes]
fairAndSquares = filter(isFair, squares)

T = int(raw_input())
for t in xrange(T):
    A, B = map(long, raw_input().split())

    res = 0
    for i in fairAndSquares:
        if A <= i <= B:
            res = res + 1

    print "Case #{:d}: {:d}".format(t+1, res)
