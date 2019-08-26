"""
Using classes to model fractions
Created Spring 2019
Lab 08
@author: Ethan Walters (emw45)
"""
import sys


def computeGCD(alpha, beta):
    """
    This function computes the lowest common divisor given a fraction
    """
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta

# Main fraction class
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        """Initializes the fraction object"""
        if denominator != 0:
            self.numerator = numerator
            self.denominator = denominator
            self.simplify()
        else:
            print('Unable to create invalid fraction', file=sys.stderr)
            sys.exit(-1)

    def __str__(self):
        """
        String method that prints out the fraction to console
        """
        return str(self.numerator) + '/' + str(self.denominator)

    def get_numerator(self):
        """
        Accessor method to get the numerator
        """
        return self.numerator

    def get_denominator(self):
        """
        Accessor method to get the denominator
        """
        return self.denominator

    def simplify(self):
        """
        Method that simplifies a fraction based on conditions (e.g. fraction 2/4 --> 1/2)
        """
        gcd = computeGCD(self.numerator, self.denominator)
        if gcd != 0:
            self.numerator = self.numerator//gcd
            self.denominator = self.denominator//gcd
        elif self.denominator < 0:
            self.numerator = self.numerator * -1
            self.denominator = self.denominator * -1

    def __mul__(self, other):
        """
        Method that multiplies two fraction objects together
        """
        self.numerator = self.numerator * other.get_numerator()
        self.denominator = self.denominator * other.get_denominator()

# Test cases
f2 = Fraction(1, 2)
f_num = Fraction.get_numerator(1)
# bad_fraction = Fraction(2, 0)
# bad_fraction2 = Fraction(1/2)

f3 = Fraction(2, 4)
f4 = Fraction(3, 6)
f5 = Fraction(4, 8)

print(f2)
print(f_num)
print(f3)
print(f4)
print(f5)
