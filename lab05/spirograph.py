'''
Python program that draws a spirograph
Created Spring 2019
Lab05
@author: Ethan Walters (emw45)
'''

import turtle
import math

window = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()

while True:

    choice = str(input('Would you like to draw a spirograph? '))
    if choice == 'n':
        break
    elif choice is not 'y':
        print('Enter another choice')
    else:
        mov_rad = float(input('Enter the moving radius: '))
        fix_rad = float(input('Enter the fixed radius: '))
        pen_offset = float(input('Enter the pen offset: '))
        color = str(input('Enter the color: '))

        time = 0.0

        x = (fix_rad + mov_rad) * math.cos(time) + pen_offset * math.cos(((fix_rad + mov_rad) * time) / mov_rad)
        y = (fix_rad + mov_rad) * math.sin(time) + pen_offset * math.sin(((fix_rad + mov_rad) * time) / mov_rad)

        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(color)
        while time < 100:
                x = (fix_rad + mov_rad) * math.cos(time) + pen_offset * math.cos(((fix_rad + mov_rad) * time) / mov_rad)
                y = (fix_rad + mov_rad) * math.sin(time) + pen_offset * math.sin(((fix_rad + mov_rad) * time) / mov_rad)
                time += 0.1
                time + x
                time + y
                pen.goto(x, y)
window.exitonclick()