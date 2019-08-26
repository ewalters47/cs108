'''
Login ID generator
Created Spring 2019
Lab03
@author: Ethan Walters (emw45)
'''

# Get required inputs from user
first_name = str(input('Please enter your first name: '))
last_name = str(input('Please enter your last name: '))
student_number = str(input('Please enter your number: '))

# Compute user login and make all lowercase
login = first_name[0:1] + last_name[0:15] + student_number[5:7]
login = login.lower()

# Print user login
print(login)
