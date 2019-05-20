import sys
import random

# naive strategy: put tokens in all vases but one, hope to win
def simulate1():
    vases = [0] * 20

    for i in xrange(99):
        vases[random.randint(0, 19)] += 1 # legit play
        vases[i % 19] += 1 # cheating
    vases[19] += 1 # my own play

    print vases
    for i in xrange(19):
        if vases[i] <= vases[19]:
            return 0
    return 1

def simulate2(startPeek):
    # Put random tokens for days 1-70, then poll all vases, then fill the empty ones
    vases = [0] * 20

    pollResults = []
    for i in xrange(1, 100):
        vases[random.randint(0, 19)] += 1 # legit play
        if i < startPeek:
            vases[i % 19] += 1 # cheating
        elif len(pollResults) < 19:
            pollResults = [x + 1./20. for x in pollResults] # add current day token
            pollResults.append(vases[len(pollResults)]) # peek
        else:
            idx = pollResults.index(min(pollResults))
            vases[idx] += 1 # cheat
            pollResults[idx] += 1

    vases[19] += 1 # my own play

    print vases
    for i in xrange(19):
        if vases[i] <= vases[19]:
            return 0
    return 1

def simulate3(startPeek = 50, discardedPots = 10):
    # Step 1: fill 10 vases randomly for a while
    # Step 2: peek the other 10
    # Step 3: we will bet for the min of these 10. Fill the other ones
    # Put random tokens for days 1-70, then poll all vases, then fill the empty ones
    vases = [0] * 20

    pollResults = []
    chosenVase = None
    for i in xrange(1, 100):
        vases[random.randint(0, 19)] += 1 # legit play

        if i < startPeek:
            vases[i % discardedPots] += 1 # cheating
        elif len(pollResults) < 20 - discardedPots:
            pollResults = [x + 1./20. for x in pollResults] # add current day token
            pollResults.append(vases[discardedPots + len(pollResults)]) # peek
        else:
            if chosenVase is None:
                idx = pollResults.index(min(pollResults))
                pollResults[idx] = 1e9
                chosenVase = discardedPots + idx

            idx = pollResults.index(min(pollResults))
            vases[discardedPots + idx] += 1 # cheat
            pollResults[idx] += 1

    vases[chosenVase] += 1 # my own play

    for i in xrange(20):
        if i != chosenVase and vases[i] <= vases[chosenVase]:
            return 0
    return 1

success = 0
for i in xrange(1000):
    #success += simulate2(71)
    #success += simulate3(60, 10)
    success += simulate3(60, 10)
print success / 1000.
