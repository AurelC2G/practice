def inputInts():
    return map(int, raw_input().split())

T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    M = []
    for n in xrange(N):
        M.append(inputInts())

    breakpoints = []
    mult = 1
    for i in xrange(N):
        for j in xrange(i+1, N):
            if M[i][0] == M[j][0] or M[i][1] == M[j][1]:
                continue

            newVal = M[i][0] - M[j][0]
            newMult = M[j][1] - M[i][1]
            if newVal * newMult <= 0:
                continue

            breakpoints = [x * newMult for x in breakpoints]
            breakpoints.append(mult * (M[i][0] - M[j][0]))
            mult *= newMult

            # That code is equivalent to the following, but without float precision issues
            #bp = float(M[i][0] - M[j][0]) / float(M[j][1] - M[i][1])
            #if bp > 0:
            #    breakpoints.add(bp)

        breakpoints = set(breakpoints)

    print "Case #{:d}: {:d}".format(testId+1, len(breakpoints) + 1)
