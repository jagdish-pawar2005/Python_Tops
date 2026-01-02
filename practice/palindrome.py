# 123454321 is a palindrome

number =123454321
temp = number
sum = 0
while number !=0:
    rem = number%10
    sum = (sum*10)+rem
    number = number//10 

if temp == sum:
    print("number is palindrome")
else:
    print("number is not palindrome")