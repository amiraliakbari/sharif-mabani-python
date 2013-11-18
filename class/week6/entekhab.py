#c(n, r) = c(n-1, r) + c(n-1, r-1)
#r <= n
#r,n >= 0

def c(n, r):
    if r == 0:
        return 1
    if n == r:
        return 1
    return c(n-1, r) + c(n-1, r-1)

print c(6, 4)