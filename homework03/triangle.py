'''
Turtle graphics program to draw a user specified triangle, draw a perpendicular line,
and compute the area of the triangle.
Created Spring 2019
Homework03
@author: Ethan Walters (emw45)
'''

# Import required libraries
import turtle

# Receive points from user
x1 = int(input('Please enter x1 value: '))
y1 = int(input('Please enter y1 value: '))
x2 = int(input('Please enter x2 value: '))
y2 = int(input('Please enter y2 value: '))
x3 = int(input('Please enter x3 value: '))
y3 = int(input('Please enter z3 value: '))

# Create tuples to represent the 3 points for the triangle
point1 = (x1, y1)
point2 = (x2, y2)
point3 = (x3, y3)

# Create a height point for the perpendicular line
height = (x3, y1)

# Set up perimeter
line1 = x1 + x2
line2 = x2 + x3
line3 = x3 + x1
perimeter = line1 + line2 + line3

# Set up area
base = x1 + x2
area_height = x3 + y1
area = .5 * base * area_height

# Set up turtle environment
window = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()

# Draw the triangle
pen.penup()
pen.goto(point1)
pen.pendown()
pen.goto(point2)
pen.goto(point3)
pen.goto(point1)
pen.goto(point3)
pen.goto(height)

# Goto top-left location and print the perimeter and area
pen.penup()
pen.goto(-200, 200)
pen.pendown()
pen.write('Perimeter: ' + str(perimeter), font = ("Arial", 20, "italic"))
pen.penup()
pen.goto(-200, 250)
pen.pendown()
pen.write('Area: ' + str(area), font = ("Arial", 20, "italic"))

# Keep the window open until it is clicked
window.exitonclick()