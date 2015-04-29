import turtle

while turtle.xcor() < 100:
    turtle.forward(1)

turtle.left(180)

while turtle.xcor() > 0:
    turtle.forward(1)

turtle.done()