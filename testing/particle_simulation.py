


'''
GUI controller for a particle simulation
Lab 12
November 29, 2018
@author: Ethan Walters (emw45)
@author: kvlinden
'''

from tkinter import *
from random import randint
from testing.particle import *
from testing.helpers import *

class ParticleSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the particle simulator GUI '''
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.width)
        self.canvas.bind('<Button-1>', self.check_remove_particle)
        self.canvas.pack()
        self.terminated = False
        self.p_list = []
        Button(self.window, text='Add Particle', command=self.add_particle).pack()    
        Button(window, text='Quit', command=self.safe_exit).pack()
        
        while not self.terminated:
            self.canvas.delete(ALL)
            for particle in self.p_list:
                particle.move(self.canvas)
                particle.render(self.canvas)
                for p2 in self.p_list:
                    particle.bounce(p2)
            self.canvas.after(50)
            self.canvas.update()
    
    
    #Define the add_particle method to add a particle once a button click event has taken place
    def add_particle(self):
        rand_velx = randint(-25, 25)
        rand_vely = randint(-25, 25)
        rand_radius = randint(5, 25)
        rand_x = randint(25, self.canvas.winfo_reqwidth() - 25)
        rand_y = randint(25, self.canvas.winfo_reqheight() - 25)
        rand_color = get_random_color()
        rand_particle = Particle(velX = rand_velx, velY = rand_vely, x = rand_x, y = rand_y, radius = rand_radius, color = rand_color)
        self.p_list.append(rand_particle)
    
    #Remove a particle from the list and canvas if a user clicks on a particle    
    def check_remove_particle(self, event):
        copy = self.p_list[:]
        for particle in copy:
            if distance(event.x, event.y, particle.get_x(), particle.get_y()) <= particle.get_radius():
                self.p_list.remove(particle)
    
    #Safely exit the GUI program        
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()
    
