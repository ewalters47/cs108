from math import pi

diameter_in = int(input('Please enter the diameter of a circle in inches: '))

diameter_cm = diameter_in * 2.54

circumference = pi * diameter_cm

area = (diameter_cm / 2)**2 * pi

print('Circumference in Inches:', circumference)
print('Area is:', area)