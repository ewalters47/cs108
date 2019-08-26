'''
Model a single particle
Created Fall 2014
Updated Summer, 2015
Updated Fall, 2018
Updated Spring 2019

@author: smn4
@author: kvlinden
@author: cwieri39
@author: Ethan Walters (emw45) - used for lab 12
'''

from old.lab12.helpers import *
import math

DAMPENING_FACTOR = 0.88





class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''

    def __init__(self, x=50, y=50, velX=10, velY=15, radius=15, color='#663977'):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.radius = radius
        self.color = color

    def render(self, canvas):
        '''
        Render a particle onto the canvas
        '''

        canvas.create_oval(self.x - self.radius,
                           self.y - self.radius,
                           self.x + self.radius,
                           self.y + self.radius,
                           fill=self.color)

    def get_radius(self):

        return self.radius

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y

    def move_right(self, canvas):

        self.x += 10

    def move(self, canvas):
        '''
        The move method allows a particle to move on the canvas within its boundries
        '''

        self.x += self.velX
        self.y += self.velY

        if self.x + self.radius > canvas.winfo_reqwidth() or self.x - self.radius < 0:
            self.velX *= -1

        if self.y - self.radius > canvas.winfo_reqheight() or self.y - self.radius < 0:
            self.velY *= -1

    # def is_clicked(self, event):
    #
    #     return distance(event.x, event.y, self.x, self.y) < self.radius

    def hits(self, other):
        if self == other:
            # I can't collide with myself.
            return False
        else:
            # Determine if I overlap with the target particle.
            return (self.radius + other.get_radius()) >= distance(self.x, self.y, other.get_x(), other.get_y())

    def bounce(self, target):
        ''' This method modifies this Particle object's velocities based on its
            collision with the given target particle. It modifies both the magnitude
            and the direction of the velocities based on the interacting magnitude
            and direction of particles. It only changes the velocities of this
            object; an additional call to bounce() on the other particle is required
            to implement a complete bounce interaction.

            The collision algorithm is based on a similar algorithm published by K.
            Terzidis, Algorithms for Visual Design.

            target  the other particle
         '''
        if self.hits(target):
            print("tests passed.....")


