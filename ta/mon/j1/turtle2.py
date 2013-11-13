import turtle

while turtle.heading() < 360:
    turtle.left(1)
    turtle.forward(5)

    if turtle.xcor() > 100:
        turtle.right(40)

    if turtle.xcor() < -100:
        turtle.right(100)

turtle.done()
