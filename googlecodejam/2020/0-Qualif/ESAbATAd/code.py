import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

def inputInts():
    return list(map(int, input().split()))

def query(P):
    global q
    q += 1
    print(1+P)
    sys.stdout.flush()
    ans = input()
    if ans == 'N':
        sys.exit(1)
    return int(ans)

def answer(ans):
    print(''.join(map(str, ans)), file=sys.stderr)
    print(''.join(map(str, ans)))
    sys.stdout.flush()
    if input() == 'N':
        sys.exit(2)

T, B = inputInts()
for testId in range(T):
    q = 1
    res = [None] * B
    bits_known = 0
    next_bit = 0

    # First index we found that cares about reversal (mirror bit is different)
    reversalIdx = None

    # An index to a bit that is mirrored (making it trivial to check complement)
    # Initially this is None, and as long as it is we have only looked at mirrored bits.
    # As long as this is the case, we don't have to look at complement, because it is
    # equivalent to reversal.
    complementIdx = None

    while bits_known < B:
        if q % 10 == 1:
            if complementIdx is not None and res[complementIdx] != query(complementIdx):
                print('Detected complement', file=sys.stderr)
                res = [(None if i is None else 1-i) for i in res]

            if reversalIdx is not None and res[reversalIdx] != query(reversalIdx):
                print('Detected reversal', file=sys.stderr)
                res.reverse()

        if B%2 == 1 and next_bit == B//2:
            # Only one left!
            print('Fetching last bit', file=sys.stderr)
            res[next_bit] = query(next_bit)
            bits_known += 1
        elif q % 10 == 0: # Last request before shuffle!
            if complementIdx is not None and B%2 == 1 and res[B//2] is None:
                # if we already care about complements, might as well query the middle digit
                print('Fetching middle bit', file=sys.stderr)
                res[B//2] = query(B//2)
                bits_known += 1
            else:
                # discard the result if we can't query a full pair
                print('Dropping next query', file=sys.stderr)
                query(0)
        else:
            # Query the next mirrored pair
            print('Fetching next pair at index {}'.format(next_bit), file=sys.stderr)
            res[next_bit] = query(next_bit)
            mirror = B-next_bit-1
            res[mirror] = query(mirror)
            if res[next_bit] == res[mirror]:
                complementIdx = next_bit
            else:
                reversalIdx = next_bit
            bits_known += 2
            next_bit += 1

    answer(res)
