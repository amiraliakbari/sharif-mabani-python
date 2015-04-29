s = set()
n = int(input())
for i in range(n):
    x = int(input())
    s.add(x)

l = list(s)
l.sort()

for i in range(len(l)):
    print l[i], ',',
