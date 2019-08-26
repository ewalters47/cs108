'''
This GUI view for the country-guess game quizzes the user on country names
randomly chosen by the country-guess model class giving the hints provided
by the model.

Created Summer, 2015

@author: kvlinden
'''
from tkinter import *

from testing.country_guess.game import Game


class App:
    '''This class implements a GUI for the country-guess game.'''
    
    def __init__(self, window):
        '''Build the country-guess GUI window'''
        
        # Define the model game object using countries listed in countries.txt.
        self._game = Game('countries.txt')
        
        main_frame = Frame(window)
        main_frame.pack(padx=10, pady=10)
        label_font = ('Helvetica')        
        
        # Display a world map on the main window.
        logo = PhotoImage(file='images/who.gif')
        image_label = Label(main_frame, image=logo)
        image_label.image = logo
        image_label.pack()

        # Set up the basic user prompt widget.
        self._hint_variable = StringVar()
        self._hint_variable.set('Try to guess a country. {0}'.format(self._game.get_hint()))
        hint_label = Label(main_frame, textvariable=self._hint_variable, font=label_font)
        hint_label.pack(anchor=W)

        # Set up a user control panel for guessing and giving up.
        # The answer input box responds to either a Guess button press or an enter.
        input_frame = Frame(main_frame)
        input_frame.pack(anchor=W, fill=X)
        self._entry_variable = StringVar()
        entry_field = Entry(input_frame, textvariable=self._entry_variable, font=label_font)
        entry_field.bind('<Return>', self.guess)
        entry_field.pack(side=LEFT, padx=5)
        guess_button = Button(input_frame, text='Guess', command=self.guess, font=label_font)
        guess_button.pack(side=LEFT, padx=5)
        giveup_button = Button(input_frame, text='Give Up', command=self.give_up, font=label_font)
        giveup_button.pack(side=LEFT, padx=5)
        quit_button = Button(input_frame, text='Quit', command=main_frame.quit, font=label_font)
        quit_button.pack(side=RIGHT)
    
    def guess(self, event=None):
        '''Process a user guess - If it's correct move on to a new question;
        if it's incorrect, give a hint.'''
        if self._game.check_answer(self._entry_variable.get()):
            self._game.reset()
            self._hint_variable.set('Good! Try another. {0}'.format(self._game.get_hint()))
        else:
            self._hint_variable.set('Nope... Try again. {0}'.format(self._game.get_hint()))
        self._entry_variable.set('')
            
    def give_up(self):
        '''Process a user give-up request by giving the answer and moving on
        to a new question.'''
        answer = self._game.get_answer()
        self._game.reset()
        hint = self._game.get_hint() 
        self._hint_variable.set('The answer was {0}. Try another. {1}'.format(answer, hint))
        self._entry_variable.set('')
        

if __name__ == '__main__':
    # Construct and start the main GUI interface.
    root = Tk()
    root.title('Country Guess')
    app = App(root)
    root.mainloop()
