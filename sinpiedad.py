import sys
n=int(sys.argv[1])
print 0 if any([n%x==0 for x in xrange(2, n)])else 1