"""
Exceptions & Testing
Created Spring 2019
Lab 10
@author: Ethan Walters (emw45)
"""

# Import required modules
import turtle
from old.lab10 import Sun
from old.lab10 import Planet
from old.lab10 import SolarSystem

# Set up turtle window
window = turtle.Screen()
window.setworldcoordinates(-1, -1, 1, 1)

# Create new solar system
ss = SolarSystem()
ss.add_sun(Sun("SUN", 8.5, 1000, 5800, 'yellow'))  # Add sun
ss.add_planet(Planet("EARTH", .475, 5000, 0.6, 'blue'))  # Add earth

# Get user inputs for adding a new planet to solar system
planet_name = input('Enter the name of the planet: ')
planet_rad = float(input('Enter the radius of the planet: '))
planet_mass = float(input('Enter the mass of the planet: '))
planet_dist = float(input('Enter the distance from the sun: '))
planet_color = input('Enter planet color: ')
# Error handling
try:
    user_planet = Planet(planet_name, planet_rad, planet_mass, planet_dist, planet_color)
    ss.add_planet(user_planet)
except ValueError as err:
    print(err)

# Keep the window open until it is clicked
window.exitonclick()
