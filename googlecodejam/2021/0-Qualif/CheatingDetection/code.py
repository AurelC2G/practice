import sys
import itertools
import math
import collections
import functools

T = int(input())
input() # P
for testId in range(T):
    T = [
        [int(c) for c in input()]
        for i in range(100)
    ]

    # Estimate difficulty of questions
    goodAnswers = [
        sum([T[i][j] for i in range(100)])
        for j in range(10000)
    ]
    estimatedDifficulty = [
        -3. if g == 100 else
        -math.log((g/100) / (1-(g/100)))
        for g in goodAnswers
    ]

    # Now we are looking for surprising players: they answered easy questions wrong or hard questions correctly
    mostSurprises = -1
    mostSurprising = None
    for i in range(100):
        correct = sum(T[i]) / 10000.
        if correct < 0.45:
            continue
        estimatedSkill = 3. if correct == 1. else math.log(correct / (1-correct))
        estimatedSkill = max(-3., estimatedSkill)
        estimatedSkill = min(3., estimatedSkill)

        s = 0
        for j in range(10000):
            p = 1 / (1 + math.exp(-(estimatedSkill - estimatedDifficulty[j])))
            if (p < 0.1 and T[i][j]) or  (p > 0.9 and not T[i][j]):
                s += 1
        if s > mostSurprises:
            mostSurprises = s
            mostSurprising = i

    print("Case #{:d}: {:d}".format(testId+1, mostSurprising+1))

