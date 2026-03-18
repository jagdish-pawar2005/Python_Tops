class Parent:
    def show(self):
        print("this is parent class")

class Child(Parent):
    def show(self):
        print("this is child class")

c = Child()
c.show()  # This will call the show method of the child class, overriding the parent class method