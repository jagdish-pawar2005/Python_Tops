# Read file and print data

file = open("examp.txt", "r")

data = file.read()

print("File Content:")
print(data)

file.close()