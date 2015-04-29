




def fact(n):
   print n
   if n < 2:
       return 1
   return n * fact(n-1)


def fib(n):
    print n
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
fib(4)

















def C(n, r):
    if n < 2:
        return n
    if r < 2:
        return n
    if r > n:
        return 0
    if r == n:
        return 1

    return C(n-1, r) + C(n-1, r-1)
