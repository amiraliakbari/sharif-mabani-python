def devisors(n):
    r = 0
    i = 1
    while i <= n:
        if n % i == 0:
            r += 1
        i += 1

    return r

def is_prime(n):
    x = devisors(n)
    if x == 2:
        return True
    else:
        return False

print is_prime(3)
