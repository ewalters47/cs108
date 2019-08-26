"""
GUI for the calculator class
Created Spring 2019
Lab 11
@author: Ethan Walters (emw45)
"""
from old.lab11 import Calculator
from tkinter import *


class GUI:

    def __init__(self, window):

        self.window = window
        self.calc = Calculator()
        self.input1 = StringVar()
        self.input2 = StringVar()
        self.result = StringVar()

        # Create the first input label and entry
        input1_label = Label(window, text="Input 1:")
        input1_label.grid(row=0, column=0, sticky=E)
        input1_entry = Entry(window, width=6, textvariable=self.input1)
        input1_entry.grid(row=0, column=1, sticky=W)

        # Create the second input label and entry
        input2_label = Label(window, text="Input 2:")
        input2_label.grid(row=1, column=0, sticky=E)
        input2_entry = Entry(window, width=6, textvariable=self.input2)
        input2_entry.grid(row=1, column=1, sticky=W)

        # Create a frame for the operators
        operator_frame = Frame(window)
        operator_frame.grid(row=2, column=0, columnspan=2)

        self.operator = StringVar()
        self.operator.set('+')

        # Create the addition button
        add_button = Radiobutton(operator_frame, text="+", variable=self.operator, value='+')
        add_button.pack(side=LEFT)

        # Create the subtraction button
        subtract_button = Radiobutton(operator_frame, text="-", variable=self.operator, value='-')
        subtract_button.pack(side=LEFT)

        # Create the multiplication button
        multiply_button = Radiobutton(operator_frame, text="*", variable=self.operator, value='*')
        multiply_button.pack(side=LEFT)

        # Create the division button
        divide_button = Radiobutton(operator_frame, text="/", variable=self.operator, value='/')
        divide_button.pack(side=LEFT)

        # Create the calculate button that once clicked, calls the do_calculation method
        calculate_button = Button(window, text="Calculate", command=self.do_calculation)
        calculate_button.grid(row=3, column=0, sticky=W)

        # Create the result label
        result_label = Label(window, text="Result:")
        result_label.grid(row=3, column=1)

        # Create the result label that displays the output of the operation
        self.result_display_label = Label(window, textvariable=self.result, width=10)
        self.result_display_label.grid(row=3, column=2, sticky=W)

        # Create error label
        self.error_label_text = StringVar()
        self.error_label_text.set('Welcome to Calculator')
        error_label = Label(window, textvariable=self.error_label_text)
        error_label.grid(row=5, columnspan=2, sticky=W)

    def do_calculation(self):
        """This method calculates what the user has entered with exception handling"""
        try:
            result = self.calc.calculate(self.input1.get(), self.operator.get(), self.input2.get())
            self.result.set(result)
        except Exception as err:
            self.error_label_text.set(err)


if __name__ == '__main__':
    """Start the GUI loop"""
    root = Tk()
    root.title('Calculator')
    app = GUI(root)
    root.mainloop()
