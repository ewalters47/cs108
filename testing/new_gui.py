'''
GUI Test
@author: Ethan Walters
'''

from tkinter import *

root = Tk()
root.geometry("800x600")
root.title('Test GUI')

c = Canvas(root, width=800, height=600)
c.pack()

pic = PhotoImage(file='meme.ppm')

c.create_image(200, 200, image=pic)

root.mainloop()