import turtle

def draw_A():
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.backward(55)
    turtle.right(120)
    turtle.forward(45)



# draw first A
draw_A()

turtle.penup()

# move
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)

turtle.pendown()

# draw second A
draw_A()

turtle.done()
