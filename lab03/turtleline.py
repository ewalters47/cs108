'''
Turtle graphics program to draw a user specified line
Created Spring 2019
Lab03
@author: Ethan Walters (emw45)
'''

import turtle
import math


x1 = int(input('Please enter the x1 value: '))
y1 = int(input('Please enter the y1 value: '))
x2 = int(input('Please enter the x2 value: '))
y2 = int(input('Please enter the y2 value: '))

point1 = (x1, y1)
point2 = (x2, y2)

window = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()

pen.penup()
pen.goto(point1)
pen.write('p1' + str(point1), font = ("Arial", 20, "italic"))

pen.pendown()
pen.goto(point2)
pen.write('p2' + str(point2), font = ("Arial", 20, "italic"))

window.exitonclick()