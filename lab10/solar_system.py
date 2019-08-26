"""
Exceptions & Testing
Created Spring 2019
Lab 10
@author: Ethan Walters (emw45)
"""

# Import required modules


class SolarSystem:

    def __init__(self):
        self.sun = None
        self.planets = []

    def add_sun(self, a_sun):
        if isinstance(a_sun, Sun):
            self.sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system')
        self._sun = a_sun

    def add_planet(self, a_planet):
        if isinstance(a_planet, Planet):
            self.planet = a_planet
        else:
            raise TypeError('add_planet(): cannot add' + str(type(a_planet)) + ' to solar system')
        self.planets.append(a_planet)

    def showplanets(self):
        for a_planet in self.planets:
            print(a_planet)
