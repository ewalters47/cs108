"""
Exceptions & Testing
Created Spring 2019
Lab 10
@author: Ethan Walters (emw45)
"""

import turtle


class Sun:

    def __init__(self, name, rad, m, temp, color):
        if rad < 0 or m < 0 or temp < -273.15:
            raise ValueError('Numeric properties must be greater than 0 and the temperature'
                             'must be greater than absolute zero.')
        self.name = name
        self.radius = rad
        self.mass = m
        self.temp = temp
        self.color = color
        self.x = 0
        self.y = 0
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.pencolor(self.color)
        self.pen.shape('circle')
        self.pen.shapesize(self.radius, self.radius)
        self.pen.goto(self.x, self.y)

    def getmass(self):
        return self.mass

    def __str__(self):
        return self.name


if __name__ == '__main__':

    window = turtle.Screen()
    sun = Sun('Sun', 45, 78, 35, 'yellow')
    window.exitonclick()
