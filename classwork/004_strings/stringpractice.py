st = "sun rieses In East $ @ ^   "

# count Length of the string
print(len(st))  

# convert to lower case
print(st.lower()) 

# convert to upper case
print(st.upper()) 

# convert to symbol are also upper case
print(st.casefold())

# convert to first latter of string are title case
print(st.title())

# remove spaces from start and end
print(st.strip())  

# replace s with m
print(st.replace("s","m"))  

# find the word of in all over string
print(st.find("I")) 

# startswith check the latter of starting with "s" => true/ false
print(st.startswith("s"))

# endswith check the last latter of string "^" => true / false
print(st.endswith("^"))

# split the string on the space
print(st.split(" ",7)) 

# join the string with all sentance
print(st.join("abc"))

# is check the sentance is that character?
print("jhvjh".isalpha())

# is check the sentance is that number?
print("jvvh".isdigit())

# is check the number/char 
print("vghgch4543".isalnum())

# zero fill
print("jaggi".zfill(11))

# center fill
print("jagdish".center(11,"0"))