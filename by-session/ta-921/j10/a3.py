a = []

def f(n):
    if n == 0:
        print a
        return

    a.append(0)
    f(n-1)
    a.pop()

    a.append(1)
    f(n-1)
    a.pop()

f(3)
