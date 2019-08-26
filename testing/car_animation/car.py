"""
Created Fall 2014
Updated to a separate class, Summer, 2015

@author: smn4
@author: kvlinden
@author ds33
"""

class Car:
    """ Encapsulate the car object.
        Invariant:
            vertical_velocity >= 0 or y > height
    """
    
    def __init__(self, width=0, height=0, velocity=0, body_color='black'):
        """ Create a car object with the given color for depiction
        on a canvas with the given width and height. """
        self.x = 0        # Start on the far left...
        self.y = height   # ...at the bottom of the canvas.
        self.width = width
        self.height = height
        self.velocity = velocity
        self.vertical_velocity = 0
        self.body_color = body_color

    def modify_velocity(self, delta):
        """ Update the car's horizontal velocity. """
        self.velocity += delta
    
    def modify_vertical_velocity(self, delta):
        """ Update the car's vertical velocity, provided that
        it stay above ground. And make sure that it's never negative.
        """
        if delta >= 0.0 or self.y < self.height:
            self.vertical_velocity += delta
        else:
            self.vertical_velocity = max(self.vertical_velocity, 0)
    
    def move(self):
        """ Move the car based on the horizontal and vertical velocities
        and the given canvas width and height.
        """
        self.x = (self.x + self.velocity) % self.width
        self.y = min((self.y - self.vertical_velocity), self.height)

    def render(self, canvas):
        """ Draw the current state of the car on the given canvas. """

        canvas.create_rectangle(self.x, self.y-20, self.x+50, self.y-10,
                                fill=self.body_color)  # body
        canvas.create_polygon(self.x+10, self.y-20,
                              self.x+20, self.y-30,
                              self.x+30, self.y-30,
                              self.x+40, self.y-20,
                              outline='black', fill='white')  # windows

        # Draw the wheels if the car is on, or near, the ground.
        if self.y >= self.height - 5:
            canvas.create_oval(self.x + 10, self.y - 10, self.x + 20, self.y,
                               fill='black')  # wheel one
            canvas.create_oval(self.x + 30, self.y - 10, self.x + 40, self.y,
                               fill='black')  # wheel two
        # Draw a wing if the car is in the air
        else:
            canvas.create_polygon(self.x + 7, self.y - 10,
                                  self.x + 37, self.y - 10,
                                  self.x + 5, self.y + 2,
                                  outline='black', fill='grey')  # a wing


if __name__ == '__main__':

    c = Car()
    assert c.x == 0
    assert c.y == 0
    assert c.vertical_velocity == 0
    c.modify_vertical_velocity(-1)
    assert c.vertical_velocity == 0

    print('all tests passed...')
