import sys


class Temperature:

    ABSOLUTE_ZERO_CELSIUS = -273.15

    def __init__(self, degrees=0.0):

        if degrees < Temperature.ABSOLUTE_ZERO_CELSIUS:
            print('Error: Invalid temperature')
            sys.exit(-1)
        else:
            self.degrees = degrees

    def __str__(self):
        return str(self.degrees)

    def get_fahrenheit(self):
        return (self.degrees * 9/5) + 32

    def get_celsius(self):
        return self.degrees


t1 = Temperature(-500)
print(t1)
