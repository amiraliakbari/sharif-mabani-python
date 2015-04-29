def f(n):
    if n < 2:
        print 'A'
        return 1
    a = f(n-1)
    print 'B'
    b = f(n-2)
    print 'C'
    return a + b

f(6)
