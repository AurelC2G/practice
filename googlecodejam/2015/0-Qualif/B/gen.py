from random import randint

print 100
for t in xrange(100):
    print 1000
    v = []
    for i in xrange(1000):
        v.append(randint(1, 1000))
    print ' '.join(map(str, v))
