T = int(raw_input())
for testId in range(T):
    X, Y = map(int, raw_input().split())

    res = []

    # It is always possible, in two steps, to move in any direction by 1.
    # For example, to move of 1 towards North, make one step towards S, then
    # another one towards N.
    # For the small input, where we don't need the optimal solution, this is
    # enough.

    while X > 0:
        res.append('W')
        res.append('E')
        X -= 1
    while X < 0:
        res.append('E')
        res.append('W')
        X += 1
    while Y > 0:
        res.append('S')
        res.append('N')
        Y -= 1
    while Y < 0:
        res.append('N')
        res.append('S')
        Y += 1

    print "Case #{:d}: {:s}".format(testId+1, ''.join(res))
