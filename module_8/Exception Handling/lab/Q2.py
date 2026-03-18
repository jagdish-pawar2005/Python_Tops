try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    print("Division =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Enter integers only.")

except Exception as e:
    print("Some other error occurred:", e)

finally:
    print("Program finished.")