def sum_num(n):
    a=0
    while n>0:
        a=n%10+a
        n=n/10
    return a


for i in range(1, 100):
    if sum_num(i) % 11 == 0:
        print i
        break
