from tkinter import *

class Main:

    def __init__(self, window):

        self.window = window
        self.canvas = Canvas(window, width=600, height=400)
        self.canvas.pack(fill=BOTH)

        self.render()

    def render(self):
        self.canvas.create_line(34, 67, 50, 67)


if __name__ == '__main__':
    root = Tk()
    app = Main(root)
    root.mainloop()
