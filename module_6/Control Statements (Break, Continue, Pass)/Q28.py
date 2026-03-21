# Write a Python program to stop the loop once 'banana' is found using the break statement. 
# List1 = ['apple', 'banana', 'mango']
fruits = ['apple','banana','mango','orange']
for i in fruits:
    if i == 'banana':
        print("banana found. loop stoped")
        break
    print(i)