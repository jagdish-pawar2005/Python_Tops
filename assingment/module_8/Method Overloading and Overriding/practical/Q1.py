# Method Overloading and Overriding
class Calculator:
    def add(self, a, b, c=0):
        result = a + b + c
        print("Sum =", result)

c = Calculator()

c.add(10, 20)        # two arguments
c.add(10, 20, 30)    # three arguments
