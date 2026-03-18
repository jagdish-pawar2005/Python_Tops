class Calc:

    def add(self, a,b,c):
        print(f"Addition is {a+b+c}")

    def add(self,a,b):
        print(f"Addition is {a+b}")

c = Calc()
c.add(10,20)
c.add(10,20,30)