import turtle

def circle():
    while turtle.heading() < 359:
        turtle.forward(1)
        turtle.left(1)
    turtle.left(1)

def poly(r, teta):
    n = 360 / teta
    while n > 0:
        n = n - 1
        turtle.forward(r)
        turtle.left(teta)

n = 10
while n > 0:
    n = n - 1
    poly(10, 30)
    turtle.forward(40)

turtle.done()

