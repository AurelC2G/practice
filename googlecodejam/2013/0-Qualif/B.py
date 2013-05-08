# read in number of cases
T = int(raw_input())
for t in xrange(T):
    N, M = map(int,raw_input().split())

    g = []
    for i in xrange(N):
        tmp = map(int,raw_input().split())
        g.append(tmp)

    maxForRow = [0]*N
    maxForCol = [0]*M
    for i in range(N):
        for j in range(M):
            maxForRow[i] = max(maxForRow[i], g[i][j])
            maxForCol[j] = max(maxForCol[j], g[i][j])

    res = "YES"
    for i in range(N):
        for j in range(M):
            if maxForRow[i] > g[i][j] and maxForCol[j] > g[i][j]:
                res = "NO"
                break

    print "Case #{:d}: {:s}".format(t+1, res)
