#fib(n) = fib(n - 1) + fib(n - 2)
#fib(1) = 1
#fib(2) = 1

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    temp = fib(n - 1) + fib(n - 2)
    #print n, temp
    return temp


print fib(10)