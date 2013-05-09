
T = int(raw_input())
for testId in range(T):
    A, N = map(int, raw_input().split())
    S = map(int, raw_input().split())
    S.sort()

    s = 0 # Current index in S
    current = 0 # Operations used
    res = len(S) # We can solve by removing all items

    while current < res:
        # Consume everything we can
        while s < len(S) and A > S[s]:
            A += S[s]
            s += 1

        # We can decide to finish now by removing everything
        res = min(res, current + len(S) - s)

        # If the list is empty, we're done
        if s == len(S):
            break

        # Try to add something
        while current < res and A <= S[s]:
            current += 1
            A += A-1

    print "Case #{:d}: {:d}".format(testId+1, res)
