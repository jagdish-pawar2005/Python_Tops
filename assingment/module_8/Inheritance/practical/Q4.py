class Parent:
    def show(self):
        print("Parent class method")

class Child1(Parent):
    def display1(self):
        print("Child1 class")

class Child2(Parent):
    def display2(self):
        print("Child2 class")

c1 = Child1()
c2 = Child2()

c1.show()
c1.display1()

c2.show()
c2.display2()