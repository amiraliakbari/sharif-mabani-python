from turtle import *

def kokh(level, length):
    if level == 1:
        forward(length)
        return
    kokh(level - 1, length / 3)
    left(60)
    kokh(level - 1, length / 3)
    right(120)
    kokh(level - 1, length / 3)
    left(60)
    kokh(level - 1, length / 3)

speed(20)
kokh(5, 300.0)
done()