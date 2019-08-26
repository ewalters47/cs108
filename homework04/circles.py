'''
Python program that draws circles and determines their overlap
Created Spring 2019
Homework04
@author: Ethan Walters (emw45)
'''

# Import required modules
import turtle
from math import sqrt

# Get user inputs
x1 = int(input('Please input x1 value for circle center: '))
y1 = int(input('Please input y1 value for circle center: '))
x2 = int(input('Please input x2 value for circle center: '))
y2 = int(input('Please input y2 value for circle center: '))
radius1 = int(input('Please enter the radius for circle 1: '))
radius2 = int(input('Please enter the radius for circle 2: '))

# Create the center for both circles
center1 = (x1, y1)
center2 = (x2, y2)

# Compute the sum of both radii
radii_sum = radius1 + radius2

# Set up turtle environment
window = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()

# Draw the two circles
pen.penup()
pen.goto(center1)
pen.pendown()
pen.circle(radius1)

pen.penup()
pen.goto(center2)
pen.pendown()
pen.circle(radius2)

# Go to location for writing text
pen.penup()
pen.goto(0, -100)

# Compute the distance
distance = sqrt((x1-x2)**2 + (y1-y2)**2)

# Use if statements to determine circle position and print required results
if radius1 > (distance + radius2):
    pen.write('Circle 1 contains circle 2', font=("Arial", 20))
elif distance < radii_sum:
    pen.write('Circle 1 and Circle 2 Overlap', font=("Arial", 20))
elif distance > radii_sum:
    pen.write('Circles are disjoint', font=("Arial", 20))

# Keep the window open until it is clicked
window.exitonclick()