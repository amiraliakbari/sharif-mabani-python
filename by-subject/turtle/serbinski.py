import turtle
def serb(l):
  if l <= 10.0:
    turtle.left(60)
    turtle.forward(l)
    turtle.right(120)
    turtle.forward(l)
    turtle.right(120)
    turtle.forward(l)
    turtle.right(180)
    return
  serb(l/3.0)
  turtle.forward(l/3.0)
  serb(l/3.0)
  turtle.backward(l/3.0)
  turtle.left(60)
  turtle.forward(l/3.0)
  turtle.right(60)
  serb(l/3.0)
  turtle.right(120)
  turtle.forward(l/3.0)
  turtle.left(120)

serb(100)

