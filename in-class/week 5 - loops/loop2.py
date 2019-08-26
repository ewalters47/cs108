sum = 0

while True:
    value = float(input('Enter test score: '))
    if value < 0:
        break
    sum = sum + value
print(sum)


