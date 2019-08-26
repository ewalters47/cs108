'''
Python program to find perfect numbers
Created Spring 2019
Lab05
@author: Ethan Walters (emw45)
'''

found_perfects = 0

for value in range(2, 10000):

    low = 1
    high = value
    divisors = []

    while low < high:
        if low % value:
            high == value / low
            divisors.append(low)
            if high != low:
                divisors.append(high)
    if low % value:
        print(value, 'is a perfect number')
    else:
        break