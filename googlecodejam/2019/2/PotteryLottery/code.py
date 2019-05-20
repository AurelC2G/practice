import sys

def inputInts():
    return map(int, raw_input().split())

def action(V, P):
    print "{:d} {:d}".format(V+1, P)
    sys.stdout.flush()

def peek(vase):
    action(vase, 0)
    ans = inputInts()
    return ans[0]

def cheat(vase):
    action(vase, 1)

T = int(raw_input())
for testId in range(T):

    startPeek = 60
    discardedPots = 10
    
    pollResults = []
    chosenVase = None

    for i in xrange(1, 101):
        if i != int(raw_input()):
            sys.exit(1)

        if i < startPeek:
            cheat(i % discardedPots)
        elif len(pollResults) < 20 - discardedPots:
            pollResults = [x + 1./20. for x in pollResults] # add current day token
            pollResults.append(peek(discardedPots + len(pollResults))) # peek
        elif i == 100:
            action(chosenVase, 100) # my own play
        else:
            if chosenVase is None:
                idx = pollResults.index(min(pollResults))
                pollResults[idx] = 1e9
                chosenVase = discardedPots + idx

            idx = pollResults.index(min(pollResults))
            cheat(discardedPots + idx)
            pollResults[idx] += 1
