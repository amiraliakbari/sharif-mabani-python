import turtle

n = 1
while turtle.heading() < 360:
      turtle.forward(n)
      turtle.left(1)
      n = n + 0.005

turtle.done()

