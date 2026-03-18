import re

# words = "sun rises in the east"

# # k = re.match("sun",words)
# k = re.search("sun",words)
# k = re.findall("s",words)
# # k =re.split(" ",words)
# k = re.sub("s","x",words)
# print(k)

# email="user@example.com"
# k = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email)
# print(k)
# if k:
#     print("valid email")
# else:
#     print("invalid email")

# ******************************************

# phone="9778565578"
# k = re.match(r"^[6-9]\d{9}$",phone) # ^[6-9] means the first digit must be between 6 and 9, # \d{9} means the next 9 digits can be any digit from 0 to 9,
# print(k)                                  #and $ indicates the end of the string. This pattern ensures that the phone number is exactly 10 digits long and starts with a valid digit. 
# if k:
#     print("valid phone number")
# else:
#     print("invalid phone number")

# create a password example
password="MySecurePass123"
k = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password)
print(k)
if k:
    print("valid password")
else:
    print("invalid password")