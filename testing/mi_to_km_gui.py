from tkinter import *
import random

root = Tk()



red = (255, 0, 0)
color = red

class GUI:

    def __init__(self, width=800, height=600):

        self.canvas = Canvas(width, height)
        self.color = color
        self.canvas.pack()




app = GUI()
root.mainloop()