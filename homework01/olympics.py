''' Turtle graphics program to draw the olympics logo
Created Spring 2019
Homework 01
@author: Ethan Walters (emw45)
'''

import turtle

# Set up turtle module
window = turtle.Screen()
pen = turtle.Turtle()

# Draw blue circle
pen.pensize(8)
pen.pencolor("blue")
pen.circle(50)

# Draw black circle
pen.up()
pen.forward(120)
pen.down()
pen.pencolor("black")
pen.circle(50)

# Draw red circle
pen.up()
pen.forward(120)
pen.down()
pen.pencolor("red")
pen.circle(50)

# Draw green circle
pen.up()
pen.backward(110)
pen.right(90)
pen.down()
pen.pencolor("green")
pen.circle(50)

# Draw yellow circle
pen.up()
pen.right(90)
pen.forward(120)
pen.left(90)
pen.down()
pen.pencolor("yellow")
pen.circle(50)

# Keep the window open until it is clicked.
window.exitonclick()