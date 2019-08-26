"""
Exceptions & Testing
Created Spring 2019
Lab 10
@author: Ethan Walters (emw45)
"""

try:
    'hi' + 4
except TypeError:
    print('Cannot add a word and integer together')

try:
    10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')

try:
    'person'.find_first('e')
except AttributeError:
    print('Cannot use find_first method')

try:
    [0,1,2]['summer']
except TypeError:
    print('Must be integer or slice operation')

try:
    ['hi','there','student'][5]
except IndexError:
    print('The index is out of range')

try:
    print(name)
except NameError:
    print('name is not defined as anything')

try:
    9 <= (3, 4)
except TypeError:
    print('You cannot compare integers and tuples')

try:
    f = open('missingFile.txt')
except FileNotFoundError:
    print('missingFile.txt cannot be found')
