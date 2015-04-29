
def sum2(x, y):
    return x+y

def f(*args):
    s = 0
    for i in range(len(args)):
        s += args[i]
    return s

print f(1, 2, 3)
print f(1)
print f(1, 2, 3, 4)
print f()

a = (1, 2)
a = ()

a = (1)
print a

a = (1,)
print a
