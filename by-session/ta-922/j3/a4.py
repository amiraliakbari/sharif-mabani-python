n = int(raw_input())

a = []
i = 0
while i < n:
    x = int(raw_input())
    a.append(x)
    i += 1

j = 0
S = 0
while j < len(a):
    S += a[j]
    j += 1

print S
