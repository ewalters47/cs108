''' Turtle graphics program to draw the letters 'CS'
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

# Draw the letter C
pen.backward(100)
pen.right(90)
pen.forward(200)
pen.left(90)
pen.forward(100)

# Set up pen to draw the S
pen.up()
pen.left(90)
pen.forward(200)
pen.right(90)
pen.forward(150)
pen.left(180)

# Draw the letter S
pen.down()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.hideturtle()


# Keep the window open until it is clicked.
window.exitonclick()