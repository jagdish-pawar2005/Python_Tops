# traingle pattern
lines = 5 
stars =lines -1 
space =1
for i in range(lines):
    for j in range(lines-i-1):
        print(" ", end="")
    for k in range((2*i+1)):
        print("*", end="")
    print()  

for i in range(lines-1):
    for j in range(space):
        print(" ", end="")
    for k in range((2*stars-1)):
        print("*", end="")
    print()   
    stars -= 1
    space += 1 

    # *        *
    # * *    * *
    # * * *  * *  
    # * *  * * *
    # *        *
