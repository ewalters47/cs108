print('Please enter a 3 digit number where the first and last digits differ by at least 2')

number = int(input())

digit1 = ((number//100)%10)
digit2 = ((number//10)%10)
digit3 = ((number//1)%10)

#Reverse the order of the integers
rev_number = (digit3*100 + digit2*10 + digit1*1)

difference = abs(number - rev_number)

diff_digit1 = (difference//100)%10
diff_digit2 = (difference//10)%10
diff_digit3 = (difference//1)%10

#Reverse the order of the difference integers
rev_diff = (diff_digit3*100 + diff_digit2*10 + diff_digit1*1)

print(difference + rev_diff)