n = int(raw_input())

x = 2

while 2 * x <= n:
    y = n - x
    print "Checking:", x, ",", y

    prime_x = True
    i = 2
    while i < x:
        if x % i == 0:
            prime_x = False
            break
        i = i + 1

    prime_y = True
    i = 2
    while i < y:
        if y % i == 0:
            prime_y = False
            break
        i = i + 1

    if prime_x and prime_y:
        print y, "+", x
        break

    x = x + 1


#amiraliak...@gmail.com


#if x == True:
#if x:
