try:
    filename = input("Enter file name: ")
    f = open(filename, "r")

    num = int(input("Enter a number: "))
    result = 10 / num

    print("Division Result:", result)
    print("File Content:", f.read())

except FileNotFoundError:
    print("Error: File not found")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid number entered")

finally:
    try:
        f.close()
    except:
        pass