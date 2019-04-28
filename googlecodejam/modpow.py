def modPow(b, e, mod):
    res = 1
    b = b % mod
    while e > 0:
        if e%2 == 1:
            res = (res * b) % mod
        e = e // 2
        b = (b * b) % mod
    return res
