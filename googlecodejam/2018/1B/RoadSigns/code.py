import sys
import itertools
import math
import collections
import functools

def inputInts():
    return map(int, raw_input().split())

T = int(raw_input())
for testId in range(T):
    S = int(raw_input())

    finishedSequences = [0, 1] # size, count

    activeSeqs = []
    for i in xrange(S):
        D,A,B = inputInts()

        newSeqs = []

        # New sequence that starts with this sign (length, N, M)
        newSeqs.append([1, D-B, None])
        newSeqs.append([1, None, D+A])

        seqsEnding = []
        for seq in activeSeqs:
            if seq[1] == D-B or seq[2] == D+A:
                newSeqs.append([seq[0] + 1, seq[1], seq[2]])
                continue

            # neither matches, we have to increase one of the constraints
            if seq[1] is None:
                newSeqs.append([seq[0] + 1, D-B, seq[2]])
            elif seq[2] is None:
                newSeqs.append([seq[0] + 1, seq[1], D+A])
            else:
                # can't, sequence is over
                seqsEnding.append(seq[0])

        for l in set(seqsEnding):
            if l > finishedSequences[0]:
                finishedSequences = [l, 1]
            elif l == finishedSequences[0]:
                finishedSequences[1] += 1

        activeSeqs = newSeqs

    for l in set([seq[0] for seq in activeSeqs]):
        if l > finishedSequences[0]:
            finishedSequences = [l, 1]
        elif l == finishedSequences[0]:
            finishedSequences[1] += 1

    print "Case #{:d}: {:d} {:d}".format(testId+1, finishedSequences[0], finishedSequences[1])
