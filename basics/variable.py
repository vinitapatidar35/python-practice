"""
variable.py

Covers:
- Variables (creation, naming rules, multiple assignment, reassignment)
- Data types: int, float, str, bool, NoneType
- Type conversion (int, float, str)
- type() and isinstance() for type checking
- Dynamic typing in Python
- f-strings: syntax, expressions, formatting, multiline usage
- print() with custom sep parameter
"""

name , age , city = "vinita" , 21 , "Indore"
print(f"my name is :  {name} and i am {age} old .")
cgpa = 7.7
cgpa = int(cgpa)
print(cgpa)
print(type(name))
print(type(age))
print(type(city))
add = cgpa + 9.0
print(add)

print(f"Hello Vinita")

name = "Vinita"
age = 21
print(f"My name is {name}")

print(f"My name is {name} and I am {age} old.")

price = 100
discount = 20
print(f"Final price: {price - discount}")

name = "vinita"
print(f"Caps: {name.upper()}")
print(f"Next year age: {age + 1}")

cgpa = 7.0700
print(f"CGPA: {cgpa:.2f}")

name = "Vinita"
age = 21
city = "Indore"
cgpa = 7.07
print(f"Hi! I am {name}, {age} years old from {city}. CGPA: {cgpa}")

print(f"Name: {name}\nAge: {age}\nCity: {city}")

name = "Vinita"
age = 21
cgpa = 7.07
is_student = True

my_name = "Vinita"
age1 = 21
_score = 100

name, age, city = "Vinita", 21, "Indore"

x = y = z = 0

x = 10
x = 20
x = "hello"

age = 21
year = 2026
print(type(age))

cgpa = 7.07
price = 99.99
print(type(cgpa))

name = "Vinita"
city = 'Indore'
print(type(name))

is_student = True
has_job = False
print(type(is_student))

result = None
print(type(result))

age = int("21")

age = 21
print("Age: " + str(age))

x = float(5)

y = int(7.9)

price = float("99.99")

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

print(isinstance(age, int))
print(isinstance(name, int))

x = 10
x = "hello"
x = 3.14

name = "vinita"
print("my name is",name )

name = "muskan"
print("info@datawith",name,".com", sep = "")
print("suppport@datawith",name,".com", sep="")