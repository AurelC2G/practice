import sys

def check(row):
    seen = set()
    for i in row:
        seen.add(i)

    if '.' in seen:
        return 'NOPE'
    elif 'X' not in seen:
        return 'O'
    elif 'O' not in seen:
        return 'X'
    else:
        return 'DRAW'


# read in number of cases
T = int(raw_input())
for t in xrange(T):
    g = []
    for i in range(4):
        g.append(str(raw_input()))
    sys.stdin.readline()

    results = set()
    for i in range(4):
        results.add(check(g[i]))
        results.add(check([a[i] for a in g]))
    results.add(check([g[0][0], g[1][1], g[2][2], g[3][3]]))
    results.add(check([g[0][3], g[1][2], g[2][1], g[3][0]]))

    if 'X' in results:
        res = 'X won'
    elif 'O' in results:
        res = 'O won'
    elif 'NOPE' in results:
        res = 'Game has not completed'
    else:
        res = 'Draw'

    # output answer
    print "Case #{:d}: {:s}".format(t+1, res)
