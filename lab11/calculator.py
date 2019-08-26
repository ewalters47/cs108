"""
Provide calculator functionality
Created Fall 2014
Updated Summer 2015
Updated Spring 2019: for lab11

@author: smn4
@author: kvlinden
@author: Ethan Walters (emw45)
"""


class Calculator:
    
    def __init__(self):
        """ Initialize calculator memory to 0 """
        self._memory = 0

    def calculate(self, operand1, operator, operand2):
        """ Perform the specified calculation """
        try:
            operand1 = float(operand1)
        except ValueError:
            raise ValueError('could not convert string to float: \'' + operand1 + '\'')
        try:
            operand2 = float(operand2)
        except ValueError:
            raise ValueError('could not convert string to float: \'' + operand2 + '\'')
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        else:
            raise ValueError('Invalid operation: ' + operator)


if __name__ == '__main__':
    # Do a simple test of 1+1. See the more extensive tests in test.py.
    calc = Calculator()
    print(calc.calculate('2', '*', '4'))
