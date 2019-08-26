"""
Exceptions & Testing
Created Spring 2019
Lab 10
@author: Ethan Walters (emw45)
"""

import turtle


class Planet:

    def __init__(self, name, rad, m, dist, color):
        if rad < 0 or m < 0 or dist < 0:
            raise ValueError('Planet numeric properties must be positive.')
        self.name = name
        self.radius = rad
        self.mass = m
        self.distance = dist
        self.color = color
        self.x = dist
        self.y = 0
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.pencolor(self.color)
        self.turtle.shape('circle')
        self.turtle.shapesize(self.radius, self.radius)
        self.turtle.goto(self.x, self.y)

    def getname(self):
        return self.name

    def getradius(self):
        return self.radius

    def getmass(self):
        return self.mass

    def getdistance(self):
        return self.distance

    def setname(self, newname):
        self.name = newname

    def __str__(self):
        return self.name


if __name__ == '__main__':

    # Set up turtle window for planets
    window = turtle.Screen()
    # Valid planets
    earth = Planet('Earth', 67, 56, 345, 'blue')
    mars = Planet('Mars', 34, 56, 88, 'red')
    venus = Planet('Venus', 78, 34, 106, 'orange')
    window.exitonclick()

    # # Test cases for exceptions
    # jupiter = Planet('Jupiter', -34, 67, 34)
    # saturn = Planet('Saturn', 65, -42, 56)
    # uranus = Planet('Uranus', 78, 32, -12)
