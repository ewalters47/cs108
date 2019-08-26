
try:
    f = int(input('numerator: ')) / int(input('denominator: '))
    print(f)
except ZeroDivisionError:
    print('Unable to divide by zero')
# except ValueError:
#     print('Please enter an integer')
# except:
#     print('Some error happened')
