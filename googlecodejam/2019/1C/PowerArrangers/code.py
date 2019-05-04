import sys
import itertools
import math
import collections
import functools

def inputInts():
    return map(int, raw_input().split())


def ask(n):
    global peeks
    peeks += 1
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

    S = set()
    for perm in itertools.permutations('ABCDE'):
        S.add(''.join(perm))

    peeks = 0

    res = ''

    expected = [24, 6, 2, 1, 1]
    remaining = range(119)
    for guess in xrange(4):
        results = {
            c: []
            for c in 'ABCDE'
            if c not in res
        }
        for n in remaining:
            peek = ask(n * 5 + guess + 1)
            results[peek].append(n)

        sys.stderr.write(str({
            c: len(v)
            for c,v in results.iteritems()
        }) + "\n")

        for c,v in results.iteritems():
            if len(v) != expected[guess]:
                res += c
                remaining = v
                break

    for c in 'ABCDE':
        if c not in res:
            res += c
            break

    sys.stderr.write("Found {} in {}\n".format(res, peeks))
    reply(res)
