import turtle

l = int(raw_input())

turtle.left(60)
turtle.forward(l)
turtle.right(120)
turtle.forward(l)
turtle.backward(.6 * l)
turtle.right(120)
turtle.forward(.45 * l)

turtle.done()
