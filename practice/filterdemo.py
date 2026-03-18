l =[4,5,6,9,8,11,14,15,18,20]
k=[]
def odd(a):
    
    if a%2!=0:
        print("odd",a)

        for i in range(len(l)):
            k.append(odd(l[i]))

print(k)