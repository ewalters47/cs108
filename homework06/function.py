'''
Python program that draws a stick figure from a function
Created Spring 2019
Homework06
@author: Ethan Walters (emw45)
'''

import turtle
from math import sqrt

# Create function
def draw_stick_figure(x, y, scale):

    # Set up turtle
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.hideturtle()

    # Go to specified coordinates
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Draw the head
    pen.circle(scale)
    pen.right(90)

    # Draw the body
    pen.forward(scale * 2)

    # Draw the left leg
    pen.right(45)
    pen.forward(sqrt(scale ** 2 + scale ** 2))

    # Move the pen
    pen.left(135)
    pen.up()
    pen.forward(scale * 2)
    pen.left(135)
    pen.down()

    # Draw the right leg
    pen.forward(sqrt(scale ** 2 + scale ** 2))

    # Draw the arms
    pen.right(45)
    pen.forward(scale)
    pen.left(90)
    pen.forward(scale)
    pen.right(180)
    pen.forward(scale * 2)

    # Keep the window open until it is clicked.
    window.exitonclick()

# Call the function
draw_stick_figure(-50, 50, 50)