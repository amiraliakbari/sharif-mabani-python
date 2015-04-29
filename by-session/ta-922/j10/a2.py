import turtle
from math import *

def f(x):
    return cos(x) * (x ** 2) + sin(x) + 4


x = 0.0
y = 50.0
step = 0.5

x0 = x
fx0 = f(x0)

while x <= y:
    fx = f(x)
    turtle.forward((x - x0) * 10)
    turtle.left(90)
    turtle.forward((fx - fx0) * 10)
    turtle.right(90)

    x0 = x
    fx0 = fx
    x += step

turtle.done()