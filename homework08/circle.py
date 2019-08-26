"""
Circle class that represents circle objects
Created Spring 2019
Homework 08
@author: Ethan Walters (emw45)
"""

import sys
import math
import turtle


class Circle:
    """Initialize the Circle class constructor"""
    def __init__(self, x=0, y=0, x1=0, y1=0, radius=100, color='black', filled=False, window=turtle.Screen(),
                 pen=turtle.Turtle()):

        # If the radius is less than 0, exit the program
        if radius > 0:
            self.x = x
            self.y = y
            self.x1 = x1
            self.y1 = y1
            self.center = (x, y)
            self.radius = radius
            self.color = color
            self.filled = filled
            self.window = window
            self.pen = pen
        else:
            print('Error: circle cannot have a negative radius')
            sys.exit(-1)

    def __str__(self):
        """Create a string method to print the Circle's current state and values"""

        return 'X Position: %s\nY Position: %s\nCenter Position: %s\nRadius: %s' \
               '\nColor: %s\nFilled: %s\nArea: %s\nCircumference: %s'\
               % (self.x, self.y, self.center, self.radius, self.color, self.filled, self.get_area(),
                  self.get_circumference())

    def get_area(self):
        """Create an accessor method to get the area of the circle"""

        return round(math.pi * self.radius ** 2, 2)

    def get_circumference(self):
        """Create an accessor method to get the circumference of the circle"""

        return round(2 * math.pi * self.radius, 2)

    def modify_radius(self, delta):
        """Create a mutator method set the circle radius"""

        self.radius = delta

    def overlaps(self):
        """Create a method to define which circles overlap"""

        distance = math.sqrt((self.x - self.x1) ** 2 + (self.y - self.y1) ** 2)
        radius1 = 130
        radii_sum = self.radius + radius1
        if distance < radii_sum:
            return True
        else:
            return False

    def render(self):
        """Create a render method to draw the circle"""

        self.pen.goto(self.center)
        self.pen.circle(self.radius)
        self.window.exitonclick()


c1 = Circle(34, 56, 23, 45, 100, 'black', False)
print(c1)

c2 = Circle.render()
