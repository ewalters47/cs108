"""
Modules and files
Created Spring 2019
Lab 09
@author: Ethan Walters (emw45)
"""

import sys


class Employee:
    """Create employee class with required instance variables"""
    def __init__(self, line=''):

        if line == '':
            self.first = 'John'
            self.last = 'Smith'
            self.rank = 'IT Director'
            self.salary = 43

            if self.salary < 20000:
                print('Error: Salary must be greater than $20000', sys.stderr)
                sys.exit(-1)

        else:
            strings = line.split()
            self.first = strings[0]
            self.last = strings[1]
            self.rank = strings[2]
            self.salary = int(strings[3])

    def __str__(self):
        """Set up string method to return a string of data"""

        return  '%s, %s.: %s, ($%d)' % (self.last, self.first[0], self.rank, self.salary)

    def get_rank(self):
        """Accessor method to get the rank of an employee"""
        return self.rank

    def get_salary(self):
        """Accessor method to get the salary of an employee"""
        return self.salary


if __name__ == '__main__':
    # Test cases
    p1 = Employee()
    print(p1)
    print(p1.get_rank())
    print(p1.get_salary())
