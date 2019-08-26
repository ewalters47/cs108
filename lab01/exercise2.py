''' Turtle graphics program to draw a star
Created Spring 2019
Lab 01
@author: Ethan Walters (emw45)
'''

# Gain access to the collection of code named "turtle".
import turtle

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()
turtle.setup(width = 800, height = 600, startx = 100, starty = 100)

# Create a turtle and name it pen.
pen = turtle.Turtle()

# Tell the pen to draw the star
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.hideturtle()

# Keep the window open until it is clicked.
window.exitonclick()