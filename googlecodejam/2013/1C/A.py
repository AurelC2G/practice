import sys

sys.setrecursionlimit(100000)

def isConsonnant(c):
    return c not in ['a', 'e', 'i', 'o', 'u']


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

    res = 0
    a = 0
    keepLooking = True
    
    # [a, L-1] are the bounds for this search
    while keepLooking:
        keepLooking = False

        # Look for a chunk of the right size within those bounds
        for i in range(a, L-1 - n + 2):
            if chunks[i] < n:
                continue
 
            # we got one. add all the substrings that hold it

            # first, the ones that start before
            # start in [a, i]
            # end in [i+n-1, L-1]
            res += (i - a + 1) * (L-1 - (i+n-1) + 1)

            # then, the ones that start in the middle of this chunk
            # start in [i+1, i + chunks[i] - n]
            # end in [start + n, L-1]
            # => SUM(L-1 - (start + n) + 2)
            res += (chunks[i] - n) * (L-1 + 2 - n) - (((i+chunks[i]-n)*(i+chunks[i]-n+1)/2) - (i*(i+1)/2))

            # remaining options don't contain this full chunk. Because we went through chunks in
            # ascending order, we know we don't have valid substring that contain chunks before
            # this one, hence they cannot end earlier, and have to start later:
            a = i + chunks[i] - n + 1
            keepLooking = True
            break

    print "Case #{:d}: {:d}".format(testId+1, res)
