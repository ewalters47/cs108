from tkinter import *


class GUI:

    def __init__(self, window):

        self.window = window
        self.width = 800
        self.height = 600
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()

        self.canvas.create_rectangle(34, 65, 120, 146, fill="red")





if __name__ == '__main__':
    root = Tk()
    root.title('Test GUI')
    app = GUI(root)
    root.mainloop()