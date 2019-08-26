'''def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a + b + c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)
'''

def change(my_int, my_float, my_string, my_list, my_tuple, my_dict):
    my_int = 2
    my_float = 2.0
    my_string = 'two'
    my_list[0] = 2
    my_tuple = (2, 3)
    my_dict['one'] = 2

i = 1
f = 1.0
s = 'one'
l = [1, 2]
t = (1, 2)
d = {'one': 1}
change(i, f, s, l, t, d)
print(i, f, s, l, t, d)