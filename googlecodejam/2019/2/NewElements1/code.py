def inputInts():
    return map(int, raw_input().split())

from fractions import Fraction

T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    M = []
    for n in xrange(N):
        M.append(inputInts())

    breakpoints = set()
    for i in xrange(N):
        for j in xrange(i+1, N):
            if M[i][0] == M[j][0] or M[i][1] == M[j][1]:
                continue

            a = M[i][0] - M[j][0]
            b = M[j][1] - M[i][1]
            if a*b > 0:
                breakpoints.add(Fraction(a, b))

    print "Case #{:d}: {:d}".format(testId+1, len(breakpoints) + 1)
