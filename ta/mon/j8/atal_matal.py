def f(a, start):
    if len(a) == 1:
        return a[0]
    d = (start + 15 - 1) % len(a)
    del a[d]
    return f(a, d % len(a))

n = int(input())
print 1 + f(range(n*2), 0) / 2
