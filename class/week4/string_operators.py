a = "Hello World!"
print a[0]
print a[0:5]
print "Hello world!"[5:10]
print a[6:2]
print a[-6]
print a[-6:-1]
print a[-6:1]
print a[-6:]
print a[:-6]
print a[:]
print a[10:15]
print 2 * a
print "jam " + "2 reshte"
print "Hello" in a
print "hello" in a
print "hello" not in a
print len(a)

for i in range(0, len(a)):
    print a[:i]
