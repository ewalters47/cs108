'''
Number sorting program
Created Spring 2019
Lab03
@author: Ethan Walters (emw45)
'''


# Get numbers from user input
num1 = int(input('Please enter number 1: '))
num2 = int(input('Please enter number 2: '))
num3 = int(input('Please enter number 3: '))
num4 = int(input('Please enter number 4: '))

# Create the lists
num_list = []
num_list2 = []

# Append the numbers to the first list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

# Add the min number from list1 into list2, then remove the min number from list1 so that min number is only in list2.
# Repeat this process until all numbers are sorted in order.
num_list2.append(min(num_list))
num_list.remove(min(num_list))
num_list2.append(min(num_list))
num_list.remove(min(num_list))
num_list2.append(min(num_list))
num_list.remove(min(num_list))
num_list2.append(min(num_list))
num_list.remove(min(num_list))

# Print the second number list to display results
print(num_list2)