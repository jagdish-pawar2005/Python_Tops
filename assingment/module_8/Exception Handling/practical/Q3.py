try:
    file = open("sample.txt", "r")
    data = file.read()
    print("File Content:")
    print(data)

except FileNotFoundError:
    print("Error: File does not exist")

finally:
    print("Closing the file")
    try:
        file.close()
    except:
        pass