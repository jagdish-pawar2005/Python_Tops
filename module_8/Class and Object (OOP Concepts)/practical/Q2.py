# global variable
x = 100

class Demo:
    def show(self):
        # local variable
        y = 50
        print("Local variable:", y)
        print("Global variable:", x)

# create object
d = Demo()
d.show()