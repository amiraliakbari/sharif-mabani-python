a = {(1, 2): {"a": "b"}, 20: 200, "20": 100, 20: 400}
print a[(1,2)]

a['new key'] = "new value"
print a

print a[20]
a[20] = 300
print a[20]

for i in range(0, 20):
    a[i] = i

key = 100
#key = 20
if a.has_key(key):
    print a[key]
else:
    print "nothing!"
