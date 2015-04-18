from random import randint

print 100

for t in xrange(100):
    print 1000, randint(1000000,1000000000)
    v = []
    for i in xrange(1000):
        v.append(str(randint(1, 100000)))
    print ' '.join(v)

