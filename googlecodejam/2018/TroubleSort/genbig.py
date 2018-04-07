import random

print 100
for test in xrange(100):
    print 10000
    print ' '.join([str(random.randint(0, 1000000000)) for i in xrange(10000)])
