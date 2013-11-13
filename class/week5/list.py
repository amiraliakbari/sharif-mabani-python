a = "ali,hassan, hossein"
print a.split(",")
print a.split("s")

b = [1, 2, "ali", True, "salam"]
print b
print b[0]
print len(b)
b[1] = 0
print b
del b[2]
print b
b.insert(2, "ali")
print b
b.insert(4, 10)
print b
b.insert(10, "salam")
print b

a = [1, 2]
b = [3, 4]
print a + b
a.extend(b)
print a

print b * 2

print 1 in a
print "ali" in a