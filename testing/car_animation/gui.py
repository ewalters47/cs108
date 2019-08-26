"""
Created Fall 2014
Updated, Summer, 2015

@author: smn4
@author: kvlinden
"""
from tkinter import *
from testing.car_animation.car import Car


class CarAnimation:
    
    def __init__(self, window):
        """ Create a car animation GUI. """

        self.window = window
        width = 600
        height = 200
        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        control_frame = Frame(window)
        control_frame.pack(pady=5)
        self.pause_button = Button(control_frame, text="Pause",
                                   command=self.pause)
        self.pause_button.pack(side=LEFT)
        self.resume_button = Button(control_frame, text="Resume",
                                    command=self.resume,
                                    state=DISABLED)
        self.resume_button.pack(side=LEFT)
        self.faster_button = Button(control_frame, text="Faster",
                                    command=self.faster)
        self.faster_button.pack(side=LEFT)
        self.slower_button = Button(control_frame, text="Slower",
                                    command=self.slower)
        self.slower_button.pack(side=LEFT)
        self.fly_button = Button(control_frame, text="Fly",
                                 command=self.fly)
        self.fly_button.pack(side=LEFT)
        self.land_button = Button(control_frame, text="Land",
                                  command=self.land)
        self.land_button.pack(side=LEFT)
        
        self.car = Car(width=width, height=height,
                       velocity=5, body_color='blue')
        self.terminated = False
        self.paused = False
        self.rate = 50  # wait time between frames

        # Schedule the first animation frame.
        self.window.after(0, self.animation)

    def animation(self):
        """Run one animation frame and then schedule the next."""

        if not self.paused:
            self.canvas.delete(ALL)
            self.car.move()
            self.car.render(self.canvas)

        # Schedule the next animation frame.
        self.window.after(self.rate, self.animation)

    def pause(self):
        """ Stop the car animation temporarily. """
        self.paused = True
        self.pause_button.config(state='disabled')
        self.resume_button.config(state='active')

    def resume(self):
        """ Restart the car animation. """
        self.paused = False
        self.pause_button.config(state='active')
        self.resume_button.config(state='disabled')

    def faster(self):
        """ Speed the car up. """
        self.car.modify_velocity(2)

    def slower(self):
        """ Slow the car down. """
        self.car.modify_velocity(-2)
        
    def fly(self):
        """ Make the car rise up. """
        self.car.modify_vertical_velocity(2)

    def land(self):
        """ Make the car come down. """
        self.car.modify_vertical_velocity(-2)


if __name__ == '__main__':
    root = Tk()
    root.title('Skytrip')
    app = CarAnimation(root)
    root.mainloop()