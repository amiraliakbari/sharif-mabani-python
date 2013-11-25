def f(**kwargs):
    return (kwargs['x'] ** 2 + kwargs['y'] ** 2) ** 0.5

print f(x=1, y=2)
print f(y=2, x=1)

