'''
A GUI controller for a Tic-Tac-Toe game...

For a discussion of using a lambda function to pass the current value
of a variable to a callable, function object under closure, see:
    http://tkinter.unpythonic.net/wiki/CallbackConfusion

Created Fall, 2014
Updated Summer, 2015

@author: Serita Nelesen
@author: kvlinden

'''
from tkinter import *
from game import TicTacToe


class App:

    def __init__(self, window):
        ''' Initialize a 3X3 Tic-Tac-Toe GUI '''
        self.WIDTH = 3
        self._game = TicTacToe(self.WIDTH)
        window.bind("<Key>", self.process_key_event)

        # Create and place all nine buttons, then draw the (empty) board.
        self._buttons = []
        for i in range(self.WIDTH * self.WIDTH):
            button = Button(window, width=3, height=1, font=('Helvetica', 48),
                            command=lambda i=i: self.process(i))
            self._buttons.append(button)
            button.grid(row=i // self.WIDTH, column=i % self.WIDTH)
        self.draw_board()

        # Create and place the information bar.
        self._message_variable = StringVar()
        self._message_variable.set('Welcome...')
        label = Label(window, font=('Helvetica', 10), textvariable=self._message_variable)
        label.grid(row=self.WIDTH, column=0, columnspan=self.WIDTH, sticky=W)

    def draw_board(self):
        ''' Draw the current state of the board on the GUI using the game model state '''
        for i in range(self.WIDTH * self.WIDTH):
            self._buttons[i].config(text=self._game.get_cell(i // self.WIDTH, i % self.WIDTH))

    def disable_buttons(self):
        ''' Turn off input for all the buttons, regardless of their current state '''
        for button in self._buttons:
            button.config(state='disabled')

    def process(self, button_number):
        ''' Process a click of button with the given button_number '''
        try:
            self._game.make_move(button_number // self.WIDTH, button_number % self.WIDTH)
            self._buttons[button_number].config(state='disabled')
            self.draw_board()
            winner = self._game.get_winner()
            if winner != None:
                self._message_variable.set('{0} wins!'.format(winner))
                self.disable_buttons()
            elif self._game.is_cat_game():
                self._message_variable.set('Draw...')
            else:
                self._message_variable.set('')
        except ValueError as e:
            self._message_variable.set(e)

    def process_key_event(self, event):
        '''Move the expanding circle's center based on the arrow keys.
           Also, change color using the 'c' key.
        '''
        print('keysym?', event.keysym)


if __name__ == '__main__':
    root = Tk()
    root.title('Tic Tac Toe')
    app = App(root)
    root.mainloop()
