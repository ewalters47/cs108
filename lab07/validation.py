'''
Python program that uses string methods for validation
Created Spring 2019
Lab07
@author: Ethan Walters (emw45)
'''


# Define isValidSSN function
def isValidSSN(string):
    if len(string) == 11 and string[3] == '-' and string[6] == '-' and string[0:3].isdigit() and string[4:6].isdigit() and string[7:10]:
        return True
    else:
        return False


# Define isValidPassword function
def isValidPassword(password):
    digits = 0
    if len(password) >= 8:
        for char in password:
            if char.isdigit() or char.isalpha():
                if char.isdigit():
                    digits += 1
                continue
            else:
                return False
                break
        if digits >= 2:
            return True
        else:
            return False
    else:
        return False


# Define isValidPrefix function
def isValidPrefix(card_number):
    if card_number[0:2] == '37' or card_number[0] == '4' or card_number[0] == '5' or card_number[0] == '6':
        return True
    else:
        return False


# Define sum_of_odds function
def sum_of_odds(card_number):
    numsum = 0
    pos = 0
    for digit in card_number:
        if pos % 2 == 0:
            numsum + int(digit)
        pos += 1
    return numsum

# Define sum_of_double_evens function
def sum_of_double_evens(card_number):
    numsum = 0
    pos = 0
    for digit in card_number:
        if pos % 2 == 0:
            numsum += 2 * int(digit)
    return numsum

# Define isValidCC function
def isValidCC(cc):
    if isValidPrefix(cc) and len(cc) >= 13 and len(cc) <= 16 and cc.isdigit() and sum_of_odds(cc) + sum_of_double_evens(cc) % 10:
        return True
    else:
        return False


def printMenu():
    '''Print the text menu.'''
    print('\nPlease select from the following list of options (type the appropriate character):')
    print('A. Social security number validation')
    print('B. Password validation')
    print('C. Credit card validation')
    # Add menu options here for three new string tests.
    print('Q. Quit')


# Run the text-menu interface until the user wants to quit.
while True:
    printMenu()
    choice = input('Choice: ').upper()

    # Use if statements to call required functions based on what the user inputs in the console
    if choice == 'A':
        ssn = input('Enter social security number: ')
        if isValidSSN(ssn):
            print('This is a valid SSN')
        else:
            print('This is an invalid SSN')
    elif choice == 'B':
        pword = input('Enter a password: ')
        if isValidPassword(pword):
            print('This is a valid password')
        else:
            print('This is an invalid password')
    elif choice == 'C':
        credit_card = input('Input a credit card number: ')
        if isValidCC(credit_card):
            print('This is a valid credit card')
        else:
            print('This is an invalid credit card')

    # Add code here to handle tests for the three string types.
    # Each option should read a value from the user, pass it to the appropriate check routine and print the result.

    elif choice == 'Q':
        break

    else:
        print('I\'m sorry, {0} is not a valid option.'.format(choice))

print('\nGood-bye!')
