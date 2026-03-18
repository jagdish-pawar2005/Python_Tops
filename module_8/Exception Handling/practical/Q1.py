try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Choose the operation (+, -, *, /): ")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter valid integers")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")