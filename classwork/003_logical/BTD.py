# binary to decimal
num=10010000
decimal=0
power=0
while num>0:
    rem=num%10
    decimal=decimal+rem*(2**power)
    num=num//10
    power=power+1
print(decimal)

# ocatal to decimal
# hexadecimal to decimal