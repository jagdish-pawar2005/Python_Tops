
try:
    a = 10 
    b = "jagdish"
    print(a + b)
except Exception as e:
    print(e)

# user take input and convert casting to int
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError as e:
    print(e)


try:
    print(name)
except Exception as e:
    print(e)

