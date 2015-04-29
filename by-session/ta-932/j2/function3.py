
def is_prime(x):
    prime_x = True
    i = 2
    while i < x:
        if x % i == 0:
            prime_x = False
            break
        i = i + 1
    return prime_x

n = int(raw_input())
x = 2

while 2 * x <= n:
    y = n - x
    print "Checking:", x, ",", y

    prime_x = is_prime(x)
    prime_y = is_prime(y)
    if prime_x and prime_y:
        print y, "+", x
        break

    x = x + 1


#amiraliakbari@gmail.com






#if x == True:
#if x:

