# Written By: Ben Nguyen
# Code source is from @pythonlearnerr on instagram
# Creating a virus drawing with turtle
# 24 October 2022
import turtle
from turtle import *
speed(50)
color('cyan')
bgcolor('black')
b = 200
goto(290, 65)
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
turtle.exitonclick()
