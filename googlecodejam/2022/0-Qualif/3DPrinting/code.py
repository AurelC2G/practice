def inputInts():
    return list(map(int, input().split()))


T = int(input())
for testId in range(T):
    ink = [inputInts(), inputInts(), inputInts()]

    res = []
    for k in range(4):
        res.append(min([i[k] for i in ink]))

    if sum(res) < 1000000:
        print("Case #{:d}: IMPOSSIBLE".format(testId+1))
    else:
        tot = 0
        for k in range(4):
            res[k] = min(res[k], 1000000-tot)
            tot += res[k]
        print("Case #{:d}: {}".format(testId+1, ' '.join(map(str, res))))
