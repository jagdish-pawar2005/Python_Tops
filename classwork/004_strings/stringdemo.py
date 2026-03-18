st ="Sun Rise In The East ß µ ς       "

# print(len(st))  #count the length
# print(st.lower())
# print(st.upper())
# print(st.casefold())  #this conver the string and spacial char in lower case
print(st.capitalize()) #first latter is capital 
print(st.strip())  # remove the space end and start
print(st.isalnum())  # check the string is number.
print(st.title())  #convert the firt char in string
print(st.replace("Rise","Down",5)) # replace the word
print(st.find("The")) # find in the string 
print(st.startswith("S"))  #check the current string start with S
print(st.endswith(" ")) # chek the string is end with white space
print(st.join("ABC")) 
print("22121eee".isdigit())
print("ssbs11$".isalnum())
print("abd".zfill(10))
print("hello".center(10,'*'))