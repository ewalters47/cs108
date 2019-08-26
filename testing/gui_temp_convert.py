from tkinter import *


def convert():

    val = temp_c.get()
    temp_f.set((val * 9.0 / 5) + 32)


root = Tk()
root.geometry("300x200")
root.title("GUI Temp Convert")

frame = Frame(root)
frame.pack()


temp_c = DoubleVar()
temp_f = DoubleVar()


celsius_label = Label(frame, text='Input temp in C:')
celsius_label.grid(row=0, column=0)

celsius_input = Entry(frame, width=8, textvariable=temp_c)
celsius_input.grid(row=0, column=1)

fahrenheit_label = Label(frame, text='Temp in F:')
fahrenheit_label.grid(row=1, column=0)

convert_button = Button(frame, text='Convert', command=convert)
convert_button.grid(row=0, column=2)

f_result_label = Label(frame, textvariable=temp_f)
f_result_label.grid(row=1, column=1, sticky=W)

root.mainloop()

