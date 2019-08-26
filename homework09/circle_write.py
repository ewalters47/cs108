"""
Python program that writes circle data to a file
Created Spring 2019
Homework 09
@author: Ethan Walters (emw45)
"""

with open('circles.txt', 'w') as file:
    file.write('0 0 100 black unfilled\n100 0 10 gold filled\n130 20 20 blue filled')
