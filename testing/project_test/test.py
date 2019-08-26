from tkinter import *
from testing.project_test.helpers import *

class App:

	def __init__(self, window, width=1200, height=600, x=100, y=200, vel_y=randint(3, 10), color="blue"):

		self.window = window
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.vel_y = vel_y
		self.color = get_random_color()

		self.canvas = Canvas(window, width=self.width, height=self.height, bg="gray")
		self.canvas.pack()

		# Set up animation variables
		self.rate = 10
		self.terminated = True
		self.window.after(0, self.animation)

		# Create the control frame for buttons and bind the arrow keys to the process_keys method
		self.control_frame = Frame(window)
		self.control_frame.pack(side=BOTTOM, pady=2)
		self.canvas.bind("<Key>", self.process_keys)
		self.canvas.focus_set()

		# Welcome text that displays when module is first run, this disappears once the game has started
		self.welcome_text = self.canvas.create_text(600, 300, fill="red", font="Tahoma 24", text="Welcome! Press "
		                                                                                          "Start to "
		                                                                                   "play game.")

		# Call the create_widgets method
		self.create_widgets()

	def render(self):

		self.canvas.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill="blue")

		self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 200, fill=self.color)
		self.canvas.create_rectangle(self.x + 200, self.y, self.x + 250, self.y + 200, fill=self.color)
		self.canvas.create_rectangle(self.x + 400, self.y, self.x + 450, self.y + 200, fill=self.color)
		self.canvas.create_rectangle(self.x + 600, self.y, self.x + 650, self.y + 200, fill=self.color)
		self.canvas.create_rectangle(self.x + 800, self.y, self.x + 850, self.y + 200, fill=self.color)

	def move(self):

		self.y += self.vel_y

		if self.y < 0 or self.y > self.canvas.winfo_height():  # top & bottom of canvas, don't need to change x
			self.vel_y = -self.vel_y

	def create_widgets(self):
		"""Set up all buttons on the bottom of the GUI"""

		quit_button = Button(self.control_frame, text="Quit", command=self.quit)
		quit_button.pack(side=RIGHT)

		play_button = Button(self.control_frame, text="Start", command=self.start)
		play_button.pack(side=LEFT, padx=2)

	def start(self):
		"""Once the user has clicked the Start button, call this method to begin the game - this will start the
		animation loop"""
		self.terminated = False

	def animation(self):
		"""Create animation loop"""
		if not self.terminated:
			self.canvas.delete(ALL)
			self.render()  # Render the blue box (player) on to the canvas
			self.move()  # Move the rectangles within the canvas boundaries

		self.window.after(self.rate, self.animation)

	def move_right(self):

		self.x += 10

	def move_left(self):

		self.x -= 10

	def move_up(self):

		self.y -= 10

	def move_down(self):

		self.y += 10

	def process_keys(self, event):
		"""Set up arrow keys to correspond to the player movements (left, right, up, down)"""
		if event.keysym == "Right":
			self.move_right()
		if event.keysym == "Left":
			self.move_left()
		if event.keysym == "Up":
			self.move_up()
		if event.keysym == "Down":
			self.move_down()

	def quit(self):
		self.window.destroy()  # Once user has clicked the quit button, exit the GUI program


# Driver code
if __name__ == '__main__':
	root = Tk()
	root.title('Avoid the blocks')
	app = App(root)
	root.mainloop()



# class Player:
#
# 	def __init__(self, x=100, y=200, color="blue"):
#
# 		self.x = x
# 		self.y = y
# 		self.color = color
#
# 	def render(self, canvas):
#
# 		canvas.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill=self.color)
#
#
#
#
#
# 	def __init__(self, x=200, y=300, vel_y=randint(3, 10)):
#
# 		self.x = x
# 		self.y = y
# 		self.vel_y = vel_y
# 		self.color = get_random_color()
#
# 	def render(self, canvas):
#
# 		rect1 = canvas.create_rectangle(self.x, self.y, self.x+50, self.y+200, fill=self.color)
# 		rect2 = canvas.create_rectangle(self.x+200, self.y, self.x+250, self.y+200, fill=self.color)
# 		rect3 = canvas.create_rectangle(self.x+400, self.y, self.x + 450, self.y+200, fill=self.color)
# 		rect4 = canvas.create_rectangle(self.x+600, self.y, self.x+650, self.y+200, fill=self.color)
# 		rect5 = canvas.create_rectangle(self.x+800, self.y, self.x+850, self.y+200, fill=self.color)
#
#
#
# 	def get_position(self):
#
# 		return (self.x, self.y)
#


