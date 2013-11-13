a = [1, 2, 3, 4]
b = []

for i in range(len(a)-1, -1, -1):
    b.append(a[i])

print b

c = []
for i in rnage(1, len(a) + 1):
    c.append(a[-i])
