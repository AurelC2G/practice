import random
print 1
print 255
for i in xrange(255):
    print ''.join([random.choice(['R', 'P']) for x in xrange(500)])
