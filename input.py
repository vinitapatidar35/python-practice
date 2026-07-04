"""
input.py

Covers:
- input() function basics - always returns a string
- Type casting user input to int/float
- Using input() with an f-string for output
- Multiple inputs taken one after another
"""

name = input("Enter your name: ")
print("Hello,", name)

age = input("Enter your age: ")
print(type(age))

age = int(age)
print(type(age))
print(f"Next year you will be {age + 1} years old")

height = float(input("Enter your height in meters: "))
print(f"Your height is {height} m")

city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"{name} lives in {city}, {country}")