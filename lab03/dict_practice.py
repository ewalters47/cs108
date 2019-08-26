'''
Dictionary practice
Created Spring 2019
Lab03
@author: Ethan Walters (emw45)
'''

# Add values to dictionary
scoreDict = {"Joe": 10, "Tom": 23, "Barb": 13, "Sue": 19, "Sally": 12}

# Print Barb's score
print(scoreDict["Barb"])

# Set Sally's score to 13
scoreDict["Sally"] = 13

# Remove Tom from the dictionary
del scoreDict["Tom"]

# Print the results
print(scoreDict)