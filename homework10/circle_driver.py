"""
Driver program for the circle class with exception handling
Created Spring 2019
Homework 09
@author: Ethan Walters (emw45)
"""


with open('circles.txt', 'r') as file:

    try:
        for i in file:
            i.split()
    except NameError:
        print('File name is incorrect')
