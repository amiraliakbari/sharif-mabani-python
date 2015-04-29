

n = 3


# f(n) -> ['000', '001', '010', '011']

#0 00
#0 01
#0 10
#0 11
#1 00
#1 01
#1 10
#1 11


# f(n=2, k=4) -> ['00', '01', '02', '03', '10', '11', ..]

k = 4

def f(n):
    global k

    if n <= 0:
        return []
    if n == 1:
        l = []
        for i in range(k):
            l.append(str(i))
        return l

    l = f(n-1)  # ['00', '01', '10', '11']
    l2 = []
    for y in range(k):
      for x in l:
        l2.append(str(y) + x)

    return l2

# int(1.2) -> 1
# str(1)  -> '1'

print f(3)













