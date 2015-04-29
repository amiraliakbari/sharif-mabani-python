a = {2, 1, 3, 4}
b = set([1, 2, 3, 3])
c = {1, 2, 3, 5}
d = {1, 2, 3, 4}
print len(a)
print 4 in b
print len(b)
print b < a
print b < c
print a < c
print c < a
print a == c
print d < a
print d <= a
print a | c
print a & c