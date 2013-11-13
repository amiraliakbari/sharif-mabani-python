def sum2(a):
    b = a[len(a)/2:]
    s = 0
    for i in range(len(b)):
        s += b[i]
    return s


print sum2([1, 2, 3, 4, 5, 6])
