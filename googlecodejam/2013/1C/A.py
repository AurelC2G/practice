import sys

sys.setrecursionlimit(1000)

def isConsonnant(c):
    return c not in ['a', 'e', 'i', 'o', 'u']

# [a, b] are the bounds for this search
def solve(a, b):
    # Look for a chunk of the right size within those bounds
    for i in range(a, b - n + 2):
        if chunks[i] < n:
            continue

        # we got one. add all the substrings that hold it
        # start in [a, i]
        # end in [i+n-1, b]
        res = (i - a + 1) * (b - (i+n-1) + 1)

        # remaining options don't contain this full chunk:

        # either they start later
        res += solve(i+1, b)

        # or they end earlier
        res += solve(a, i+n-2)
        
        return res

    # no chunk is long enough in this substring
    return 0



T = int(raw_input())
for testId in range(T):
    line = raw_input().split()
    S, n = line[0], int(line[1])
    L = len(S)

    # chunks[i] = Starting at S[i], how many consecutive consonnants?
    chunks = [0 for i in range(L)]
    if isConsonnant(S[L-1]):
        chunks[L-1] = 1
    for i in range(L-2, -1, -1):
        if isConsonnant(S[i]):
            chunks[i] = 1 + chunks[i+1]

    res = solve(0, L-1)
    print "Case #{:d}: {:d}".format(testId+1, res)
