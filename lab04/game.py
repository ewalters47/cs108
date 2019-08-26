'''
Python rock, paper, scissors game
Created Spring 2019
Lab04
@author: Ethan Walters (emw45)
'''

# Import random module
from random import *

# Get user input choice
user_choice = int(input('Please enter 0 for rock, 1 for paper, or 2 for scissors: '))

# Determine computer choice using the random module
computer_choice = randint(0, 2)

# Game logic
if user_choice == 0:
    if computer_choice == 1:
        print('Computer wins!')
    elif computer_choice == 2:
        print('You win!')
    else:
        print('It is a draw!')

if user_choice == 1:
    if computer_choice == 2:
        print('Computer wins!')
    elif computer_choice == 1:
        print('You win!')
    else:
        print('It is a draw!')

if user_choice == 2:
    if computer_choice == 0:
        print('Computer wins!')
    elif computer_choice == 1:
        print('You win!')
    else:
        print('It is a draw!')