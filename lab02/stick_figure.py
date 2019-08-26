'''
Python program to draw scalable stick figure using Turtle Graphics
Created Spring 2019
Lab 02
@author: Ethan Walters (emw45)
'''

import turtle
import math

UNIT = 50

window = turtle.Screen()
pen = turtle.Turtle()

# Draw the head
pen.circle(UNIT)
pen.right(90)

# Draw the body
pen.forward(UNIT*2)

# Draw the left leg
pen.right(45)
pen.forward(math.sqrt(UNIT**2 + UNIT**2))

# Move the pen
pen.left(135)
pen.up()
pen.forward(UNIT*2)
pen.left(135)
pen.down()

# Draw the right leg
pen.forward(math.sqrt(UNIT**2 + UNIT**2))

# Draw the arms
pen.right(45)
pen.forward(UNIT)
pen.left(90)
pen.forward(UNIT)
pen.right(180)
pen.forward(UNIT*2)

# Hide the turtle after the stick figure has been drawn
pen.hideturtle()

# Keep the window open until it is clicked.
window.exitonclick()