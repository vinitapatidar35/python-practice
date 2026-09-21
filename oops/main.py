from car import Car
# Making the actual cars (Objects)
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
print(car1) # gives memory address of this car obj 

print(car1.color)
print(car1.year)
car1.drive()
car1.stop()
car1.describe()

print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()
car2.describe()
print(Car.no_of_tyres)
