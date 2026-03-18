# if-else , match-case

# age=10
# if age>=18:
#     print("Eligible for vote..")
# else:
#     print("not eligible for vote..")


# a=10
# b=200
# c=150
# if a>b and a>c:
#     print('a is largest')
# elif b>c:
#     print('b is largest')  
# else:
#     print('c is largest')

# choice =2
# match choice:
#     case 1:
#         print('Gujrati')
#     case 2:
#         print('Hindi')
#     case 3:
#         print('English')
#     case _:
#         print('invalid selection') 
 

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

op = input("Enter operation: (+,-,*,/,):")

match op:
    case'+':
        print("result:",a+b)
    case'-':
        print("result:",a-b)
    case'*':
        print("result:",a*b)
    case'/':
        if b !=0:
            print("result:",a/b)
        else:
            print("error:Division by zero")
    case _:
        print("invalid operation")
        