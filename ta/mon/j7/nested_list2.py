n = 3
m = []
for i in range(n):
    m.append([])
    for j in range(n):
        t = (i+1) * (j+1)
        m[-1].append(t)

print m
#m = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
