import turtle

def circle():
    while turtle.heading() < 359:
        turtle.forward(1)
        turtle.left(1)
    turtle.left(1)

def poly(r, n):
    teta = 360.0 / n
    while n > 0:
        n = n - 1
        turtle.forward(r)
        turtle.left(teta)

def abc():
    n = 6
    while n > 0:
        n = n - 1
        poly(20, 3)
        turtle.left(60)

def done():
    turtle.done()

print "lib.laki.lakposht"

