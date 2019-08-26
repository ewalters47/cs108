x = float(input('Enter value: '))

if 0.0 < x < 7:
    print('acid')
elif x == 7.0:
    print('neutral')
elif 7 < x < 14:
    print('base')
else:
    print('Value out of range!')