'''
Find genome strings
Created Spring 2019
Homework 07
@author: Ethan Walters (emw45)
'''


genome = input('Enter a genome string: ')

starting_index = 0
while True:
    start = genome.find('ATG', starting_index)
    if start == -1:
        break
        print('No gene found')
    end = genome.find('TAG', starting_index + 3)
    if end == 'TAG':
        break
    end2 = genome.find('TAA', starting_index + 6)
    if end == 'TAA':
        break
    end3 = genome.find('TGA', starting_index + 9)
    if end == 'TGA':
        break


    print('Gene 1:', genome[5:8])
    print('Gene 2:', genome[16:19])
    starting_index = end + 3
