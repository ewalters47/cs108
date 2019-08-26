"""
Final Project for CS108
Created Spring 2019
Description: Move with the arrow keys and avoid the falling enemies
GitHub Repo: https://github.com/ewalters47/cs108/tree/master/project
@author: Ethan Walters (emw45)
"""

# All code from helpers.py is from lab 12 helpers.py
from project.helpers import *


class Player:

	def __init__(self, x=600, y=550, radius=15, color="blue"):
		"""Set player instance variables"""
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color

	def render(self, canvas):
		"""Render the player on to the canvas"""

		canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.color, tag="player")

	def move_right(self, canvas):
		"""These methods move the player based on x/y coordinates within the boundaries of the canvas"""

		self.x += 10
		if self.x + self.radius > canvas.winfo_reqwidth():
			self.x -= 10

	def move_left(self):

		self.x -= 10
		if self.x - self.radius < 0:
			self.x += 10

	def move_up(self, canvas):

		self.y -= 10
		if self.y - self.radius < 0:
			self.y += 10

	def move_down(self, canvas):

		self.y += 10
		if self.y - self.radius > canvas.winfo_reqheight() - 30:
			self.y -= 10

	def get_radius(self):

		return self.radius

	def get_x(self):

		return self.x

	def get_y(self):

		return self.y


class Enemy:

	def __init__(self, x=50, y=50, radius=25, vel_y=3, color="white"):
		"""Set up enemy instance variables"""
		self.x = x
		self.y = y
		self.radius = radius
		self.vel_y = vel_y
		self.color = color
		self.width = 1200

	def render(self, canvas):
		"""Render the enemy onto the canvas"""

		canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.color, tag="enemy")

	def move(self, canvas):
		"""This method allows the enemy to move down and off the canvas"""

		self.y += self.vel_y

	def get_radius(self):

		return self.radius

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def check_collision(self, player):
		"""If the distance between the center of the player and the center of the enemy ball are less than
		the sum of both radii, there is a collision"""

		# distance is from lab 12 helpers.py
		return distance(self.x, self.y, player.get_x(), player.get_y()) <= (self.radius + player.get_radius())


# Driver code
if __name__ == '__main__':
	test = Enemy()
	print(test.get_y())
	print(test.get_radius())
