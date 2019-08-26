"""
Loan class for loan calculator GUI
Created Spring 2019
Homework 11
@author: Ethan Walters (emw45)
"""


class Loan:

    def __init__(self, years, principal, interest):

        if self.years and self.principal and self.interest < 0:
            raise ValueError('Values must be greater than 0')
        else:
            self.years = years
            self.principal = principal
            self.interest = interest / 100

    def set_years(self, new_years):

        self.years = new_years

    def set_principal(self, new_principal):

        self.principal = new_principal

    def set_interest(self, new_interest):

        self.interest = new_interest

    def compute_monthly_payment(self):

        n = self.years * 12  # number of monthly payments
        i = (self.interest / 100) / 12  # monthly interest rate (decimal)
        monthly_payment = (i * self.principal * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
