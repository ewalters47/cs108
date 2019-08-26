from tkinter import *


def convert():

    gb_val = gb_unit.get()
    mb_unit.set(gb_val * 1024)


root = Tk()
root.geometry("300x200")
root.title('GB to MB Conversion')

frame = Frame(root)
frame.pack()

mb_unit = DoubleVar()
gb_unit = DoubleVar()

input_gb_label = Label(frame, text='Input amount in GB:')
input_gb_label.grid(row=0, column=0)

gb_entry = Entry(frame, width=8, textvariable=gb_unit)
gb_entry.grid(row=0, column=1)

convert_button = Button(frame, text='Convert', command=convert)
convert_button.grid(row=0, column=2)

is_equal_text = Label(frame, text='Is equal to:')
is_equal_text.grid(row=1, column=0, sticky=E)

mb_output = Label(frame, textvariable=mb_unit)
mb_output.grid(row=1, column=1, sticky=W)

mb_output_txt = Label(frame, text='MB')
mb_output_txt.grid(row=1, column=2, sticky=W)







root.mainloop()