'''
Python program to compute wind chill
Created Spring 2019
Lab04
@author: Ethan Walters (emw45)
'''

# Get user inputs
fah_temp = int(input('Input the temperature in Fahrenheit: '))
wind_speed = int(input('Input the wind speed (in MPH): '))

# If the wind speed is below 2 or the fahrenheit temp is below -50 or above 41, print an error message to the user
if wind_speed < 2 or fah_temp < -50 or fah_temp > 41:
    print('Insufficient values, program will exit')

# If sufficient values are supplied, calculate the wind chill temperature
else:
    wind_chill_temp = 35.74 + 0.6215*fah_temp - 35.75*wind_speed**0.16 + 0.4275*fah_temp * wind_speed**0.16

    # Print results to console including layer count based on wind chill temperature value
    print('The wind chill temperature is: ', wind_chill_temp)

    if wind_chill_temp < -40:
        print('Stay home')
    elif -40 <= wind_chill_temp < -10:
        print('Wear 4 Layers')
    elif -10 <= wind_chill_temp < 20:
        print('Wear 3 Layers')
    elif 20 <= wind_chill_temp < 40:
        print('Wear 2 Layers')
    elif wind_chill_temp >= 40:
        print('Wear 1 Layer')