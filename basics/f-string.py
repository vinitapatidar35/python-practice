"""
f-string.py

Covers:
- f-strings (formatted string literals) basics
- Injecting variables and expressions inside { }
- Printing literal curly braces using {{ }}
"""

name = "vinita"
age = 21

message = f" my name is {name} and i am {age} year old"
print(message)
print(f"my name is {name} and i am {age} year old")
print(f"2 + 3 = {2+3}")
print(f"{{we can print any expression or variable using curly braces but for txt we need double curly braces}}")