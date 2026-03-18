class Father:
    def skill1(self):
        print("Father: Driving")

class Mother:
    def skill2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child: Programming")

c = Child()
c.skill1()
c.skill2()
c.skill3()