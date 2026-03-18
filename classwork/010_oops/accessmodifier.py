# python access modifiers is not like other programming languages like java,
# c++ etc. In python we have 3 types of access modifiers
# 1. public
# 2. protected
# 3. private
# In python we can access all the members of a class from outside the class, but we can use access modifiers to restrict the access of members of a class.
# you can use public access modifier by default, you don't need to specify it.
class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"
    def display(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)
obj = MyClass()
print(obj.public_var) # I am public
print(obj._protected_var) # I am protected
print(obj._MyClass__private_var) # AttributeError: 'MyClass' object has no attribute '__private_var'

# print(dir(obj)) # ['_MyClass__private_var', '_protected_var', 'public_var']# we can access private variable by using name mangling,
#  but it is not recommended to do so. It is better to use getter and setter methods to access private variables.