# Check cursor position using tell()

file = open("examp.txt", "r")

print("Current cursor position:", file.tell())

data = file.read(5)   # read first 5 characters
print("Data read:", data)

print("Cursor position after reading:", file.tell())

file.close()