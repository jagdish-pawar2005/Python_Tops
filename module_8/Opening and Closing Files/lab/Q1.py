#  Write a Python program to open a file in write mode, write some text, and then close it. 

file = open("sample.txt", "w")

file.write("hello i am jack")
file.close()

print("data written to successfully")