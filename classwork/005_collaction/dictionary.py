# a = {
#     "name": "jagdish",
#     "age": None,
#     "age": None,# duplicate key will override the previous value
#     "city": "delhi"
# }
# print(a)

# ****for ex*****

st ={
    "name" : "jagdish",
    "email" : "jagdish23@gmail.com",
    "sub" : ["hindi","eng","guj"],
    "hobbies" : ("cricket","Kabbidi"),
    "isMinor" : False,
    "Age" : 22,
    4j+5 : "abd",
    "name1" : "Chetan"
}

# print(st['name'])  
# print(st.get("name1")) #to get a single value from dictionary
# print("continue...")
# print(st) 

# print(st.keys()) #only give the key's 
# print(st.values()) # only give the value's
# print(st.items()) #display the both key and items
# print(st)


# for i in st:  # using for loop print only keys 
#     print(i)

# for i,j in st.items(): # using for loop print keys and values
#     print(i,j)


person = {
    "name" : "jagdish",
    "email":  "jagdish123@gmail.com"
}

# person['name'] = 20
# person.setdefault("name","abc")
# print(person)

# person['name1'] = "xyz"
# person.update({"name":"chetan","age":22})
# person.pop("name")
# print(person)

# person.clear() #deleting dictionary keys and values 
# del person
# print(person)


# ****example***

student = {
    "str" : {
        "name":"jagdish",
        "email":"jagdish123@gmail.com"
    },
    "str1": {
        "name":"chetan",
        "email":"chetu23@gmail.com",
        "sub":["eng","hindi","guj"]
    }
}

# print(student['str']['name']) 
# # print(student['str1']['sub'][0]) # in the dictionary name of student -> str1 -> sub -> [0]eng

# for i,j in student.items():
#     print(i)

