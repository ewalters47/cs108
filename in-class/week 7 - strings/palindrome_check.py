def reverse(string):
    if string[0::] == string[::-1]:
        return True
    else:
        return False


print(reverse('hello'))
print(reverse('racecar'))
print(reverse('civic'))
print(reverse('rotor'))



