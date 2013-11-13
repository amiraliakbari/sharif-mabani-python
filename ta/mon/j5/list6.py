n = input("Tedad adad?")
a = []

for i in range(n):
    a.append(input("Addad " + str(i) + " om ra vared konid:"))

s = 0
for i in range(n):
    s += a[i]
print s


m = 100000000000000000000000
for i in range(n):
    if a[i] < m:
        m = a[i]
print m


a.append(2)
a.append(4)

print len(a)

