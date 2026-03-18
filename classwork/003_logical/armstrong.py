number = 153
temp = number
sum = 0
while number !=0 :
    rem = number%10
    sum = sum +(rem**3)
    number = number//10

if temp == sum:
    print("Armstrong")
else:
    print("Not armstrong")