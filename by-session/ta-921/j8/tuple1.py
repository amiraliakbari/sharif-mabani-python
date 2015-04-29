a = (1, 2)
b = (1, 3, 5, 7, 8, 11)
print a[0]
#b[3] = 3  # error!


x1 = a[0]
y1 = a[1]

x1, y1 = a
b1, b2, b3, b4, b5, b6 = b
print b4
#b1, b2 = b  # error!

a = 1, 2, 3
print a


def f():
    return 1, 3

a = f()
x, y = f()

x = f()[0]
