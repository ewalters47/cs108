'''
Python program to calculate the day of the week
Created Spring 2019
Lab04
@author: Ethan Walters (emw45)
'''

# Get user inputs
year = int(input('Please input the year: '))
month = int(input('Please input the month: '))
day_of_month = int(input('Please input the day of the month: '))

# Do necessary year conversions
century = (year//100)
year_of_century = (year % 100)

# If user enters 1 or 2 for month, set to 13 or 14 respectively and subtract the year by 1
if month == 1:
    month = 13
    year = year - 1
elif month == 2:
    month = 14
    year = year - 1

# Compute the day of the week using Zeller's congruence formula
day_of_the_week = (day_of_month + ((26 * (month + 1)) // (10)) + year_of_century + ((year_of_century // 4)) + ((century) // (4)) + (5 * century)) % 7

# Create the days list
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Print the day of the week using day_of_the_week as an index
if day_of_the_week == 0:
    print('Day of the week:', days[0])
elif day_of_the_week == 1:
    print('Day of the week:', days[1])
elif day_of_the_week == 2:
    print('Day of the week:', days[2])
elif day_of_the_week == 3:
    print('Day of the week:', days[3])
elif day_of_the_week == 4:
    print('Day of the week:', days[4])
elif day_of_the_week == 5:
    print('Day of the week:', days[5])
elif day_of_the_week == 6:
    print('Day of the week:', days[6])