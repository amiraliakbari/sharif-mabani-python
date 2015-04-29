a = []

def f(n, k):
    if k == 0:
        if n == 0:
            print a
        return
    if n < 0:
        print "invalid:", a
        return
    a.append(0)
    f(n, k-1)
    a.pop()
    a.append(1)
    f(n-1, k-1)
    a.pop()
    a.append(2)
    f(n-2, k-1)
    a.pop()

f(5, 3)