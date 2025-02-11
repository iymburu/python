# using oop create a class called cars that has the following attributes model,color and year of manufacture
# implement constructor method and a method function that prints(my favorite car is (model)it is (color)and manufactured in(year of manufacture))
# create five instances
class Car:
    def __init__(self, model, color, year_of_manufacture):
       self.model = model
       self.color = color
       self.year_of_manufacture = year_of_manufacture
    def function(self):
       print(f"My favorite car is a {self.model}. It is {self.color} and was manufactured in {self.year_of_manufacture}")

car1 = Car("Mercedes", "blue", 1999)
car1.function()


car2 = Car("Audi", "red" , 2001)
car2.function()

car3 = Car("BMW", "pink", 2002)
car3.function()

car4 = Car("Tesla", "blue", 2003)
car4.function()

car5 = Car("Charger", "silver" , 2024)
car5.function()