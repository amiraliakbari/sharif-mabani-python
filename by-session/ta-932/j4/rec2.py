




def g(x):
    y = x + 1
    return y * 2

def f(x):
    z = g(x + 1)
    return z / 2


print f(3)
