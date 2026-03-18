# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age 
#     def display(self):
#         print(self.name,self.age)

# class student(person):
#     # def __init__(self, name, age):
#     #     super().__init__(name, age) # write when you add new argument
#     def show(self):
#         print(self.name,self.age)

# # p1=person("chetan","22")
# # p1.display()

# s1=student("jagdish",21)
# s1.show()

# Q2

# class Animal:
#     def eat (self):
#         print("something")

# class dog(Animal):
#     def bark(self):
#         print("Bhow bhow..")

# D=dog()
# D.eat()
# D.bark()

# Q3

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print(self.name,self.salary)

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         self.department=department
#         super().__init__(name, salary)
    
#     def show(self):
#         print(self.name,self.salary,self.department)

# E=Manager("chetan","100000","IT")
# E.show()

# Q4

# class bank:
#     def intrest_rate(self):
#         print("bank rate is 5 %:)")

# class SBI(bank):  #inherit class bank
#     def intrest_rate(self): #method
#         print("intrest is 9 %")

# b=bank()
# s=SBI()

# b.intrest_rate() #method overriding 
# s.intrest_rate() 