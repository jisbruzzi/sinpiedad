import sys
n=long(sys.argv[1])
print 1 if all([n%x for x in xrange(2,n)])else 0
