

def f(n):
    x = n * n + n + 1
    return x


n = 10
s = 0
i = 1

while i < 10:
    s = s + f(i)
    i = i + 1

print s