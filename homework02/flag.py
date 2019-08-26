'''
Turtle graphics program to draw a flag
Created Spring 2019
Homework02
@author: Ethan Walters (emw45)
'''

import turtle

# Get the unit entered from the user
unit = int(input('Please enter a scalable unit: '))

# Set flag width and height variables
flag_width = unit/2
flag_height = unit/3

window = turtle.Screen()
pen = turtle.Turtle()

# Draw outer flag rectangle
pen.forward(flag_width)
pen.right(90)
pen.forward(flag_height)
pen.right(90)
pen.forward(flag_width)
pen.right(90)
pen.forward(flag_height)

# Draw inner circle and fill with red
pen.up()
pen.goto(flag_width/1.45, -flag_height/2)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.circle(unit/10)
pen.end_fill()

# Hide turtle after drawing has finished
pen.hideturtle()

# Keep the window open until it is clicked
window.exitonclick()