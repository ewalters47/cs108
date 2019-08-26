"""
Final Project for CS108
Created Spring 2019
Description: Move with the arrow keys and avoid the falling enemies
GitHub Repo: https://github.com/ewalters47/cs108/tree/master/project
@author: Ethan Walters (emw45)
"""


from project.game import *
# All code from helpers.py is from lab 12 helpers.py
from project.helpers import *
from tkinter import *


class GUI:

	def __init__(self, window, width=1200, height=600):
		"""Set up instances of other classes and the enemy list"""

		self.player = Player()
		self.enemy = Enemy()
		self.enemy_list = []
		self.error = StringVar()
		self.result = StringVar()
		self.lives = StringVar()
		self.lives = 5

		# Set up canvas
		self.window = window
		self.width = width
		self.height = height
		self.canvas = Canvas(window, width=self.width, height=self.height, bg="gray")
		self.canvas.pack()

		# Set up animation variables
		self.rate = 50
		self.terminated = True
		self.window.after(0, self.animation)

		# Create the control frame for buttons and bind the arrow keys to the process_keys method
		self.control_frame = Frame(window)
		self.control_frame.pack(side=BOTTOM, pady=2)
		self.error_frame = Frame(window)
		self.error_frame.pack(side=BOTTOM, pady=2)

		self.canvas.bind("<Key>", self.process_keys)
		self.canvas.focus_set()

		# Welcome text that displays when module is first run, this disappears once the game has started
		self.welcome_text = self.canvas.create_text(600, 300, fill="red", font="Tahoma 24", text="Welcome! Press Start to Play Game")

		# Call the create_widgets method
		self.create_widgets()

	def create_widgets(self):
		"""Set up all buttons on the bottom of the GUI"""

		play_button = Button(self.control_frame, text="Start", command=self.start)
		play_button.pack(side=LEFT, padx=2)

		restart_button = Button(self.control_frame, text="Restart", command=self.reset)
		restart_button.pack(side=LEFT, padx=2)

		quit_button = Button(self.control_frame, text="Quit", command=self.quit)
		quit_button.pack(side=LEFT)

		life_label = Label(self.control_frame, text="Lives:")
		life_label.pack(side=LEFT, padx=2)

		life_update_label = Label(self.control_frame, textvariable=self.result)
		life_update_label.pack(side=RIGHT, padx=2)

		error_label = Label(self.error_frame, textvariable=self.error)
		error_label.pack(side=RIGHT, padx=2)

		info_label = Label(self.error_frame, text="Welcome to Dodger! Use the arrow keys to avoid the falling enemies for as long as you can.")
		info_label.pack(side=BOTTOM, pady=2)

	def start(self):
		"""Once the user has clicked the Start button, call this method to begin the game - this will start the
		animation loop"""
		self.terminated = False

	def game_over(self):
		"""If the player has collided with an enemy, this method gets called"""

		self.terminated = True
		self.canvas.create_text(600, 300, fill="red", font="Tahoma 48", text="Game Over!", tag="game_over")

	def reset(self):
		"""Clear all canvas items. For some reason .delete(ALL) doesn't work here so tags are used"""
		self.canvas.delete("enemy")
		self.canvas.delete("player")
		self.canvas.delete("game_over")

	def update_life(self):

		try:
			if self.lives >= 0:
				result = self.lives
				self.result.set(self.lives)
				self.lives -= 1

				self.result.set(result)
			else:
				raise ValueError("Value must be greater than 0")
		except ValueError as err:
			self.error.set(err)

	def create_random_enemy(self):
		"""Create a random enemy based on the Enemy class - concept is from lab 12"""
		rand_enemy = Enemy(randint(25, self.width - 25), randint(25, 30), 10, randint(1, 2), get_random_color())
		self.enemy_list.append(rand_enemy)

	def animation(self):
		"""Create animation loop"""
		if not self.terminated:
			self.canvas.delete(ALL)
			self.player.render(self.canvas)  # Render the player (blue ball)
			self.create_random_enemy()  # Call the create_random_enemy method

			for e in self.enemy_list:
				e.render(self.canvas)  # Render the enemy on to the canvas
				e.move(self.canvas)  # Move the enemy down based on its velocity
				if e.check_collision(self.player):  # Check for collision against the player - if it's true, then call the game_over method
					self.game_over()
					self.canvas.delete("enemy")
					self.update_life()

		self.window.after(self.rate, self.animation)  # Schedule next animation frame

	def process_keys(self, event):
		"""Set up arrow keys to correspond to the player movements (left, right, up, down)"""
		if event.keysym == "Right":
			self.player.move_right(self.canvas)
		if event.keysym == "Left":
			self.player.move_left()
		if event.keysym == "Up":
			self.player.move_up(self.canvas)
		if event.keysym == "Down":
			self.player.move_down(self.canvas)

	def quit(self):
		self.window.destroy()  # Once user has clicked the quit button, exit the GUI program


# Driver code
if __name__ == '__main__':
	root = Tk()
	root.title('Dodger')
	app = GUI(root)
	root.mainloop()
