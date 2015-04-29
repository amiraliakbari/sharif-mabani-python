import turtle

r = 1

while turtle.heading() < 359:
    turtle.left(10)
    turtle.forward(r)
    r = r + 1

turtle.done()
