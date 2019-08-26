"""
Loan calculator GUI
Created Spring 2019
Homework 11
@author: Ethan Walters (emw45)
"""

from tkinter import *
from old.homework11.loan import Loan


class GUI:

    def __init__(self, window):

        self.window = window
        self.calc = Loan
        self.years = StringVar()
        self.principal = StringVar()
        self.interest = StringVar()
        self.result = StringVar()

        years_label = Label(window, text="Enter length in years:")
        years_label.grid(row=0, column=0, sticky=W)
        years_input = Entry(window, width=8, textvariable=self.years)
        years_input.grid(row=0, column=1)

        principal_label = Label(window, text="Enter loan amount:")
        principal_label.grid(row=1, column=0, sticky=W)
        principal_input = Entry(window, width=8, textvariable=self.principal)
        principal_input.grid(row=1, column=1)

        interest_label = Label(window, text="Enter annual interest:")
        interest_label.grid(row=2, column=0, sticky=W)
        interest_input = Entry(window, width=8, textvariable=self.interest)
        interest_input.grid(row=2, column=1)

        calculate_button = Button(window, text="Calculate", command=self.calculate)
        calculate_button.grid(row=3, column=0, sticky=W, pady=5)

        result_label = Label(window, text='Result:')
        result_label.grid(row=4, column=0, sticky=W)

        self.result_display_label = Label(window, textvariable=self.result)
        self.result_display_label.grid(row=4, column=1, sticky=W)

        self.error_label_text = StringVar()
        self.error_label_text.set('Welcome to Loan Calculator')
        error_label = Label(window, textvariable=self.error_label_text)
        error_label.grid(row=5, column=0, sticky=W)

    def calculate(self):
        try:
            result = self.calc.compute_monthly_payment(self.years.get(), self.principal.get(), self.interest.get())
            self.result.set(result)
        except Exception as err:
            self.error_label_text.set(err)


if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.title('Loan Calculator')
    root.geometry("300x200")
    root.mainloop()
