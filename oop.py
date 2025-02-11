# object oriented programming
class Person:
    def __init__(self, name, age):
        # this is a constructor method
        # it takes two parameters and initialize it as attributes
        self.name = name
        self.age = age
    def myfunction(self):
        print(f"Hello,my name is {self.name} and my age is {self.age}")
        # this is a method function
#create an object or an instance of a class
myobj=Person("John", 3)
myobj.myfunction()

myobj2=Person("Mary", 5)
myobj2.myfunction()

myobj3=Person("Maddy", 11)
myobj3.myfunction()

myobj4=Person("Henry", 34)
myobj4.myfunction()

myobj5=Person("Marionette",30)
myobj5.myfunction()