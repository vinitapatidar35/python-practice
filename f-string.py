#f-strings (formatted string literals) are the modern, easiest, and fastest way to format and transform strings in Python.
#By placing an f or F directly before your opening quote, you can inject variables, numbers, or even code expressions directly inside curly braces {}.

name = "vinita"
age = 21

message = f" my name is {name} and i am {age} year old"
print(message)
print(f"my name is {name} and i am {age} year old")
print(f"2 + 3 = {2+3}")
print(f"{{we can print any expression or variable using curly braces but for txt we need double curly braces}}")