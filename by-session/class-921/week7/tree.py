from turtle import *

def tree(level, length):
    pensize(level)
    if level == 1:
        forward(length)
        #right(90)
        #circle(length / 2)
        #left(90)
        backward(length)
        return
    forward(length)
    left(40)
    tree(level - 1, length * 3 / 4)
    right(100)
    tree(level - 1, length * 2 / 3)
    left(60)
    backward(length)

speed(20)
left(90)
tree(7, 100.0)
done()