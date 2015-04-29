a = []

def f(n, k):
    if k == 0:
        print a
        return

    for i in range(n):
        a.append(i)
        f(n-i, k-1)
        a.pop()

f(5, 3)

