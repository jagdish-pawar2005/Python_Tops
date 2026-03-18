class Student:

    __id = 10 

    def set(self, id):
        self.__id = id


    def get(self):
        print(self.__id)

s=Student()
s.set(20)
s.get()

# we can not access private variable directly from outside the class,
#  but we can access it using getter and setter methods.