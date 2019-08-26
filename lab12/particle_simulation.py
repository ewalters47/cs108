'''
GUI controller for a particle simulation
Created Fall 2014
Updated Spring 2019

@author: smn4
@author: kvlinden - updated to use callback animation, Fall, 2018
@author: Ethan Walters (emw45) - used for lab 12
'''

from tkinter import *
from old.lab12.particle import *
from old.lab12.helpers import *

class ParticleSimulation:

    def __init__(self, window):

        self.window = window
        self.particle = Particle()
        self.width = 400
        self.delay = 50
        self.p_list = []

        '''Create the canvas'''
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.width)
        self.canvas.pack()
        self.canvas.after(0, self.animation)

        add_particle_button = Button(window, text="Add Particle", command=self.add_particle)
        add_particle_button.pack()

        self.canvas.bind("<Key>", self.process_keys)
        self.canvas.focus_set()

        self.terminated = False

    def process_keys(self, event):
        """Set up arrow keys to correspond to the player movements (left, right, up, down)"""
        if event.keysym == "Right":
            self.particle.move_right(self.canvas)

    def add_particle(self):
        '''Define the add_particle method to create a random particle that 
        renders to the canvas once the button click event has been called'''
        rand_particle = Particle(randint(25, self.width - 25), randint(25, self.width - 25), randint(-25, 25), randint(-25, 25), randint(5, 25), get_random_color())
        self.p_list.append(rand_particle)

    def animation(self):
        '''Set up animation loop for particles'''
        self.canvas.delete(ALL)
        for p1 in self.p_list:

            p1.move(self.canvas)
            p1.render(self.canvas)
            for p2 in self.p_list:
                p1.bounce(p2)
        self.canvas.after(self.delay, self.animation)

    # def check_remove_particle(self, event):
    #
    #     copy = self.p_list[:]
    #
    #     for p in copy:
    #         if Particle.is_clicked():
    #             self.p_list.remove(p)


if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')
    app = ParticleSimulation(root)
    root.mainloop()
