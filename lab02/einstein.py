'''
Einstein program for CS 108
Created Spring 2019
Lab 02
@author: Ethan Walters (emw45)
'''


# Prompt user for required integers
number = int(input('Please enter a 3 digit number where the first and last digits differ by at least 2: '))

# Store inputed integers
digit1 = ((number//100)%10)
digit2 = ((number//10)%10)
digit3 = ((number//1)%10)

# Reverse integer order
rev_number = (digit3 * 100 + digit2 * 10 + digit3 * 1)

# Calculate difference
difference = abs(number - rev_number)

# Store difference integers
diff_digit1 = (difference//100)%10
diff_digit2 = (difference//10)%10
diff_digit3 = (difference//1)%10

# Reverse difference integers
rev_diff = (diff_digit3 * 100 + diff_digit2 * 10 + diff_digit1 * 1)

# Print sum of difference and rev_diff
print(difference + rev_diff)




