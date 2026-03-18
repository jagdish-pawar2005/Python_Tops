class demo:
    name = "jack" # class property/ class variable
    age = 22
    
    def __init__(self):
        self.course = "Python" #do not access in class method, only access in instance method
    def display(self):
        print(self.name,self.course)

    @classmethod  #class method
    def test(cls):
        print(cls.age)

d = demo()
d.test()
d.display()