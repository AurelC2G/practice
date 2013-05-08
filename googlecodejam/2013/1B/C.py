import sys

sys.setrecursionlimit(10000)

class Dico:
    def __init__(self):
        self.isLeaf = False
        self.next = {}

    def append(self, l, startIndex):
        if startIndex == len(l):
            self.isLeaf = True
            return

        letter = l[startIndex]
        if letter not in self.next:
            self.next[letter] = Dico()
        self.next[letter].append(l, startIndex+1)

    def getWords(self, S, index, lettersBeforeWildcard):
        res = []

        if self.isLeaf:
            res.append((0, 0, lettersBeforeWildcard))

        if index == len(S):
            return res

        letter = S[index]
        if letter in self.next:
            sub = self.next[letter].getWords(S, index+1, max(0, lettersBeforeWildcard-1))
            res = res + [(1 + nbLetters, nbWildcards, w) for (nbLetters, nbWildcards, w) in sub]

        if lettersBeforeWildcard == 0:
            for otherLetter, nextDico in self.next.iteritems():
                if otherLetter == letter:
                    continue
                sub = nextDico.getWords(S, index+1, 4)
                res = res + [(1 + nbLetters, 1 + nbWildcards, w) for (nbLetters, nbWildcards, w) in sub]

        return res


dico = Dico()

f = open('garbled_email_dictionary.txt', 'r')
for word in f:
    word = word.strip()
    if word != '':
        dico.append(list(word), 0)
f.close()

cache = {}

def solve(startPos, lettersBeforeWildcard):
    key = (startPos, lettersBeforeWildcard)
    if key in cache:
        return cache[key]

    if startPos == len(S):
        cache[key] = (True, 0)
        return cache[key]

    # We need to decide what will be our next word.
    options = dico.getWords(S, startPos, lettersBeforeWildcard)
    if len(options) == 0:
        cache[key] = (False, 0)
        return cache[key]
    foundRes = False
    res = 0
    for (nbUsed, nbWildcards, nbBeforeNextWildcard) in options:
        (b, r) = solve(startPos + nbUsed, nbBeforeNextWildcard)
        r += nbWildcards
        if b and (not foundRes or r < res):
            foundRes = True
            res = r
    cache[key] = (foundRes, res)

    return cache[key]


T = int(raw_input())
for t in xrange(T):
    S = raw_input()
    cache.clear()

    (b, res) = solve(0, 0)
 
    print "Case #{:d}: {:d}".format(t+1, res)
