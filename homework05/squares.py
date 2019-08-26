'''
Python program that computes and displays the squares of consecutive integers
Created Spring 2019
Homework05
@author: Ethan Walters (emw45)
'''

# Get user input
input = int(input('Please enter the desired difference between squares: '))
default = 0

# Create a while loop to compute squares
while default < input:
    print(default*default)
    default += 1
