count = 0
for i in range(3, 101):
    num = i
    flag = 0
    for i in range (2, num):
        if num%i == 0:
            flag = 1
            break

    if flag==0:
        print(f"{num} is Prime")
        count += num
    else:
        pass
print("sum is:", count)
   
#factorial of 1 to 999
