import sys
import itertools
import math
import collections
import functools

def removeUniques(uniques):
    for u,n in uniques.iteritems():
        c = counts[u]
        if not c:
            continue
        res.extend([n for i in xrange(c)])
        for l in digits[n]:
            if counts[l] == c:
                del counts[l]
            else:
                counts[l] -= c

T = int(raw_input())
for testId in range(T):
    S = raw_input()

    digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

    counts = collections.Counter()
    counts.update(list(S))

    res = []

    removeUniques( {
        'G': 8,
        'U': 4,
        'W': 2,
        'X': 6,
        'Z': 0,
    })

    removeUniques({
        'F': 5,
        'H': 3,
        'O': 1,
        'S': 7,
    })

    # Only 9 remains
    res.extend([9 for i in xrange(counts['I'])])

    print "Case #{:d}: {}".format(testId+1, ''.join(map(str, sorted(res))))
