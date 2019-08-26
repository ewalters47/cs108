"""
Driver program for the circle class
Created Spring 2019
Homework 09
@author: Ethan Walters (emw45)
"""

from old.homework09.circle import Circle

with open('circles.txt', 'r') as file:

    for i in file:
        i.split()


if __name__ == '__main__':
    c1 = Circle(i)
    c1.render()

