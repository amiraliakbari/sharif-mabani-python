
def fib(n):
    if n <=1:
        return 1
    return fib(n-1) + fib(n-2)

def C(n, r):
    if n == r:
        return 1
    if r <= 1:
        return n
    return C(n-1, r) + C(n-1, r-1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
