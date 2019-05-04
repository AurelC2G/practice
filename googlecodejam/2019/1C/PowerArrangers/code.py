import sys
import itertools
import math
import collections
import functools

def inputInts():
    return map(int, raw_input().split())


def ask(n):
    print n
    sys.stdout.flush()
    ans = raw_input()
    if ans == 'N':
        sys.exit(1)
    return ans

def reply(res):
    print res
    sys.stdout.flush()
    if raw_input() == 'N':
        sys.exit(1)

T, F = inputInts()
for testId in range(T):
    res = 0

    S = set()
    for perm in itertools.permutations('ABCDE'):
        S.add(''.join(perm))

    nextLook = 0

    while len(S) > 1:
        remaining = list(S)
        for guess in xrange(5):
            peek = ask(nextLook * 5 + guess + 1)
            remaining = filter(lambda w: w[guess] == peek, remaining)
            if (len(remaining) == 1):
                S.remove(remaining[0])
                break
        nextLook += 1

    reply(list(S)[0])
