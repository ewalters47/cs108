from project.helpers import *  # Just for random color function


class Player:

	def __init__(self, x=100, y=200, color="blue"):

		self.x = x
		self.y = y
		self.color = color

	def render(self, canvas):

		canvas.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill=self.color)

	def move_right(self):

		self.x += 10

	def move_left(self):

		self.x -= 10

	def move_up(self):

		self.y -= 10

	def move_down(self):

		self.y += 10


class Rectangles:

	def __init__(self, x=200, y=300, vel_x=10, vel_y=randint(3, 10)):

		self.x = x
		self.y = y
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.color = get_random_color()

	def render(self, canvas):

		rect1 = canvas.create_rectangle(self.x, self.y, self.x+50, self.y+200, fill=self.color)
		rect2 = canvas.create_rectangle(self.x+300, self.y+100, self.x+350, self.y+250, fill=self.color)

	def move(self, canvas):

		self.y += self.vel_y

		if self.y < 0 or self.y > canvas.winfo_height():  # top & bottom of canvas, don't need to change x
			self.vel_y = -self.vel_y
