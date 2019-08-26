'''
How to get key events
Created Fall 2014
@author: smn4
'''
from tkinter import *

class Key_Event_Demo:
    def __init__(self, window):
#         window.geometry('+1500+100')
        
        canvas = Canvas(window, bg='white',
                        width = 300, height = 200)
        canvas.pack()
        
        canvas.bind("<Key>", self.processKeyEvent)   
        canvas.focus_set() 
    
    def processKeyEvent(self, event):
        print("keysym?", event.keysym)
        print("char?", event.char)
        print("keycode?", event.keycode)

if __name__ == '__main__':
    window = Tk()
    window.title("Key Events")
    app = Key_Event_Demo(window)
    window.mainloop()