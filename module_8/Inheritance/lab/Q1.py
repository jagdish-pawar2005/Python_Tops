# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# Single Inheritance
class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def display(self):
        print("This is the child class.")

c=Child()
c.show()
c.display()

print("-----------------------------")
# Multiple Inheritance
class Father:
    def skill1(self):
        print("Father's skill: Programming")
class Mother:
    def skill2(self):
        print("Mother's skill: Cooking")
class baby(Father, Mother):
    def skill3(self):
        print("Child's skill: Painting")
    
c=baby()
c.skill1()
c.skill2()
c.skill3()
print("-----------------------------")
# Multilevel Inheritance
class car:
    def brand(self):
        print("Brand: Toyota")
class model(car):
    def model_name(self):
        print("Model: Camry")
class year(model):
    def year_of_manufacture(self):
        print("Year of Manufacture: 2020")
c=year()
c.brand()
c.model_name()
c.year_of_manufacture()