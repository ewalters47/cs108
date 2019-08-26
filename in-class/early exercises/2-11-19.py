x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

temp_value = y
y = x
x = temp_value

print('Swapped values:', x, y)
print('Sum: ', x+y)