class student:

    sid = 1
    name = "jack"
    email = "jack@example.com"

    def to_data(self): 
        print(self.sid,self.name,self.email)

s1=student()
s1.to_data()

s2=student()
s2.sid = 2
s2.name = "chetan"
s2.email = "chetu23@gmail.com"
s2.to_data()

# constructor is a special method which is used to initialize the object of a class
# it is automatically called when we create an object of a class
# constructor types
# 1. default constructor
# 2. parameterized constructor
# 3. copy constructor
class student:

    def __init__(self,sid,name,email):
        self.sid = sid
        self.name = name
        self.email = email

    def to_data(self):
        print(self.sid,self.name,self.email)

# static method vs instatnce method vs class method differences

# static method is a method which is defined in a class but it does not have access to the instance variables of the class
# instance method is a method which is defined in a class and it has access to the instance variables of the class
# class method is a method which is defined in a class and it has access to the class variables of the class

