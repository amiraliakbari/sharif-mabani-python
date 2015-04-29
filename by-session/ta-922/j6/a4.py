def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def s(a):
    if len(a) < 2:
        return a

    a1 = a[:len(a)/2]
    a2 = a[len(a)/2:]
    a1_s = s(a1)
    a2_s = s(a2)
    a_s = merge(a1_s, a2_s)
    return a_s

