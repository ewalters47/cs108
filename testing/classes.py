from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window
        self.width = 800
        self.height = 600
        self.canvas = Canvas(width=self.width, height=self.height, bg="grey")
        self.canvas.pack()

        self.add_square()
    def add_square(self):

        square = Square

class Square:

    def __init__(self):

        self.width = 100
        self.height = 100
        self.canvas.create_rectangle(width=self.width, height=self.height)






if __name__ == "__main__":
    root = Tk()
    root.title("Test GUI")
    root.geometry("800x600")
    app = GUI(root)
    root.mainloop()