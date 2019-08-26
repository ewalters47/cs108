int1 = int(input('Please enter number 1: '))
int2 = int(input('Please enter number 2: '))
int3 = int(input('Please enter number 3: '))

if int1 < int2 > int3:
    print(int2)
elif int2 < int1 > int3:
    print(int1)
else:
    print(int3)