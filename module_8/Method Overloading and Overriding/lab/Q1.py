# Write Python programs to demonstrate method overloading and method overriding.
# Method Overloading
class calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c    
c = calculator()
print(c.add(2, 3, 4))  # This will call the second add method


print("-----------------------------")
# Method Overriding
class Parent:
    def show(self):
        print("this is parent class")
class child(Parent):
    def show(self):
        print("this is child class")
c=child()
c.show()  # This will call the show method of the child class, overriding the parent class method